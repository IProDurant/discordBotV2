from discord.ext import commands
import discord
import datetime

class help(commands.Cog, name="help"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context):
        """Help Command"""
        x = 1
        discordEmbed = discord.Embed(title="Commands & Modules", url="https://www.sanfransentinel.com/billy-bot-fq.html", description="", color=0x00fc8a)
        for command in self.bot.commands:
            if not command.aliases:
                discordEmbed.add_field(name="[{}] {}".format(x, command), value="No current aliases", inline=True)
                x = x + 1
            else:
                discordEmbed.add_field(name="[{}] {}".format(x, command), value="{}".format(command.aliases), inline=True)
                x = x + 1
        discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        discordEmbed.timestamp = datetime.datetime.utcnow()
        discordEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/891340523724501022/992379876797587466/unknown.png')
        await ctx.send(embed=discordEmbed)
            

def setup(bot: commands.Bot):
    bot.add_cog(help(bot))