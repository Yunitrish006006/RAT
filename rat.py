from dis import disco
from typing import Optional
from unittest import result
import discord
import discord.ui
from discord import app_commands
from components import log,pickup
from discord.utils import get
from components import jobs,job_colors,departments,department_colors
from random import randint
from x import token
from datetime import datetime
import asyncio
import os, sys
from random import shuffle

ENABLED_GUILDS:list[discord.Object]=[]

GUILDS:list[discord.Guild]=[]

class RAT(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        # for guild in [discord.Object(id=1060524409460379768),discord.Object(id=764126539041734679),discord.Object(id=1003642488826900551)]:
        #     self.tree.copy_global_to(guild=guild)
        #     await self.tree.sync(guild=guild)
        print("setting up hook")
        self.add_view(RPG_status_board_view())

client = RAT(intents=discord.Intents.default())
history = log(sync_log=True)

@client.event
async def on_ready():
    history.println(f'~ $ 機器人[{client.user}](ID: {client.user.id})已啟動')
    global GUILDS,ENABLED_GUILDS
    GUILDS = [guild for guild in client.guilds]
    history.println('=====================篩選伺服器中=======================')
    GUILDS = pickup(GUILDS,history)
    history.println("======================篩選後名單========================")
    for guild in GUILDS:
        history.println(guild.name)
        ENABLED_GUILDS.append(discord.Object(id=guild.id))
    history.println('===================同步伺服器指令中=====================')
    for guild in ENABLED_GUILDS:
        if(client.get_guild(guild.id).name!="彰化師範大學"):
            history.println("同步"+client.get_guild(guild.id).name+"指令中....")
            client.tree.copy_global_to(guild=guild)
            await client.tree.sync(guild=guild)
        else:
            history.println("同步"+client.get_guild(guild.id).name+"指令中....")
            client.tree.copy_global_to(guild=guild)
            await client.tree.sync(guild=guild)
    history.println("=====================初始化身分組=======================")
    for go in ENABLED_GUILDS:
        if(client.get_guild(guild.id).name!="彰化師範大學"):
            guild = client.get_guild(go.id)
            for selection,color in zip(jobs,job_colors):
                if selection.emoji == None : role_name = selection.label
                else: role_name = (selection.emoji).name+"."+selection.label
                if not get(guild.roles,name=role_name): 
                    await guild.create_role(name=role_name,hoist=True,colour=color)
                    history.println("創建 "+role_name+" 至 "+guild.name)
        else:
            guild = client.get_guild(go.id)
            for selection,color in zip(departments,department_colors):
                if selection.emoji == None : role_name = selection.label
                else: role_name = (selection.emoji).name+"."+selection.label
                if not get(guild.roles,name=role_name): 
                    await guild.create_role(name=role_name,hoist=True,colour=color)
                    history.println("創建 "+role_name+" 至 "+guild.name)
        history.println(guild.name+" 初始化完畢")
    history.println("========================================================")
#=================================================================================================
class RPG_status_board_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="refresh",custom_id="RPG_status_board.refresh_button")
    async def test(self,interaction:discord.Interaction,Button:discord.ui.Button):
        await interaction.response.edit_message(content=interaction.message.content+"#")
    
@client.tree.command(name="test")
async def test(interaction:discord.Interaction):
    await interaction.response.send_message(content="button!",view=RPG_status_board_view())
