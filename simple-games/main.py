from dotenv import load_dotenv
from discord.ext import commands
import os
from dice import roll_dice
from hangman import existing_unfinished_game, start_game

load_dotenv()
my_token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(name="copycat",
             help="I will repeat whatever you type after $copycat",
             brief="Returns input (stop copying me!)")
async def copycat(ctx, *args):
    await ctx.channel.send(" ".join(args))


@bot.command(name="hangman",
             help="Begin and interact with the Hangman game",
             brief="Play hangman!")
async def hangman(ctx):
    existing_game = existing_unfinished_game(str(ctx.author))
    if not existing_game:
        await start_game(ctx)
    await ctx.channel.send("Hangman!")


@bot.command(name="ping",
             help="When you type $ping, I return pong!",
             brief="Returns pong")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command(name="roll")
async def roll(ctx, num_dice=1):
    if num_dice > 10:
        return await ctx.channel.send("I can only roll a maximums of 10 dice at once!")
    await ctx.channel.send("Rolling...")
    await ctx.channel.send(embed=roll_dice(num_dice))


bot.run(my_token)
