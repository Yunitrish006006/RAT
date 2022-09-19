import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all() , command_prefix="!")

@bot.event
async def on_ready():
    print('Login As：', bot.user)
    game = discord.Game('Eating oil')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1021197140892061778)
    await channel.send(f"{member} join!!")
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1021197140892061778)
    await channel.send(f"{member} leave!!")
    print(f"{member} leave!")

@bot.command()
async def getBotLatency(ctx):
    await ctx.reply(f"Result: {round(bot.latency * 1000)}ms")

import json
with open('items.json',"r",encoding="utf8") as file:
    data = json.load(file)
bot.run(data['token'])
