
if __name__ == "__main__":
    import os
    from openai import OpenAI

    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
        api_key="sk-cc47b40266194755b4d3985ccc82e10c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant. The answers need to be short and simple as possible."},
        {"role": "user", "content": "大模型的发展前景如何？"},
    ]

    # messages = [
    #     ChatCompletionSystemMessageParam(role="system", content="You are a helpful assistant."),
    #     ChatCompletionUserMessageParam(role="user", content="你是谁？"),
    # ]


    completion = client.chat.completions.create(
        model="qwen-flash",
        messages=messages,
        extra_body={"enable_thinking": True},
        stream=True
    )
    is_answering = False  # 是否进入回复阶段
    print("\n" + "=" * 20 + "思考过程" + "=" * 20)
    for chunk in completion:
        delta = chunk.choices[0].delta
        if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
            if not is_answering:
                print(delta.reasoning_content, end="", flush=True)
        if hasattr(delta, "content") and delta.content:
            if not is_answering:
                print("\n" + "=" * 20 + "完整回复" + "=" * 20)
                is_answering = True
            print(delta.content, end="", flush=True)
