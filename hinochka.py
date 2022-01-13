#!/usr/bin/python
# -*- coding: utf8 -*-
import json
from typing import Text
import discord
import os
import time
from discord import embeds
from discord import emoji
from discord import guild
from discord import user
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.ext.commands.help import HelpCommand
from discord.utils import _URL_REGEX, get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check, MissingPermissions
import asyncio
import discord_components
from discord_components import DiscordComponents, Button, ButtonStyle
from pprint import pprint
from discord_components.dpy_overrides import send
from discord_components.ext.filters import guild_filter
from pypresence import Presence
import random
from discord import FFmpegPCMAudio
import aiohttp
import timer
import requests
from requests import get
from asyncio import sleep
import aiohttp
import asyncio
import random
from datetime import datetime
from googlesearch import search 
from dotenv import load_dotenv
import datetime
import json
import os
import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

# Silence useless bug reports messages




custom_prefixes = {}
default_prefixes = ['h!']


async def determine_prefix(client, message):
    guild = message.guild
    
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes


colors = [0x8592aa]



intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = determine_prefix, intents=intents)
client.remove_command("help")

api_key = "89756129ff31a0ca6891bdc0048668bf"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

responses = [ # Or values, however you want to name it
    'думаю так',
    'остаточно так',
    'ніт звісно',
    'авжеж друже',
]



random_resp = random.choice(responses)

pp = [
    '12 см',
    '1000-7 cм',
    '0 см',
    '16 см',
    'horu.pp.ua',
    'informatik.pp.ua',
]

random_resp = random.choice(pp)

guild_welcome = {929114606130049086}

@client.event
async def on_ready():
    while True:
         time = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
         await client.change_presence(status=discord.Status.online, activity=discord.Game(f"помер від крінжі"))
    

@client.event
async def on_guild_join(guild):
    emb = discord.Embed(title = f'Всім привіт, дякую що додали мене на сервер {guild.name}😄', description = f'Я Хінн. Крінжовенький україномовний бот з непоганим функціоналом. В мій асортимент входить модераційний, утилітний, та розважальний розділ.', color = 0x8592aa)
    emb.add_field(name = 'Трішки інформації про мене:', value = 'Мій префікс: **h!** але ви зможете його змінити за потребою\nІнформація про мене: **h?hinn**\nКоманда для списку команд: **h?help**\nПриємного користування, якщо я вам звісно стану у пригоді :D')
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/924403524987682826/926977339756261436/hinnstartlogo.png')
    emb.set_footer(text = 'Хінн | 2022 ', icon_url = 'https://cdn.discordapp.com/attachments/925461149359673427/926927760088260628/d7f2a5c1f921583e90f373455589fcf8.jpg')
    await guild.text_channels[0].send(embed = emb)

@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"Ух ти, захотіли рандомного мема з назвою {data['title']}?😲", color = 0x8592aa).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


@client.command()
@commands.has_permissions(manage_messages=True)
@commands.has_permissions( administrator = True )
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    clear = discord.Embed(title = '🧼Здав ЗНО по прибиранні', description = 'Готовий похвалитись, я почистив цей чат😎', color = 0x8592aa)
    await ctx.send(embed=clear)


@client.command()
@commands.has_permissions(kick_members = True)
async def kick( ctx, member: discord.Member, *, reason=None, guild: discord.Guild):
    try:
        bot_id = "<@923260509724213288>"
        author = ctx.author
        await member.kick(reason=reason)
        await ctx.send(emb = discord.Embed(description = f'**{member} вигнали за причиною ' + reason + ' радіємо хлопці та дівчата!**', color = 0x8592aa))
        embed = discord.Embed(title = f'Вас вигнали з серверу {guild}')
        await member.send(embed = embed)

    except discord.DiscordException:
        embed_no_arg = discord.Embed(title = f'Таакс, щось тут пішло не так👀', description = f'{author}, щось мені здається що для виконання цієї команди недостатньо аргументів, якщо я не відповідаю то...\nКікніть користувача правою кнопкою миші', color = 0x627bad)
        await ctx.send(embed = embed_no_arg)
            
        
