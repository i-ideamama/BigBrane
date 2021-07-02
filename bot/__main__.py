from os import getenv

from dotenv import load_dotenv

from bot.bot import StarterBot

load_dotenv()

bot = StarterBot()
bot.run(getenv("BOT_TOKEN"))
