import discord, json, requests
from discord.ext import commands
from cogs.utils import rpc_module as rpc


class deposit:
    def __init__(self, bot):
        self.bot = bot
        self.rpc = rpc.Rpc()

    @commands.command(pass_context=True)
    async def deposit(self, ctx):
        """Shows wallet info"""
        account = ctx.message.author
        user_addy = self.rpc.getaccountaddress(str(account))
        await self.bot.say(account.mention + "'s Deposit Address: `" + str(user_addy) + "`")


def setup(bot):
    bot.add_cog(deposit(bot))