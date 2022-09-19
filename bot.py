import discord
import json
import random
from discord.ext import commands

with open('items.json',"r",encoding="utf8") as file:
    data = json.load(file)

bot = commands.Bot(intents=discord.Intents.all() , command_prefix="!")

@bot.event
async def on_ready():
    print('Login As：', bot.user)
    game = discord.Game('Eating oil')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(data['Welcome_channel'])
    await channel.send(f"{member} join!!")
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(data['Leave_channel'])
    await channel.send(f"{member} leave!!")
    print(f"{member} leave!")

@bot.command()
async def latency(ctx):
    await ctx.reply(f"Result: {round(bot.latency * 1000)}ms")

@bot.command()
async def random_local_picture(ctx):
    random_picture = random.choice(data['local_picture'])
    picture = discord.File(random_picture)
    await ctx.reply(file = picture)

@bot.command()
async def random_net_picture(ctx):
    random_picture = random.choice(data['net_picture'])
    await ctx.reply(random_picture)

bot.run(data['token'])