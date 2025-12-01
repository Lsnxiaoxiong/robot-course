from enum import Enum

from openai import OpenAI

ALIYUN_BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
ALIYUN_API_KEY = 'sk-ddaf46f7c4c743fb8993a3a9f4fa122d'
DEEPSEEK_BASE_URL = 'https://api.deepseek.com/v1'
DEEPSEEK_API_KEY = 'sk-167357ec3614423ca14eca722adb7e7a'


class Model:
    def __init__(self, base_url: str, api_key: str, model_name: str):
        self.base_url = base_url
        self.api_key = api_key
        self.model_name = model_name
        self.client = OpenAI(base_url=base_url, api_key=api_key)


class ModelEnum(Enum):
    """
    模型枚举类
    千问3模型需要设置参数：
        extra_body={"enable_thinking": False}
        parallel_tool_calls=True
    """
    QWEN3_235B_A22B = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen3-235b-a22b')
    QWEN3_30B_A3B = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen3-30b-a3b')
    QWEN3_30B = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen3-32b')
    QWEN3_06B = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen3-0.6b')

    QWEN_VL_PLUS = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-vl-plus')

    QWEN3_MAX = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen3-max')
    QWEN_FLASH = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-flash')
    QWEN_PLUS = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-plus')
    QWEN_TURBO = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-turbo')
    QWEN_TURBO_LATEST = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-turbo-latest')
    QWEN_TURBO_2025_04_28 = Model(base_url=ALIYUN_BASE_URL, api_key=ALIYUN_API_KEY, model_name='qwen-turbo-2025-04-28')


    DEEPSEEK_R1 = Model(base_url=DEEPSEEK_BASE_URL, api_key=DEEPSEEK_API_KEY, model_name='deepseek-reasoner')
    DEEPSEEK_V3 = Model(base_url=DEEPSEEK_BASE_URL, api_key=DEEPSEEK_API_KEY, model_name='deepseek-chat')