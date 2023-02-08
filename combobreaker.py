from discord.ext import commands
import datetime
import random


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        emote_str = '<:fanfare:1062698357493076010>'
        if (
                hour == minute and
                message.content == '{:02d}:{:02d} {}'.format(hour, minute, emote_str) and
                message.channel.id == 1062697676493295699 and
                random.randrange(10) == 0
            ):
            await message.reply('C-C-C-C-COMBO BREAKER {}'.format(emote_str))



def setup(bot):
    bot.add_cog(MyCog(bot))