# Clan: Agentic Orchestration Framework

Clan is an agentic orchestration framework for software engineering automation. It leverages LLM-powered agents to plan, generate, review, and test code and documentation, enabling dynamic and extensible workflows for building and evolving software projects.

## Key Features
- Modular, extensible agent system (DeveloperAgent, TaskPlannerAgent, etc.)
- Step-by-step, context-aware project planning and execution
- Unified agent for generating and updating all types of files (code, docs, configs, etc.)
- Interactive CLI with project summary-driven suggestions
- Multi-language support and easy extensibility

## Example Usage

```bash
python -m clan.main
```
You will be prompted to enter the programming language (default: Python) and your project requirement (e.g., "Implement a queue in Python").

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
Clan supports multiple LLM providers (e.g., OpenAI, Ollama). Set the appropriate environment variables in a `.env` file or your shell:

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
- You can extend or customize agents and workflows as needed.

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