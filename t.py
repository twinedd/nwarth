import discord, os
from discord.ext import commands
from main import baba

token = 'TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='1', intents=intents)
@bot.command()
async def img(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            file_url = i.url
            image_path = f'images/{file_name}'
            await i.save(f'images/{file_name}')
            await ctx.send(baba(model_path='keras_model.h5', labels_path='labels.txt', image_path=image_path))

    else:
        await ctx.send('bb')

bot.run(token)