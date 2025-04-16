import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from webhook_server import app, discord_client
import uvicorn
from db import init_db, init_mapping_table

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
discord_client = bot

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def main():
    init_db()
    init_mapping_table()
    await bot.load_extension("cogs.request")
    await bot.load_extension("cogs.admin")  # <-- flyttad hit!
    
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    
    await asyncio.gather(
        bot.start(TOKEN),
        server.serve()
    )

asyncio.run(main())
