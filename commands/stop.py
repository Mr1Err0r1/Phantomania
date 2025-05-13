from datetime import datetime
from discord.ext import commands

@commands.command()
async def stoppuhr(ctx):
    await ctx.send("Timmer startet! Type `!stop`, to stop the timer.")
    start_time = datetime.now()

    def check(msg):
        return msg.author == ctx.author and msg.content.lower() == "!stop"

    try:
        msg = await ctx.bot.wait_for("message", check=check, timeout=3600)  # 1 Stunde max.
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        await ctx.send(f"The time has stopped! Verstrichene Zeit: {elapsed_time}")
    except asyncio.TimeoutError:
        await ctx.send("Stoppuhr wurde nicht gestoppt und ist abgelaufen.")
