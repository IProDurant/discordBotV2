from discord.ext import commands
import discord

class leave(commands.Cog, name="leave"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def leave(self, ctx: commands.Context):
        """Bot leaves current voice channel"""
        if discord.utils.get(ctx.guild.roles, name="Blacklisted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.message.add_reaction('👋')
        else:
            await ctx.send("**I'm not connected to a voice channel!**")


def setup(bot: commands.Bot):
    bot.add_cog(leave(bot))