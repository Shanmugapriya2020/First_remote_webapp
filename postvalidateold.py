
import anthropic

client = anthropic.Anthropic(
    api_key="<<YOUR_API_KEY_GOES_HERE>>",
)

# Read the prompt from file
with open("sample_input_prompt.txt", "r", encoding="utf-8") as f:
    user_prompt = f.read()

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                }
            ]
        }
    ],
    thinking={
        "type": "enabled",
        "budget_tokens": 16000
    }
)
print(message.content)