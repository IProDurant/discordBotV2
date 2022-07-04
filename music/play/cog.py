from discord.ext import commands
from discord.utils import get
import discord
from yt_dlp import YoutubeDL
import time
import requests
import datetime
import random
thinkMessages = []
thinkMessages = [line.strip() for line in open("Text Files/ThinkMessages.txt", 'r')]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'quiet': True, 'playlist': True, 'extract-audio': True}
import botmain

class play(commands.Cog, name="play"):
        """Plays a song or playlist"""
        
        def __init__(self, bot: commands.Bot):
            self.bot = bot
        
        def search(self, arg):
            try: requests.get("".join(arg))
            except: arg = " ".join(arg)
            else: arg = "".join(arg)

            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
                song = {'source': info['url'], 'title': info['title'], 'duration': info['duration'], 'url' : info['thumbnail'], 'directurl' : info['webpage_url'], 'views' : info['view_count'], 'likes' : info['like_count']}
                botmain.song_queue.append(song)
                return

        def play_next(self, ctx, *arg):
            voice: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            if len(botmain.recentlyplayed) >= 5:
                del botmain.recentlyplayed[0]
            botmain.recentlyplayed.append(botmain.song_queue[0])
            del botmain.song_queue[0]
            botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
            if len(botmain.song_queue) > 0:
                voice.play(discord.FFmpegPCMAudio(botmain.song_queue[0]['source'], **FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            else:
                return
        
        def create_embed(self, ctx, playType, songLengthMins, songUrl):
            discordEmbed = discord.Embed(title=playType, description="", color=0x00fc8a)
            discordEmbed.add_field(name="{}".format(botmain.song_queue[-1]['title']), value="Song Length : {}".format(songLengthMins), inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_thumbnail(url=songUrl)
            return discordEmbed

        @commands.command()
        async def play(self, ctx: commands.Context, *arg):
            """Play music command"""
            if ctx.author.voice and ctx.author.voice.channel:
                voiceChannel = ctx.message.author.voice.channel
            else:
                await ctx.send("**You are not connected to voice!**")
                return
            if discord.utils.get(ctx.guild.roles, name="Blacklisted") in ctx.author.roles:
                await ctx.send("**You are currently blacklisted!**")
                return
            if not arg:
                await ctx.send("**Please enter a valid song!**")
                return
            thinkingMessage = await ctx.send("{}".format(random.choice(thinkMessages)))
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            self.search(arg)
            if voice and voice.is_connected():
                await voice.move_to(voiceChannel)
            else:
                voice = await voiceChannel.connect()
            if not voice.is_playing():
                if len(botmain.song_queue) > 1:
                    del botmain.song_queue[0]
                    del botmain.song_queue[0]
                voice.play(discord.FFmpegPCMAudio(botmain.song_queue[0]['source'], **FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
                await thinkingMessage.delete()
                await ctx.send(embed=self.create_embed(ctx, "Now Playing", str(datetime.timedelta(seconds=botmain.song_queue[-1]['duration'])), botmain.song_queue[-1]['url']))
                botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
            else:
                await thinkingMessage.delete()
                await ctx.send(embed=self.create_embed(ctx, "Queued", str(datetime.timedelta(seconds=botmain.song_queue[-1]['duration'])), botmain.song_queue[-1]['url']))

def setup(bot: commands.Bot):
    bot.add_cog(play(bot))