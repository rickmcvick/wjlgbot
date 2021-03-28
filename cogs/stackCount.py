# stackCount

import discord
from discord.ext import commands
import asyncio

class bot_commands(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'Counts everyone in the WJLG server! Not buggy!', help = 'Be sure to always use \'.\' before using bot commands!')
    async def stack(self, ctx):
        # guild = discord.utils.get(bot.guilds, name=GUILD)
        count = len(ctx.guild.members)
        await ctx.send(f'There are {count} people on the stack!')

def setup(bot):
    bot.add_cog(bot_commands(bot))
    print('Stack count is loaded')