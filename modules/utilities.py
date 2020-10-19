import discord
from discord.ext import commands
from discord.ext.commands import errors
from os import listdir
from random import randint
from datetime import datetime
from json import load, dump

cmdChannel = '🤖┃comandos' # Put here name of channel of only commands
cmdChannelM = '<#764261852988964864>' # Put here ID of channel of only commands

class Utilities(commands.Cog, name = 'Utilidades'):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def load(self, ctx, extension): # Load module command
        # Discord return
        try:
            self.client.load_extension(f'modules.{extension}')

            e = discord.Embed(description = f'Módulo `{extension}` carregado com sucesso, {ctx.author.mention}!', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.delete()
        
        except errors.ExtensionNotFound:
            e = discord.Embed(description = f'Módulo `{extension}` não existe, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

        except errors.ExtensionAlreadyLoaded:
            e = discord.Embed(description = f'Módulo `{extension}` já foi carregado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A load module has been called!\n\nLog: Author: {ctx.author}, Target: {extension}')

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unload(self, ctx, extension): # Unload module command
        # Discord return
        if extension != 'utilities': # **UTILITIES IS A MAIN COMMAND**
            try:
                self.client.unload_extension(f'modules.{extension}')

                e = discord.Embed(description = f'Módulo `{extension}` descarregado com sucesso, {ctx.author.mention}!', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()

            except errors.ExtensionNotLoaded:
                e = discord.Embed(description = f'Módulo `{extension}` já foi descarregado ou não existe, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
        else:
            e = discord.Embed(description = f'Não é possível descarregar um módulo principal, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A unload module command has been called!\n\nLog: Author: {ctx.author}, Target: {extension}')
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def list(self, ctx): # List available modules command
        # Discord return
        extensions = list()
        for filename in listdir('./modules'):
            if filename.endswith('.py'):
                extensions.append(f'{filename[:-3]}')
        
        extensions = ', '.join(extensions)

        e = discord.Embed(description = f'Módulos: `{extensions}`.', colour = 0x3AFE00, timestamp = datetime.utcnow())
        e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
        await ctx.send(embed = e)
        await ctx.message.delete()

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A list module command has been called!\n\nLog: Author: {ctx.author}')

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def reload(self, ctx, extension): # Reload module command
        # Discord return
        try:
            self.client.reload_extension(f'modules.{extension}')

            e = discord.Embed(description = f'Módulo `{extension}` recarregado com sucesso, {ctx.author.mention}!', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.delete()

        except Exception:
            e = discord.Embed(description = f'Não foi possível recarregar`{extension}`, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A reload module command has been called!\n\nLog: Author: {ctx.author}, Target: {extension}')

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def reloadall(self, ctx): # Reload all modules command
        # Discord return
        extensions = list()
        for filename in listdir('./modules'):
            if filename.endswith('.py'):
                # Discord return
                self.client.reload_extension(f'modules.{filename[:-3]}')
                extensions.append(f'{filename[:-3]}')

                # Console return
                print(f'\n[+] module {filename[:-3]} has been reloaded.')
        
        extensions = ', '.join(extensions)

        e = discord.Embed(description = f'Todos os módulos foram recarregados com sucesso, {ctx.author.mention}!', colour = 0x3AFE00, timestamp = datetime.utcnow())
        e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
        await ctx.send(embed = e)
        await ctx.message.delete()
        
        # Console return 
        print('\n', f'-'*30)
        print(f'\n[+] A reload all modules command has been called!\n\nLog: Author: {ctx.author}')

# Cog setup
def setup(client):
    client.add_cog(Utilities(client))