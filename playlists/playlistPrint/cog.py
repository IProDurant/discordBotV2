from discord.ext import commands
from discord.utils import get
import discord
import botmain
import datetime

class playlistPrint(commands.Cog, name="playlistPrint"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['plp', 'playlists', 'playlistprint'])
    async def playlistPrint(self, ctx: commands.Context, arg=999):
        """Prints information about all playlists"""
        amount = int(arg)
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        if len(botmain.list_of_playlists) == 0:
            await ctx.send("Playlists are currently empty!")
            return
        else:
            if amount != 999:
                if amount > len(botmain.list_of_playlists):
                    await ctx.send("There are only {} playlists!".format(len(botmain.list_of_playlists)))
                    return
                amount=amount-1
                if len(botmain.list_of_playlists[amount]) == 1:
                    await ctx.send("This playlist are currently empty!")
                    return
                else:
                    num = 1
                    pltime = 0
                    embedVar = discord.Embed(title="Playlist name : {}".format(botmain.list_of_playlists[amount][0]), description="\u200b", color=0x00fc8a)
                    songurl = botmain.list_of_playlists[amount][1]['url']
                    for e in range(len(botmain.list_of_playlists[amount])):
                        if e == 0:
                            continue
                        time = botmain.list_of_playlists[amount][num]['duration']
                        pltime= pltime + time
                        mins = str(datetime.timedelta(seconds=time))
                        embedVar.add_field(name='[{}] {}'.format(num, botmain.list_of_playlists[amount][num]['title']), value="Song Length : {}".format(mins), inline=False)
                        num = num + 1
                    pltime2 = str(datetime.timedelta(seconds=pltime))
                    embedVar.set_footer(text="Total playlist time : {} minutes".format(pltime2))
                    embedVar.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                    embedVar.set_thumbnail(url=songurl)
                    await ctx.send(embed=embedVar)
                    return
            else:
                num = 1
                eVar = discord.Embed(title="Playlists", description="", color=0x00fc8a)
                for e in range(len(botmain.list_of_playlists)):
                    eVar.add_field(name='[{}] {}'.format(num, botmain.list_of_playlists[e][0]), value="\u200b", inline=False)
                    num = num + 1 
                eVar.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=eVar)
                

def setup(bot: commands.Bot):
    bot.add_cog(playlistPrint(bot))