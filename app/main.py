from os import getenv

from dotenv import load_dotenv

from app.bot import StarterBot

import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = StarterBot()
bot.run(getenv("BOT_TOKEN"))
