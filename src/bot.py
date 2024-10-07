import datetime
from src.db.database import Database
from game.player import Player
from game.teamgenerator import TeamGenerator
from steam.steamProfile import SteamProfile
from discord.ext import commands

class TenMansBot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.launch_time = datetime.datetime.now(datetime.UTC)

        self.db = Database()

    async def on_ready(self):
        if (self.user == None):
            return 'failed to log in'
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def get_launch_time_str(self) -> str:
        return f"Bot started at: {self.launch_time.strftime('%F %T')} UTC."
    
    def get_server_info(self, ctx: commands.Context) -> str:
        if (ctx.guild is not None):
            return f'Server ID: {ctx.guild.id}\n Server Name: {ctx.guild.name}'
        return 'server not available'
    
    async def list_channels(self, ctx: commands.Context):
        if (ctx.guild is not None):
            for c in ctx.guild.channels:
                await ctx.send(f'Channel: {c.name} - ID: {c.id}')
        await ctx.send('channel list not available')

    async def list_users_in_channel(self, ctx, channelName):
        channel = next((x for x in ctx.guild.channels if x.name == channelName), None)
        if channel is not None:
            if not channel.members:
                await ctx.send(f'{channel.name} is empty')
            else:
                await ctx.send(f'Users in channel {channelName}:')
                for m in channel.members:
                    await ctx.send(f'{m.name} - ID: {m.id}')
        else:
            await ctx.send(f'Channel "{channelName}" not found')

    async def create_teams(self, ctx: commands.Context, channelName):
        if (ctx.guild == None):
            await ctx.send('unable to fetch server info, aborting')
            return
        channel = next((x for x in ctx.guild.channels if x.name == channelName), None)
        if channel is not None:
            if not channel.members:
                await ctx.send(f'{channel.name} is empty')
            else:
                await ctx.send(f'{len(channel.members)} users found in channel {channelName}')
                players = []
                for m in channel.members:
                    players.append(Player(m.name, m.id))

                if len(players) % 2 > 0:
                    players.append(Player('Fake Player', 0))
                gen = TeamGenerator(players)
                teams = gen.generate_even_teams()
                await ctx.send(teams[0].list_players())
                await ctx.send(teams[1].list_players())
        else:
            await ctx.send(f'Channel "{channelName}" not found')

    async def register_player(self, ctx: commands.Context, steam_profile_path: str):
        if steam_profile_path is not None:
            profile = SteamProfile(steam_profile_path)
            print(profile.miniprofile)