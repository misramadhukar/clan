import subprocess
import os

def execute_command(command, shell_type="bash"):
    if shell_type == "bash":
        shell_executable = "/bin/bash" if os.name != "nt" else "C:\\Program Files\\Git\\bin\\bash.exe"
    elif shell_type == "git bash":
        shell_executable = "C:\\Program Files\\Git\\bin\\bash.exe"
    elif shell_type == "powershell":
        shell_executable = "powershell.exe"
    elif shell_type == "shell":
        shell_executable = None  # Use default
    else:
        shell_executable = None
    try:
        result = subprocess.run(command, shell=True, executable=shell_executable, capture_output=True, text=True)
        output = result.stdout.strip()
        error = result.stderr.strip()
        return {"output": output, "error": error, "returncode": result.returncode}
    except Exception as e:
        return {"output": "", "error": str(e), "returncode": -1} 