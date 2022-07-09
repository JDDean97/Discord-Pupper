import os
import random
import discord
import webStuff
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
intents = discord.Intents.default()
intents.messages = True

prechar = '$'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message:discord.Message):
    if message.author == client.user:
        return
    
    if message.content[0] == prechar:

        if message.content[1:].lower() == 'quote':
            quotes = ['what is a man?', 'double knot em and forgot em']
            response = random.choice(quotes)
            await message.channel.send(response)
    
        if message.content[1:].lower() == "dog":
            embedImage = discord.Embed()
            dogUrl = webStuff.getImgUrl()
            embedImage.set_image(url=dogUrl)
            await message.channel.send(embed=embedImage)

    

client.run(TOKEN)