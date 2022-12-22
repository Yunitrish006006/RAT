import discord
from discord import app_commands
from discord.ui import Button, View
import config

class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 1021197140334227456))
            self.synced = True
        print(f"logged in as {self.user}")

client = bot_client()
tree = app_commands.CommandTree(client)

@tree.command(name="test",description="a test command",guild=discord.Object(id = 1021197140334227456))
async def self(interaction:discord.Integration,name: str):
    await interaction.response.send_message(f"Test:{name}")

class yes_button(Button):
    def __init__(self):
        super().__init__(label="Yes",style=discord.ButtonStyle.green,emoji="👌")
    async def callback(self,interaction):
        await interaction.response.send_message("ok",ephemeral=True)

class no_button(Button):
    def __init__(self):
        super().__init__(label="No",style=discord.ButtonStyle.red,emoji="❌")
    async def callback(self,interaction):
        await interaction.response.send_message("no",ephemeral=True)

class yes_no_view(View):
    @discord.ui.button(label="Yes",style=discord.ButtonStyle.green,emoji="👌")
    async def callback(self,button,interaction):
        await interaction.response.send_message("yee")
    

@tree.command(name="button_demo",description="a test button",guild=discord.Object(id = 1021197140334227456))
async def self(interaction:discord.Integration,name: str):
    view = yes_no_view()
    # yb = yes_button()
    # nb = no_button()
    # view.add_item(yb)
    # view.add_item(nb)
    await interaction.response.send_message(f"Test",view=view,ephemeral=True)

@tree.command(name="close",description="turn off this bot globally",guild=discord.Object(id = 1021197140334227456))
async def self(interaction:discord.Integration):
    await interaction.response.send_message(f"turing off....")
    await client.close()

client.run(config.token)
