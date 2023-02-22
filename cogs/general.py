import discord
import random

from discord.ext import commands

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        responses = ["Yes", 
                     "No", 
                     "Yes, if Tacoman wills it", 
                     "No... I mean yes... Well... Ask again later", 
                     "The answer is unclear... Seriously I double checked", 
                     "I won't answer that, but scotticus will", "It's a coin flip really...", 
                     "Yes, he will... Sorry I was't really listening", 
                     "I could tell you but I'd have to permanently ban you", "Yes, No, Maybe... I don't know, could you repeat the question?", "If you think I'm answering that, you're clearly mistaking me for idiot.", "Do you REALLY want me to answer that? OK... Maybe ", "YesNoYesNoYesNoYesNoYesNo ", "Ask yourself this question in the mirror three times, the answer will become clear ", "You want an answer? OK, here's your answer: NO", "gay", "https://c.tenor.com/5-yxqQEbeqMAAAAM/jojo-anime.gif", "https://c.tenor.com/9TAeo9ON19YAAAAM/no-jojo.gif", "yeah idc", "ask yourself", "damn, ok", "ask <@752389287391002674>"]
        await ctx.reply(f'{random.choice(responses)}')

    @commands.command()
    async def pun(self, ctx):
        responses = ["Light travels faster than sound. That's why some people appear bright until you hear them speak",
        "I have a few jokes about unemployed people, but none of them work",
        "When life gives you melons, you're dyslexic",
        "Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea",
        "I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over",
        "It's hard to explain puns to kleptomaniacs because they always take things literally",
        "Two windmills are standing in a wind farm. One asks, “What’s your favorite kind of music?” The other says, “I’m a big metal fan.”",
        "Did you hear about the guy whose whole left side was cut off? He’s all right now",
        "I can’t believe I got fired from the calendar factory. All I did was take a day off",
        "The man who survived pepper spray and mustard gas is now a seasoned veteran",
        "My dad farted in an elevator, it was wrong on so many levels",
        "What do you call a bee that can’t make up its mind? A maybe",
        "England doesn't have a kidney bank, but it does have a Liverpool"]
        await ctx.reply(f'{random.choice(responses)}')

def setup(bot):
    bot.add_cog(general(bot))