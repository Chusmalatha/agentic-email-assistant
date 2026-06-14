import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel

from tools import save_email

load_dotenv()

model = GroqModel(
    model_name="llama-3.3-70b-versatile"
)

agent = Agent(
    model,
    system_prompt="""
You are an AI Email Assistant.

Rules:
1. First, generate the professional email based on the user's request.
2. Once the email is generated, call the `save_generated_email` tool to save it. Do not output any conversational text or final response to the user in the same turn that you call the tool.
3. After the tool executes and returns the file path, write the final response to the user: start by printing the file location where the email was saved, followed by a blank line, and then the complete generated email content.
4. Never show raw tool calls, function tags (like `<function=...>` or `</function>`), JSON, or function syntax in your final response to the user.
"""
)


@agent.tool_plain
def save_generated_email(email_content: str) -> str:
    path = save_email(email_content)

    return f"""
EMAIL_PATH:
{path}

EMAIL_CONTENT:
{email_content}
"""