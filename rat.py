import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.utils import get
from discord import Colour

NCUE = 764126539041734679
token="MTAyMDM1OTg0NTU5NTA1NDA4MA.GOf8cn.wOtFJKWl8wR-r1WjM4Lw8dfG_UPFJWxM0sVDLk"
guild_list = []
jobs = [
    discord.SelectOption(label="miner",emoji="⛏️",description="a career that can get lot of jeweris"),
    discord.SelectOption(label="farmer",emoji="🥦",description="a career that can grow foods"),
    discord.SelectOption(label="smith",emoji="⚒️",description="a career that can make tools and weapons"),
    discord.SelectOption(label="hunter",emoji="🏹",description="a career that can get meats from nature")
]
departments = [
    discord.SelectOption(label="資工系",emoji="👓",description="資訊工程學系"),
    discord.SelectOption(label="資管系",emoji="🔐",description="資訊管理學系"),
    discord.SelectOption(label="電機系",emoji="🪛",description="電機工程學系"),
    discord.SelectOption(label="機電系",emoji="⚙️",description="機電工程學系")
]
grades = [discord.SelectOption(label=str(i)) for i in range(109,115)]

async def initialize_roles(guild_id,selections:list[discord.SelectOption],colors:list[discord.Colour]):
    guild = client.get_guild(guild_id)
    for n in range(len(selections)):
        if selections[n].emoji == None : val = selections[n].label
        else: val = (selections[n].emoji).name+"."+selections[n].label
        if not get(guild.roles,name=val): 
            await guild.create_role(name=val,hoist=True,colour=colors[n])

class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        global guild_list
        await self.wait_until_ready()
        guild_list = [g for g in client.guilds]
        remove_list = []
        for g in guild_list:
            if g.name not in ['彰化師範大學','無名氏','三隻狗']:
                remove_list.append(g)
                print("🔴  " + g.name)
            else:
                print("🟢  " + g.name)
        for i in remove_list: guild_list.remove(i)

        
        if not self.synced:
            for g in guild_list:
                print("Synchronizing "+g.name+".....")
                await tree.sync(guild=discord.Object(id=g.id))
            self.synced = True
        for i in guild_list:
            career_colors = [Colour.dark_gold(),Colour.green(),Colour.dark_grey(),Colour.from_rgb(139,69,19)]
            if(i.id == NCUE):
                await initialize_roles(guild_id=i.id,selections=departments+grades,colors=[Colour.blue() for _ in range(len(departments+grades))])
            else:
                await initialize_roles(guild_id=i.id,selections=jobs,colors=career_colors)
        print(f"logged in as {self.user}")

client = bot_client()
tree = app_commands.CommandTree(client)

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
            placeholder ="選擇你的科系",
            min_values=1,
            max_values=1,
            options=departments
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} 已加入 {self.values[0]}",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

class grade_select(Select):
    def __init__(self):
        super().__init__(
            placeholder = "選擇你的級數",
            min_values=1,
            max_values=1,
            options=grades
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} 已加入 {self.values[0]}",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.label)
            if current.name==self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

class yes_no_view(View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Button(style=discord.ButtonStyle.green,emoji="✔"))
        self.add_item(Button(style=discord.ButtonStyle.red,emoji="✘"))

class select_view(View):
    def __init__(self,item,timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(item)

for g in guild_list:
    @tree.command(name="test",description="a test command",guild=g)
    async def self(interaction:discord.Integration,name: str):
        await interaction.response.send_message(f"Test:{name}")

    @tree.command(name="test_button",description="a test button",guild=g)
    async def self(interaction:discord.Integration):
        await interaction.response.send_message(f"Test",view=yes_no_view(),ephemeral=True)

    @tree.command(name="close",description="turn off this bot globally",guild=g)
    async def self(interaction:discord.Integration,password:str):
        if password=="ratoff":
            await interaction.response.send_message(f"turing off rat .....")
            await client.close()

    @tree.command(name="job",description="test of selector",guild=g)
    async def self(interaction:discord.Integration):
        await interaction.response.send_message(f"select your job",view=select_view(job_select()),ephemeral=True)
    if(g.id == NCUE):
        @tree.command(name="選擇科系",description="選擇自己科系以加入相關討論區",guild=g)
        async def self(interaction:discord.Integration):
            await interaction.response.send_message(f"選擇你的科系",view=select_view(department_select()),ephemeral=False)
        @tree.command(name="選擇級數",description="選擇自己級數以加入相關討論區",guild=g)
        async def self(interaction:discord.Integration):
            await interaction.response.send_message(f"選擇你的級數",view=select_view(grade_select()),ephemeral=False)

client.run(token)
