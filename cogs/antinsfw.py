import defaults
import time
import discord
from discord.ext import commands


class AntiNSFW(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print('AntiNSFW cog loaded')
  
  @commands.Cog.listener()
  async def on_guild_channel_update(self, before, after):
    if after.category.id == defaults.categoryID:
      if after.nsfw == True:
        if before.nsfw == False and after.nsfw == True:
          async for log in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update):
            user = log.user
          await after.edit(nsfw = False)
          if defaults.enableantiNSFWpy == True:
            try:
              member = after.guild.get_member(user.id)  
              username = f"{member.name}#{member.discriminator} ({member.id})"
              channel = after.guild.get_channel(defaults.logsChannel)
              await channel.send(f"{username} tried to enable NSFW in {after.name}({after.id}) <t:{int(time.time())}>")
              print(f"{username} tried to enable NSFW in {after.name}({after.id})")
            except Exception as e:
              print(e)

async def setup(bot):
  if defaults.enableVCLogpy == True and defaults.enableantiNSFWpy == True:
    await bot.add_cog(AntiNSFW(bot))