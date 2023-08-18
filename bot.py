from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import discord
import os
import datetime
import asyncio
import math
from discord import app_commands

load_dotenv()

def get_token():
    return os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = 'hehe ', intents = intents, help_command=None)
bot.activity = discord.Game("hehe help")

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        print("Worked")


@bot.event
async def on_command_error(ctx:commands.Context, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.relpy("You are do not have permissions")

    elif isinstance(error, commands.BadArgument):
        await ctx.reply("Bad argument.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing a required argument for this.")

async def startup():
    await bot.load_extension("cogs.bancog")
    await bot.load_extension("cogs.unbancog")
    await bot.load_extension("cogs.mutecog")
    await bot.load_extension("cogs.unmutecog")
    await bot.load_extension("cogs.kickcog")
    await bot.load_extension("cogs.triviacog")

    async with aiohttp.ClientSession() as session:
        bot.session = session

        await bot.start(get_token())

asyncio.run(startup())
