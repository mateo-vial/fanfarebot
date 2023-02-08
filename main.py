from discord.ext import commands

with open('token.txt', mode='r') as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix='$',  help_command=None)
@bot.event
async def on_ready():
    print('Le bot est prêt.')

bot.load_extension('fanfare')
bot.load_extension('combobreaker')

bot.run(TOKEN)