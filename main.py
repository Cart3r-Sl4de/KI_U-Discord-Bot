import discord, os, random, asyncio, discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions

file_location = os.path.dirname(os.path.abspath(__file__))
intents = discord.Intents.all()
intents.members = True

class KIU_Calc(commands.Bot):
    async def on_ready(self):
        print('Logged in as {0.user}'.format(icarus_bot))
        print('Floor ice cream gives you health!')

    async def setup_hook(self):
        for filename in os.listdir(os.path.join(file_location, './holyForge/')):
            if filename.endswith('.py') and filename.find("arsenal") == -1:
                await self.load_extension(f'holyForge.{filename[:-3]}')
        try:
            synced = await icarus_bot.tree.sync()
            print(f'Commands synced: {len(synced)}')
        except Exception as e:
            print(f'Ran into error: {e}')

icarus_bot = KIU_Calc(command_prefix="$", intents=intents, activity=discord.Game('floor ice cream'), status=discord.Status.idle)

token_path = os.path.join(file_location, 'chuckie_cheese_battlecry.token')
with open(token_path, 'r') as file:
    battleCry = file.readline().strip()

@icarus_bot.event
async def on_message(message):
    if message.author == icarus_bot.user:
        return

    mention = message.author.mention

    #basic commands
    if message.content.startswith('^hello'):
        await message.channel.send(
            'Huh, you usually don\'t meet such nice bosses.')

@icarus_bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Latency is: {round(icarus_bot.latency * 1000)}ms')

#Dyntos more powerful than Hades, eh? He can't top the Tetragrammaton
icarus_bot.run(battleCry)
