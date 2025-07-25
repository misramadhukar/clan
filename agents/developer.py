from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient
import re, json

class DeveloperAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Developer Agent", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, project_view, requirement, context=None):
        prompt = (
            "You are a software developer. Given the current project structure and the following requirement, "
            "generate or update all necessary files. Return a JSON array where each item has: file (path), content (full file content), and description (brief change description).\n"
            f"Project structure:\n{project_view}\n"
            f"Requirement:\n{requirement}\n"
            f"Context:\n{context or ''}\n"
        )
        response = self.llm.generate(prompt)
        response = re.sub(r'<think>[\s\S]*?</think>', '', response, flags=re.IGNORECASE)
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                file_changes = json.loads(match.group(0))
            else:
                file_changes = []
        except Exception:
            file_changes = []
        self.remember({"requirement": requirement, "file_changes": file_changes})
        return file_changes 