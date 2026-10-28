from openai import OpenAI
from spinner import Spinner 

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
print("Hello! Welcome to GiggleByte! Type 'exit' to stop.\n")

# 3. Main conversation loop
while True:
    user_input = input("You: ")
    if(user_input.lower().strip() in ["exit"]):
        print("GiggleByte: Catch ya on the flip side! 👋")
        break

    spinner = Spinner("GiggleByte is typing")
    spinner.start()
    messages.append({"role":"user","content":user_input})
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