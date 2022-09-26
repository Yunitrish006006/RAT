import discord
import json
import random
from discord.ext import commands

class cmds(commands.Cog):
    def __init__(self, client):
        self.client = client
	
    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f"Result: {round(self.client.latency * 1000)}ms")
    
    @commands.command(aliases = ['rp','rpt'])
    async def repeat(self,ctx,*,option):
        await ctx.send(f"u said {option}")

    @commands.command()
    async def random_local_picture(self,ctx):
        with open('items.json',"r",encoding="utf8") as file:
            data = json.load(file)
        random_picture = random.choice(data['local_picture'])
        picture = discord.File(random_picture)
        await ctx.reply(file = picture)

    @commands.command()
    async def random_net_picture(self,ctx):
        with open('items.json',"r",encoding="utf8") as file:
            data = json.load(file)
        random_picture = random.choice(data['net_picture'])
        await ctx.reply(random_picture)

async def setup(client):
	await client.add_cog(cmds(client))