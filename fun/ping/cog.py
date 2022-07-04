from discord.ext import commands

class Ping(commands.Cog, name="Ping"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Checks to see if the bot is alive"""
        await ctx.send(f"Pong! in {round(self.bot.latency * 1000)}ms")

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))