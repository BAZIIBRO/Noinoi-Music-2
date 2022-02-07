from NoinoiMusic.config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":noinoi:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "NoinoiMusic"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

call_py = PyTgCalls(user, overload_quiet_mode=True)
