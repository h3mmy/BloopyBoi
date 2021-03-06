"""Bot Module"""
import os
import sys
import disnake

from disnake.ext import commands

DESCRIPTION = '''The BloopyBoi, one of bloop.'''

intents = disnake.Intents.default()

bot = commands.Bot(command_prefix='!', description=DESCRIPTION, intents=intents)

@bot.event
async def on_ready():
    """Announces self to std.out"""
    print(f'We have logged in as {bot.user.name} {bot.user.id}')

@bot.command()
async def hello(ctx):
    """Says hello, prints ctx maybe"""
    if ctx:
        await ctx.send('Hello to you as well humanoid! This is an experiment.')

@bot.slash_command()
async def wink(inter):
    """Does a wink"""
    await inter.response.send_message("winked")

bot.load_extension("cogs.inspire")
bot.load_extension("cogs.blissfest")
# bot.add_cog(Greetings(bot))
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
# def __main__():
#     bot.run(os.getenv('DISCORD_BOT_TOKEN'))

# if __name__ == "__main__":
#     sys.exit(__main__())  # pragma: no cover
