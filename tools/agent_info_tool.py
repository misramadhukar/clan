import yaml
import os

def load_agent_info(yaml_path=None):
    if yaml_path is None:
        yaml_path = os.path.join(os.path.dirname(__file__), '../data/agent_info.yaml')
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('agents', []) 