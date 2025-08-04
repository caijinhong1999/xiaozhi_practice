from openai import OpenAI, api_key, base_url

class LLM:
    def __init__(self, config):
        self.model_name = config.get("model_name")
        self.api_key = config.get("api_key")
        self.url = config.get("url")
        self.client = OpenAI(api_key=self.api_key, base_url=self.url)

    def stream_response(self, dialogue):
        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=dialogue,
            stream=True  # 关键点：开启流式响应
        )
        print("AI：", end="", flush=True)
        full_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_response += content
        print()
        return full_response

def run():
    config = {
        "model_name": "glm-4.5",
        "api_key": "f3fa8a1a11104471bd535295d25c554b.HK0bioHzjrG3S07K",
        "url": "https://open.bigmodel.cn/api/paas/v4/",
    }

    llm = LLM(config)
    dialogue = [
        {"role": "system", "content": "冷酷一点回答"}
    ]

    print("输入内容开始对话，输入 ':wq' 退出。")
    while True:
        user_input = input("你：")
        if user_input.strip() == ":wq":
            print("对话结束。")
            break

        dialogue.append({"role": "user", "content": user_input})
        response = llm.stream_response(dialogue)
        dialogue.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    run()
