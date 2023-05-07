import discord
import config
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True

def hasrestarted():
  print("""
  /$$$$$$   /$$                           /$$                     /$$
 /$$__  $$ | $$                          | $$                    | $$
| $$  \__//$$$$$$    /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$
|  $$$$$$|_  $$_/   |____  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
 \____  $$ | $$      /$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  | $$
 /$$  \ $$ | $$ /$$ /$$__  $$| $$        | $$ /$$| $$_____/| $$  | $$
|  $$$$$$/ |  $$$$/|  $$$$$$$| $$        |  $$$$/|  $$$$$$$|  $$$$$$$
 \______/   \___/   \_______/|__/         \___/   \_______/ \_______/
  """)

class CustomHelpCommand(commands.HelpCommand):
  def __init__(self):
    super().__init__()
  
  async def send_bot_help(self, mapping):
    for cog in mapping:
      await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')
  
  async def send_cog_help(self, cog):
    await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')
  
  async def send_group_help(self, group):
    await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')
  
  async def send_command_help(self, command):
    await self.get_destination().send(command.name)

bot = commands.Bot(command_prefix = commands.when_mentioned_or('vc.') ,intents=intents, help_command=CustomHelpCommand())

@bot.event
async def on_ready():
  hasrestarted()
  print(f"Online as {bot.user}")

async def load():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
  await load()
  await bot.start(config.token)

asyncio.run(main())