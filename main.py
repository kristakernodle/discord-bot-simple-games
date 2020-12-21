from dotenv import load_dotenv
from discord.ext import commands
import os
from dice import roll_dice

load_dotenv()
my_token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(name="roll")
async def roll(ctx, num_dice=1):
    if num_dice > 10:
        await ctx.channel.send("I can only roll a maximums of 3 dice at once!")
    await ctx.channel.send("Rolling...")
    await ctx.channel.send(embed=roll_dice(num_dice))


@bot.command(name="ping",
             help="When you type $ping, I return pong!",
             brief="Returns pong")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(name="copycat",
             help="I will repeat whatever you type after $copycat",
             brief="Returns input (stop copying me!)")
async def copycat(ctx, *args):
    await ctx.channel.send(" ".join(args))

bot.run(my_token)
