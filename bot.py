import discord
from discord.ext import commands
from commands import timer, clock

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.add_command(timer.timer)
bot.add_command(clock.clock)

@bot.event
async def on_ready():
    print(f"Bot online as: {bot.user}")

bot.run("YOUR_DISCORD_TOKEN")
