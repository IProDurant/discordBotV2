from discord.ext import commands
import discord
import botmain

class stop(commands.Cog, name="Stop"):
    """Stops bot and clears queue"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx: commands.Context):
        """Stops bot and clears queue"""
        if discord.utils.get(ctx.guild.roles, name="Blacklisted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.stop()
            botmain.song_queue.clear()
            await ctx.send("**Music has been stopped!**")
        else:
            await ctx.send("**There is no music currently playing!**")

def setup(bot: commands.Bot):
    bot.add_cog(stop(bot))