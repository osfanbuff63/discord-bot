from turtle import hideturtle
from discord.ext import commands
import discord
from random import choice

bot = commands.Bot(command_prefix='!', helpCommand=help)
client = discord.client

@bot.command
async def github(ctx):
    await ctx.send('Check out osfanbuff63\'s projects on GitHub here! https://github.com/osfanbuff63')

@bot.command
async def rules(ctx):
    await ctx.send(
     "*This is copied from #info. Current as of August 7th, 2022*"
    )
# This command is disabled for now - i plan to split these up
#@bot.group()
#async def info(ctx, *, arg):
#    if ctx.invoked_subcommand is None:
#        await ctx.send("No subcommand provided, type `!help` for help!")

#@info.command()
#async def source(ctx):
#    await ctx.send("Check out and contribute to the bot's source code here: https://github.com/osfanbuff63/discord-bot")

#@info.command()
#async def discord_bot(ctx):
#    await ctx.send(
#        "osfanbuff63\'s Discord Bot version {version}"
#        "Licensed under the MIT License"
#        "For the source code, run `!info source`"
#    )

@bot.command
async def hug(ctx, arg):
    await ctx.send(f'{ctx.message.author.mention} hugs {arg}')

@bot.command
async def user(ctx):
    user = choice(ctx.message.channel.guild.members)
    await ctx.send(f'Today\'s random user is {user}')
