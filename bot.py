import discord
import os
import dotenv as dv
from quotesgeneratorapi_wrapper.quotesgenerator import getQuotes
from mylist import mylist
import random

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
    if message.content.startswith("$quote"):
        category = len(mylist)
        category = mylist[random.randint(a=0, b=category)]
        await message.channel.send(getQuotes(api_key=APININJA_TOKEN, category=category))


client.run(token=TOKEN_DISCORD)
