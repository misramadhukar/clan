from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES

class RequirementsManager:
    def __init__(self, llm_client=None, config=None):
        self.llm = llm_client or LLMClient()
        self.config = config or PROMPT_TEMPLATES
        self.requirements = []  # List of (requirement, timestamp, user/system)

    def add_requirement(self, requirement, source="user"):
        import datetime
        self.requirements.append({
            "requirement": requirement,
            "timestamp": datetime.datetime.now().isoformat(),
            "source": source
        })

    def get_current_requirement(self):
        if self.requirements:
            return self.requirements[-1]["requirement"]
        return None

    def get_history(self):
        return self.requirements

    def suggest_next_steps(self, project_state=None):
        # Use LLM to suggest next steps or clarifications for the user
        current_req = self.get_current_requirement()
        project_view = project_state.get_project_view() if project_state else ""
        prompt = self.config.get(
            "requirement_suggestion_prompt",
            "Given the current requirement and project structure, suggest the next steps or clarifications for the user.\n\nRequirement: {requirement}\n\nProject Structure:\n{project_view}\n\nRespond with a list of suggestions."
        ).format(requirement=current_req, project_view=project_view)
        return self.llm.generate(prompt) 