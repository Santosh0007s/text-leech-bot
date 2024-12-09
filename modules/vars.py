import os

API_ID    = os.environ.get("API_ID", "22624627")
API_HASH  = os.environ.get("API_HASH", "361cbca2db6bb5cba3a0a8b8f8f31dfa")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
