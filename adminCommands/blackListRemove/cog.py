from discord.ext import commands
import discord

class blackListRemove(commands.Cog, name="blackListRemove"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['blr', 'bl-'])
    @commands.has_permissions(administrator=True)
    async def blackListRemove(self, ctx: commands.Context, user: discord.Member):
        """ADMIN ONLY Removes targetted user from blacklist"""
        arg = user.id
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        if role not in user.roles:
            await ctx.send("Person is not on the blacklist!")
            return
        else:
            await user.remove_roles(role)
            await ctx.send("<@{}> has been removed from the blacklist".format(arg))

        
def setup(bot: commands.Bot):
    bot.add_cog(blackListRemove(bot))