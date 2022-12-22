import discord
import json
import random
from discord.ext import commands

class cmds(commands.Cog):
    def __init__(self, client):
        self.client = client
	
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f"Result: {round(self.client.latency * 1000)}ms")
    
    @commands.command(aliases = ['rp','rpt'])
    async def repeat(self,ctx,*args):
        await ctx.send(' '.join(args))

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
    
    @commands.command()
    async def dlt(self, ctx, *args):
        mesg = ' '.join(args)
        await ctx.send(mesg)
        await ctx.message.delete()
        
async def setup(client):
	await client.add_cog(cmds(client))