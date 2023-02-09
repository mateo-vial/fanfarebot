import discord
from discord.ext import commands
from discord.ext import tasks
import datetime
from pytz import timezone

user_ids_warn = [] # User ID (int)

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

        # Warning
        if hour == minute+2 or (hour, minute) in [(23, 58), (0, 59)]:
            msg_content = ':warning: Attention :warning: fanfare dans 2 minutes'
            for user_id in user_ids_warn:
                user = await self.bot.fetch_user(user_id)
                await user.send(msg_content)

    @fanfare.before_loop
    async def fanfare_before_loop(self):
        await self.bot.wait_until_ready()
        now = datetime.datetime.now(tz=timezone('Europe/Paris'))
        next_run = now.replace(second=5, microsecond=0) + datetime.timedelta(minutes=1)
        await discord.utils.sleep_until(next_run)
        self.chan_fanfare = self.bot.get_channel(1062697676493295699)


def setup(bot):
    bot.add_cog(Fanfare(bot))