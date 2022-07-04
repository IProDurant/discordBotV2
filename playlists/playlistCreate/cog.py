from discord.ext import commands
import discord
import datetime
import botmain

class playlistCreate(commands.Cog, name="playlistCreate"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def createPlaylist(self, arg):
        title = arg
        listName = arg
        listName = list()
        listName.append(title)
        return listName

    @commands.command(aliases=['plm', 'plmake', 'playlistmake', 'playlistcreate', 'newplaylist'])
    async def playlistCreate(self, ctx: commands.Context, arg):
        """Creates a playlist"""
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        role2 = discord.utils.get(ctx.guild.roles, name='Groove Master')
        if role in user.roles:
            await ctx.send("You are currently blacklisted!")
            return
        if role2 in user.roles:
            newPlaylist = self.createPlaylist(arg)
            botmain.list_of_playlists.append(newPlaylist)
            emb = discord.Embed(title="Playlist created", description="Name of playlist : {}".format(newPlaylist), color=0x00fc8a)
            #emb.add_field(name="Please use ?playlistAdd to add songs!", value="pls pls pls", inline=False)
            emb.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=emb)
        else:
            await ctx.send("You are not groovy enough to use this command!")

def setup(bot: commands.Bot):
    bot.add_cog(playlistCreate(bot))