import discord
from discord.ext import commands
from datetime import datetime

mutedRole = '🔇┃Mutado' # Put here the name of muted members role
memberRole = '👤┃Membro' # Put here the name of members default role
punished = 764688902304169994 # Punishment chat ID

class Moderator(commands.Cog, name = 'Moderação'):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member] = None, *, reason: str = 'Motivo não informado.'): # Ban command
        # Discord return
        if members is None:
            e = discord.Embed(description = f'Você não informou o usuário a ser banido, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
        else:
            for member in members:
                await member.ban(reason = reason)
                
                e = discord.Embed(colour = 0xFE0000, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = f'{member.mention}')
                e.add_field(name = ':crown: Moderador', value = f'{ctx.author.mention}')
                e.add_field(name = ':grey_question: Motivo', value = f'{reason}')
                e.set_author(name = 'BANIDO', icon_url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()
                
                memberName = member
        
        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A ban command has been called!\n\nLog: Author: {ctx.author}, Target: {memberName}')

    @commands.command()
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member = None): # Unban command
        # Discord return
        if member is None:
            e = discord.Embed(description = f'Você não informou o usuário a ser desbanido, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
        else:
            try:
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')


                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        
                        e = discord.Embed(title = 'DESBANIDO', colour = 0x3AFE00, timestamp = datetime.utcnow())
                        e.add_field(name = ':bust_in_silhouette: Usuário', value = f'{member}')
                        e.add_field(name = ':crown: Moderador', value = f'{ctx.author.mention}')
                        e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                        await ctx.send(embed = e)
                        await ctx.message.delete()
            
            except Exception:
                await ctx.message.add_reaction('❌')
                e = discord.Embed(description = f'Não foi possível desbanir "{member}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A unban command has been called!\n\nLog: Author: {ctx.author}, Target: {member}')

    @commands.command()
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, members: commands.Greedy[discord.Member] = None, *, reason: str = 'Motivo não informado.'): # Kick command
        # Discord return
        if members is None:
            e = discord.Embed(description = f'Você não informou o usuário a ser kickado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
        else:
            for member in members:
                await member.kick(reason = reason)

                e = discord.Embed(colour = 0xFEA600, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = f'{member.mention}')
                e.add_field(name = ':crown: Moderador', value = f'{ctx.author.mention}')
                e.add_field(name = ':grey_question: Motivo', value = f'{reason}')
                e.set_author(name = 'KICKADO', icon_url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()
                
                memberName = member

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A kick command has been called!\n\nLog: Author: {ctx.author}, Target: {memberName}')

    @commands.command()
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, member: discord.Member = None, *, reason: str = 'Motivo não informado.'): # Mute command
        # Discord return
        if member is None:
            e = discord.Embed(description = f'Você não informou o usuário a ser mutado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
        else:
            role = discord.utils.get(ctx.guild.roles, name = mutedRole)
            if role in member.roles:
                e = discord.Embed(description = f'O usuário já está mutado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                muted = discord.utils.get(ctx.guild.roles, name = mutedRole)
                default = discord.utils.get(ctx.guild.roles, name = memberRole)
                await member.add_roles(muted)
                await member.remove_roles(default)

                e = discord.Embed(colour = 0xFEA900, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = f'{member.mention}')
                e.add_field(name = ':crown: Moderador', value = f'{ctx.author.mention}')
                e.add_field(name = ':grey_question: Motivo', value = f'{reason}')
                e.set_author(name = 'MUTADO', icon_url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()

                # Console return
                print('\n', f'-'*30)
                print(f'\n[+] A mute command has been called!\n\nLog: Author: {ctx.author}, Target: {member}')

    @commands.command()
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member = None):
        # Discord return
        if member is None:
            e = discord.Embed(description = f'Você não informou o usuário a ser desmutado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
        else:
            role = discord.utils.get(ctx.guild.roles, name = mutedRole)
            if role not in member.roles:
                e = discord.Embed(description = f'O usuário não está mutado, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                muted = discord.utils.get(ctx.guild.roles, name = mutedRole)
                default = discord.utils.get(ctx.guild.roles, name = memberRole)
                await member.add_roles(default)
                await member.remove_roles(muted)

                e = discord.Embed(colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = f'{member.mention}')
                e.add_field(name = ':crown: Moderador', value = f'{ctx.author.mention}')
                e.set_author(name = 'DESMUTADO', icon_url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()

                # Console return
                print('\n', f'-'*30)
                print(f'\n[+] A mute command has been called!\n\nLog: Author: {ctx.author}, Target: {member}')

    @commands.command()
    @commands.bot_has_permissions(manage_messages = True)
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5): # Clear chat command
        # Discord return
        if amount == 1:
            await ctx.channel.purge(limit = amount)
            e = discord.Embed(description = f'{ctx.author.mention} deletou {amount} mensagem.', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.delete()
        else:
            await ctx.channel.purge(limit = amount)
            e = discord.Embed(description = f'{ctx.author.mention} deletou {amount} mensagens.', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.delete()

        # Console return
        print('\n', f'-'*30)
        print(f'\n[+] A clear command has been called!\n\nLog: Author: {ctx.author}')

# Cog setup
def setup(client):
    client.add_cog(Moderator(client))
