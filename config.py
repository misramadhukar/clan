PROMPT_TEMPLATES = {
    # Code generation prompt
    "code_generator": (
        "Write clean, production-ready Python code for the following task. "
        "Output only the code, with clear and concise comments. "
        "Do not include explanations or extra text.\n"
        "Task: {task}"
    ),

    # Code review prompt
    "code_reviewer": (
        "Review the following Python code for correctness, style, and best practices. "
        "Provide actionable feedback and suggestions for improvement.\n"
        "Code:\n{code}"
    ),

    # Unit test generation prompt
    "unit_tester": (
        "Write comprehensive and well-structured unit tests for the following Python code. "
        "Use pytest conventions where appropriate.\n"
        "Code:\n{code}"
    ),

    # Project structure design prompt
    "file_agent_structure": (
        "Given the following requirement, design a Python project structure as a JSON list of file and folder paths. "
        "Only output the JSON list, with no explanations.\n"
        "Requirement: {requirement}"
    ),

    # Task planning prompt
    "task_planner_prompt": (
        "Given the following requirement and current project structure, generate a JSON list of file-level tasks. "
        "Each task in the list must be a JSON object with the following keys: 'file', 'action', and 'description'.\n\n"
        "Requirement: {requirement}\n\n"
        "Project Structure:\n{project_view}\n\n"
        "Respond ONLY with a JSON list in this format:\n"
        "[\n  {{\"file\": \"<file_path>\", \"action\": \"create|update|delete\", \"description\": \"<brief description>\"}},\n  ...\n]"
    ),

    # Code transformation prompt
    "transformer_agent": (
        "Transform the following code and any accompanying text into well-written, production-ready Python code.\n"
        "- Remove unnecessary explanations and non-code text.\n"
        "- Ensure comments are clear and concise.\n"
        "- Enforce PEP8 style and best practices.\n"
        "- Ensure the code is ready for production use.\n"
        "- Only output the improved code.\n\n"
        "Context (if any): {context}\n\nCode:\n{code}"
    ),
} 