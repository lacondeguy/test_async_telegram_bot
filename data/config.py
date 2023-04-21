import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWM_TOKEN = os.getenv("OWM_TOKEN")
FIXER_TOKEN = os.getenv("FIXER_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")