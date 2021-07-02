from loggin import basicConfig, INFO
from os import getenv

from dotenv import load_dotenv

from bot.bot import StarterBot


basicConfig(level=INFO)
load_dotenv()

bot = StarterBot()
bot.run(getenv("BOT_TOKEN"))
