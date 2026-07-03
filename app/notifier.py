import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(title, message, color=3066993, fields=None):
    if not DISCORD_WEBHOOK_URL:
        print("⚠️ Discord Webhook URL no configurada.")
        return

    payload = {
        "embeds": [
            {
                "title": title,
                "description": message,
                "color": color,
                "fields": fields or [],
                "footer": {"text": "DockerGuard-SecOps v1.0 | Homelab Agent"}
            }
        ]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code != 204:
            print(f"❌ Error enviando a Discord: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Falla de red en el webhook: {e}")