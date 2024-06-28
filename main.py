import os
import discord
from dotenv import load_dotenv
import re
from responses import scryfall_query

load_dotenv()

TOKEN: str = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
          
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if bool(re.search(r'\[\[([A-Za-z0-9_ ]+)\]\]',message.content)) == True:
        print(f'Identified one or more scryfall queries')
        await scryfall_query(message)



client.run(TOKEN)