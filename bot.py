import discord
from os import listdir
from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents.default() # Default intents import
intents.members = True # IMPORTANT INTENT!!! THIS ALLOW ON_MEMBER_JOIN

status = cycle(['pedra na mãe do adm', 'bomba no vizinho', 'pedra no portão da vizinha chata', 'linha no fio pra tirar pipa', 'robrox', 'tijolo na cabeça do adm']) # Tasks
print(f'\n{"-" * 12}> STARTING BOT <{"-" * 12}')

# Setup
client = commands.Bot(command_prefix = '!', intents = intents, case_insensitive = True, help_command = None) # Change client prefix in 'command_prefix = '
token = '' # Put your application Token here

@client.event
async def on_ready(): # When the client is started
    # Discorn return
    change_status.start()
    # client.remove_command('help') # If you want to use only personalized help command

    # Console return
    print(f'\n{client.user.name}({client.user.id}) IS ONLINE!')

# Status
@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

# Auto-load extensions
for filename in listdir('./modules'):
    if filename.endswith('.py'):
        # Discord return
        client.load_extension(f'modules.{filename[:-3]}')

        # Console return
        print(f'\n[+] Plugin {filename[:-3]} has been loaded.')

# Run client setup
client.run(token)