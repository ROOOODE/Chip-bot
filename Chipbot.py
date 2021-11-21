import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

from discord.utils import MAX_ASYNCIO_SECONDS

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name=""))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
  if message.content.startswith('!도움' or '!help' or '!도움말'):
      embed = discord.Embed(title = 'Chip bot', description = "**!칩 게임 준비** - *칩 게임에 참가합니다.*\n**!칩 게임 팀 (팀명)** - *칩 게임 팀을 고릅니다.*\n**!칩 게임 시작** - *칩 게임을 시작합니다. (사회자 전용)*\n**!칩 게임 중단** - *칩 게임을 중단합니다. (사회자 전용)*\n**!핑** - *핑을 확인합니다.*" , color = 0xf5d22e)
      await message.channel.send(embed=embed)
  elif(message.content == '!핑'):
      embed = discord.Embed(title = ':ping_pong: 퐁!', description = str(int(client.latency*1000)) + 'ms', color = 0x00ff00)
      await message.channel.send(embed=embed)
  elif(message.content == '!칩 게임 준비'):
      embed = discord.Embed(title = '', description = "" , color = 0x00ff00)
      await message.channel.send(embed=embed)
  if message.content.startswith('!칩 게임 팀'):
    embed = discord.Embed(title = "팀을 선택해주십시오" , description = "" , color = 0x191919)
    msg = await message.channel.send(embed=embed)
    await msg.add_reaction("⬜")
    await msg.add_reaction("🟥")
    await msg.add_reaction("🟦")
    await msg.add_reaction("🟩")
    await msg.add_reaction("🟨")
    await msg.add_reaction("🟧")
    await msg.add_reaction("🟪")
    await msg.add_reaction("🟫")
    await msg.add_reaction("⬛")
      
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "⬜":
        await reaction.message.channel.send(user.name + "")
    print(str(reaction.emoji))
    if str(reaction.emoji) == "🟥":
      print(str(reaction.emoji))
      member = user
      await member.add_roles(client.get_guild(911606835985920000).get_role(911612258646376469))
    if str(reaction.emoji) == "🟦":
      await reaction.message.channel.send(user.name + "")  
    if str(reaction.emoji) == "🟩":
      await reaction.message.channel.send(user.name + "")
    if str(reaction.emoji) == "🟨":
      await reaction.message.channel.send(user.name + "")
    if str(reaction.emoji) == "🟧":
      await reaction.message.channel.send(user.name + "")  
    if str(reaction.emoji) == "🟪":
      await reaction.message.channel.send(user.name + "")  
    if str(reaction.emoji) == "🟫":
      await reaction.message.channel.send(user.name + "")
    if str(reaction.emoji) == "⬛":
      await reaction.message.channel.send(user.name + "")

client.run("토큰")