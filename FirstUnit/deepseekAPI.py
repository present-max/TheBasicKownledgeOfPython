import os   #系统模块，用于管理环境变量
from openai import OpenAI   #用于调用OpenAI API

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),  #获取环境变量中的API密钥
    base_url="https://api.deepseek.com" )        #OpenAI API的地址

response = client.chat.completions.create(   #调用OpenAI API的chat.completions.create方法
    model="deepseek-v4-pro",   #使用deepseek-v4-pro模型
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},   #系统消息
        {"role": "user", "content": "Hello"},   #用户消息
    ],
    stream=False
)
print(response.choices[0].message.content)