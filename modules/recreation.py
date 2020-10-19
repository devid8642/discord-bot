import discord
from discord import File
from random import choice
from discord.ext import commands
from random import randint
from datetime import datetime

cmdChannel = '🤖┃comandos' # Put here name of channel of only commands
cmdChannelM = '<#764261852988964864>' # Put here ID of channel of only commands

class Recreation(commands.Cog, name = 'Recreação'):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ['oi', 'hi', 'hello', 'salve', 'olá', 'ola'])
    async def eae(self, ctx): # A hello command
        if ctx.channel.name == cmdChannel:
            # Discord return
            helloMessages = [f'Fala aí {ctx.author.mention}!', f'E aí {ctx.author.mention}?', f'Salve {ctx.author.mention}!', f'De boa {ctx.author.mention}?']
            await ctx.send(choice(helloMessages))

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A hello command has been called!\n\nLog: Author: {ctx.author}')
            await ctx.message.delete()
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['genie'])
    async def genio(self, ctx, *, question = None): # A genie lamp command
        if ctx.channel.name == cmdChannel:
            if question is None:
                e = discord.Embed(description = f'Me pergunte algo, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                # Discord return 
                responses = [
                    'Sim.',
                    'Não.',
                    'Definitivamente, não...',
                    'Definivamente, SIM!',
                    'Claro que não.',
                    'Claro que sim!',
                    'Nem ferrando!!!',
                    'Lógico que sim!',
                    'Acho que não...',
                    'Acho que sim...'
                ]

                e = discord.Embed(title = ':man_genie: Gênio', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':grey_question: Pergunta', value = f'{question}')
                e.add_field(name = ':grey_exclamation: Resposta', value = f'{choice(responses)}')
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.delete()

                # Console return
                print('\n', f'-'*30)
                print(f'\n[+] A genio command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['coin', 'coinflip'])
    async def moeda(self, ctx): # A roll coin command
        if ctx.channel.name == cmdChannel:
            # Discord return    
            coin = randint(1, 2)

            if coin == 1:
                e = discord.Embed(title = ':coin: Moeda', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':grey_exclamation: Resultado', value = f'```Coroa!```')
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
            elif coin == 2:
                e = discord.Embed(title = ':coin: Moeda', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':grey_exclamation: Resultado', value = f'```Cara!```')
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
            await ctx.message.delete()

            #Console return
            print('\n', f'-'*30)
            print(f'\n[+] A coinflip command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['roll', 'rolar', 'dice'])
    async def dado(self, ctx, limit = 20): # A roll dice command
        if ctx.channel.name == cmdChannel:
            # Discord return
            result = randint(0, limit)
            
            e = discord.Embed(title = f':game_die: {ctx.author.name} rolou o dado', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.add_field(name = ':straight_ruler: Lados', value = f'```{limit}```')
            e.add_field(name = ':grey_exclamation: Resultado', value = f'```{result}```')
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A roll command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
    
    @commands.command(aliases = ['joke', 'piadoca', 'jokes'])
    async def piada(self, ctx): # A joke command
        if ctx.channel.name == cmdChannel:
            # Discord return
            jokes = [
                'você conhece a piada do pônei?\n- Pô nei eu',
                'o que o pagodeiro foi fazer na igreja?\n- Cantar pá God',
                'o que o pato falou para a pata?\n- Vem quá',
                'você sabe qual é o rei dos queijos?\n- O reiqueijão',
                'o que acontece quando chove na Inglaterra?\n- Vira Inglalama',
                'o que o tomate foi fazer no banco?\n- Tirar extrato',
                'como se chama a pessoa que viu o Thor de perto?\n- Vi-Thor',
                'por que a velhinha não usa relógio?\n- Porque ela é sem hora',
                'por que há uma cama elástica no polo Norte?\n- Para o urso polar',
                'o que a vaca disse para o boi?\n- Te amuuuuuuuuuuuu',
                'Por que a aranha é o animal mais carente do mundo? \n– Porque ela é um aracneedyou.',
                'Por que o pinheiro não se perde na floresta? \n– Porque ele tem uma pinha.',
                'Sabe como é a piada do pintinho caipira? \n– Pir.',
                'Um caipira chega à casa de um amigo que está vendo TV e pergunta: \n– E aí, firme? O outro responde: \n– Não, furtebol.',
                'Por que o Napoleão era chamado sempre pras festas na França? \n– Porque ele era bom na party.',
                'O que aconteceu com os lápis quando souberam que o dono da faber castell morreu? \n– Ficaram desapontados.',
                'A plantinha foi ao hospital, mas não foi atendida. Por quê? \n– Porque lá só tinha médico de plantão.',
                'Você conhece o site do cavalinho? \n– É www ponto cavalinho ponto com ponton com ponto com ponto com.',
                'Qual é a fórmula da água benta? \n- H Deus O.',
                'O que é, o que é: Maconha enrolada em jornal? \n– Baseado em fatos reais',
                'O que a Xuxa foi fazer no bar? \n– Foi beber ca sasha (cachaça)',
                'Havia dois caminhões voando. Um caiu. Por que o outro continuou voando? \n– Porque era caminhão pipa.',
                'Por que a formiga tem quatro patas? \n– Porque se tivesse cinco se chamaria fivemiga.',
                'Quando os americanos comeram carne pela primeira vez? \n– Quando chegou Cristóvão com lombo.'
            ]

            e = discord.Embed(title = ':microphone: Piadocas', description = f'{ctx.author.mention}, {choice(jokes)}', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A joke command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['jankenpon'])
    async def jokenpo(self, ctx, *, move = None): # A jankenpon game command to play with the bot
        if ctx.channel.name == cmdChannel:
            # Discord return
            if move is None:
                e = discord.Embed(description = f'Use `pedra`, `papel` ou `tesoura` para jogar, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                botMoves = ['pedra', 'papel', 'tesoura']
                botMove = choice(botMoves)
                if move.lower() == 'pedra' and botMove.lower() == 'pedra':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, empatamos!', colour = 0xF2FE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟡')
                elif move.lower() == 'pedra' and botMove.lower() == 'papel':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você perdeu!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🔴')
                elif move.lower() == 'pedra' and botMove.lower() == 'tesoura':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você venceu!', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟢')
                elif move.lower() == 'papel' and botMove.lower() == 'pedra':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você venceu!', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟢')
                elif move.lower() == 'papel' and botMove.lower() == 'papel':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, empatamos!', colour = 0xF2FE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟡')
                elif move.lower() == 'papel' and botMove.lower() == 'tesoura':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você perdeu!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🔴')
                elif move.lower() == 'tesoura' and botMove.lower() == 'pedra':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você perdeu!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🔴')
                elif move.lower() == 'tesoura' and botMove.lower() == 'papel':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, você venceu!', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟢')
                elif move.lower() == 'tesoura' and botMove.lower() == 'tesoura':
                    e = discord.Embed(title = ':video_game: Jokenpo', description = f'{ctx.author.mention} jogou `{move.lower()}` e eu joguei `{botMove.lower()}`, empatamos!', colour = 0xF2FE00, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('🟡')
                else:
                    e = discord.Embed(description = f'Use `pedra`, `papel` ou `tesoura` para jogar, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await ctx.send(embed = e)
                    await ctx.message.add_reaction('❌')

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A joke command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

# Cog setup
def setup(client):
    client.add_cog(Recreation(client))