from discord.ext import commands
import discord
import discord.utils

class blackList(commands.Cog, name="blackList"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['bl'])
    @commands.has_permissions(administrator=True)
    async def blackList(self, ctx: commands.Context):
        """ADMIN ONLY  Shows current users on blacklist"""
        i = 1
        embedVar = discord.Embed(title="Blacklisted", description="These Users are currently Blacklisted!", color=0x00fc8a)
        guild = self.bot.get_guild(ctx.guild.id)
        memberList = guild.members
        role = discord.utils.get(ctx.guild.roles, name="Blacklisted")
        print(ctx.guild.members)
        print(memberList)
        for user in ctx.guild.members:
            if role in user.roles:
                print("1")
                embedVar.add_field(name=i, value="<@{}>".format(user.id), inline=False)
                i = i + 1
        print(i)
        if i == 1:
            await ctx.send("**There is no-one currently blacklisted!**")
        else:
            await ctx.send(embed=embedVar)   

        
def setup(bot: commands.Bot):
    bot.add_cog(blackList(bot))