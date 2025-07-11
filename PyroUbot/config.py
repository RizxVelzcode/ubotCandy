import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8087059316").split()))

API_ID = int(os.getenv("API_ID", "28207958"))

API_HASH = os.getenv("API_HASH", "e892e41a3289bb62455c8a84d14f2a38")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7914468140:AAENsRBycB_6NskrBbtZ19ElpZ1bZj0VAjQ")

OWNER_ID = int(os.getenv("OWNER_ID", "8087059316"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Tillulkuntulllsjjs:Tillulkuntulllsjjs@tillulkuntulllsjjs.yuhycve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002323130008"))
