from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents , command_prefix="!")

@bot.event
async def on_ready():
    print("勞贖出現了!")

# @bot.event
# async def on_ready():
#     print('Login As：', bot.user)
#     game = discord.Game('lol')
#     await bot.change_presence(status=discord.Status.online, activity=game)

import json

with open('items.json',"r",encoding="utf8") as file:
    data = json.load(file)
bot.run(data['token'])
