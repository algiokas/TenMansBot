import datetime
from src.player import Player
from src.teamgenerator import TeamGenerator
from discord.ext import commands

class TenMansBot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.launch_time = datetime.datetime.now(datetime.UTC)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def get_launch_time_str(self) -> str:
        return f"Bot started at: {self.launch_time.strftime('%F %T')} UTC."
    
    def get_server_info(self, ctx: commands.Context) -> str:
        return f'Server ID: {ctx.guild.id}\n Server Name: {ctx.guild.name}'
    
    async def list_channels(self, ctx: commands.Context):
        for c in ctx.guild.channels:
            await ctx.send(f'Channel: {c.name} - ID: {c.id}')

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




