import discord
from discord.ext import commands
import os

TOKEN = os.environ.get("MTQ4Nzg2MTAyMDU5NTcyMDI3OQ.GUBJR-.Qr0HrqgMY1h1htwoGsDX_-lAHXNXvrvp9sV9IE")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} جاهز!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "هلا":
        await message.channel.send("أهلين:)")
    await bot.process_commands(message)

bot.run(TOKEN)
