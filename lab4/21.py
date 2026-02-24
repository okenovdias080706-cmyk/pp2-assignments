import importlib
import sys

q = int(sys.stdin.readline())

for _ in range(q):
    module_path, attr_name = sys.stdin.readline().strip().split()
    
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    
    if not hasattr(module, attr_name):
        print("ATTRIBUTE_NOT_FOUND")
        continue
    
    attr = getattr(module, attr_name)
    
    if callable(attr):
        print("CALLABLE")
    else:
        print("VALUE")