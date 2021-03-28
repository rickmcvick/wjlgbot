# jokes.py

import random
import discord
from discord.ext import commands
import asyncio
import requests

class fun_things(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'Want some really bad dad jokes? This is the command for you! ', 
                      help = 'Be sure to always use \'.\' before using bot commands!'
                      )
    async def jokes(self, ctx):
        url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        joke_msg = requests.get(url, headers=headers).json().get('joke')
        await ctx.send(joke_msg)

def setup(bot):
    bot.add_cog(fun_things(bot))
    print('Jokes are loaded')