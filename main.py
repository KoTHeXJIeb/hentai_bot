
import aiohttp
import discord
import discord.ext.commands
from discord.ext.commands import bot
import random
import requests
import asyncio
import rule34

import config

cmd_timeout = 0

bot = discord.ext.commands.Bot(command_prefix='h!', allowed_mentions=discord.AllowedMentions(everyone=False))

loop = asyncio.get_event_loop()
rule34 = rule34.Rule34(loop)

@bot.event
async def on_ready():
    print("The bot is running!")

@bot.command()
async def timeout(ctx, time):
    cmd_timeout = time
    await ctx.send('Timeout set to ' + str(cmd_timeout))

@bot.command()
async def hentai_pic(ctx):
    await ctx.message.delete()
    while True:
        r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/hentai').json()
        embed = discord.Embed(title='PIC', color = discord.Colour.purple())
        for i in r:
            embed.set_image(url=r[i])
        await ctx.send(embed=embed)
        await asyncio.sleep(cmd_timeout)

@bot.command()
async def hentai_gif(ctx):
    await ctx.message.delete()
    while True:
        r = requests.get('https://anime-api.hisoka17.repl.co/img/nsfw/boobs').json()
        embed = discord.Embed(title='GIF', color = discord.Colour.purple())
        for i in r:
            embed.set_image(url=r[i])
        await ctx.send(embed=embed)
        await asyncio.sleep(cmd_timeout)

@bot.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="test", description="test")
        while True:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/hentai_femdom/new.json?sort=hot') as r:
                    res = await r.json()
                    max = len(res['data']['children'])
                    embed.set_image(url=res['data']['children'][random.randint(0, max)]['data']['url'])
                    await ctx.send(embed=embed)
                    await asyncio.sleep(cmd_timeout)
    else:
        await ctx.send('You need to be in NSFW channel to use this command!')

@bot.command()
async def generateLink(ctx):
    print(rule34.urlGen(tags='furry', limit=5))

bot.run(config.token)