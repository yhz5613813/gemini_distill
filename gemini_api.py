import asyncio
import time
import threading
from google import genai
from queue import Queue
from prompt import *

class GoogleGenAIUploader:
    def __init__(self, api_key, prompt):
        self.client = genai.Client(api_key=api_key)
        self.task_queue = asyncio.Queue()  # 改用 asyncio.Queue
        self.prompt = prompt
    
    def upload_and_process(self, file_path):
        """同步上传文件"""
        print(f"Uploading file: {file_path}...")
        video_file = self.client.files.upload(file=file_path)
        print(f"Completed upload: {video_file.uri}")
        
        while video_file.state.name == "PROCESSING":
            time.sleep(1)
            video_file = self.client.files.get(name=video_file.name)
        
        if video_file.state.name == "FAILED":
            raise ValueError("File processing failed")
        
        return video_file
    
    def generate_summary(self, video_file):
        """同步生成摘要"""
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[video_file, self.prompt]
        )
        return response.text
    
    async def worker(self):
        while True:
            file_path = await self.task_queue.get()
            if file_path is None:
                break
            try:
                # 在 executor 中运行同步任务
                loop = asyncio.get_running_loop()
                video_file = await loop.run_in_executor(None, self.upload_and_process, file_path)
                summary = await loop.run_in_executor(None, self.generate_summary, video_file)
                
                yield file_path, summary  # 返回文件路径和摘要
                print(f"\n[Result] {file_path}: {summary}\n")  # 实时输出结果
            except Exception as e:
                print(f"\n[Error] {file_path}: {e}\n")  # 发生错误时输出
            self.task_queue.task_done()
    
    async def process_files(self, file_paths):
        """启动 workers 并返回异步生成器"""
        for file_path in file_paths:
            await self.task_queue.put(file_path)
        
        return self.worker()  # 返回异步生成器

