import asyncio, os, re
import discord, requests

from contextlib import suppress
from discord.ext import commands

Prefix = '.'

Client_ID = os.environ['CLIENT_ID']
key = os.environ['TOKEN']

Guild_ID = 1
Developer_ID = os.environ['DEVELOPER_ID']

color = discord.Color.from_rgb(88, 100, 241)

Intents = discord.Intents.all()
Intents.guilds, Intents.members, Intents.messages = True, True, True

client = discord.Client(intents=Intents)

@client.event
async def on_ready():
    print(f"{client.user}!")


client.run(key)
