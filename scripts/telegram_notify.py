import os
import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    return response.json()

def main():
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    public_url = os.environ.get("PUBLIC_URL")
    
    if not public_url:
        public_url = "No URL obtained. Check cloudflared logs."
    
    message = f"""
🚀 *AI Model Auto Deployed!*

Model: `{os.environ.get('MODEL_NAME', 'unknown')}`
Public API URL: `{public_url}`

Use POST `{public_url}/generate` with JSON:
```json
{{"prompt": "Your text", "max_length": 100}}
