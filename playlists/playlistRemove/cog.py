from discord.ext import commands
import discord
from discord.utils import get
import botmain

class playlistRemove(commands.Cog, name="playlistRemove"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def playlistSearch(self, arg):
        for i,lst in enumerate(botmain.list_of_playlists):
            for j,playlist in enumerate(lst):
                if playlist == arg:
                    return i
        return (None, None)

    @commands.command(aliases=['plr', 'pl-', 'playlistremove'])
    async def playlistRemove(self, ctx: commands.Context, arg, arg2):
        """Removes song from playlist"""
        role = discord.utils.get(ctx.guild.roles, name="Groove Master")
        playlistNum = self.playlistSearch(arg)
        songNum = int(arg2)
        user = ctx.author
        lengthOfList = len(botmain.list_of_playlists[playlistNum])
        lengthOfList = lengthOfList - 1
        if role in user.roles:
            if playlistNum == None:
                await ctx.send("That playlist does not exist!")
                return
            if songNum == 0:
                await ctx.send("You cannot remove the name of the playlist!")
                return
            else:
                if songNum > lengthOfList:
                    if lengthOfList == 0:
                        await ctx.send("There are no songs in selected playlist!")
                        return
                    await ctx.send("There are only {} songs in that playlist!".format(lengthOfList))
                    return
                else:
                    await ctx.send("**{}** has been removed from the playlist {}".format(botmain.list_of_playlists[playlistNum][songNum]['title'], botmain.list_of_playlists[playlistNum][0]))
                    del botmain.list_of_playlists[playlistNum][songNum]



def setup(bot: commands.Bot):
    bot.add_cog(playlistRemove(bot))