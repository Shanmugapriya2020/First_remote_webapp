import os
import anthropic
from dotenv import load_dotenv

# Load your .env file to get the API key
load_dotenv()

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Read user prompt from a Markdown file
markdown_file = "sample_input_prompt.md"  # Change filename if needed
with open(markdown_file, "r", encoding="utf-8") as f:
    user_prompt = f.read()

# Create message to Claude
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": user_prompt}
            ]
        }
    ]
)

# Get the text content from Claude
response_text = message.content[0].text

# Print or save to file
print(" Claude Response:\n")
print(response_text)

output_file = "output_from_claude.yaml"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(response_text)

# Optional: print confirmation
print(" Claude Response saved as YAML:")
print(f" {os.path.abspath(output_file)}")