from discord.ext import commands
import discord
from discord.utils import get
import botmain

class playlistClear(commands.Cog, name="playlistClear"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def playlistSearch(self, arg):
        for i,lst in enumerate(botmain.list_of_playlists):
            for j,playlist in enumerate(lst):
                if playlist == arg:
                    return i
        return (None, None)

    @commands.command(aliases=['plc', 'plq', 'playlistclear'])
    async def playlistClear(self, ctx: commands.Context, arg):
        """Clears all songs in a playlist"""
        role = discord.utils.get(ctx.guild.roles, name="Groove Master")
        playlistNum = self.playlistSearch(arg)
        user = ctx.author
        lengthOfList = len(botmain.list_of_playlists[playlistNum])
        lengthOfList = lengthOfList - 1
        if role in user.roles:
            if playlistNum == None:
                await ctx.send("That playlist does not exist!")
                return
            else:
                if lengthOfList == 0:
                    await ctx.send("There are no songs in selected playlist!")
                    return
                else:
                    await ctx.send("**{}** has been cleared!".format(botmain.list_of_playlists[playlistNum][0]))
                    name = botmain.list_of_playlists[playlistNum][0]
                    botmain.list_of_playlists[playlistNum].clear()
                    botmain.list_of_playlists[playlistNum].append(name)


def setup(bot: commands.Bot):
    bot.add_cog(playlistClear(bot))