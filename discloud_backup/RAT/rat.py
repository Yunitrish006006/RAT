import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.utils import get
import config
id1 = 1003642488826900551
id2 = 1021197140334227456
id3 = 1006986600951058533
guild_from = 0
class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = id3))
            await tree.sync(guild = discord.Object(id = id2))
            await tree.sync(guild = discord.Object(id = id1))
            self.synced = True
        guild = client.get_guild(id3)
        if not get(guild.roles,name="⛏️-Miner"): await guild.create_role(name="⛏️-Miner",colour=discord.Colour.dark_gold(),hoist=True)
        if not get(guild.roles,name="🥦-farmer"): await guild.create_role(name="🥦-farmer",colour=discord.Colour.green(),hoist=True)
        if not get(guild.roles,name="⚒️-smith"): await guild.create_role(name="⚒️-smith",colour=discord.Colour.dark_grey(),hoist=True)
        if not get(guild.roles,name="🏹-hunter"): await guild.create_role(name="🏹-hunter",colour=discord.Colour.from_rgb(139,69,19),hoist=True)
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

class job_select(Select):
    def __init__(self):
        list = [
            discord.SelectOption(label="miner",emoji="⛏️",description="as u can see"),
            discord.SelectOption(label="farmer",emoji="🥦",description="as u can see"),
            discord.SelectOption(label="smith",emoji="⚒️",description="as u can see"),
            discord.SelectOption(label="hunter",emoji="🏹",description="as u can see")
        ]
        super().__init__( placeholder ="select your job", min_values=1, max_values=1,  options=list)
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name},You have select {self.values[0]} as your job",ephemeral=True)
        if self.values[0] == "miner":
            role = get(guild.roles, name="⛏️-Miner")
            await user.edit(roles=[role])
        elif self.values[0] == "farmer":
            role = get(guild.roles, name="🥦-farmer")
            await user.edit(roles=[role])
        elif self.values[0] == "smith":
            role = get(guild.roles, name="⚒️-smith")
            await user.edit(roles=[role])
        elif self.values[0] == "hunter":
            role = get(guild.roles, name="🏹-hunter")
            await user.edit(roles=[role])

class yes_no_view(View):
    @discord.ui.button(label="Yes",style=discord.ButtonStyle.green,emoji="👌")
    async def callback(self,button,interaction):
        await interaction.response.send_message("yee")

@tree.command(name="test_burron",description="a test button")
async def self(interaction:discord.Integration):
    view = View()
    yb = yes_button()
    nb = no_button()
    view.add_item(yb)
    view.add_item(nb)
    await interaction.response.send_message(f"Test",view=view,ephemeral=True)

@tree.command(name="close",description="turn off this bot globally")
async def self(interaction:discord.Integration,check:str):
    await interaction.response.send_message(f"turing off....")
    await client.close()

@tree.command(name="job",description="test of selector")
async def self(interaction:discord.Integration):
    view = View()
    view.add_item(job_select())
    await interaction.response.send_message(f"select your job",view=view,ephemeral=True)

client.run(config.token)