#0x8592aa

@client.command()
@commands.has_permissions(ban_members = True)
async def ban( ctx, user_id: int, *, reason=None, member: discord.Member):
    await ctx.channel.purge(limit=1)
    author = ctx.author
    try:
        await ctx.guild.ban(reason=reason)
        await ctx.send(embed = discord.Embed(description = f'**{user_id} забанили за причиною ' + reason + '.**', color = 0x8592aa))
        if SEND_PUNISHMENT_PERSONAL_MESSAGE:
            await user.send(embed = discord.Embed(description = f'**F, вас забанили**', color = 0x8592aa))
    except discord.DiscordException:
            no_user = discord.Embed(title = 'ех, рідний тернопіль', description = 'Щось мені здається, що мені недостатньо аргументів для виконнаня бану🤔', color = 0x8592aa)
            await ctx.send(embed = no_user)

   

@client.command(name='unban')
@commands.has_permissions(administrator=True)
async def unban(ctx, *, user_id: int, member: discord.Member, guild: discord.Guild):
        await ctx.message.delete()
        try:
            user = await client.fetch_user(user_id=user_id)
            await ctx.guild.unban(user)
            await ctx.send(embed = discord.Embed(description = f'**Користувач з ID {user_id} успішно розбанений.**', color = 0x8592aa))
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await user.send(embed = discord.Embed(description = f'**Вас успішно розбанено на сервері!**', color = 0x8592aa))
        except discord.DiscordException:
            await ctx.send(embed = discord.Embed(description = f'**Користувач з ID {user_id} не забанений, тому не може бути розбаненим.**', color = 0x8592aa))

