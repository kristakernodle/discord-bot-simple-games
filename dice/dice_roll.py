import cloudinary
import cloudinary.api
import cloudinary.uploader
import discord
from io import BytesIO
import os
from PIL import Image
import random
import requests


def embed_image(image_url, footer=''):
    image_dict = {"url": image_url}
    embed_dict = {"image": image_dict,
                  "footer": {"text": footer}}
    return discord.Embed.from_dict(embed_dict)


def cloudinary_public_id(rolled_dice):
    if type(rolled_dice) is int:
        return f"dice/{rolled_dice}_rolled_dice.png"
    return f"dice/{'_'.join(list(map(str, rolled_dice)))}_rolled_dice.png"


def roll_dice(num_dice):
    dice_list = [1, 2, 3, 4, 5, 6]
    rolled_dice = random.choices(dice_list, k=num_dice)

    cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'),
                      api_key=os.getenv('CLOUD_API_KEY'),
                      api_secret=os.getenv('CLOUD_API_SECRET'))

    cloudinary_url = cloudinary.CloudinaryImage(cloudinary_public_id(rolled_dice)).url
    pub_id_status = requests.get(cloudinary_url).status_code

    if pub_id_status == 404:
        all_die_images = list()
        final_image_width = 0
        for die_num in rolled_dice:
            die_url = cloudinary.CloudinaryImage(f"dice/{die_num}_rolled_dice.png").url
            my_request = requests.get(die_url)
            img = Image.open(BytesIO(my_request.content))
            final_image_width += img.width
            all_die_images.append(img)
        first_img = all_die_images[0]
        final_image = Image.new('RGBA', (final_image_width, first_img.height))
        for idx, img in enumerate(all_die_images):
            final_image.paste(img, (idx*img.width, 0), img)
        buf = BytesIO()
        final_image.save(buf, 'png')
        buf.seek(0)
        image_bytes = buf.read()
        buf.close()

        upload_response = cloudinary.uploader.upload(image_bytes,
                                                     public_id=cloudinary_public_id(rolled_dice).strip('.png'))

        return embed_image(upload_response['url'], ", ".join(list(map(str, rolled_dice))))
    return embed_image(cloudinary_url, ", ".join(list(map(str, rolled_dice))))
