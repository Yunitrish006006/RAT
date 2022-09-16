from genericpath import commonprefix
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

import json

with open('items.json',"r",encoding="utf8") as file:
    data = json.load(file)
client.run(data['token'])