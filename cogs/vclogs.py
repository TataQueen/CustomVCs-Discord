import defaults
import datetime
from discord.ext import commands

class VoiceChat_Logs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('VCLogs cog loaded')

  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
    now = datetime.datetime.now()
    formattime = now.strftime("%H:%M:%S")
    channel = self.bot.get_channel(defaults.logsChannel)
    username = f"{member.name}#{member.discriminator} ({member.id})"
    if before.channel is None and after.channel is not None:
      await channel.send(f"{username} has connected to {after.channel.name}({after.channel.id}) {formattime}")
      if after.channel.id == defaults.masterChannel and defaults.customVCLog == True:
        await channel.send(f"{username} is trying to create a custom channel {formattime}")
    elif before.channel is not None and after.channel is not None:
      if before.channel.id == after.channel.id and defaults.sameChannelUpdates == True:
        await channel.send(f"{username} has updated their status on {after.channel.name}({after.channel.id}) {formattime}")
        return 0
      await channel.send(f"{username} has moved between {before.channel.name}({before.channel.id}) and {after.channel.name}({after.channel.id}) {formattime}")
    elif before.channel is not None and after.channel is None:
      await channel.send(f"{username} has disconnected from {before.channel.name}({before.channel.id}) {formattime}")
    



async def setup(bot):
  if defaults.enableVCLogpy == True:
    await bot.add_cog(VoiceChat_Logs(bot))