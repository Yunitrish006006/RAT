import discord
from discord.ui import Select
from discord import SelectOption
from Log import log

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

available_servers = ['彰化師範大學','無名氏','三隻狗','Yun 的伺服器']

class slection(Select):
    def __init__(self, *, custom_id: str = "job_selection", placeholder:str = "select your job", min_values: int = 1, max_values: int = 1, options: list[SelectOption] = ..., disabled: bool = False, row: int = None) -> None:
        super().__init__(custom_id=custom_id, placeholder=placeholder, min_values=min_values, max_values=max_values,options=options, disabled=disabled, row=row)


def pickup(guild_list:list,log:log):
    temp = []
    for g in guild_list:
            if g.name in available_servers:
                temp.append(g)
                log.println("🟢  " + g.name)
            else:
                log.println("🔴  " + g.name)
    return temp
def get_ids(guild_list:list):
    temp = []
    for guild in guild_list:
        temp.append(guild.id)
    return temp