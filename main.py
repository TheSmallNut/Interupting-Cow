from discord.ext import commands
import API.secret as secret
import os

bot = commands.Bot(command_prefix='!')


def loadModules():
    # Change "cogs" to your folder name
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            bot.load_extension(f"modules.{filename[:-3]}")


loadModules()


bot.run(secret.INTERRUPTINGCOW)
