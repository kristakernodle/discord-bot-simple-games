from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()
my_token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(name="ping",
             help="long description",
             brief="short description")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(name="copycat",
             help="This function repeats whatever you send to it.",
             brief="brief")
async def copycat(ctx, *args):
    await ctx.channel.send(" ".join(args))

bot.run(my_token)
