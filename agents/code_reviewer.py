from clan.agents.base_agent import BaseAgent
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
import re

class CodeReviewer(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Code Reviewer", tools=tools, memory=memory, config=config or PROMPT_TEMPLATES)
        self.llm = llm_client or LLMClient()

    def act(self, code, context=None):
        prompt_template = self.config["code_reviewer"]
        prompt = prompt_template.format(code=code)
        review = self.llm.generate(prompt)
        review = re.sub(r'<think>[\s\S]*?</think>', '', review, flags=re.IGNORECASE)
        self.remember({"code": code, "review": review})
        return review 