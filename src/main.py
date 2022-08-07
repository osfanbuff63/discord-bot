import os
import commands
import logger
import discord

version = 'v0.1.0-SNAPSHOT'
client = discord.client
running_on = os.name
token = os.getenv("discord_token")

print(
    "osfanbuff63\'s Discord Bot version {version} running on {running_on}"
    "Licensed under the MIT License"
    "Source code available on GitHub in osfanbuff63/discord-bot"
    )
