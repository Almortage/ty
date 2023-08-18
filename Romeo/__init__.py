import os
import asyncio
import logging
from config import *
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from Romeo.Helpers.data import LOG_TEXT
from pyromod import listen 


if not START_PIC:
    START_PIC = "https://telegra.ph//file/a9a90059ae47fa840b0b3.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "romeorj",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN )
    


async def Romeo():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]ALMORTAGEL...")
    LOG.print("[bold yellow]sᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ɴᴏᴡ.......")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(Romeo())
