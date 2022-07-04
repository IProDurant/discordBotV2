from discord.ext import commands
import discord
import asyncio
import time
import datetime
from music import play
import music.play as play
import botmain

class skip(commands.Cog, name="Skip"):
    """Skips current song"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['next'])
    async def skip(self, ctx: commands.Context):
        """Skips current song"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if discord.utils.get(ctx.guild.roles, name="Blacklisted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        if voice.is_connected():
            if discord.utils.get(ctx.guild.roles, name='Groove Master') in ctx.author.roles:
                if len(botmain.song_queue) > 1:
                    discordEmbed = discord.Embed(title="Song Skipped", description=botmain.song_queue[0]['title'], color=0x00fc8a)
                    discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                    discordEmbed.add_field(name="Now Playing", value=botmain.song_queue[1]['title'], inline=False)
                    discordEmbed.set_thumbnail(url=botmain.song_queue[1]['url'])
                    await ctx.send(embed=discordEmbed)
                    voice.stop()
                    play.play_next()
                    await asyncio.sleep(0.5)
                    botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
                else:
                    await ctx.send("**There is only 1 song in the queue!**")

            else:
                if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
                    vcChannel = ctx.message.author.voice.channel
                    x = 0
                    for i in vcChannel.members:
                        x = x + 1
                    if len(botmain.song_queue) > 1:
                        if x >=4:
                            reaction = '\N{THUMBS UP SIGN}'
                            discordEmbed = discord.Embed(title="Skip Vote", description="", color=0x00fc8a)
                            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                            discordEmbed.add_field(name="Current Song", value="{}".format(botmain.song_queue[0]['title']), inline=False)
                            discordEmbed.add_field(name="Up Next", value="{}".format(botmain.song_queue[1]['title']), inline=False)
                            discordEmbed.set_thumbnail(url=botmain.song_queue[0]['url'])
                            msg = await ctx.send(embed=discordEmbed)
                            await msg.add_reaction(reaction)
                            await asyncio.sleep(10)
                            voteTotal = 0
                            message = await ctx.channel.fetch_message(msg.id)
                            for i in message.reactions:
                                voteTotal += i.count
                            voteRequired = x*0.67
                            if voteTotal > voteRequired:
                                await msg.delete()
                                discordEmbed = discord.Embed(title="Skip Successful", description="", color=0x00fc8a)
                                discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                                discordEmbed.add_field(name="Now Playing", value=botmain.song_queue[1]['title'], inline=False)
                                discordEmbed.set_thumbnail(url=botmain.song_queue[1]['url'])
                                await ctx.send(embed=discordEmbed)
                                voice.stop()
                                play.play_next()
                                botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
                            else:
                                await msg.delete()
                                await ctx.send("**Vote Failed!**")      
                        else:
                            songImageUrl = botmain.song_queue[1]['url']
                            discordEmbed = discord.Embed(title="Song Skipped", description=botmain.song_queue[0]['title'], color=0x00fc8a)
                            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                            discordEmbed.add_field(name="Now Playing", value=botmain.song_queue[1]['title'], inline=False)
                            discordEmbed.set_thumbnail(url=songImageUrl)
                            await ctx.send(embed=discordEmbed)
                            voice.stop()
                            play.play_next()
                            await asyncio.sleep(0.5)
                            botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
                    else:
                        await ctx.send("**There are not enough songs to skip!**")
                else:
                    await ctx.send("**You must be in the same VC as me to begin a vote!**")
        else:
            await ctx.send("**I'm not currently playing any music!**")

def setup(bot: commands.Bot):
    bot.add_cog(skip(bot))