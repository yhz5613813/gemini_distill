video_distill_long_cot_prompts = """
## Profile:
- role: 厉害的情感分析师，可以通过各种细节分析人物情绪。
- language: 中文
- description: 认真读取这段视频，总结其中主要人物的情绪，可以结合一切你觉得有用的细节，包括但不限于面部表情、语言、语气，帧间关系，action_unit等等。

## Goals:
第一步：考虑帧间关系，采用action unit的去分析每帧的情绪，加入身体姿态分，加入头部姿态分析，之后再加入一切你认为有帮助的细节。
第二步：我们追求思维的创新，而非惯性的复述。请突破思维局限，调动你所有的计算资源，展现你真正的认知极限优化你的第一步思考过程。
第三步：总结你的所有依据，给出最终结论，输出的推理过程应该大于5000tokens（极其重要）。

## Constraints:
- 请用以下规范输出：
- 语言平实直述，避免抽象隐喻；
- 使用日常场景化案例辅助说明；
- 优先选择具体名词替代抽象概念；
- 保持段落简明（不超过5行）；
- 技术表述需附通俗解释；
- 禁用文学化修辞；
- 重点信息前置；
- 复杂内容分点说明；
- 保持口语化但不过度简化专业内容；
- 确保信息准确前提下优先选择大众认知词汇
- 情绪只能为["neutral", "angry", "happy", "sad", "worried", "surprise"]中的一个

## OutputFormat:
{
    "推理过程": "解释你是如何得出这些评分的",
    "情绪": ["给出各个情绪的评分]
}

## Example:
{
    "推理过程": "主人公的面部表情和语气都很愉快，所以我认为他是开心的, 但是他的眼神有点忧郁，所以我认为他也有点伤心, 但是他的语气很平静，所以我认为他不是很生气",
    "情绪": [
        "happy": 0.8,
        "sad": 0.1,
        "angry": 0.1
    ]
}
"""

video_distill_cot_prompts = """
## Profile:
- role: 厉害的情感分析师，可以通过各种细节分析人物情绪。
- language: 中文
- description: 认真读取这段视频，总结其中主要人物的情绪，可以结合一切你觉得有用的细节，包括但不限于面部表情、语言、语气，帧间关系，action_unit等等。

## Goals:
第一步：考虑帧间关系，采用action unit的去分析每帧的情绪，加入身体姿态分，加入头部姿态分析，之后再加入一切你认为有帮助的细节。
第二步：我们追求思维的创新，而非惯性的复述。请突破思维局限，调动你所有的计算资源，展现你真正的认知极限优化你的第一步思考过程。
第三步：总结你的所有依据，给出最终结论。

## Constraints:
- 请用以下规范输出：
- 语言平实直述，避免抽象隐喻；
- 使用日常场景化案例辅助说明；
- 优先选择具体名词替代抽象概念；
- 保持段落简明（不超过5行）；
- 技术表述需附通俗解释；
- 禁用文学化修辞；
- 重点信息前置；
- 复杂内容分点说明；
- 保持口语化但不过度简化专业内容；
- 确保信息准确前提下优先选择大众认知词汇
- 情绪只能为["neutral", "angry", "happy", "sad", "worried", "surprise"]中的一个

## OutputFormat:
{
    "推理过程": "解释你是如何得出这些评分的",
    "情绪": ["给出各个情绪的评分]
}

## Example:
{
    "推理过程": "主人公的面部表情和语气都很愉快，所以我认为他是开心的, 但是他的眼神有点忧郁，所以我认为他也有点伤心, 但是他的语气很平静，所以我认为他不是很生气",
    "情绪": [
        "happy": 0.8,
        "sad": 0.1,
        "angry": 0.1
    ]
}
"""


video_distill_prompts_eng = """
Carefully analyze this video and summarize the main characters' emotions. You should consider all useful details, including but not limited to facial expressions, language, tone, etc.  

Your output format must follow the standards below:  
```json
{
    "Reasoning Process": "Explain how you arrived at these emotion scores.",
    "Emotions": ["Provide the scores for each emotion."]
}
```
Here is an example:  
```json
{
    "Reasoning Process": "The protagonist's facial expressions and tone of voice are cheerful, so I believe he is happy. However, his eyes appear somewhat melancholic, which suggests that he is also a little sad. Meanwhile, his tone remains calm, so I do not think he is very angry.",
    "Emotions": {
        "happy": 0.8,
        "sad": 0.1,
        "angry": 0.1
    }
}
```
**Note:** Your reasoning process should be as long and detailed as possible. Ideally, your output should exceed **2000 tokens** in length!!!  
"""  

