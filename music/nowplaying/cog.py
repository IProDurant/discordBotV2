from discord.ext import commands
import discord
import botmain
import time
import datetime

class nowPlaying(commands.Cog, name="nowPlaying"):
    """Displays current song playing"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["np"])
    async def nowPlaying(self, ctx: commands.Context):
        """Displays current song playing"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            maxTime = botmain.song_start + botmain.song_queue[0]['duration']
            currentTime = time.mktime(datetime.datetime.today().timetuple())
            maxTime = maxTime - currentTime
            timeLeft = str(datetime.timedelta(seconds=maxTime))
            discordEmbed = discord.Embed(title="{}".format(botmain.song_queue[0]['title']), url="{}".format(botmain.song_queue[0]['directurl']), description="", color=0x00fc8a)
            discordEmbed.add_field(name="Song Length / Time remaining", value="{} / {}".format(str(datetime.timedelta(seconds=botmain.song_queue[0]['duration'])), timeLeft), inline=True)
            discordEmbed.add_field(name="Likes", value="{:,}".format(botmain.song_queue[0]['likes']), inline=True)
            discordEmbed.add_field(name="Views", value="{:,}".format(botmain.song_queue[0]['views']), inline=True)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_thumbnail(url=botmain.song_queue[0]['url'])
            await ctx.send(embed=discordEmbed)
        else:
            await ctx.send("**No music is playing currently!**")

def setup(bot: commands.Bot):
    bot.add_cog(nowPlaying(bot))