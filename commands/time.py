from datetime import datetime
import pytz
from discord.ext import commands

@commands.command()
async def uhrzeit(ctx, region="Europe/Berlin"):
    try:
        zeitzone = pytz.timezone(region)
        jetzt = datetime.now(zeitzone)
        await ctx.send(f"Die aktuelle Uhrzeit in {region} ist: {jetzt.strftime('%H:%M:%S')}")
    except pytz.UnknownTimeZoneError:
        await ctx.send("Ungültige Zeitzone. Beispiele: `Europe/Berlin`, `America/New_York`")
