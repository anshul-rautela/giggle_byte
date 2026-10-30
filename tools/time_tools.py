from datetime import datetime
def get_current_datetime():
    return datetime.now().strftime("%A, %d %B %Y, %I:%M %p")

SCHEMAS = [{
    "type": "function",
    "function": {
        "name": "get_current_datetime",
        "description": "Get the current local date, time and day of the week. Use this whenever the user asks what time or date it is.",
        "parameters": {"type": "object", "properties": {}},
    },
}]

FUNCTIONS = {"get_current_datetime": get_current_datetime}
