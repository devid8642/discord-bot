import discord
from discord.ext import commands
from time import sleep
from datetime import datetime

class Errors(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): # When an error has ocurred
        if isinstance(error, commands.MissingPermissions): # If user don't have permission to execute the command
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Você não tem permissão para isso, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
        
        if isinstance(error, commands.CommandNotFound): # If the command not exists
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Esse comando não existe, {ctx.author.mention}, tente usar {self.client.command_prefix}ajuda!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

        if isinstance(error, commands.DisabledCommand): # If the command is disabled
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Esse comando está desabilitado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
        
        if isinstance(error, commands.UserInputError): # If the input has incorrect
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Argumentos inválidos, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

        if isinstance(error, commands.BotMissingPermissions): # If the bot don't have permission to exucute the command
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Eu não tenho permissão para isso, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

        if isinstance(error, commands.NotOwner): # If user don't have permission to execute the command
            await ctx.message.add_reaction('❌')
            e = discord.Embed(description = f'Você não tem permissão para este comando, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

# Cog setup
def setup(client):
    client.add_cog(Errors(client))