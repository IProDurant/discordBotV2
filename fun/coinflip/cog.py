from discord.ext import commands
import time
import random

class CoinFlip(commands.Cog, name="CoinFlip"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['flip'])
    async def coinflip(self, ctx: commands.Context):
        """50 50 coinflip"""
        coinMessage = await ctx.send("Flipping :coin:")
        time.sleep(1)
        rareEvent = random.randrange(1, 101)
        if rareEvent == 100:
            await coinMessage.edit(content="Coin landed on its side! {}".format(ctx.author.mention))
        else:
            await coinMessage.edit(content=random.choice(["Heads! {}".format(ctx.author.mention),
                                                        "Tails! {}".format(ctx.author.mention)]))
        

def setup(bot: commands.Bot):
    bot.add_cog(CoinFlip(bot))