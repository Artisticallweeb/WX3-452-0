import discord
import praw
import random

from discord.ext import commands
from utils.constants import REDDIT_CLIENT, REDDIT_SECRET

# Initialize the reddit instance
reddit = praw.Reddit(client_id=REDDIT_CLIENT,
                     client_secret=REDDIT_SECRET,
                     ser_agent='bot')

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Random meme command 
    @commands.command(aliases=["memes"])
    async def meme(self, ctx):
        memes_submissions = reddit.subreddit("dankmemes").new()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = memes_submissions.__next__()

        embed = discord.Embed(title='you found MEMES!!', color=0xff00ea)
        embed.set_image(url=submission.url)
        embed.add_field(
            name="View Online",
            value=f"[Link]({submission.url})",
        )
        embed.add_field(
            name="Subreddit",
            value="r/memes",
        )
        await ctx.send(embed=embed)

    # Random cats command
    @commands.command(aliases=["cat","kitty"])
    async def cats(self, ctx):
        memes_submissions = reddit.subreddit("catpictures").new()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = memes_submissions.__next__()

        embed = discord.Embed(title='you found CATS!! awwwwww', color=0xff00ea)
        embed.set_image(url=submission.url)
        embed.add_field(
            name="View Online",
            value=f"[Link]({submission.url})",
        )
        embed.add_field(
            name="Subreddit",
            value="r/cats",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["dogs","doggos"])
    async def dog(self, ctx):
        memes_submissions = reddit.subreddit("dogpictures").new()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = memes_submissions.__next__()

        embed = discord.Embed(title='you found DOGGOS!!', color=0xff00ea)
        embed.set_image(url=submission.url)
        embed.add_field(
            name="View Online",
            value=f"[Link]({submission.url})",
        )
        embed.add_field(
            name="Subreddit",
            value="r/dogs",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(reddit(bot))