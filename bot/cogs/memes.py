import random
import asyncpraw
import discord
from discord.ext import tasks, commands
from os import getenv

reddit = reddit = asyncpraw.Reddit(
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("CLIENT_SECRET"),
    user_agent=getenv("USER_AGENT")
)


class Memes(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.bot.loop.create_task(self.startup())
        
    async def startup(self):
        self.bot.wait_until_ready
        self.subreddits = ["memes","dankmemes"]
        # self.channel = bot.get_channel(800179553519140868)
        

    @commands.command()
    async def meme(self, ctx):
        random_subreddit = random.choice(["memes","dankmemes"])
        subreddit = await reddit.subreddit(random_subreddit)
        hot = subreddit.hot(limit=5)
        posts = []

        async for post in hot:
            posts.append(post)
        
        random_post = random.choice(posts)
        title = random_post.title
        url = random_post.url
        embed=discord.Embed(title=title,colour=discord.Colour.blue())
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Memes(bot))