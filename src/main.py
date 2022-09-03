# Copyright 2022 osfanbuff63
#   
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import commands
import logger
import discord

global license
global version
global repo

version = "v1.0.0"
client = discord.Client()
token = os.getenv("DISCORD_TOKEN")
running_on = os.name
license = "Apache License 2.0"
repo = "https://github.com/osfanbuff63/discord-bot"

print(f"osfanDiscordBot63 version {version} running on {running_on}")
print(f"Licensed under the {license}")    
print(f"Source code available here: {repo}")
print("")
print("Starting up!")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

client.run(token)
