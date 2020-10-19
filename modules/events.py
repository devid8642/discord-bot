import discord
import json
from discord.ext import commands
from datetime import datetime
from json import load, dump

welcomeChannel = 763772865341423667 # Welcome channel ID (without ', only ID, need to be a integer)
autoRole = '👤┃Membro' # ID of autorole when a member join the server
helpCommand = 'ajuda' # Put here the name or alias of default help command

class Events(commands.Cog, name = 'Eventos'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member): # When a member join the server
        # Welcome message
        e = discord.Embed(colour = 0x3AFE00, timestamp = datetime.utcnow())
        e.set_author(name = member, icon_url = member.avatar_url)
        e.add_field(name = 'Bem-vindo(a)!', value = f'{member.mention}, seja bem vindo(a) ao {member.guild.name}! Use {self.client.command_prefix}{helpCommand} para ver a lista de comandos!')
        e.set_image(url = member.guild.icon_url)
        e.set_footer(icon_url = member.avatar_url, text = f'ID: {member.id}')
        await self.client.get_channel(welcomeChannel).send(embed = e)

        # Autorole
        role = discord.utils.get(member.guild.roles, name = autoRole)
        await member.add_roles(role)

# Cog setup
def setup(client):
    client.add_cog(Events(client))