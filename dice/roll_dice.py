import random
import discord
from PIL import Image
import requests
from io import BytesIO


def roll_die():
    roll_assets_dir_url = "https://raw.githubusercontent.com/kristakernodle/discord-bot-simple-games/main/dice/roll_assets/"
    die_name_convention = "_dice_magicon_nounproject.png"
    asset_dict = {1: "one",
                  2: "two",
                  3: "three",
                  4: "four",
                  5: "five",
                  6: "six"}

    die = random.randint(1, 6)
    die_num = asset_dict[die]
    die_url = "".join([roll_assets_dir_url, die_num, die_name_convention])

    image_dict = {"url": die_url}
    embed_dict = {"thumbnail": image_dict}
    return discord.Embed.from_dict(embed_dict)


def roll_dice(num_dice):
    pass
