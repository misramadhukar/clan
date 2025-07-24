import sys
from clan.factories.python_factory import PythonAgentFactory
from clan.factories.core_agent_factory import CoreAgentFactory
from clan.orchestrator.orchestrator import Orchestrator
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
from clan.agents.user_interaction_agent import UserInteractionAgent
from dotenv import load_dotenv
import io
load_dotenv()

def get_agent_factory(language, llm_client=None, config=None):
    if language.lower() == "python":
        from clan.factories.python_factory import PythonAgentFactory
        return PythonAgentFactory(llm_client=llm_client, config=config)
    # Add more languages here as needed
    else:
        raise ValueError(f"Unsupported language: {language}")

def run_orchestrator_interactive():
    llm_client = LLMClient()
    language = input("Enter the programming language for your project (default: Python): ") or "python"
    factory = get_agent_factory(language, llm_client=llm_client, config=PROMPT_TEMPLATES)
    from clan.orchestrator.orchestrator import Orchestrator
    orchestrator = Orchestrator(factory)
    user_agent = factory.create_user_interaction_agent()
    # First requirement (outside loop)
    suggestions = user_agent.generate_suggestions(context="project ideas")
    requirement = user_agent.act(
        prompt_message="Please enter your project requirement.",
        suggestions=suggestions
    )
    orchestrator.run_workflow(requirement)
    # Loop for next steps, using latest project summary as context
    while True:
        project_summary = orchestrator.project_summary
        suggestions = user_agent.generate_suggestions(context=project_summary)
        next_action = user_agent.act(
            prompt_message="What would you like to do next?",
            suggestions=suggestions + ["Run another requirement.", "Exit."],
            context=project_summary
        )
        if next_action.strip().lower().startswith("run"):
            suggestions = user_agent.generate_suggestions(context=project_summary)
            requirement = user_agent.act(
                prompt_message="Please enter your next project requirement.",
                suggestions=suggestions,
                context=project_summary
            )
            orchestrator.run_workflow(requirement)
        elif next_action.strip().lower().startswith("exit"):
            print("Goodbye!")
            break
        else:
            print("Unrecognized option. Please choose a suggestion or type 'Exit' to quit.")

if __name__ == "__main__":
    run_orchestrator_interactive() 