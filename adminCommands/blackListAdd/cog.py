from discord.ext import commands
import discord
import discord.utils

class blackListAdd(commands.Cog, name="blackListAdd"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['bl+', 'bla'])
    @commands.has_permissions(administrator=True)
    async def blackListAdd(self, ctx: commands.Context, user: discord.Member):
        """ADMIN ONLY Adds targetted user to blacklist"""
        arg = user.id
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        if role in user.roles:
            await ctx.send("Person is already on the blacklist!")
            return
        else:
            await user.add_roles(role)
            await ctx.send("<@{}> has been added to the blacklist".format(arg))

        
def setup(bot: commands.Bot):
    bot.add_cog(blackListAdd(bot))