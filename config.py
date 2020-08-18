import os
import re
import json

def jsonc_to_json(string):
    # ブロックコメント除去
    string = re.sub(r'/\*.*?\*/', r'', string, flags=re.DOTALL)

    # ラインコメント除去
    string = re.sub(r'//.*\n', r'\n', string)
    return '\n'.join(filter(lambda x: x.strip(), string.split('\n')))

def get_config(filename='config.jsonc'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, filename)
    with open(json_path, "r", encoding="utf-8") as fp:
        jsonc=fp.read()
        config = json.loads( jsonc_to_json(jsonc))
        return config