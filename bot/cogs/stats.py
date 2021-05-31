from discord.ext.commands import Bot, Cog, Context, command


class Stats(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command()
    async def ping(self, ctx: Context):
        await ctx.send(f"{self.bot.latency}s")


def setup(bot: Bot):
    cog = Stats(bot)
    bot.add_cog(cog)


def teardown(bot: Bot):
    pass
