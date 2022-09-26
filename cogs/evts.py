import discord
from discord.ext import commands

class evts(commands.Cog):
    def __init__(self, client):
        self.client = client
	
    @commands.Cog.listener()
    async def on_ready(self):
        await print("bot launched")
	
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

async def setup(client):
	await client.add_cog(evts(client))