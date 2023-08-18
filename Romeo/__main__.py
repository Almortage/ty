
import asyncio
import importlib

from pyrogram import idle
from Romeo import LOG
from Romeo.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Romeo.modules." + all_module)
    LOG.print("[bold yellow]تم تشغيل بوتك")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
