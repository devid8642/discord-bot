import discord
from discord.ext import commands
from datetime import datetime, timedelta
import wikipedia
from socket import gethostbyname
from requests import get
from whois import whois

wikipedia.set_lang("pt") # Set output lang of wikipedia summary

cmdChannel = '🤖┃comandos' # Put here name of channel of only commands
cmdChannelM = '<#764261852988964864>' # Put here ID of channel of only commands

class Information(commands.Cog, name = 'Informação'):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['pong', 'latency', 'latencia', 'latência'])
    async def ping(self, ctx): # When a user says ping
        if ctx.channel.name == cmdChannel
            # Discord return
            await ctx.message.delete()
            e = discord.Embed(title = ':satellite: Latência', description = f'Minha latência atual é {round(self.client.latency * 1000)}ms, {ctx.author.mention}!', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A ping command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['information', 'userinfo', 'uinfo'])
    async def info(self, ctx, member: discord.Member = None): # User info command
        # Discord return
        if ctx.channel.name == cmdChannel:
            if member is None:
                member = ctx.author
            
            e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            message = await ctx.send(embed = e)
            
            try:
                await ctx.message.delete()

                e = discord.Embed(title = f':mag: Informações de ```{member.name}```', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = f'```{member.name}```')
                e.add_field(name = ':credit_card: ID', value = f'```{member.id}```')
                e.add_field(name = ':frame_photo: Avatar', value = f'**[Clique Aqui]({member.avatar_url})**')
                e.add_field(name = ':calendar: Membro desde', value = f'```{member.joined_at.strftime("%d/%m/%Y")}, {member.joined_at.strftime("%H:%M")}```')
                e.add_field(name = ':calendar: Data de criação', value = f'```{member.created_at.strftime("%d/%m/%Y")}, {member.created_at.strftime("%H:%M")}```')
                e.set_thumbnail(url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await message.edit(embed = e)
            
            except Exception:
                e = discord.Embed(description = f'Não foi possível encontrar "{member}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await message.edit(embed = e)
                await ctx.message.add_reaction('❌')

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A info command has been called!\n\nLog: Author: {ctx.author}, Target: {member}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
            
    @commands.command(aliases = ['server'])
    async def serverinfo(self, ctx): # Server info command
        if ctx.channel.name == cmdChannel:
            # Discord return
            await ctx.message.delete()
            e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            message = await ctx.send(embed = e)

            region = str(ctx.guild.region)

            e = discord.Embed(title = ':mag: Informações do servidor', colour = 0x3AFE00, timestamp = datetime.utcnow())
            e.add_field(name = ':page_facing_up: Nome', value = f'```{ctx.guild.name}```')
            e.add_field(name = ':credit_card: ID do Servidor', value = f'```{ctx.guild.id}```')
            e.add_field(name = ':earth_americas: Região', value = f'```{region.title()}```')
            e.add_field(name = ':crown: Dono', value = f'```{str(ctx.guild.owner)}```')
            e.add_field(name = ':credit_card: ID do Dono', value = f'```{ctx.guild.owner_id}```')
            e.add_field(name = ':globe_with_meridians: Membros', value = f'```{ctx.guild._member_count}```')
            e.add_field(name = ':speech_balloon: Canais', value = f'```{len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}```')
            e.add_field(name = ':thought_balloon: Texto', value = f'```{len(ctx.guild.text_channels)}```')
            e.add_field(name = ':microphone: Voz', value = f'```{len(ctx.guild.voice_channels)}```')
            e.add_field(name = ':calendar: Data de Criação', value = f'```{ctx.guild.created_at.strftime("%d/%m/%Y")}, {ctx.guild.created_at.strftime("%H:%M")}```')
            e.set_thumbnail(url = ctx.guild.icon_url)
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await message.edit(embed = e)

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A server-info command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
    
    @commands.command(aliases = ['wikipedia', 'summary'])
    async def wiki(self, ctx, *, query = None): # Wikipedia search command
        if ctx.channel.name == cmdChannel:
            # Discord return
            if query is None:
                e = discord.Embed(description = f'Me informe o nome do resumo que deseja, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)

                try:
                    e = discord.Embed(title = f':mag: Pesquisa sobre ```{query}```', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.add_field(name = ':white_check_mark: Resultado', value = f'```{wikipedia.summary(query, sentences = 3)}```')
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.delete()

                except Exception:
                    e = discord.Embed(description = f'Não foi possível pesquisar "{query}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.add_reaction('❌')

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A wiki command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['dnsresolver', 'resolve'])
    async def dnsr(self, ctx, *, dns = None): # Command to resolve a DNS/Hostname
        if ctx.channel.name == cmdChannel:
            # Discord return
            if dns is None:
                e = discord.Embed(description = f'Me informe o domínio que deseja resolver, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)

                try:
                    e = discord.Embed(title = f':satellite: Resolvendo ```{dns}```', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.add_field(name = ':white_check_mark: Resultado', value = f'```{gethostbyname(dns)}```')
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.delete()

                except Exception:
                    e = discord.Embed(description = f'Não foi possível resolver "{dns}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.add_reaction('❌')

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A dns command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command(aliases = ['iptracker', 'track'])
    async def ipt(self, ctx, *, target = None): # Command to track a IP Address
        if ctx.channel.name == cmdChannel:
            # Discord return
            if target is None:
                e = discord.Embed(description = f'Me informe o Endereço IP ou o Domínio que deseja rastrear, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)

                try:
                    response = get(f'http://ip-api.com/json/{target}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query')
                    data = response.json()

                    e = discord.Embed(title = f':mag: Rastreando ```{target}```', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.add_field(name = ':globe_with_meridians: Continente', value = f'```{data["continent"]}```')
                    e.add_field(name = ':globe_with_meridians: País', value = f'```{data["country"]}```')
                    e.add_field(name = ':globe_with_meridians: Código do país', value = f'```{data["countryCode"]}```')
                    e.add_field(name = ':statue_of_liberty: Estado', value = f'```{data["regionName"]}```')
                    e.add_field(name = ':cityscape: Cidade', value = f'```{data["city"]}```')
                    e.add_field(name = ':earth_africa: Latitude', value = f'```{data["lat"]}```')
                    e.add_field(name = ':earth_africa: Longitude', value = f'```{data["lon"]}```')
                    e.add_field(name = ':map: Fuso Horário', value = f'```{data["timezone"]}```')
                    e.add_field(name = ':inbox_tray: Provedor', value = f'```{data["isp"]}```')
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.delete()

                except Exception:
                    e = discord.Embed(description = f'Não foi possível rastrear "{target}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.add_reaction('❌')

            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A ip tracker command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
    
    @commands.command(aliases = ['useravatar'])
    async def avatar(self, ctx, *, member: discord.Member = None): # Command to see an user avatar (PNG or GIF)
        if ctx.channel.name == cmdChannel:
            # Discord return
            if member is None:
                member = ctx.author
            
            e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            message = await ctx.send(embed = e)

            try:
                e = discord.Embed(title = f':frame_photo: Avatar de {member}', colour = 0x3AFE00, timestamp = datetime.utcnow())
                e.add_field(name = ':bust_in_silhouette: Usuário', value = member.mention)
                e.add_field(name = ':link: Link', value = f'**[Clique Aqui]({member.avatar_url})**')
                e.set_image(url = member.avatar_url)
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await message.edit(embed = e)

            except Exception as e:
                await ctx.send(e)
                e = discord.Embed(description = f'Não foi possível encontrar o avatar de "{member.mention}", {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await message.edit(embed = e)
                await ctx.message.add_reaction('❌')
            
            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A avatar command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

    @commands.command()
    async def whois(self, ctx, *, domain = None): # Command to Whois a domain
        if ctx.channel.name == cmdChannel:
            # Discord return
            if domain is None:
                e = discord.Embed(description = f'Me informe o domínio que deseja visualizar, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)

                try:
                    response = whois(domain)
                    name_servers = ''

                    if 'name_servers' in response:
                        for server in response.name_servers:
                            name_servers += server
                            name_servers += ', '
                    elif 'name_server' in response:
                        for server in response.name_server:
                            name_servers += server
                            name_servers += ', '

                    e = discord.Embed(title = f':mag: Pesquisando ```{domain}```', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    if 'domain_name' in response:
                        if isinstance(response.domain_name, list):
                            if len(response.domain_name) == 1:
                                e.add_field(name = ':satellite: Domínio', value = f'```{response.domain_name}```')
                            else:
                                e.add_field(name = ':satellite: Domínio', value = f'```{response.domain_name[0]}```')
                        else:
                            e.add_field(name = ':satellite: Domínio', value = f'```{response.domain_name}```')
                    if 'registrar' in response:
                        e.add_field(name = ':pencil: Registrar', value = f'```{response.registrar}```')
                    if 'whois_server' in response:
                        e.add_field(name = ':desktop: Servidor de Whois', value = f'```{response.whois_server}```')
                    if 'updated_date' in response:
                        cupdate = []
                        if isinstance(response.updated_date, list):
                            for rsp in response.updated_date:
                                cupdate.append(rsp)
                        if len(cupdate) == 0:
                            e.add_field(name = ':calendar: Data de atualização', value = f'```{response.updated_date}```')
                        else:
                            e.add_field(name = ':calendar: Data de atualização', value = f'```{str(response.updated_date[0])}```')
                    if 'creation_date' in response:
                        ccreate = []
                        if isinstance(response.creation_date, list):
                            for rsp in response.creation_date:
                                ccreate.append(rsp)
                        if len(ccreate) == 0:
                            e.add_field(name = ':calendar: Data de criação', value = f'```{response.creation_date}```')
                        else:
                            e.add_field(name = ':calendar: Data de criação', value = f'```{str(ccreate[0])}```')
                    if 'expiration_date' in response:
                        cexpiration = []
                        if isinstance(response.expiration_date, list):
                            for rsp in response.expiration_date:
                                cexpiration.append(rsp)
                        if len(cexpiration) == 0:
                            e.add_field(name = ':calendar: Data de expiração', value = f'```{response.expiration_date}```')
                        else:
                            e.add_field(name = ':calendar: Data de expiração', value = f'```{str(response.expiration_date[0])}```')
                    if 'country' in response:
                        e.add_field(name = ':globe_with_meridians: País', value = f'```{response.country}```')
                    if 'state' in response:
                        e.add_field(name = ':statue_of_liberty: Estado', value = f'```{response.state}```')
                    if 'city' in response:
                        e.add_field(name = ':cityscape: Cidade', value = f'```{response.city}```')
                    if 'address' in response:
                        e.add_field(name = ':office: Endereço', value = f'```{response.address}```')
                    if 'name' in response:
                        e.add_field(name = ':credit_card: Nome', value = f'```{response.name}```')
                    if 'org' in response:
                        e.add_field(name = ':busts_in_silhouette: Organização', value = f'```{response.org}```')
                    e.add_field(name = ':globe_with_meridians: Servidores', value = f'```{name_servers}```')
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.delete()
                
                except Exception as e:
                    e = discord.Embed(description = f'Não foi possível pesquisar "{domain}", {ctx.author.mention}', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.add_reaction('❌')
            
            # Console return
            print('\n', f'-'*30)
            print(f'\n[+] A whois command has been called!\n\nLog: Author: {ctx.author}')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')
    
    @commands.command(aliases = ['temp', 'weather', 'previsao', 'temperatura', 'metereologia'])
    async def tempo(self, ctx, *, city = None): # Weather command
        if ctx.channel.name == cmdChannel:
            if city is None:
                e = discord.Embed(description = f'Me informe a cidade que deseja visualizar, {ctx.author.mention}!', colour = 0xFE0000, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                await ctx.send(embed = e)
                await ctx.message.add_reaction('❌')
            else:
                e = discord.Embed(description = f'Processando... {ctx.author.mention}', colour = 0xF2FE00, timestamp = datetime.utcnow())
                e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                message = await ctx.send(embed = e)

                try:
                    response = get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=TOKEN') # Your Token here
                    data = response.json()

                    e = discord.Embed(title = f':satellite: Previsão de `{city.title()}`', colour = 0x3AFE00, timestamp = datetime.utcnow())
                    e.add_field(name = ':thermometer: Temperatura atual', value = f'```{data["main"]["temp"] - 273.15:.1f} °C```')
                    e.add_field(name = ':thermometer: Temperatura mínima', value = f'```{data["main"]["temp_min"] - 273.15:.1f} °C```')
                    e.add_field(name = ':thermometer: Temperatura máxima', value = f'```{data["main"]["temp_max"] - 273.15:.1f} °C```')
                    e.add_field(name = ':compression: Pressão atmosférica', value = f'```{data["main"]["pressure"]} hPa```')
                    e.add_field(name = ':droplet: Umidade', value = f'```{data["main"]["humidity"]}%```')
                    e.add_field(name = ':dash: Velocidade do vento', value = f'```{data["wind"]["speed"] * 1.6:.1f} KM/h```')
                    e.add_field(name = ':sunny: Tempo', value = f'```{data["weather"][0]["main"]}```')
                    e.set_footer(icon_url =  ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                
                except Exception:
                    e = discord.Embed(description = f'Não foi possível pesquisar "{city.title()}", {ctx.author.mention}', colour = 0xFE0000, timestamp = datetime.utcnow())
                    e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
                    await message.edit(embed = e)
                    await ctx.message.add_reaction('❌')
        else:
            e = discord.Embed(description = f'Eu não posso executar comandos aqui, {ctx.author.mention}! Use o canal {cmdChannelM}!', colour = 0xFE0000, timestamp = datetime.utcnow())
            e.set_footer(icon_url = ctx.author.avatar_url, text = ctx.author.name)
            await ctx.send(embed = e)
            await ctx.message.add_reaction('❌')

# Cog setup
def setup(client):
    client.add_cog(Information(client))
