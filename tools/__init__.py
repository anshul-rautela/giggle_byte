import json
from . import time_tools

_modules = [time_tools]

TOOL_SCHEMAS = []
_functions = {}
for module in _modules:
    TOOL_SCHEMAS += module.SCHEMAS
    _functions.update(module.FUNCTIONS)

def run_tool(name, arguments):
    func = _functions.get(name)
    args = json.loads(arguments) if arguments else {}
    return str(func(**args))