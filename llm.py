import os
import requests

class LLMClient:
    def __init__(self, provider=None, api_key=None, endpoint=None):
        self.provider = provider or os.getenv("PROVIDER", "openai")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.endpoint = endpoint

    def generate(self, prompt, **kwargs):
        if self.provider == "openai":
            return self._generate_openai(prompt, **kwargs)
        elif self.provider == "mcp":
            return self._generate_mcp(prompt, **kwargs)
        elif self.provider == "ollama":
            return self._generate_ollama(prompt, **kwargs)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _generate_openai(self, prompt, model="gpt-3.5-turbo", **kwargs):
        import openai
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response.choices[0].message.content.strip()

    def _generate_mcp(self, prompt, **kwargs):
        endpoint = self.endpoint or os.getenv("MCP_ENDPOINT")
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        data = {
            "prompt": prompt,
            "max_tokens": kwargs.get("max_tokens", 512),
            "temperature": kwargs.get("temperature", 0.7),
        }
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json().get("text", "").strip()

    def _generate_ollama(self, prompt, model=None, **kwargs):
        import json
        endpoint = self.endpoint or os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/api/generate/")
        model = model or os.getenv("OLLAMA_MODEL", "llama2")
        data = {
            "model": model,
            "prompt": prompt,
            "stream": True,
        }
        response = requests.post(endpoint, json=data, stream=True)
        response.raise_for_status()
        full_output = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line)
                    content = chunk.get("response") or chunk.get("choices", [{}])[0].get("message", {}).get("content", "")
                    full_output += content
                except Exception:
                    pass  # Ignore streaming parse errors
        return full_output.strip() 