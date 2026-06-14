import os
from datetime import datetime


def save_email(content: str):
    os.makedirs("saved_emails", exist_ok=True)

    filename = f"saved_emails/email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename