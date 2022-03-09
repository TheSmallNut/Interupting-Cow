from discord.ext import commands
import discord
import os
import json
import random

with open('./json/usersToMoo.json', 'r') as f:
    data = json.load(f)

USERSTOMOO = data["peopleToMoo"]
MESSAGESTOSEND = ["MOO!", "Moo!", "MOOOO!!!", "Mooooo", "Moooo", "Moo Moo"]
JOKES = ["I am udderly in love with you!", "I am not amoosed.",
         "And then I told my therapist that I feel seen, but not herd…", "An udder day, an udder dollar.", "Seize the moo-ment!", "Cow bells make such beautiful moosic.", "What did the mama cow say to the baby cow? It’s pasture bedtime!"]


class interruptingCow(commands.Cog, name="interruptingCow"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Moo", aliases=["moo", "MOO", "moooo", "MOOO"])
    async def _Moo(self, ctx):
        await ctx.send(f"{random.choice(JOKES)}")

    @commands.command(name="addMOOER", aliases=["addmooer", "add"])
    async def _addMOER(self, ctx, userID):
        data["peopleToMoo"].append()

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        # if user.id in USERSTOMOO:
        randomNumber = random.randint(0, 20)
        if randomNumber == 0:
            await channel.send(f"{random.choice(MESSAGESTOSEND)}")


def setup(bot):
    print("Interrupting Cow Cog Loaded")
    bot.add_cog(interruptingCow(bot))


def teardown(bot):
    print("Interrupting Cow Cog Unloaded")
