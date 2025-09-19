from openai import OpenAI

# Initialize client
client = OpenAI(api_key="your_api_key_here")

# Make a request to GPT (with Codex abilities built-in)
response = client.chat.completions.create(
    model="gpt-4o-mini",  # you can also use gpt-4.1, gpt-4o, or gpt-5 when available
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Write a Python function that checks if a number is prime."}
    ]
)

print(response.choices[0].message.content)
