import json

def load_json(path):
  with open(path) as f:
    text = f.read()
  return json.loads(text)

def write_json(path, data_obj):
  json_str = json.dumps(data_obj, indent=2)
  with open(path, 'w') as f:
    f.write(json_str)

