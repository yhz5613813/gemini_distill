from gemini_api import GoogleGenAIUploader
from prompt import *
import json
import aiofiles

import asyncio
import json
import aiofiles
from tqdm.asyncio import tqdm

async def main():
    uploader = GoogleGenAIUploader(api_key="AIzaSyDGXSgl5MAC6qVBS3ax2zwbOaYvVLejFl4", prompt=video_distill_cot_prompts)
    file_paths = [r"C:\Users\16497\Documents\WeChat Files\wxid_m1v1dc1w6o1g22\FileStorage\Video\2025-02\be5706074270e2dcaf83e0643d4ae0e1.mp4"] * 3
   
    write_lock = asyncio.Lock()  # 线程安全的文件写入锁
    
    async def save_summary(file_path, summary):
        """异步写入 summary 到 JSONL 文件"""
        async with write_lock:
            async with aiofiles.open("summaries.jsonl", mode="a", encoding="utf-8") as f:
                await f.write(json.dumps({"file": file_path, "summary": summary}, ensure_ascii=False) + "\n")
    
    # 创建进度条
    progress_bar = tqdm(total=len(file_paths), desc="Processing Videos", unit="file")

    async for file_path, summary in await uploader.process_files(file_paths):
        await save_summary(file_path, summary)  # 先写入 JSONL
        progress_bar.update(1)  # 进度条 +1
        print(f"\n[Done] {file_path}: {summary[:100]}...")  # 打印前 100 个字符，避免太长
    
    progress_bar.close()  # 关闭进度条

# 运行主函数
asyncio.run(main())
