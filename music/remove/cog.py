from discord.ext import commands
import discord
from discord.utils import get
import botmain
import asyncio

class remove(commands.Cog, name="Remove"):
    """Removes song from queue, or clears entire queue"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['cq', 'r'])
    async def remove(self, ctx: commands.Context, arg):
        """Removes song from queue, or clears entire queue"""
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        entryNum = int(arg)
        queueLength = len(botmain.song_queue)
        if discord.utils.get(ctx.guild.roles, name="Groove Master") in ctx.author.roles:
            if entryNum != None:
                if entryNum > queueLength:
                    await ctx.send("**There are only {} songs in the queue!**".format(len(botmain.song_queue)))
                elif entryNum == 1:
                    entryNum = entryNum - 1
                    await ctx.send("**{} has been removed from the queue**".format(botmain.song_queue[entryNum]['title']))
                    voice.stop()
                else:
                    entryNum = entryNum - 1
                    await ctx.send("**{} has been removed from the queue**".format(botmain.song_queue[entryNum]['title']))
                    del botmain.song_queue[entryNum]
            else:
                botmain.song_queue.clear()
                voice.stop()
                await ctx.send("**Queue has been cleared and music has been stopped!**")
        else:
            if voice.is_connected():
                if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
                    vcChannel = ctx.message.author.voice.channel
                    x = 0
                    if entryNum > len(botmain.song_queue):
                        await ctx.send("**There are only {} songs in the queue!**".format(len(botmain.song_queue)))
                        return
                    elif entryNum == 1:
                        await ctx.send("**Please use ?skip or ?stop instead!**")
                    else:
                        for i in vcChannel.members:
                            x = x + 1
                        if x >=3:
                            entryNum = entryNum - 1
                            songImageUrl = botmain.song_queue[entryNum]['url']
                            reaction = '\N{THUMBS UP SIGN}'
                            discordEmbed = discord.Embed(title="Remove Vote", description="", color=0x00fc8a)
                            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                            discordEmbed.add_field(name="Current Song", value="{}".format(botmain.song_queue[entryNum]['title']), inline=False)
                            discordEmbed.set_thumbnail(url=songImageUrl)
                            msg = await ctx.send(embed=discordEmbed)
                            await msg.add_reaction(reaction)
                            await asyncio.sleep(10)
                            votes = 0
                            message = await ctx.channel.fetch_message(msg.id)
                            for i in message.reactions:
                                votes += i.count
                            requiredVotes = x*0.67
                            if votes > requiredVotes:
                                await msg.delete()
                                await ctx.send("**Song Removed Successfully**")
                                del botmain.song_queue[entryNum]
                            else:
                                await msg.delete()
                                await ctx.send("**Vote Failed!**")
                        else:
                            entryNum = entryNum - 1
                            await ctx.send("**{} has been removed from the queue**".format(botmain.song_queue[entryNum]['title']))
                            del botmain.song_queue[entryNum]
                            
                else:
                    await ctx.send("**You must be in the same VC as me to begin a vote!**")
            else:
                await ctx.send("**I'm not currently playing any music!**")

def setup(bot: commands.Bot):
    bot.add_cog(remove(bot))