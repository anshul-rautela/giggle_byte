from openai import OpenAI

#calling ollama's llama3.1
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="llama3.1" 
)
messages = [
    {
        "role": "system",
        "content": (
            "You are GiggleByte, a sharp-witted stand-up comedian turned AI assistant. "
            "Answer the user's question accurately, but infuse your explanation with clever puns, "
            "humorous analogies, and a lighthearted tone throughout."
        )
    }
]
print("Hello welcome to GiggleByte! Type 'exit' to stop.\n")
while True:
    user_input = input("You: ")
    if(user_input.lower().strip() in ["exit"]):
        print("GiggleByte: Catch ya on the flip side! 👋")
        break
    
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model="llama3.1",                      
        stream=True,
        messages = messages
    )
    full_reply = ""

    print("GiggleByte: ", end="", flush=True)

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)          
            full_reply += content   

    print("\n")
    messages.append({"role":"assistant","content":full_reply})