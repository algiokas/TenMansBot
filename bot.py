import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
APPLICATION_ID = os.getenv('DISCORD_APPLICATION_ID')
PUBLIC_KEY = os.getenv('DISCORD_PUBLIC_KEY')
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

MY_GUILD = discord.Object(id=GUILD_ID)

class TenMansBot(commands.Bot):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = TenMansBot(command_prefix='&', intents=intents)
client.run(BOT_TOKEN)