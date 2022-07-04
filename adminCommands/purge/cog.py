from discord.ext import commands

class Purge(commands.Cog, name="Purge"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['clear'])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx: commands.Context, amount=5):
        """ADMIN ONLY Clears messages in selected channel"""
        await ctx.channel.purge(limit=amount)

        
def setup(bot: commands.Bot):
    bot.add_cog(Purge(bot))