from discord.ext import commands
from discord.utils import get
import discord
import random
import botmain

class shuffle(commands.Cog, name="Shuffle"):
    """Shuffles current queue"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def shuffle(self, ctx: commands.Context):
        """Shuffles current queue"""
        if discord.utils.get(ctx.guild.roles, name="Blacklisted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            if len(botmain.song_queue) > 1:
                voice.stop()
                await ctx.send("**Queue has been shuffled!**")
                random.shuffle(botmain.song_queue)
                return
            elif len(botmain.song_queue) == 0:
                await ctx.send("**Queue is currently empty!**")
                return
            else:
                await ctx.send("**There isn't enough to shuffle!**")
                return
        else:
            await ctx.send("**There is no music currently playing!**")

def setup(bot: commands.Bot):
    bot.add_cog(shuffle(bot))