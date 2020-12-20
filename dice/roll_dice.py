import random
import discord
from PIL import Image
import requests
import cloudinary.uploader


def get_asset_url(die_num):
    roll_assets_dir_url = "https://raw.githubusercontent.com/kristakernodle/discord-bot-simple-games/9aecff71d3c5a4fa7693d594f67284a14f245981/dice/roll_assets/"
    die_name_convention = "_black_dice.svg"
    return "".join([roll_assets_dir_url, str(die_num), die_name_convention])


def embed_thumbnail(image_url):
    image_dict = {"url": image_url}
    embed_dict = {"thumbnail": image_dict}
    return discord.Embed.from_dict(embed_dict)


def roll_dice(num_dice):
    dice_list = [1, 2, 3, 4, 5, 6]
    rolled_dice = random.choices(dice_list, k=num_dice)
    if len(rolled_dice) == 1:
        die_url = get_asset_url(rolled_dice[0])
        return embed_thumbnail(die_url)

    all_die_images = list()
    final_image_width = 0
    for die_num in rolled_dice:
        die_url = get_asset_url(die_num)
        response = requests.get(die_url)
        img = Image.open(response.raw)
        final_image_width += img.width
        final_image_height = img.height
        all_die_images.append(img)

    final_image = Image.new('RGB', final_image_width, final_image_height)
    for idx, img in enumerate(all_die_images):
        final_image.paste(img, ((idx+1)*img.width), 0)

    upload_response = cloudinary.uploader.upload(final_image)


