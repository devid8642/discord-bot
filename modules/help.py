import discord
from discord.ext import commands
from datetime import datetime

cmdChannel = '🤖┃comandos' # Put here name of channel of only commands
cmdChannelM = '<#764261852988964864>' # Put here ID of channel of only commands
helpCommand = 'ajuda' # Put here the name of default help command

class Help(commands.Cog, name = 'Ajuda'):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['h', 'commands', 'ajuda', 'cmd', 'cmds'])
    async def help(self, ctx, *, page: str = '0'): # Members help command based in pages
        if ctx.channel.name == cmdChannel:
            if page == '0':
                e = discord.Embed(title = ':memo: Ajuda', description = f'Para visualizar uma página digite {str(self.client.command_prefix)}{helpCommand} <Página>.', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':page_facing_up: Página 1', value = 'Ver os comandos referentes a recreação e diversão.', inline = False)
                e.add_field(name = ':page_facing_up: Página 2', value = 'Ver os comandos referentes a informações.', inline = False)
                e.set_footer(icon_url = ctx.author.avatar_url, text = f'{ctx.author.name} • Página {page}')
                await ctx.send(embed = e)
                await ctx.message.delete()
            elif page == '1':
                e = discord.Embed(title = ':memo: Ajuda', description = f'Para visualizar uma página digite {self.client.command_prefix}ajuda <Página>.', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':video_game: Comandos - Recreação/Diversão', value = f'**meme** - Um meme aleatório pra alegrar seu dia.\n**moeda** - Cara ou coroa?\n**genio** - Pergunte ao gênio.\n**eae** - Saudar {self.client.user.name}.\n**piada** - Vai uma piadoca?\n**jokenpo** - Vamos jogar pedra, papel ou tesoura?\n**dado** - Role o dado.')
                e.set_footer(icon_url = ctx.author.avatar_url, text = f'{ctx.author.name} • Página {page}')
                await ctx.send(embed = e)
                await ctx.message.delete()
            elif page == '2':
                e = discord.Embed(title = ':memo: Ajuda', description = f'Para visualizar uma página digite {self.client.command_prefix}ajuda <Página>', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':information_source: Comandos - Informações', value = f'**avatar** - Visualizar o avatar de um usuário.\n**dnsr** - Resolver um DNS/Hostname.\n**info** - Ver as informações de um usuário.\n**ipt** - Rastrear um IP/Hostname.\n**ping** - Visualizar a latência atual do Bot.\n**serverinfo** - Ver as informações do servidor.\n**tempo** - Mostra a previsão do tempo de uma cidade.\n**wiki** - Pesquisar um resumo na Wikipédia.\n**whois** - Pesquisar o Whois de um domínio')
                e.set_footer(icon_url = ctx.author.avatar_url, text = f'{ctx.author.name} • Página {page}')
                await ctx.send(embed = e)
                await ctx.message.delete()
            else:
                e = discord.Embed(title = ':memo: Ajuda', description = f'Para visualizar uma página digite {self.client.command_prefix}ajuda <Página>.', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':page_facing_up: Página 1', value = 'Ver os comandos referentes a recreação e diversão.', inline = False)
                e.add_field(name = ':page_facing_up: Página 2', value = 'Ver os comandos referentes a informações.', inline = False)
                e.set_footer(icon_url = ctx.author.avatar_url, text = f'{ctx.author.name} • Página 0')
                await ctx.send(embed = e)
                await ctx.message.delete()
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    # STAFF HELP COMMANDS
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def ajudamod(self, ctx): # Help commands to moderators
        e = discord.Embed(title = ':memo: Ajuda - Moderação', colour = 0xF2FE00, timestamp = datetime.utcnow())
        e.add_field(name = ':shield: Comandos', value = f'**clear** - Limpar chat.\n**kick** - Kickar usuário.\n**mute** - Mutar usuário.\n**unmute** - Desmutar usuário.\n**ban** - Banir usuário.\n**unban** - Desbanir usuário.')
        e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
        await ctx.author.send(embed = e)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def ajudaadm(self, ctx): # Help commands to admins
        e = discord.Embed(title = ':memo: Ajuda - Administração', colour = 0xFE0000, timestamp = datetime.utcnow())
        e.add_field(name = ':crown: Comandos', value = f'**list** - Listar todos os módulos disponíveis.\n**load** - Carregar um módulo.\n**unload** - Descarregar um módulo.\n**reload** - Recarregar um módulo.\n**reloadall** - Recarregar todos os módulos.')
        e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
        await ctx.author.send(embed = e)
        await ctx.message.delete()
    # STAFF HELP COMMANDS END

# Cog setup
def setup(client):
    client.add_cog(Help(client))