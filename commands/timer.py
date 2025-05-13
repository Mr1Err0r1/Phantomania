import asyncio
import re
from discord.ext import commands
from utils.translate import get_translation

timers = {}  # Speichert aktive Timer {user_id: remaining_seconds}

def parse_time(time_str):
    """Wandelt '5s', '5m', '5h' in Sekunden um"""
    total_seconds = 0
    matches = re.findall(r'(\d+)([smhd])', time_str.lower())

    for value, unit in matches:
        value = int(value)
        if unit == "s":
            total_seconds += value
        elif unit == "m":
            total_seconds += value * 60
        elif unit == "h":
            total_seconds += value * 3600
        elif unit == "d":
            total_seconds += value * 86400

    return total_seconds

@commands.command()
async def timer(ctx, duration: str):
    global timers
    locale = ctx.guild.preferred_locale
    user_id = ctx.author.id

    if user_id in timers:
        await ctx.send("⏳ Du hast bereits einen laufenden Timer!")
        return

    seconds = parse_time(duration)
    timers[user_id] = seconds
    message = get_translation("timer_started", locale, time=duration)
    await ctx.send(message)

    while timers[user_id] > 0:
        await asyncio.sleep(1)
        timers[user_id] -= 1

    message = get_translation("time_up", locale)
    await ctx.send(message)
    del timers[user_id]  # Timer entfernen

@commands.command()
async def adjust_timer(ctx, adjustment: str):
    """Erhöht oder verkürzt den aktuellen Timer um '5s', '5m', '5h' etc."""
    global timers
    user_id = ctx.author.id

    if user_id not in timers:
        await ctx.send("🚫 Kein aktiver Timer gefunden.")
        return

    change = parse_time(adjustment)
    if adjustment.startswith("-"):
        timers[user_id] = max(0, timers[user_id] - change)
    else:
        timers[user_id] += change

    await ctx.send(f"⏳ Timer angepasst! Neue verbleibende Zeit: {timers[user_id]} Sekunden.")
