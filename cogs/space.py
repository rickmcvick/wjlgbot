# space.py

import os
import random
import discord
from discord.ext import commands
import asyncio
import giphypop

term = ['outerspace']

class bot_commands(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'Posts gifs about space! Sourced from GIPHY, quite buggy....', 
                      help = 'Be sure to always use \'.\' before using bot commands!'
                      )
    async def space(self, ctx):
        search = random.choice(term)
        g = giphypop.Giphy()
        results = g.translate(None,search)
        await ctx.send(results)

def setup(bot):
    bot.add_cog(bot_commands(bot))
    print('Space is loaded')