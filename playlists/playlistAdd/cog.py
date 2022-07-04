from discord.ext import commands
from discord.utils import get
import discord
from yt_dlp import YoutubeDL
import time
import datetime
import requests
import botmain
import random
thinkMessages = []
thinkMessages = [line.strip() for line in open("Text Files/ThinkMessages.txt", 'r')]
#position = 0
YDL_OPTIONS = {'format': 'bestaudio', 'quiet': True, 'playlist': True, 'extract-audio': True}

class playlistAdd(commands.Cog, name="playlistAdd"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def search(self, arg2, position):
            check = str(arg2)
            try: requests.get("".join(arg2))
            except: arg2 = " ".join(arg2)
            else: arg2 = "".join(arg2)

            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f"ytsearch:{arg2}", download=False)['entries'][0]
                song = {'source': info['url'], 'title': info['title'], 'duration': info['duration'], 'url' : info['thumbnail'], 'directurl' : info['webpage_url'], 'views' : info['view_count'], 'likes' : info['like_count']}
                botmain.list_of_playlists[position].append(song)
                return
            
    def playlistSearch(self, arg):
        for i,lst in enumerate(botmain.list_of_playlists):
            for j,playlist in enumerate(lst):
                if playlist == arg:
                    return i
        return (None)

    @commands.command(aliases=['pla', 'pl+'])
    async def playlistAdd(self, ctx: commands.Context, arg, arg2):
        """Adds a song to a playlist"""
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        role2 = discord.utils.get(ctx.guild.roles, name='Groove Master')
        if role in user.roles:
            await ctx.send("You are currently blacklisted!")
            return
        if role2 in user.roles:
            think = random.choice(thinkMessages)
            playMessage = await ctx.send("{}".format(think))
            position = self.playlistSearch(arg)
            if position == None:
                await ctx.send("That playlist does not exist!")
                return
        
            self.search(arg2, position)
            lengt = botmain.list_of_playlists[position][-1]['duration']
            songurl = botmain.list_of_playlists[position][-1]['url']
            mins = str(datetime.timedelta(seconds=lengt))
            emb = discord.Embed(title="Added to Playlist", description="", color=0x00fc8a)
            emb.add_field(name="{}".format(botmain.list_of_playlists[position][-1]['title']), value="Song Length : {}".format(mins), inline=False)
            emb.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            emb.set_thumbnail(url=songurl)
            await playMessage.delete()
            await ctx.send(embed=emb)
        else:
            await ctx.send("You arent groovy enough for this command!")
            
            

def setup(bot: commands.Bot):
    bot.add_cog(playlistAdd(bot))