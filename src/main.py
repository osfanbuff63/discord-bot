import os
import commands
import logger
import discord

version = "v0.1.0-SNAPSHOT"
client = discord.Client()
token = os.getenv("DISCORD_TOKEN")
running_on = os.name
license = "MIT License"
repo = "https://github.com/osfanbuff63/discord-bot"

print(f"osfanbuff63\"s Discord Bot version {version} running on {running_on}")
print(f"Licensed under the {license}")    
print(f"Source code available here: {repo}")
print("")
print("Starting up!")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

client.run(token)
