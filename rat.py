import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.utils import get
guilds = [
    1021197140334227456,
    764126539041734679,
    1006986600951058533
]
token="MTAyMDM1OTg0NTU5NTA1NDA4MA.GOf8cn.wOtFJKWl8wR-r1WjM4Lw8dfG_UPFJWxM0sVDLk"
class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            for guild_id in guilds:
                await tree.sync(guild=discord.Object(id=guild_id))
            self.synced = True
        for i in guilds:
            guild = client.get_guild(i)
            careers = ["⛏️.Miner","🥦.farmer","⚒️.smith","🏹.hunter"]
            career_colors = [discord.Colour.dark_gold(),discord.Colour.green(),discord.Colour.dark_grey(),discord.Colour.from_rgb(139,69,19)]
            for career,color in zip(careers,career_colors):
                if not get(guild.roles,name=career):
                    await guild.create_role(name=career,colour=color,hoist=True)
        print(f"logged in as {self.user}")

client = bot_client()
tree = app_commands.CommandTree(client)

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
        careers = [
            get(guild.roles, name="⛏️.Miner"),
            get(guild.roles, name="🥦.farmer"),
            get(guild.roles, name="⚒️.smith"),
            get(guild.roles, name="🏹.hunter")
        ]
        await interaction.response.send_message(f"{user.name},You have select {self.values[0]} as your job",ephemeral=True)
        await user.remove_roles(careers)
        if self.values[0] == "miner":
            await user.add_roles(careers[0])
        elif self.values[0] == "farmer":
            await user.add_roles(careers[1])
        elif self.values[0] == "smith":
            await user.add_roles(careers[2])
        elif self.values[0] == "hunter":
            await user.add_roles(careers[3])

class yes_no_view(View):
    @discord.ui.button(label="Yes",style=discord.ButtonStyle.green,emoji="👌")
    async def callback(self,button,interaction):
        await interaction.response.send_message("yee")
for guild_id in guilds:
    @tree.command(name="test",description="a test command",guild=discord.Object(id=guild_id))
    async def self(interaction:discord.Integration,name: str):
        await interaction.response.send_message(f"Test:{name}")

    @tree.command(name="test_button",description="a test button",guild=discord.Object(id=guild_id))
    async def self(interaction:discord.Integration):
        view = View()
        yb = yes_button()
        nb = no_button()
        view.add_item(yb)
        view.add_item(nb)
        await interaction.response.send_message(f"Test",view=view,ephemeral=True)

    @tree.command(name="close",description="turn off this bot globally",guild=discord.Object(id=guild_id))
    async def self(interaction:discord.Integration,password:str):
        if password=="ratoff":
            await interaction.response.send_message(f"turing off rat .....")
            await client.close()

    @tree.command(name="job",description="test of selector",guild=discord.Object(id=guild_id))
    async def self(interaction:discord.Integration):
        view = View()
        view.add_item(job_select())
        await interaction.response.send_message(f"select your job",view=view,ephemeral=True)

client.run(token)
