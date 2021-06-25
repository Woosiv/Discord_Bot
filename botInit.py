# Setting up the environment
from dotenv import load_dotenv
import os

import discord
from discord.ext import commands
# Load in the environment variables
load_dotenv()
botKey = os.environ['BOT_KEY']

bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx) :
    await ctx.send(ctx.guild)

bot.run(botKey)


