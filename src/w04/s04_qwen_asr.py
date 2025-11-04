import os
import dashscope

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

messages = [
    {
        "role": "system",
        "content": [
            # 此处用于配置定制化识别的Context
            {"text": ""},
        ]
    },
    {
        "role": "user",
        "content": [
            {"audio": "D:\\source\\robot-course\\src\\w04\\skk.wav"},
            # {"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"},
        ]
    }
]
response = dashscope.MultiModalConversation.call(
    # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    api_key="sk-e172d890e06248d2b84674523749652a",
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_itn":True
    }
)
print(response)