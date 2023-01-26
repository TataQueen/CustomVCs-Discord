import defaults
import discord
from discord.ext import commands
from discord.utils import get
import sqlite3

def getInfo(memberId):
  conn = sqlite3.connect("channels.db")
  c = conn.cursor()
  c.execute("SELECT * FROM custom_channels WHERE user_id=:user_id", {'user_id': memberId})
  result = c.fetchone()
  conn.close()
  if result:
    return result
  else:
    return None

def createNewEntry(memberId, channelName, userLimit, channelId):
  conn = sqlite3.connect("channels.db")
  c = conn.cursor()
  c.execute("INSERT INTO custom_channels VALUES (:user_id, :channel_name, :user_limit, :channel_id)", {'user_id':memberId, 'channel_name':channelName,'user_limit':userLimit,'channel_id':channelId})
  conn.commit()
  conn.close()

def updateChannelID(memberId, channelId):
  conn = sqlite3.connect("channels.db")
  c = conn.cursor()
  c.execute("UPDATE custom_channels SET channel_id = :channel_id WHERE user_id = :user_id", {'channel_id':channelId, 'user_id':memberId})
  conn.commit()
  conn.close()

def saveChannel(memberId, before):
  conn = sqlite3.connect("channels.db")
  c = conn.cursor()
  c.execute("UPDATE custom_channels SET channel_name = :channel_name, user_limit = :user_limit WHERE user_id = :user_id", {'channel_name':before.channel.name, 'user_limit':before.channel.user_limit, 'user_id':memberId})
  conn.commit()
  conn.close()
  print(f"Guardado el estado de {memberId}")

async def ifEmptyDelete(before):
  if len(before.channel.members) == 0 and before.channel.id not in defaults.staticChannels:
    await before.channel.delete()

class VoiceChat(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('VoiceChat cog loaded')
  
  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
    # print(before)
    # print(after)
    # voice_state = bool(member.voice)
    # print(voice_state)
    try:
      if after.channel is not None:
        if after.channel.id == defaults.masterChannel:
          if before.channel is not None:
            results = getInfo(member.id)
            if results:
              if before.channel.id == results[3]:
                saveChannel(member.id, before)
            await ifEmptyDelete(before)
          print(f"{member.name} is trying to create a channel")
          results = getInfo(member.id)
          print(results)
          voice_category = get(member.guild.categories, id=defaults.categoryID)
          if results is not None:
            channel_name = results[1]
            user_limit = results[2]
            channel = await member.guild.create_voice_channel(channel_name, category=voice_category, user_limit=user_limit)
            updateChannelID(member.id, channel.id)
          else:
            channel_name = defaults.customNameChannel(member.name)
            user_limit = defaults.userLimit
            channel = await member.guild.create_voice_channel(channel_name, category=voice_category, user_limit=user_limit)
            createNewEntry(member.id, channel_name, user_limit, channel.id)
          await member.move_to(channel)
          await channel.set_permissions(member, connect=defaults.connect, move_members=defaults.move_members, speak=defaults.speak, mute_members=defaults.mute_members ,deafen_members=defaults.deafen_members ,priority_speaker=defaults.priority_speaker ,manage_channels=defaults.manage_channels, stream=defaults.stream, view_channel=defaults.view_channel)
        elif before.channel is None:
          print(f'{member.name} se ha unido a {after.channel.id}')
        elif before.channel.id == after.channel.id:
          print(f"{member.name} se ha muteado/ensordecido")
        else:
          print(f'{member.name} se ha movido entre {before.channel.id} y {after.channel.id}')
          results = getInfo(member.id)
          if results:
            if before.channel.id == results[3]:
              saveChannel(member.id, before)
          await ifEmptyDelete(before)
      elif after.channel is None:
        print(f"{member.name} se ha desconectado")
        results = getInfo(member.id)
        if results:
          if before.channel.id == results[3]:
            saveChannel(member.id, before)
        await ifEmptyDelete(before)
      else:
        print("\n\n--------------------------------------------\nError?\n--------------------------------------------\n\n")
    except Exception as e:
      print(e)


async def setup(bot):
    await bot.add_cog(VoiceChat(bot))