@client.command()
async def userinfo(ctx,member:discord.Member):
    try:
        emb = discord.Embed(title=f'Про {member}',color=0x8592aa)
        emb.add_field(name="Приєднався на сервер:",value=member.joined_at,inline=False)
        emb.add_field(name='Нікнейм:',value=member.display_name,inline=False)
        emb.add_field(name='Айді:',value=member.id,inline=False)
        emb.add_field(name="Акаунт створено:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)
    except discord.DiscordException:
        author = ctx.message.author
        await ctx.send(embed = discord.Embed(description = f'{author}, недостатньо аргументів для виконання цієї команди!', color = 0x8592aa))
    

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

    await member.add_roles(mute_role)
    await ctx.send(embed = discord.Embed(description = f'Користувача {member.mention} замьючено.', colour = 0x8592aa))

@client.command()
async def avatar(ctx, *,  member:discord.Member):
    author = ctx.message.author
    emb = discord.Embed(title = f'Аватар для {author}', color = 0x8592aa)
    emb.set_image(url=member.avatar_url)
    emb.set_footer(text = 'Виглядає гарно')
    await ctx.send(embed = emb)



@client.command()
async def hinn(ctx):
  emb = discord.Embed(title = 'Інформація про бота Хінн:', url='https://discord.com/api/oauth2/authorize?client_id=923260509724213288&permissions=8&scope=bot', colour = 0x8592aa)
  emb.add_field(name = 'Розробники',value = 'klancyidk#7110')
  emb.add_field(name = 'Стан:',value = 'Стабільна версія 1.2')
  emb.add_field(name = 'Сімейство:', value = 'Посилання: https://discord.gg/trJZmZhAKb ')
  emb.add_field(name = 'ОС:', value = 'Не знаю для кого це потрібно але Windows 10, іноді Ubuntu 20.04')
  emb.add_field(name = 'МП:', value = 'Python 3.8.8')
  emb.add_field(name = 'Версія discord.py:', value = '1.7.3')
  emb.add_field(name = 'Мова інтерфейсу:', value = 'Українська, але думаємо над англійською.')
  emb.add_field(name = 'Хостинг бота:',value = '<:Heroku:902583914806259763>Heroku')
  emb.add_field(name = 'Додати мене на свій сервер:', value = 'Тиць на назву ембеду')
  emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/924403524987682826/931224522944815124/tumblr_366faa2e093caade0b24db7c22ac0898_39f4ebec_1280.jpg')
  emb.set_footer(text=f"klancyidk ©️ | всі права захищені.")
  await ctx.send(embed=emb)

@client.command()
async def poll(ctx, *,message,):
    author = ctx.message.author
    emb = discord.Embed(title=f"Опитування від {author}:",description=f"{message}", colour = 0x8592aa)
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@client.command()
async def say(ctx, *, text):
    await ctx.send(embed = discord.Embed(description = text,  colour = 0x8592aa))

@client.command()
async def quote(ctx,*, text,):
    author = ctx.message.author
    embed = discord.Embed(title = f'Цитата від {author} :pinched_fingers:', color = 0x8592aa)
    embed.add_field(name = text)
    embed.set_thumbnail(url=author.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def action(ctx, *, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'{author}:', description = text, color = 0x8592aa)
    await ctx.send(embed = embed)

@client.command()
async def news(ctx, *, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'Новина від {author}:', description = text, color = 0x8592aa)
    await ctx.send(embed = embed)


@client.command()
async def help(ctx):
    page1 = discord.Embed (
        title = 'Допомагаю!',
        description = '**💻Модераційні команди:**\n`ban`, `unban`, `kick`, `warn`, `mute`',
        color = 0x8592aa
    )
    page2 = discord.Embed (
        title = 'Допомагаю! х2',
        description = '**📄Інформаційні комаанди:**\n `hinn`, `userinfo`, `serverinfo`\n **💽Утилітні команди:**\n `clear`, `avatar`, `ping`, `say`, `action`, `poll`, `google`, `invite`, `nitro`, `weather`, `fox`, `quote`, `news`, `worldmap`, `ukrainemap`, `setprefix`',
        color = 0x8592aa
    )
    page3 = discord.Embed (
        title = 'Допомагаю... х3',
        description = '**☠Таймкіллери:** \n `minesweeper`, `calc`, `answer`, `ppsize`, `dota`\n**🎶Співи:** \n `play`, `skip`, `leave`, `loop`, `queue`, `shuffle`, `stop`, `resume`, `join`, `summon`, `volume`\nХінн буде співати лише з префіксом **h!**',
        color = 0x8592aa
    )
    
    

    
    
    pages = [page1, page2, page3,]

    message = await ctx.send(embed = page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed = pages[i])
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break





@client.command()
async def serverinfo(ctx):
      guild = ctx.guild
      embed = discord.Embed(title=f'Сервер {guild}', description="Який чудовий сервер!", timestamp=ctx.message.created_at, color=discord.Color.red())
      embed.set_thumbnail(url=guild.icon_url)
      embed.add_field(name="Кількість каналів:", value=len(guild.channels))
      embed.add_field(name="Ролей:", value=len(guild.roles))
      embed.add_field(name='Айді серверу:', )
      embed.add_field(name="Бусти:", value=guild.premium_subscription_count)
      embed.add_field(name="Кількість учасників:", value=guild.member_count)
      embed.add_field(name="Сервер створено:", value=guild.created_at)
      embed.add_field(name="Власник серверу:", value=guild.owner.display_name)
      embed.set_footer(text=f"Сервером зацікавився {ctx.author}", icon_url=ctx.author.avatar_url)

      await ctx.send(embed=embed)


@client.command()
async def serveravatar(ctx, guild: discord.Guild = None):
    emb = discord.Embed(title = f'Аватар серверу {guild.name}', color = 0x8592aa)
    emb.set_image(url=guild.icon_url)
    emb.set_footer(text = 'Який гарний аватар, я б сам собі такий мав :()')
    await ctx.send(embed = emb)


@client.command()
async def qd(ctx):
    await ctx.reply('https://i.ytimg.com/vi/zPc1uwMVBAg/hqdefault.jpg')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        emoji = '🤔'
        await ctx.message.add_reaction(emoji)
        


@client.command()      
async def dota(ctx):
    emb = discord.Embed(title = f'друже...', color = 0x8592aa)
    emb.set_image(url = 'https://i.gifer.com/3njl.gif')
    await ctx.reply(embed = emb)
    await ctx.author.send(embed = discord.Embed(title = 'Мої вітання!', description = f'Ви використали саму крінжову команду у всьому асортименті Хінна! За це ви отримуєте нічого! Як бачите, й вам щастить😁', color = 0x8592aa))

@client.command()
async def nitro(ctx):
    emb = discord.Embed(title = 'Бажаєте нітро?', description = 'Тримайте, https://bit.ly/3FjXsFu', color = 0x8592aa)
    await ctx.reply(embed = emb)
    await ctx.author.send(embed = discord.Embed(description = f"**Увага!**\nЩодо команди `h!nitro`, команда є максимально жартівливого змісту, ми не несемо відповідальність за ваші особисті дані, якщо ви трохи пізніше побачили підозрілі дії на вашому акаунті - це не стосується нас. **Хінн ніколи не був і не буде розбійником!**\n Дякую за розуміння, ваші деви.", color = 0x8592aa))
    
    
@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Додати мене на свій сервер",
        description="Радий бачити, що хтось хоче додати мене на сервер!😯",
        url='https://discord.com/api/oauth2/authorize?client_id=923260509724213288&permissions=8&scope=bot',
        сolor = 0x8592aa,
    )
    await ctx.reply(embed=embed)

@client.command()
async def google(ctx,*, query):
		author = ctx.author.mention
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
					    await ctx.send(embed = discord.Embed(title = 'Ух ти, хтось вирішив пошукати щось не згортаючи дискорд', description = f'Ось і результати твого пошуку, {author}\n{j}', color = 0x8592aa))


@client.command()
async def calc(ctx, operation:str):
  await ctx.reply(eval(operation))

@client.command()
async def mendeleevtable(ctx):
        emb = discord.Embed(title="Таблиця Дмитра Івановича Менделєєва", color=0x8592aa)
        emb.set_image(url="https://cdn.discordapp.com/attachments/871344183988879360/909426071198375976/unknown.png")
        await ctx.send(embed = emb)

@client.command()
async def minesweeper(ctx):
    baka = discord.Embed(description = """**Пограймо в сапер?**)\n||1️⃣|| ||2️⃣|| ||💣|| ||2️⃣|| ||💣||
||💣|| ||3️⃣|| ||2️⃣|| ||3️⃣|| ||2️⃣||
||3️⃣|| ||💣|| ||1️⃣|| ||1️⃣|| ||💣||
||💣|| ||2️⃣|| ||1️⃣|| ||1️⃣|| ||1️⃣||""", color = 0x8592aa)
    await ctx.send(embed = baka)

@client.command()
async def weather(ctx, *, city: str):
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel
        if x["cod"] != "404":
            async with channel.typing():
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                weather_description = z[0]["description"]
                embed = discord.Embed(title=f"🌦Погода у місті {city_name}",
                              color=0x8592aa,
                              timestamp=ctx.message.created_at,)
                embed.add_field(name="Опис", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                embed.add_field(name="Вологість(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(name="Атмосферний тиск(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                embed.set_thumbnail(url="https://uxwing.com/wp-content/themes/uxwing/download/27-weather/weather.png")
                embed.set_footer(text=f"Завжди вдягайтесь по погоді!")
                await channel.send(embed=embed)
        else:
            await channel.send(embed = discord.Embed(description = '**Ойо**\nВаше містечко не знайдено.'))

@client.command()
async def answer(ctx):
    pp = discord.Embed(title="Хочете моєї відповіді?", description="буде вам моя відповідь...", color = 0x8592aa)
    pp.add_field(name="І моя відповідь...", value=random.choice(responses))

    await ctx.send(embed=pp)

@client.command()
async def ppsize(ctx):
    aboba = discord.Embed(title = "ем, я соромлюсь", description = "проте я скажу...))", color = 0x8592aa)
    aboba.add_field(name = "помераю від крінжі", value = random.choice(pp))
    await ctx.send(embed = aboba)


@client.command()
@commands.has_permissions(administrator = True)
async def warn(ctx, member: discord.Member, *, text):
    emb = discord.Embed(title="Партія розчарована вами👎", description="Привіт, я Хінн і мені сказали що ви порушуєте правила! На наступний раз старайтесь дотримуватись правил аби не було конфліктів🧐", colour=0x8592aa)
    emb.add_field(name='А дістали ви попередження від:', value=ctx.message.author)
    await member.send(embed = emb)
    emb = discord.Embed(title = f'Попередження\nА дехто в нас зараз отримає по шапці! {member} отримав попередження за причиною:', description = text, color =0x8592aa)
    await ctx.send(embed = emb)


@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text) 

    emb = discord.Embed(color = 0x8592aa, title = 'Як просили, картинка з лисичкою😃') 
    emb.set_image(url = json_data['link']) 
    await ctx.send(embed = emb)

@client.command()
async def ping(ctx):
    await ctx.reply(embed = discord.Embed(title = 'Понг!', description = f'{client.latency} ms', color = 0x8592aa))

@client.command()
async def time(ctx):
    time = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
    emb = discord.Embed(title = f'🕰Котра година?', description = f'За моїми розрахунками зараз {time} година!', color = 0x8592aa)
    await ctx.reply(embed = emb)

@client.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send(embed = discord.Embed(title = 'Зміна префікса', description = f'Зміна префікса пройшла успішно👩‍🏭', color = 0x8592aa))

@client.command()
async def kiss(ctx, *, text):
    emb = discord.Embed(title = 'Поцілунки', description = text, color = 0x8592aa)
    emb.set_image(url = 'https://acegif.com/wp-content/uploads/anime-kissin-10.gif')
    await ctx.send(embed = emb)

@client.command()
async def hug(ctx, *, text):
    emb = discord.Embed(title = 'Обійми🤗', description = text, color = 0x8592aa)
    emb.set_image(url = 'https://acegif.com/wp-content/gif/anime-hug-52.gif')
    await ctx.send(embed = emb)

@client.command()
async def slap(ctx, *, text):
    emb = discord.Embed(title = "Схоже на початок бійки!", description = text, color = 0x8592aa)
    emb.set_image(url = 'https://tenor.com/view/slap-jjk-nicevagg-anime-gif-22368283')

@client.command()
async def kill(ctx):
    author = ctx.author.mention
    emb = discord.Embed(title = f'Як бажаєте, {author} !', color = 0x8592aa)
    emb.set_image(url = 'https://i.gifer.com/DU2.gif')
    await ctx.send(embed = emb)

@client.command()
async def worldmap(ctx):
    emb = discord.Embed(title = 'Карта світу', color = 0x8592aa)
    emb.set_image(url = 'https://images.ua.prom.st/2152301041_w640_h640_karta-mira-anglijskaya.jpg')
    await ctx.send(embed = emb)

@client.command()
async def ukrainemap(ctx):
    emb = discord.Embed(title = 'Карта України', color = 0x8592aa)
    emb.set_image(url = 'https://artside.com.ua/tmp/cache/images/2b/de8/25002522-630x422-r.jpg')
    await ctx.send(embed = emb)


@client.event
async def on_member_join(member):
    channelsadg = client.get_channel(924037553559072769)
    emb = discord.Embed(title = 'Хтось приєднався до нашого серверу!', color = 0x8592aa)
    emb.add_field(name = f'Привіт, {member}', value = f'Радий вас бачити на сервері {member.guild.name}, перед початком розмов рекомендую ознайомитись з правилами/рекомендацією  адміністратора.\nПриємного спілкування!')
    emb.set_thumbnail(url = member.avatar_url)
    emb.set_image(url = 'https://media.giphy.com/media/9cZQnwdzUXTDG/giphy.gif')
    await channelsadg.send(embed = emb)


print('Урааа! Робе!!!')
client.run('OTIzMjYwNTA5NzI0MjEzMjg4.YcNbWg.D_b14LzIocpJAEi3X8wK7vmrW9M')
