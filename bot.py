import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def man_plast(ctx):
    mn_plas = ["https://www.youtube.com/watch?v=T1zH0RfeZlU",
               "https://www.youtube.com/watch?v=D_u6mNlHprE",
               "https://www.youtube.com/watch?v=XLth_2Ag5_4",]
    plas = random.choice(mn_plas)

    await ctx.send(plas)

@bot.command()
async def carton(ctx):
    mn_car = ["https://www.youtube.com/watch?v=6zNiZofMemk",
              "https://www.youtube.com/watch?v=bOd0QwW0FHk",
              "https://www.youtube.com/watch?v=_tDtqKZIIEk"]
    car = random.choice(mn_car)
    await ctx.send(car)
@bot.command()
async def vidrio(ctx):
    mn_vid = ["https://www.youtube.com/watch?v=W13cDrJ299Q&pp=ygUXbWFudWFsaWRhZGVzIGNvbiB2aWRyaW8%3D",
              "https://www.youtube.com/watch?v=VrNNSYgTK5k",
              "https://www.youtube.com/watch?v=FlHPIma2zv0"]
    vid = random.choice(mn_vid)
    await ctx.send(vid)
@bot.command()
async def papel(ctx):
    mn_pap = ["https://www.youtube.com/watch?v=tWzDc0dx9oQ&pp=ygUWbWFudWFsaWRhZGVzIGNvbiBwYXBlbA%3D%3D",
              "https://www.youtube.com/watch?v=47ejbROR8ho&pp=ygUWbWFudWFsaWRhZGVzIGNvbiBwYXBlbA%3D%3D",
              "https://www.youtube.com/watch?v=5EzlPtFuYW4"]
    pap = random.choice(mn_pap)
    await ctx.send(pap)

bot.run("TOKEN")
