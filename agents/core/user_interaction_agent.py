from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient
import re, json

class UserInteractionAgent(BaseAgent):
    def __init__(self, role="User Interaction Agent", tools=None, memory=None, config=None):
        super().__init__(role=role, tools=tools, memory=memory, config=config or {})
        self.llm = LLMClient()
        self.first_message_shown = False

    def act(self, prompt_message=None, suggestions=None, context=None):
        if not self.first_message_shown:
            print("\n✨ Hi, we are Clan! Let's start building something amazing together. ✨\nWe're here to help you turn your ideas into reality—just share your vision and we'll help you bring it to life!\n")
            self.first_message_shown = True
        if prompt_message:
            print("\n" + prompt_message)
        if suggestions:
            print("Suggestions:")
            for idx, suggestion in enumerate(suggestions, 1):
                print(f"  {idx}. {suggestion}")
        user_input = input("Your input: ")
        self.remember({"prompt": prompt_message, "input": user_input, "suggestions": suggestions})
        return user_input

    def generate_suggestions(self, context=None, num_suggestions=3):
        # Use memory to build context
        past_interactions = self.recall()
        history = "\n".join([
            f"Prompt: {item['prompt']}\nInput: {item['input']}" for item in past_interactions if 'prompt' in item and 'input' in item
        ])
        prompt = (
            f"Based on the following conversation history, suggest {num_suggestions} creative and practical Python project requirements for a user. "
            "Respond with a JSON list of strings.\n"
        )
        if history:
            prompt += f"Conversation history:\n{history}\n"
        if context:
            prompt += f"Context: {context}\n"
        response = self.llm.generate(prompt)
        response = re.sub(r'<think>[\s\S]*?</think>', '', response, flags=re.IGNORECASE)
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                suggestions = json.loads(match.group(0))
            else:
                suggestions = [line.strip() for line in response.splitlines() if line.strip()]
        except Exception:
            suggestions = []
        return suggestions 