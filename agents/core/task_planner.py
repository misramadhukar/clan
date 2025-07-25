from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient
import re, json

REQUIRED_FIELDS = ["step", "agent", "action", "targets", "description", "depends_on", "expected_output"]

def validate_plan(plan):
    if not isinstance(plan, list):
        return False
    for step in plan:
        if not isinstance(step, dict):
            return False
        for field in REQUIRED_FIELDS:
            if field not in step:
                return False
    return True

class TaskPlannerAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Task Planner", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, requirement, project_state, context=None):
        project_view = project_state.get_project_view()
        prompt = (
            "You are a highly skilled project manager and software architect. Given the current project structure and the following requirement, devise a detailed, step-by-step plan to implement the requirement. "
            "For each step, specify the following fields as a JSON object: "
            "step (step number), agent (which agent to invoke, e.g., DeveloperAgent for code generation), action (what action to perform), targets (a list of files/components), description (brief step description), depends_on (list of step numbers this step depends on), and expected_output (what artifact or result this step should produce).\n"
            "If multiple files or components are closely related and should be implemented or updated together for better context, group them into a single step with a list of targets.\n"
            "For code generation or file implementation steps, use 'DeveloperAgent' as the agent name.\n"
            "If a step depends on the completion of previous steps, specify their step numbers in 'depends_on'.\n"
            "Be as granular and explicit as possible, breaking down complex tasks into atomic, actionable steps.\n"
            f"Project structure:\n{project_view}\n"
            f"Requirement:\n{requirement}\n"
            f"Context:\n{context or ''}\n"
            "Return the plan as a JSON array of steps, each with all required fields."
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
        if not validate_plan(plan):
            self.remember({"requirement": requirement, "plan": plan, "error": "Plan schema validation failed."})
            return []
        self.remember({"requirement": requirement, "plan": plan})
        return plan 