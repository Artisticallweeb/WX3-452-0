import discord
import os

from discord.ext import commands
from utils.constants import BOT_TOKEN, BOT_PREFIX

Bot = commands.Bot(
    command_prefix=BOT_PREFIX,
    intents=discord.Intents.all(),
    case_insensitive=True
)

# Load all python modules from the cogs directory
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")

# Initialize the bot
@Bot.event
async def on_ready():
  print('BOT IS RUNNING!')
  await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="👀"))

Bot.run(BOT_TOKEN)
