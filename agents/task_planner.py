from clan.agents.base_agent import BaseAgent
from clan.llm import LLMClient
import re, json

class TaskPlannerAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Task Planner", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, requirement, project_state, context=None):
        project_view = project_state.get_project_view()
        prompt = (
            "You are a project manager. Given the current project structure and the following requirement, devise a step-by-step plan to implement the requirement. "
            "For each step, specify: agent (which agent to invoke, e.g., DeveloperAgent for code generation), action (what action to perform), targets (a list of files/components), and description (brief step description).\n"
            "If multiple files or components are closely related and should be implemented or updated together for better context, group them into a single step with a list of targets.\n"
            "For code generation or file implementation steps, use 'DeveloperAgent' as the agent name.\n"
            f"Project structure:\n{project_view}\n"
            f"Requirement:\n{requirement}\n"
            f"Context:\n{context or ''}\n"
            "Return the plan as a JSON array of steps."
        )
        response = self.llm.generate(prompt)
        response = re.sub(r'<think>[\s\S]*?</think>', '', response, flags=re.IGNORECASE)
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                plan = json.loads(match.group(0))
            else:
                plan = []
        except Exception:
            plan = []
        self.remember({"requirement": requirement, "plan": plan})
        return plan 