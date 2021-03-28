# cats.py

import os
import random
import discord
from discord.ext import commands
import asyncio
import praw
from dotenv import load_dotenv

load_dotenv()
CLIENTID = os.getenv('CLIENT_ID')
CLIENTSECRET =os.getenv('CLIENT_SECRET')
USERAGENT = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id=CLIENTID, 
                     client_secret=CLIENTSECRET,
                     user_agent=USERAGENT)

class bot_commands(commands.Cog):
    """Commands involving examples."""

    def __init__(self, bot, *args, **kwargs):
        self.bot = breakpoint

    @commands.command(description = 'Posts Cats Pics from r/catpics! A smidge buggy..', help = 'Be sure to always use \'.\' before using bot commands!')
    async def cats(self, ctx):
        cat_sub = reddit.subreddit('catpics').hot()
        post_to_pick = random.randint(1,50)
        for i in range(0, post_to_pick):
            submission = next(x for x in cat_sub if not x.stickied)

        await ctx.send(submission.url)

def setup(bot):
    bot.add_cog(bot_commands(bot))
    print('Cats are loaded')