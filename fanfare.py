import discord
from discord.ext import commands
from discord.ext import tasks
import datetime

class Fanfare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fanfare.start()

    @tasks.loop(seconds=60)
    async def fanfare(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        emote_str = '<:fanfare:1062698357493076010>'
        if hour == minute:
            await self.chan_fanfare.send('{:02d}:{:02d} {}'
                                         .format(hour, minute, emote_str))

    @fanfare.before_loop
    async def fanfare_before_loop(self):
        await self.bot.wait_until_ready()

        # Compute the next minute
        now = datetime.datetime.now()
        next_run = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)

        # Troubleshooting
        print(now)
        print(next_run)

        # Await until next minute
        await discord.utils.sleep_until(next_run)
        print('sleep done')

        self.chan_fanfare = self.bot.get_channel(1062697676493295699)

def setup(bot):
    bot.add_cog(Fanfare(bot))