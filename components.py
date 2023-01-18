import discord
from discord.ui import Select
from discord import SelectOption
from discord.utils import get
from discord import Colour
#================================================================
from datetime import datetime
class log:
    text=""
    time_formet="[%Y/%m/%d %H:%M:%S]  "
    sync_log = False
    def __init__(self,time_mode:str = "default",sync_log:bool=False) -> None:
        self.set_time_mode(time_mode)
        self.text+="⚙️[ Log System ]\n"
        self.sync_log=sync_log
    def println(self,content:str="\n"):
        temp=datetime.now().strftime(self.time_formet)+" "+content
        self.text+=temp+"\n"
        if self.sync_log:print(temp)
    def print(self,content:str="\n"):
        temp=datetime.now().strftime(self.time_formet)+" "+content
        self.text+=temp
        if self.sync_log:print(temp)
    def show(self):
        return self.text
    def set_time_mode(self,mode:str):
        if(mode=="off"):
            self.time_formet=""
        elif(mode=="default"):
            self.time_formet="[%Y/%m/%d %H:%M:%S]"
        elif(mode=="time_only"):
            self.time_formet="[%H:%M:%S]"
        elif(mode=="day_only"):
            self.time_formet="[%Y/%m/%d]"
#statistic=======================================================
available_servers = ['彰化師範大學','無名氏','三隻狗','Yun 的伺服器',"Yunitrish's server","嵌入式系統 測試伺服器"]
#functions=======================================================
def pickup(guild_list:list[discord.Guild],log:log):
    to_enable:list[discord.Guild] = []
    for g in guild_list:
            if g.name in available_servers:
                to_enable.append(g)
                log.println("🟢  " + g.name)
            else:
                log.println("🔴  " + g.name)
    return to_enable
#================================================================
jobs = [
    discord.SelectOption(label="miner",emoji="⛏️",description="a career that can get lot of jeweris"),
    discord.SelectOption(label="farmer",emoji="🥦",description="a career that can grow foods"),
    discord.SelectOption(label="smith",emoji="⚒️",description="a career that can make tools and weapons"),
    discord.SelectOption(label="hunter",emoji="🏹",description="a career that can get meats from nature")
]
job_colors = [Colour.dark_gold(),Colour.green(),Colour.dark_grey(),Colour.from_rgb(139,69,19)]
#=====================================================================彰師大伺服器專用========================================================================
departments = [
    discord.SelectOption(label="資工系",emoji="👓",description="資訊工程學系"),
    discord.SelectOption(label="資管系",emoji="🔐",description="資訊管理學系"),
    discord.SelectOption(label="電機系",emoji="🪛",description="電機工程學系"),
    discord.SelectOption(label="機電系",emoji="⚙️",description="機電工程學系"),
    discord.SelectOption(label="電子系",emoji="📟",description="電子工程學系")
]
department_colors = [Colour.blue(),Colour.blue(),Colour.blue(),Colour.blue(),Colour.blue()]
grades = [discord.SelectOption(label=str(i)) for i in range(109,115)]
#===========================================================================
def add_userdata(add):
    out = []
    lst = [line.strip('\n').split(" ") for line in open(os.getcwd()+'/database/identify.txt').readlines()]
    for i in lst:
        cnt = 0
        #把檔案重複名字更新只留最後一個
        for j in out:
            if i[0]==j[0]:
                j[1]=i[1]
            else:
                cnt+=1
        if cnt == len(out):
            out.append(i)
    #如果新加入的user名字存在在檔案中 -> 更新檔案
    cnt = 0
    for i in out:
        if add[0]==i[0]:
            i[1]=add[1]
        else:
            cnt += 1
    if cnt == len(out):
        out.append(add)
    with open(os.getcwd()+'/database/identify.txt', 'w') as f:
        for i in out:
            f.write(str(i[0])+" "+str(i[1])+"\n")