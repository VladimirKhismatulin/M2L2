import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
images = os.listdir('images')
hints = ["Не мусори",
         "Используй многоразовые предметы",
         "Поищи сайты про экологию и про статистики загрязнения",
         "Говори про экологию остальным"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я бот "Не следить за экологией - это кринж"!')

@bot.command()
async def mem(ctx):
    img = random.choice(images)
    with open(f'images/{img}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)
@bot.command()
async def hint(ctx):
    await ctx.send(random.choice(hints))

bot.run("")
