# rules.py

import os
import random
import traceback
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks



class rules(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'This Prints the Server Rules!', 
                      help = 'Be sure to always use \'.\' before using bot commands!')
    async def rules(self, ctx):
        embed=discord.Embed(title='Rules', description = 'Rules of the Land for the WJLG Discord')
        embed.set_image(url='https://permies.com/i/510472/tumblr_n81h5rDQa21t1hfamo1_1280.jpg')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(rules(bot))
    print('Rules are Loaded')



    