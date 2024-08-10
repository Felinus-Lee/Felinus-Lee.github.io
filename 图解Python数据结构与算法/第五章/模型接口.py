import openai

# 设置API密钥
openai.api_key = 'your-openai-api-key'

# 定义提示语
prompt = "写一段关于气候变化的简短文章。"

# 调用GPT-3模型生成文本
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150,  # 控制生成文本的长度
    temperature=0.7,  # 控制生成文本的创意程度
    n=1,  # 生成一个响应
    stop=None  # 没有显式停止标记
)

# 打印生成的文本
print(response.choices[0].text.strip())
