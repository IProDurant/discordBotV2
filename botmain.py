import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import asyncio
import os
from discord.ext import commands
import discord
from discord.ext.commands import CommandNotFound
from discord.utils import get
intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents, case_insensitive=True, help_command=None)
from dotenv import load_dotenv
load_dotenv()
song_queue = []
recentlyplayed = []
song_start = 0
list_of_playlists = []
voiceActive = False


def main():
    load_dotenv()
    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
        client.loop.create_task(status_task())

    for folder in os.listdir("adminCommands"):  
        if os.path.exists(os.path.join("adminCommands", folder, "cog.py")):
            client.load_extension(f"adminCommands.{folder}.cog")
    for folder in os.listdir("fun"):
        if os.path.exists(os.path.join("fun", folder, "cog.py")):
            client.load_extension(f"fun.{folder}.cog")
    for folder in os.listdir("music"):
        if os.path.exists(os.path.join("music", folder, "cog.py")):
            client.load_extension(f"music.{folder}.cog")
    
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("**'{}' is not a known command! {}**".format(ctx.message.content, ctx.author.mention))
            return
        elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
            await ctx.send("**You do not have permission to use that command!**")
            return
        elif isinstance(error, (commands.MissingPermissions)):
            await ctx.send("**You do not have permission to use that command!**")
            return
    
    @client.event
    async def on_voice_state_update(member, before, after):
        if member.id != client.user.id:
            return
        if before.channel is None:
            voice = after.channel.guild.voice_client
            timeInactive = 0
            while True:
                await asyncio.sleep(1)
                timeInactive = timeInactive + 1
                if voice.is_playing() and not voice.is_paused():
                    timeInactive = 0
                if timeInactive == 600:
                    await voice.disconnect()
                    await discord.utils.get(after.channel.guild.text_channels, name="music-commands").send("**Disconnected due to lack of activity** 👋")
                if not voice.is_connected():
                    break
    
    async def status_task():
        while True:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the ♂️ slaves ♂️"))
            await asyncio.sleep(600)
            await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="your deep dark fantasies ♂️"))
            await asyncio.sleep(600)
            await client.change_presence(activity = discord.Game(name="with the DA's hat ♂️"))
            await asyncio.sleep(600)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))
            await asyncio.sleep(5)
            await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="right version ♂️"))
            await asyncio.sleep(600)
            await client.change_presence(activity = discord.Game(name="with the ♂️Gym boss♂️"))
            await asyncio.sleep(600)
            await client.change_presence(activity = discord.Game(name="with the boy next door ♂️"))
            await asyncio.sleep(600)
            
    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)

if __name__ == '__main__':
    main()
