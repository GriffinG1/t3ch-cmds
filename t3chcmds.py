import discord
from discord.ext import commands

'''Just a bunch of ascii faces'''


class t3chcmds:  # Replace "Template" with the name of the module

    def __init__(self, bot):
        self.bot = bot
		
    @commands.command()
    async def xd(self, ctx):  # Replace "commandname with the name of the command
        """Large XD made of XDs"""
        await ctx.message.delete()
        await ctx.send("XD      XD    XD  XD\n  XD  XD      XD      XD\n     XD           XD       XD\n  XD  XD      XD      XD\nXD      XD    XD  XD")

    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.message.delete()
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def shrug(self, ctx):
        """¯\_(ツ)_/¯"""
        await ctx.message.delete()
        await ctx.send("¯\_(ツ)_/¯")
    
    @commands.command()
    async def magic(self, ctx):
        """(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ"""
        await ctx.message.delete()
        await ctx.send("(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ")

    @commands.command()
    async def tableflip(self, ctx):
        """(ノಠ益ಠ)ノ彡┻━┻"""
        await ctx.message.delete()
        await ctx.send("(ノಠ益ಠ)ノ彡┻━┻")

    @commands.command()
    async def unflip(self, ctx):
        """ ┬─┬ ノ( ゜-゜ノ)"""
        await ctx.message.delete()
        await ctx.send(" ┬─┬ ノ( ゜-゜ノ)")

    @commands.command()
    async def wtf(self, ctx):
        """Ծ_Ծ"""
        await ctx.message.delete()
        await ctx.send("Ծ_Ծ")

def setup(bot):
    bot.add_cog(t3chcmds(bot))  # Change this part to the name you used earlier
