from openai import OpenAI

#calling ollama's llama3.1
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="llama3.1" 
)
response = client.chat.completions.create(
    model="llama3.1",                      
    messages=[
        {"role": "user", "content": "Tell me a joke!"}
    ]
)
print(response.choices[0].message.content)