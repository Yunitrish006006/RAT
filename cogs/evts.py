from importlib.resources import contents
import discord
import json
from discord.ext import commands

class evts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await print("bot launched")
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('items.json',"r",encoding="utf8") as file:
            data = json.load(file)
        channel = self.client.get_channel(int(data["Welcome_channel"]))
        await channel.send(f"{member.mention} welcome")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        with open('items.json',"r",encoding="utf8") as file:
            data = json.load(file)
        channel = self.client.get_channel(int(data["Leave_channel"]))
        await channel.send(f"{member.mention} bye")

    @commands.Cog.listener()
    async def on_message(self,msg):
        with open('items.json',"r",encoding="utf8") as file:
            data = json.load(file)
        temp_dic = data["key_word"]
        if msg.content.endswith("88") and msg.author != self.client.user:
            await msg.channel.reply("88")
        elif msg.content in temp_dic and msg.author != self.client.user:
            await msg.channel.send(msg.content)

async def setup(client):
	await client.add_cog(evts(client))