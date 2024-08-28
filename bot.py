import discord
import os
import dotenv as dv
from quotesgeneratorapi_wrapper.quotesgenerator import getQuotes

dv.load_dotenv()
TOKEN_DISCORD = os.getenv("TOKEN_DISCORD")
APININJA_TOKEN = os.getenv("APININJA_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send(getQuotes(APININJA_TOKEN))


client.run(token=TOKEN_DISCORD)
