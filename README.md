# AI Agent Orchestrator (Abstract Factory Pattern)

This project is an AI agent orchestration system for software engineering tasks, using a modular Abstract Factory design pattern in Python. It supports multiple LLM providers (OpenAI, Ollama, etc.) and is designed for easy extension to new programming languages.

## Architecture Overview

- **CoreAgentFactory**: Provides methods to create language-agnostic (core) agents, such as:
  - FileAgent (project structure design)
  - TaskPlannerAgent (file-level task planning)
  - SummaryAgent (project summary)
  - UserInteractionAgent (interactive CLI)
- **PythonAgentFactory**: Inherits from CoreAgentFactory and adds methods for Python-specific agents:
  - CodeGenerator
  - CodeReviewer
  - UnitTester
  - TransformerAgent (Python-specific)
- **Orchestrator**: Accepts a single factory object and uses it to create all required agents, both core and language-specific.
- **Factory Registry**: A function (`get_agent_factory`) selects the correct factory based on the user's chosen language.

## Extending to New Languages

To add support for a new language (e.g., JavaScript):
1. Create a new factory (e.g., `JavaScriptAgentFactory`) inheriting from `CoreAgentFactory` and `AgentFactory`.
2. Implement language-specific agent creation methods.
3. Register the new factory in `get_agent_factory` in `main.py`.

## How It Works

1. The user is prompted for the programming language and project requirement.
2. The correct factory is selected based on the language.
3. The orchestrator uses the factory to create all agents and manage the workflow:
   - Project structure design
   - Task planning
   - Code generation
   - Project summary
   - (Optional) Code review and testing
   - Project is saved to disk

## Example Usage

```bash
python clan/main.py
```

You will be prompted to enter the programming language (default: Python) and your project requirement (e.g., "Implement a queue in Python").

## Example Output

```
[Orchestrator] Starting workflow for task: Implement a factorial function
[Orchestrator] Project structure:
...
[Orchestrator] Generated code for main.py (task: Implement factorial): ...
[Orchestrator] Project saved to: projects/factorial_project
```

## Requirements

- Python 3.8+
- `python-dotenv` (for environment variable management)
- For OpenAI: `openai` Python package (if using OpenAI provider)
- For Ollama: [Ollama](https://ollama.com/) running locally

Install dependencies:
```bash
pip install -r requirements.txt
```

## LLM Provider Setup

The project supports multiple LLM providers. Set the following environment variables as needed (e.g., in a `.env` file):

### For Ollama (local LLM)

- `PROVIDER=ollama`
- `OLLAMA_ENDPOINT=http://localhost:11434/api/generate/` (default)
- `OLLAMA_MODEL=llama2` (or your preferred model)

Start Ollama locally and pull a model:
```bash
ollama pull llama2
ollama serve
```

### For OpenAI

- `PROVIDER=openai`
- `OPENAI_API_KEY=your_openai_api_key`

### For MCP (if supported)

- `PROVIDER=mcp`
- `MCP_ENDPOINT=your_mcp_endpoint`
- `MCP_API_KEY=your_mcp_api_key`

## Notes

- The orchestrator is interactive and will guide you through entering requirements and next steps.
- Generated projects are saved in the `projects/` directory.
- You can extend or customize agents and factories as needed.
- To add a new language, implement a new factory and register it in `get_agent_factory`.

---

## Pre-Push Checklist

Before pushing to GitHub, make sure you:

- [ ] Run all tests and a sample workflow to ensure there are no runtime errors.
- [ ] Check for leftover debug prints or TODOs in the code.
- [ ] Ensure README.md is up to date and describes the new architecture and usage.
- [ ] Ensure requirements.txt includes all necessary dependencies.
- [ ] Ensure .gitignore is set up to exclude unnecessary files (e.g., __pycache__, .env, .vscode, projects/).
- [ ] Ensure no large or sensitive files (e.g., .env with real keys) are present in the repo.
- [ ] Optionally, write a release note or PR description summarizing the milestone.

---

**Contributions and feedback are welcome!** 