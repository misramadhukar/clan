from clan.agents.base_agent import BaseAgent
from clan.project_state import ProjectState
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
import json, re

class FileAgent(BaseAgent):
    def __init__(self, project_state=None, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="File Agent", tools=tools, memory=memory, config=config or PROMPT_TEMPLATES)
        self.project_state = project_state or ProjectState()
        self.llm = llm_client or LLMClient()

    def act(self, requirement, context=None):
        prompt_template = self.config["file_agent_structure"]
        prompt = prompt_template.format(requirement=requirement)
        response = self.llm.generate(prompt)
        # Remove <think>...</think> blocks and any non-JSON text
        response = re.sub(r'<think>[\s\S]*?</think>', '', response, flags=re.IGNORECASE)
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                file_list = json.loads(match.group(0))
            else:
                file_list = [line.strip() for line in response.splitlines() if line.strip()]
        except Exception:
            file_list = []
        for file_path in file_list:
            self.project_state.write_file(file_path, "")
        self.remember({"requirement": requirement, "files": file_list})
        return file_list

    def create_or_update_file(self, path, content):
        self.project_state.write_file(path, content)

    def get_file_content(self, path):
        return self.project_state.read_file(path)

    def list_files(self):
        return self.project_state.list_files()

    def get_project_view(self):
        return self.project_state.get_project_view() 