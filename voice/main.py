# 导入openai库
from http.client import responses

from openai import OpenAI, api_key, base_url


class LLM:
    def __init__(self, config):
        self.model_name = config.get("model_name")
        self.api_key = config.get("api_key")
        self.url = config.get("url")
        self.client = OpenAI(api_key=self.api_key, base_url=self.url)

    def generate_response(self, dialogue):
        responses = self.client.chat.completions.create(
            model=self.model_name,
            messages=dialogue
        )
        return responses.choices[0].message.content

def run():
    prompt = "您好"
    config = {
            "model_name" : "glm-4.5", # glm-4.5, GLM-4-Flash
            "api_key" : "f3fa8a1a11104471bd535295d25c554b.HK0bioHzjrG3S07K",
            "url" : "https://open.bigmodel.cn/api/paas/v4/",
    }
    llm = LLM(config)
    dialogue = [
        {"role": "system", "content": "调皮一点回答"},
        {"role":"user", "content": "你好"}
    ]
    response = llm.generate_response(dialogue)
    print(response)
if __name__ == "__main__":
    run()
