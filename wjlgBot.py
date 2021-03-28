# wjlgBot.py
import os
import random
import traceback
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from twitchAPI import Twitch
from HelpCommand import NewHelpCommand

intents = discord.Intents.default()
intents.members = True

live_notification = False

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
APP_KEY = os.getenv('MY_APP_KEY')
SEC_KEY = os.getenv('MY_SEC_KEY')

bot = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents, help_command=NewHelpCommand())

twitch = Twitch(APP_KEY, SEC_KEY)
twitch.authenticate_app([])

initial_extensions = [
    'cogs.cats',
    'cogs.jokes',
    'cogs.space',
    'cogs.cute',
    'cogs.stackCount',
    'cogs.rules',
    'cogs.cmd_error_handling',
    'cogs.bad_words'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Faile to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

@tasks.loop(minutes=1)
async def loops():
    global live_notification
    info = twitch.get_streams(user_id=['170480364'])
    twitch_data = info["data"]
    if len(twitch_data):
        if live_notification == False:
            name_of_game = info["data"][0]["game_name"]
            stream_name = info["data"][0]["title"]
            if len(name_of_game):
                await bot.change_presence(activity=discord.Streaming(name=str(name_of_game), url='https://www.twitch.tv/wejustlovegames'))
                guild = discord.utils.get(bot.guilds, name=GUILD)
                announcements = guild.get_channel(349554624384073728)
                await announcements.send(f'Hey @everyone, We Just Love Games is Live! \nStreaming now: {stream_name}! Watch here at: https://www.twitch.tv/wejustlovegames')
                live_notification = True
    else:
        live_notification = False
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='your six'))

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    loops.start()

@bot.event
async def on_member_join(member):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    general = guild.get_channel(348510708063010829)
    await member.send(f'Welcome to {member.guild.name}!')
    await general.send(f'Welcome {member.mention} to {member.guild.name} you are number {guild.member_count} in the stack!')

bot.run(TOKEN)
