# catgif.py

import os
import random
import discord
from discord.ext import commands
import asyncio
import giphypop

term = ['dog', 'cat']

class bot_commands(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'Posts random GIF\'s featuring a dog or cat! Sourced from GIPHY, and a little buggy...', 
                      help = 'Be sure to always use \'.\' before using bot commands!'
                      )
    async def cute(self, ctx):
        search = random.choice(term)
        g = giphypop.Giphy()
        results = g.translate(None,search)
        await ctx.send(results)

def setup(bot):
    bot.add_cog(bot_commands(bot))
    print('Cute Gif\'s are loaded')