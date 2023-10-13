from discord import Intents
from discord.ext.commands import Bot, Context


bot = Bot(
    command_prefix=">",
    intents=Intents.all()
)


# This is a decorator
# A decorator is a function that takes a function as an argument
# Libraries often use them to pass in functions
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# Bot commands have to be async
# This means certain commands have to be called with await
@bot.command()
async def ping(ctx: Context):
    # This is an await call
    await ctx.reply("Pong!")
    # It means the bot can repond to other commands whilst replying


# Follow this guide to create a bot
# https://discordpy.readthedocs.io/en/stable/discord.html
bot.run('SECRET TOKEN')
