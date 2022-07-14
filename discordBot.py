import os
import random
import discord
from discord.ext import commands
import webStuff
import youtubeDownloader
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix='$')
intents = discord.Intents.default()
intents.messages = True


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='dog')
async def getDog(ctx):
    embedImage = discord.Embed()
    breeds = ['Labrador','Bernese Mountain Dog','Bulldog','Pitbull','Poodle','Australian Shepherd']
    choice = random.randint(0,len(breeds))
    dogUrl = webStuff.getImgUrl("dog")
    embedImage.set_image(url=dogUrl)
    dogName = str(breeds[choice])
    await ctx.send("grabbing pics of" +dogName)
    await ctx.send(embed=embedImage)

@bot.command(name='cat')
async def getDog(ctx):
    embedImage = discord.Embed()
    dogUrl = webStuff.getImgUrl("cat")
    embedImage.set_image(url=dogUrl)
    await ctx.send(embed=embedImage)

@bot.command(name='coyote')
async def getDog(ctx):
    embedImage = discord.Embed()
    dogUrl = webStuff.getImgUrl("coyote")
    embedImage.set_image(url=dogUrl)
    await ctx.send(embed=embedImage)

@bot.command(name='connect')
async def joinVoice(ctx, vnum):
    vnum = int(vnum)
    vchannel = ctx.guild.voice_channels[vnum]
    voiceClient = await vchannel.connect()

@bot.command(name="disconnect")
async def leaveVoice(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name="play")
async def playSong(ctx, url):
    fname = str( await youtubeDownloader.main(url))
    fname +=".mp4"
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(fname))
    ctx.voice_client.play(source, after=lambda e: print(e) if e else None)
    await ctx.send("playing track")
    

bot.run(TOKEN)