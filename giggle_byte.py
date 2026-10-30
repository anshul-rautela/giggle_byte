import sys     
import random
import time
from openai import OpenAI
from spinner import Spinner 
from tools import TOOL_SCHEMAS, run_tool

#tool calls
def resolve_tool_calls(client, messages, model="llama3.1"):
    resp = client.chat.completions.create(
        model=model, messages=messages, tools=TOOL_SCHEMAS
    )
    msg = resp.choices[0].message
    if not msg.tool_calls:
        return  # model needs no (more) tools
    messages.append(msg)
    for call in msg.tool_calls:
        result = run_tool(call.function.name, call.function.arguments)
        messages.append(
            {"role": "tool", "tool_call_id": call.id, "content": result}
        )

# Helper function for typewriter effect
def typewriter_print(text, base_delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Add natural pauses for punctuation
        if char in [".", "!", "?", "\n"]:
            time.sleep(base_delay * 8)  # Pause longer on sentence stops
        elif char in [",", "-", ";", ":"]:
            time.sleep(base_delay * 4)  # Slight pause on punctuation
        else:
            # Slight random variation per character
            time.sleep(base_delay + random.uniform(-0.01, 0.015))
    print()


# 1. Initialize client (using local Ollama)
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

# 2. Set system persona
messages = [
    {
        "role": "system",
        "content": (
            "You are GiggleByte, a sharp-witted stand-up comedian turned AI assistant. "
            "Answer the user's question accurately, but infuse your explanation with clever puns, "
            "humorous analogies, and a lighthearted tone throughout. "
            "Remember prior details shared in this conversation and reference them naturally when relevant."
        )
    }
]
typewriter_print("Hello! Welcome to GiggleByte—your personal stand-up comedian assistant. Ask me anything, and I will deliver the answers with a side of laughs. Type 'exit' to stop.\n")

# 3. Main conversation loop
while True:
    user_input = input("You: ")
    if(user_input.lower().strip() in ["exit"]):
        print("GiggleByte:", end="")
        typewriter_print("Goodbye! Catch ya on the flip side! 👋")
        break

    spinner = Spinner("GiggleByte is typing")
    spinner.start()
    messages.append({"role":"user","content":user_input})
    resolve_tool_calls(client, messages) 
    response = client.chat.completions.create(
        model="llama3.1",                      
        stream=True,
        messages = messages
    )

    full_reply = ""
    spinner.stop()
    print("GiggleByte: ",end ="",flush =True)

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)          
            full_reply += content   

    print("\n")
    messages.append({"role":"assistant","content":full_reply})


