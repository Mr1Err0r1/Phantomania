from datetime import datetime
import pytz
from discord.ext import commands
from utils.translate import get_translation

@commands.command()
async def clock(ctx):
    locale = ctx.guild.preferred_locale
    now = datetime.now()
    digital_time = now.strftime("🕒 %H:%M:%S")  # Digitaluhr-Format
    message = get_translation("current_time", locale, time=digital_time)
    
    await ctx.send(message)
