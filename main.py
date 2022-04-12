
import pornhub
import discord
import discord.ext.commands
from discord.ext.commands import bot
import random
from bs4 import BeautifulSoup
import requests
import json
import asyncio

import config

cmd_timeout = 60

bot = discord.ext.commands.Bot(command_prefix='h!', allowed_mentions=discord.AllowedMentions(everyone=False))

@bot.event
async def on_ready():
    print("The bot is running!")

@bot.command()
async def timeout(ctx, time):
    cmd_timeout = time
    await ctx.send('Timeout set to {time}!'.format(time))

@bot.command()
async def hentai_pic(ctx):
    await ctx.message.delete()
    while True:
        r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/hentai').json()
        embed = discord.Embed(title='Картинка OwO', color = discord.Colour.purple())
        for i in r:
            embed.set_image(url=r[i])
        await ctx.send(embed=embed)
        await asyncio.sleep(cmd_timeout)

@bot.command()
async def hentai_gif(ctx):
    await ctx.message.delete()
    while True:
        r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/boobs').json()
        embed = discord.Embed(title='Джифка OwO', color = discord.Colour.purple())
        for i in r:
            embed.set_image(url=r[i])
        await ctx.send(embed=embed)
        await asyncio.sleep(cmd_timeout)

bot.run(config.token)