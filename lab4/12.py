import json

def deep_diff(obj1, obj2, path=""):
    diffs = []
    keys = set(obj1.keys()).union(obj2.keys())
    
    for key in keys:
        current_path = f"{path}.{key}" if path else key
        val1 = obj1.get(key, "<missing>")
        val2 = obj2.get(key, "<missing>")
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            diffs.extend(deep_diff(val1, val2, current_path))
        elif val1 != val2:
            v1 = json.dumps(val1, separators=(',', ':')) if val1 != "<missing>" else "<missing>"
            v2 = json.dumps(val2, separators=(',', ':')) if val2 != "<missing>" else "<missing>"
            diffs.append(f"{current_path} : {v1} -> {v2}")
    
    return diffs

obj1 = json.loads(input())
obj2 = json.loads(input())
differences = deep_diff(obj1, obj2)
if differences:
    for line in sorted(differences):
        print(line)
else:
    print("No differences")