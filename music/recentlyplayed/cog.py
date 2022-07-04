from discord.ext import commands
import discord
import datetime
import botmain

class recentlyPlayed(commands.Cog, name="recentlyPlayed"):
    """Shows last 5 played songs"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["rp"])
    async def recentlyPlayed(self, ctx: commands.Context, *arg):
        """Shows last 5 played songs"""
        if len(botmain.recentlyplayed) == 0:
            await ctx.send("**No songs recently played**")
            return
        if not arg:
            x = 1
            discordEmbed = discord.Embed(title="Recently Played", description="", color=0x00fc8a)
            for i in range(len(botmain.recentlyplayed)):
                discordEmbed.add_field(name='[{}] {}'.format(x, botmain.recentlyplayed[i]['title']), value="Song Length : {}".format(str(datetime.timedelta(seconds=botmain.recentlyplayed[i]['duration']))), inline=False)
                x = x + 1
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.set_thumbnail(url=botmain.recentlyplayed[0]['url'])
            await ctx.send(embed=discordEmbed)
        else:
            try:
                argQueueLength = int(arg[0])
                argInt = argQueueLength - 1
            except ValueError as verr:
                await ctx.send("**Please enter a number!**")
            if argQueueLength > len(botmain.recentlyplayed):
                await ctx.send("**There has not been that many songs played!**")
            else:
                discordEmbed = discord.Embed(title="{}".format(botmain.recentlyplayed[argInt]['title']), url="{}".format(botmain.recentlyplayed[argInt]['directurl']), description="", color=0x00fc8a)
                discordEmbed.add_field(name="Song Length", value="{}".format(str(datetime.timedelta(seconds=botmain.recentlyplayed[argInt]['duration']))), inline=True)
                discordEmbed.add_field(name="Likes", value="{:,}".format(botmain.recentlyplayed[argInt]['likes']), inline=True)
                discordEmbed.add_field(name="Views", value="{:,}".format(botmain.recentlyplayed[argInt]['views']), inline=True)
                discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                discordEmbed.timestamp = datetime.datetime.utcnow()
                discordEmbed.set_thumbnail(url=botmain.recentlyplayed[argInt]['url'])
                await ctx.send(embed=discordEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(recentlyPlayed(bot))