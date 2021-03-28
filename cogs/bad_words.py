import discord
from discord.ext import commands,tasks
import random
# from itertools import cycle
import os

bot = commands.Bot(command_prefix = '.')

with open('badwords.txt','r') as file:
    bad_words = file.read().strip().lower().split(', ')

with open('responses.txt','r') as file:
    response = file.read().strip().lower().split('| ')

class filter(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.Cog.listener()
    async def on_message(self, message):
        random_response = random.choice(response)
        curse = message.content
        if not message.author.bot:
            if any(bad_word in curse.lower() for bad_word in bad_words):
                await message.channel.send(f'{message.author.mention}, {random_response}')

def setup(bot):
    bot.add_cog(filter(bot))
    print('Bad Words Loaded')