from os import listdir
from typing import List

from discord.ext.commands import Bot


class StarterBot(Bot):
    def __init__(self):
        super().__init__(command_prefix=">")

        self.load_extensions()

    def load_extensions(self):
        extensions = self.get_extensions()

        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f"Unable to load extension: {extension}")
                print(e)
    @staticmethod
    def get_extensions():
        extensions: List[str] = []

        for filename in listdir("./bot/cogs"):
            if filename.endswith("py") and filename != "__init__.py":
                extension = filename[:-3]
                extensions.append(f"bot.cogs.{extension}")

        return extensions
