import openai

openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXX"

messages = [
    {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
]

while True:
    message = input("* User: ")
    if message == "exit":
        break
    if message == "clear":
        print("\033[H\033[J")
        continue
        
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat_completion["choices"][0]["message"]["content"]
    print(f"* Assistant: {reply}")
    messages.append({"role": "assistant", "content": reply})    