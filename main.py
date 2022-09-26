import asyncio
import discord
import os
import json
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "!",intents=intents,help_command=None)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension("cogs." + filename[:-3])
            print("cogs." + filename[:-3])

async def main():
    await load()
    with open('items.json',"r",encoding="utf8") as file:
        data = json.load(file)
    await bot.start(data['token'])

asyncio.run(main())