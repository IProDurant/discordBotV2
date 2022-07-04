from discord.ext import commands
import time
import random

class roll(commands.Cog, name="roll"):
    """Rolls a dice"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['d', 'dice'])
    async def roll(self, ctx: commands.Context, *arg):
        """Rolls a dice"""
        if not arg:
            rollMessage = await ctx.send("Rolling 🎲")
            time.sleep(1)
            await rollMessage.edit(content="{} Rolled a {} 🎲".format(ctx.author.mention, random.randint(1, 6)))
        else:
            try:
                argInt = int(arg[0])
            except ValueError as verr:
                await ctx.send("Please enter a number!")
                return
            rollMessage = await ctx.send("Rolling 🎲")
            time.sleep(1)
            await rollMessage.edit(content="{} Rolled a {} 🎲".format(ctx.author.mention, random.randint(1, argInt)))
        

def setup(bot: commands.Bot):
    bot.add_cog(roll(bot))