import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.utils import get

NCUE = 764126539041734679


guilds = [
    1021197140334227456,
    764126539041734679,
    1006986600951058533
]
token="MTAyMDM1OTg0NTU5NTA1NDA4MA.GOf8cn.wOtFJKWl8wR-r1WjM4Lw8dfG_UPFJWxM0sVDLk"
jobs = [
    discord.SelectOption(label="miner",emoji="⛏️",description="a career that can get lot of jeweris"),
    discord.SelectOption(label="farmer",emoji="🥦",description="a career that can grow foods"),
    discord.SelectOption(label="smith",emoji="⚒️",description="a career that can make tools and weapons"),
    discord.SelectOption(label="hunter",emoji="🏹",description="a career that can get meats from nature")
]

department_and_grade = [
    discord.SelectOption(label="資工系",emoji="👓",description="資訊工程學系",),
    discord.SelectOption(label="資管系",emoji="🔐",description="資訊管理學系"),
    discord.SelectOption(label="電機系",emoji="🪛",description="電機工程學系"),
    discord.SelectOption(label="機電系",emoji="⚙️",description="機電工程學系")
]

def get_option_name(option:discord.SelectOption):
    return option.emoji.name+"."+option.label

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
            career_colors = [discord.Colour.dark_gold(),discord.Colour.green(),discord.Colour.dark_grey(),discord.Colour.from_rgb(139,69,19)]
            if(i == 764126539041734679):
                for n in [get_option_name(j) for j in department_and_grade]:
                    if not get(guild.roles,name=n):
                        await guild.create_role(name=n,hoist=True)
            else:
                for career,color in zip([get_option_name(j) for j in jobs],career_colors):
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
        super().__init__(
            placeholder ="select your job",
            min_values=1,
            max_values=1,
            options=jobs
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} select {self.values[0]} as job",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)
            
class department_select(Select):
    def __init__(self):
        super().__init__(
            placeholder ="選擇你的系級",
            min_values=1,
            max_values=1,
            options=department_and_grade
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} 已加入 {self.values[0]}",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

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
@tree.command(name="選擇系級",description="選擇自己系級以加入相關討論區",guild=discord.Object(id=764126539041734679))
async def self(interaction:discord.Integration):
    view = View()
    view.add_item(department_select())
    await interaction.response.send_message(f"選擇你的系級",view=view,ephemeral=False)

client.run(token)
