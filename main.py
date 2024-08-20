import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from src.bot import TenMansBot

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = TenMansBot(command_prefix='&', intents=intents)

@bot.command()
async def start_time(ctx: commands.Context):
    await ctx.send(bot.get_launch_time_str())

@bot.command()
async def server_info(ctx: commands.Context):
    await ctx.send(bot.get_server_info(ctx))

@bot.command()
async def list_channels(ctx: commands.Context):
    await bot.list_channels(ctx)

@bot.command()
async def users_in_channel(ctx: commands.Context, arg):
    await bot.list_users_in_channel(ctx, arg)

@bot.command()
async def create_teams(ctx: commands.Context, arg):
    await bot.create_teams(ctx, arg)

bot.run(BOT_TOKEN)
