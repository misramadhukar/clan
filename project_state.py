import os

class ProjectState:
    def __init__(self):
        self.files = {}  # { "path/to/file.py": "file_content", ... }

    def read_file(self, path):
        return self.files.get(path)

    def write_file(self, path, content):
        self.files[path] = content

    def list_files(self):
        return list(self.files.keys())

    def get_project_view(self):
        # Returns a string representation of the project tree
        tree = {}
        for file_path in self.files:
            parts = file_path.split('/')
            d = tree
            for part in parts[:-1]:
                if part not in d or d[part] is None:
                    d[part] = {}
                d = d[part]
            # If the last part is already a dict (directory), leave it; else set to None (file)
            if parts[-1] not in d:
                d[parts[-1]] = None
            elif isinstance(d[parts[-1]], dict):
                pass  # already a directory
            else:
                d[parts[-1]] = None
        def _tree_str(d, prefix=""):
            s = ""
            for k, v in d.items():
                s += prefix + k + ('/' if isinstance(v, dict) else '') + '\n'
                if isinstance(v, dict):
                    s += _tree_str(v, prefix + '  ')
            return s
        return _tree_str(tree)

    def commit_to_disk(self, root_dir):
        for path, content in self.files.items():
            full_path = os.path.join(root_dir, path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content) 