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

from discord.ext import commands

bot = commands.Bot(command_prefix="$?!", helpCommand=help)

@bot.hybrid_command()
async def code(ctx, help="Sends a link to osfanbuff63's GitHub page for all his projects."):
    await ctx.send("Check out osfanbuff63's GitHub here! https://github.com/osfanbuff63")

@bot.hybrid_group(fallback="source")
async def info(ctx, help="A bunch of utility commands related to the bot itself."):
    await ctx.send("The source code for this bot can be found at https://github.com/osfanbuff63/discord-bot") # TODO: mirror to codeberg?

@info.hybrid_command()
async def license(ctx, help="Shows license information for the bot."):
    await ctx.send("osfanDiscordBot63 is licensed under the Apache License 2.0. You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0. Run /info source for the source code.")

@info.hybrid_command()
async def ping(ctx, help="Pings the bot."):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latency: {latency_ms}ms")