#=================================================================================================
class job_select(discord.ui.Select):
    def __init__(self,history:log):
        super().__init__(
            placeholder ="職業類別",
            min_values=1,
            max_values=1,
            options=jobs
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        ########################################################################
        def add_userdata(add):
            out = []
            lst = [line.strip('\n').split(" ") for line in open(os.getcwd()+'/database/jobs.txt').readlines()]
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
            with open(os.getcwd()+'/database/jobs.txt', 'w') as f:
                for i in out:
                    f.write(str(i[0])+" "+str(i[1])+"\n")
        ########################################################################
        user_name=str(user.name).replace(" ","_")
        add_userdata([user_name,str(self.values[0])])
        await interaction.response.send_message(f"{user_name} 選擇了 {self.values[0]} 作為職業",ephemeral=True)
        history.println(f"{user_name} 選擇了 {self.values[0]} 作為職業")
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

class department_select(discord.ui.Select):
    def __init__(self,history:log):
        super().__init__(
            placeholder ="科系",
            min_values=1,
            max_values=1,
            options=departments
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        ########################################################################
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
        ########################################################################
        user_name=str(user.name).replace(" ","_")
        add_userdata([user_name,str(self.values[0])])
        await interaction.response.send_message(f"{user_name} 選擇了 {self.values[0]} 科系",ephemeral=True)
        history.println(f"{user_name} 選擇了 {self.values[0]} 科系")
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

@client.tree.command(name="隨機分隊",description="將語音頻道中的人分成兩隊")
async def user_work(interaction: discord.Interaction):
    user_name = (interaction.user.name).replace(" ","_")
    try:
        channel = interaction.user.voice.channel
        if channel:
            players = [x for x in channel.members]
            shuffle(players)
            half = len(players)//2
            TeamA = players[:half]
            TeamB = players[half:]
            temp = f"{channel.name} : {len(players)}人"
            temp += "\nTeamA: "
            for a in TeamA: temp+="\n" + a.mention
            temp += "\nTempB: "
            for b in TeamB: temp+="\n" + b.mention
            await interaction.response.send_message(temp)
                    
    except AttributeError:
        await interaction.response.send_message(f"您現在不再語音頻道中\n請進入語音頻道中重試!",ephemeral=True)

@client.tree.command(name="加入語音頻道",description="沒有功能")
async def joinChannel(interaction: discord.Interaction):
    user_name = (interaction.user.name).replace(" ","_")
    try:
        channel = interaction.user.voice.channel
        if channel:
            # for i in client.voice_clients:
            #     print(i.channel._get_voice_state_pair(),channel._get_voice_state_pair())
            #     if i.channel._get_voice_state_pair() == channel._get_voice_state_pair():
            #         print("tri")
            # i.disconnect()
            # await channel.guild.voice_client.disconnect()
            await channel.connect()
            await interaction.response.send_message("機器人加入頻道!",ephemeral=True)
    except AttributeError:
        await interaction.response.send_message(f"您現在不再語音頻道中\n請進入語音頻道中重試!",ephemeral=True)

@client.tree.command(name="選擇職業",description="選取職業")
async def user_work(interaction: discord.Interaction) -> None:
    user_name = (interaction.user.name).replace(" ","_")
    await interaction.response.send_message(f"{user_name},選擇你的職業: ",ephemeral=True,view=discord.ui.View().add_item(job_select(history=history)))

@client.tree.command(name="選擇科系",description="選取你的科系")
@app_commands.describe(purview='權限')
async def user_department(interaction: discord.Interaction,purview:str="private") -> None:
    user_name = (interaction.user.name).replace(" ","_")
    if(purview == "private"):
        await interaction.response.send_message(f"{user_name},選擇你的科系: ",ephemeral=True,view=discord.ui.View().add_item(department_select(history=history)))
    elif(purview == "public"):
        await interaction.response.send_message(f"請選擇你的科系: ",view=discord.ui.View().add_item(department_select(history=history)))

@client.tree.command(name="工作",description="賺錢")
async def user_work(interaction: discord.Interaction):
    earned = str(randint(1,100))
    user_name = (interaction.user.name).replace(" ","_")
    with open(os.getcwd()+"/database/works.txt",'a') as work_file:
        work_file.write(f"earned {user_name} "+earned+"\n")
    await interaction.response.send_message(f"{user_name} 賺到了 "+earned+" 元\n",ephemeral=True)
    history.println(f"{user_name} 賺到了 "+earned+" 元")

@client.tree.command(name="查詢機器人服務伺服器",description="查詢機器人服務伺服器")
async def get_bot_served(interaction: discord.Interaction):
    reply = client.user.mention + "服務於:\n"
    for guild in GUILDS:
        reply += guild.name + "\n"
    await interaction.response.send_message(reply,ephemeral=True)

@client.tree.command(name="查詢機器人執行紀錄",description="執行紀錄查詢")
async def get_bot_log(interaction: discord.Interaction):
    await interaction.response.send_message(history.show(),ephemeral=True)

@client.tree.command(name="關閉機器人")
@app_commands.describe(password='機器人金鑰')
@app_commands.rename(password='金鑰')#在使用者看到的地方將變數改為該字串
async def close_bot(interaction: discord.Interaction,password: str):
    """關閉機器人"""
    if(password=="ratoff"):
        await interaction.response.send_message(f'{interaction.user.name} 關閉了機器人')
        await client.close()
    else:
        await interaction.response.send_message(f'{interaction.user.name} 正在嘗試關閉機器人!')

@client.tree.command(name="取得成員加入時間")
@app_commands.describe(member='取得成員加入的時間')
async def get_member_join_time(interaction: discord.Interaction, member: Optional[discord.Member] = None):#Optional示範
    """Says when a member joined."""
    member = member or interaction.user
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}',ephemeral=True)

#在context_menu中，第二個選項為被作用對象

@client.tree.context_menu(name='取得成員加入時間')
async def show_member_join_date(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}',ephemeral=True)

@client.tree.context_menu(name='舉報給管理者')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(f'Thanks for reporting this message by {message.author.mention} to our moderators.',ephemeral=True)
    log_channel = interaction.guild.get_channel(interaction.channel_id)  # replace with your channel id
    embed = discord.Embed(title='被舉報訊息')
    if message.content:
        embed.description = message.content
    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at
    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='前往該訊息', style=discord.ButtonStyle.url, url=message.jump_url))
    await log_channel.send(embed=embed, view=url_view)

@client.tree.context_menu(name='每日金句')
async def dailyQuotes(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(f'您已標註金句',ephemeral=True)
    log_channel = interaction.guild.get_channel(interaction.channel_id)  # replace with your channel id
    embed = discord.Embed(title='每日金句')
    if message.content:
        embed.description = message.content
    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at
    await log_channel.send(embed=embed)

client.run(token)