import discord

from discord.ext import commands
from asyncio import sleep

# Variables for logging messages
snipe_message_author = {}
snipe_message_content = {}

class snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        await sleep(60)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]

    @commands.command(name = 'snipe')
    async def snipe(self, ctx):
        channel = ctx.channel
        try:
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
        except:
            await ctx.send(f"There are no recently deleted messages in #{channel.name}")

def setup(bot):
    bot.add_cog(snipe(bot))
