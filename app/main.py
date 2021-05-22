from os import getenv
from app.bot import StarterBot

bot = StarterBot()
bot.run(getenv("BOT_TOKEN"))
