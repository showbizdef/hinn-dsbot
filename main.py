#!/usr/bin/python
# -*- coding: utf8 -*-
import json
import discord
import os
import time
from discord import embeds
from discord import emoji
from discord import guild
from discord import user
from discord.client import Client
import discord.ext
from discord.ext.commands import bot
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



custom_prefixes = {}
default_prefixes = ['h!']


async def determine_prefix(bot, message):
    guild = message.guild
    
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes


colors = [0x627bad]

intents = discord.Intents.default()
intents.members = True
intents = discord.Intents().all()
client = commands.Bot(command_prefix = determine_prefix,)
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


@client.event
async def on_ready():
    while True:
         time = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
         await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"h!help | {time}"))
    

@client.event
async def on_guild_join(guild):
    emb = discord.Embed(title = 'Привіт! Вдячний що додали мене на сервер😄', description = f'Я Хінн. Крінжовенький україномовний бот з непоганим функціоналом. В мій асортимент входить модераційний, утилітний, та розважальний розділ. Для докладнішого ознайомлення з моїми командами напишіть `h!help` у загальному чаті', color = 0x627bad)
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/925139079673286710/925148709308739624/hinnlogo.png')
    emb.set_footer(text = 'klancyidk ©️ | всі права зафіксовані. ')
    await guild.text_channels[0].send(embed = emb)

@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", color = 0x627bad).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


@client.command()
@commands.has_permissions(manage_messages=True)
@commands.has_permissions( administrator = True )
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed = discord.Embed(description = f'**Очистка чату пройшла успішно.**', color = 0x627bad))


@client.command(pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick( ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(embed = discord.Embed(description = f'**{member} вигнали за причиною ' + reason + ' радіємо хлопці та дівчата!**', color = 0x627bad))

@client.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def ban( ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(embed = discord.Embed(description = f'**{member} забанили за причиною ' + reason + '.**', color = 0x627bad))

@client.command(name='unban')
@commands.has_permissions(administrator=True)
async def unban(ctx, *, user_id: int):
        await ctx.message.delete()
        try:
            user = await client.fetch_user(user_id=user_id)
            await ctx.guild.unban(user)
            await ctx.send(embed = discord.Embed(description = f'**Користувач з ID {user_id} успішно розбанений.**', color = 0x627bad))
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await user.send(embed = discord.Embed(description = f'**Вас успішно розбанено на сервері!**', color = 0x627bad))
        except discord.DiscordException:
            await ctx.send(embed = discord.Embed(description = f'**Користувач з ID {user_id} не забанений, тому не може бути розбаненим.**', color = 0x627bad))

@client.command()
async def userinfo(ctx,member:discord.Member):
    emb = discord.Embed(title=f'Інформація про користувача {member}',color=0x627bad)
    emb.add_field(name="Приєднався на сервер:",value=member.joined_at,inline=False)
    emb.add_field(name='Нікнейм:',value=member.display_name,inline=False)
    emb.add_field(name='Айді:',value=member.id,inline=False)
    emb.add_field(name="Акаунт створено:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Команду застосував:  {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)
    

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

    await member.add_roles(mute_role)
    await ctx.send(embed = discord.Embed(description = f'Користувача {member.mention} замьючено.', colour = 0x627bad))

@client.command()
async def avatar(ctx, *,  member:discord.Member, author):
    emb = discord.Embed(title = 'Шукаєте аватар?', color = 0x627bad)
    emb.set_image(url=member.avatar_url)
    await ctx.reply(embed = emb)


@client.command()
@commands.has_permissions(administrator = True)
async def delete_channels(ctx):
    emb = discord.Embed(title = 'Ви впевнені?', description = "Через велику кількість скарг ми обмежили користування цією командою. Ми не хотіли щоб сервери постраждали від нашої команди яка мала рятувати а не ламати гільдії над якими всю душу вкладали :(", color = 0x627bad)
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/924403524987682826/925124257615335424/obamahamburger.png')
    await ctx.send(embed = emb)

@client.command()
async def hinn(ctx):
  emb = discord.Embed(title = 'Інформація про бота Хінн:', colour = 0x627bad)
  emb.add_field(name = 'Розробники',value = 'klancyidk#7110, частково !! Yuk1ch#7849')
  emb.add_field(name = 'Стан:',value = 'у розробці, сира версія')
  emb.add_field(name = 'Сімейство:', value = 'Посилання: https://discord.gg/trJZmZhAKb ')
  emb.add_field(name = 'ОС, на якій розроблюється бот', value = 'Не знаю для кого це потрібно але Windows 10, іноді Ubuntu 20.04')
  emb.add_field(name = 'Мова програмування:', value = 'Python')
  emb.add_field(name = 'Мова інтерфейсу:', value = 'Українська, але в планах і англійська.')
  emb.add_field(name = 'Хостинг бота:',value = 'Пк Розробники ||при оновленні буде використовуватись Heroku||')
  emb.add_field(name = 'Додати мене на свій сервер:', value = 'https://discord.com/api/oauth2/authorize?client_id=918929924277043240&permissions=8&scope=bot')
  emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/918929924277043240/bf90bee409d69ea9184fbd409190ec8e.webp?size=1024')
  emb.set_footer(text=f"klancyidk ©️ | всі права зафіксовані.",icon_url= 'https://cdn.discordapp.com/avatars/748185779733266474/a_5cf15f71e322a74e53e04e5cc84d7d32.gif?size=1024')

  await ctx.send(embed=emb)

@client.command()
async def poll(ctx, *,message,):
    author = ctx.message.author
    emb = discord.Embed(title=f"Опитування від {author}:",description=f"{message}", colour = 0x627bad)
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@client.command()
async def say(ctx, *, text):
    await ctx.send(embed = discord.Embed(description = text,  colour = 0x627bad))

@client.command()
async def quote(ctx,*, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'Цитата від {author} :pinched_fingers:', color = 0x627bad)
    embed.add_field(name = text, value = 'прислухайтесь!')
    await ctx.send(embed = embed)

@client.command()
async def action(ctx, *, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'{author}:', description = text, color = 0x627bad)
    await ctx.send(embed = embed)

@client.command()
async def news(ctx, *, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'Новина від {author}:', description = text, color = 0x627bad)
    await ctx.send(embed = embed)

@client.command()
async def help(ctx):
    await ctx.send(embed = discord.Embed(description = f'**Вас вітає навігаційне меню Хінна! Розпочнемо подорож!**\n **💻Модераційні команди:**\n`ban`, `unban`, `kick`, `warn`, `mute`\n **📄Інформаційні комаанди:**\n `hinn`, `userinfo`, `serverinfo`\n **💽Утилітні команди:**\n `clear`, `avatar`, `delete_channels`, `ping`, `say`, `action`, `poll`, `find`, `invite`, `nitro`, `weather`, `fox`, `quote`, `news`, `worldmap`, `ukrainemap`, `setprefix`,  \n☠Таймкіллери: \n `minesweeper`, `calc`, `answer`, `ppsize`, `dota`, ', color = 0x627bad))


@client.command()
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.message.guild
    roles =[role for role in guild.roles]
    text_channels = [text_channels for text_channels in guild.text_channels]
    embed = discord.Embed(title=f'{guild.name} ', description="Про сервер", timestamp=ctx.message.created_at, color=0x627bad)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Кількість каналів:", value=f"{len(text_channels)}")
    embed.add_field(name="Кількість ролей:", value=f"{len(roles)}")
    embed.add_field(name="Кількість бустерів:", value=guild.premium_subscription_count)
    embed.add_field(name="Кількість учасників:", value=guild.member_count)
    embed.add_field(name="Сервер створено:", value=guild.created_at)
    embed.add_field(name="Власник серверу:", value=guild.owner)
    embed.set_footer(text=f"Команду використав {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def test(ctx):
    msg = await ctx.send(
        embed = discord.Embed(title = 'тест?', timestamp = ctx.message.created_at),
        components = [
            Button(style = ButtonStyle.green, label = 'так'),
            Button(style = ButtonStyle.red, label = 'ні')
        ])
    responce = await client.wait_for('button_click', check = lambda message: message.author == ctx.author)
    if responce.component.label == 'так':
        await responce.respond(content = 'тест буде!')
    else:
        await responce.respond(content = 'тесту не буде хехе.')

@client.command()
async def klancygay(ctx):
    await ctx.reply('погоджуюсь')

@client.command()
async def qd(ctx):
    await ctx.reply('https://i.ytimg.com/vi/zPc1uwMVBAg/hqdefault.jpg')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        emoji = '🤔'
        await ctx.message.add_reaction(emoji)
        await ctx.author.send(embed = discord.Embed(description = 'Судячи по всьому, ви не можете знайти або нормально написати якусь команду. Напишіть `h!help` для того щоб написати правильно команду або перевірити чи вона взагалі є😉', color = 0x627bad))
    


@client.command()      
async def dota(ctx):
    emb = discord.Embed(title = f'друже...', color = 0x627bad)
    emb.set_image(url = 'https://i.gifer.com/3njl.gif')
    await ctx.reply(embed = emb)
    await ctx.author.send(embed = discord.Embed(title = 'Мої вітання!', description = f'Ви використали саму крінжову команду у всьому асортименті Хінна! За це ви отримуєте нічого! Як бачите, й вам щастить😁', color = 0x627bad))

@client.command()
async def nitro(ctx):
    emb = discord.Embed(title = 'Бажаєте нітро?', description = 'Тримайте, https://bit.ly/3FjXsFu', color = 0x627bad)
    await ctx.reply(embed = emb)
    await ctx.author.send(embed = discord.Embed(description = f"**Увага!**\nЩодо команди `h!nitro`, команда є максимально жартівливого змісту, ми не несемо відповідальність за ваші особисті дані, якщо ви трохи пізніше побачили підозрілі дії на вашому акаунті - це не стосується нас. **Хінн ніколи не був і не буде розбійником!**\n Дякую за розуміння, ваші деви.", color = 0x627bad))
    
    


@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Додати мене на свій сервер",
        description="Радий бачити, що хтось хоче додати мене на сервер!😯",
        url='https://discord.com/api/oauth2/authorize?client_id=923260509724213288&permissions=8&scope=bot',
        сolor = 0x627bad,
    )
    await ctx.reply(embed=embed)

@client.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(embed = discord.Embed(description =f"**Хтось вирішив пошукати щось у гуглі не закриваючи дискорд🧐**\nОсь результати твого пошуку, {author} \n {j}", color =0x627bad))


@client.command()
async def calc(ctx, operation:str):
  await ctx.reply(eval(operation))

@client.command()
async def mendeleevtable(ctx):
        emb = discord.Embed(title="Таблиця Дмитра Івановича Менделєєва", color=0x627bad)
        emb.set_image(url="https://cdn.discordapp.com/attachments/871344183988879360/909426071198375976/unknown.png")
        await ctx.send(embed = emb)

@client.command()
async def minesweeper(ctx):
    baka = discord.Embed(description = """**Пограймо в сапер?**)\n||1️⃣|| ||2️⃣|| ||💣|| ||2️⃣|| ||💣||
||💣|| ||3️⃣|| ||2️⃣|| ||3️⃣|| ||2️⃣||
||3️⃣|| ||💣|| ||1️⃣|| ||1️⃣|| ||💣||
||💣|| ||2️⃣|| ||1️⃣|| ||1️⃣|| ||1️⃣||""")
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
                embed = discord.Embed(title=f"🌦Погода у {city_name}",
                              color=0x627bad,
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
    pp = discord.Embed(title="Хочете моєї відповіді?", description="буде вам моя відповідь...", color = 0x627bad)
    pp.add_field(name="І моя відповідь...", value=random.choice(responses))

    await ctx.send(embed=pp)

@client.command()
async def ppsize(ctx):
    aboba = discord.Embed(title = "ем, я соромлюсь", description = "проте я скажу...))", color = 0x627bad)
    aboba.add_field(name = "І його/її розмір пісюна...", value = random.choice(pp))
    await ctx.send(embed = aboba)

@client.command()
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=API_KEY_GOES_HERE')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=API_KEY_GOES_HERE&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()

    await ctx.send_message(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def warn(ctx, member: discord.Member, *, text):
    emb = discord.Embed(title="Партія розчарована вами👎", description="Привіт, я Хінн і мені сказали що ви порушуєте правила! На наступний раз старайтесь дотримуватись правил аби не було конфліктів🧐", colour=0x627bad)
    emb.add_field(name='А дістали ви попередження від:', value=ctx.message.author)
    await member.send(embed = emb)
    emb = discord.Embed(title = f'Попередження\nА дехто в нас зараз отримає по шапці! {member} отримав попередження за причиною:', description = text, color =0x627bad)
    await ctx.send(embed = emb)


@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text) 

    emb = discord.Embed(color = 0x627bad, title = 'Як просили, картинка з лисичкою😃') 
    emb.set_image(url = json_data['link']) 
    await ctx.send(embed = emb)

@client.command()
async def ping(ctx):
    await ctx.reply(embed = discord.Embed(title = 'Понг!', description = f'{client.latency} ms', color = 0x627bad))

@client.command()
async def time(ctx):
    time = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
    emb = discord.Embed(title = f'🕰Котра година?', description = f'За моїми розрахунками зараз {time} година!', color = 0x627bad)
    await ctx.reply(embed = emb)

@client.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send(embed = discord.Embed(title = 'Зміна префікса', description = f'Зміна префікса пройшла успішно👩‍🏭', color = 0x627bad))

@client.command()
async def kiss(ctx, *, text):
    emb = discord.Embed(title = 'Поцілунки', description = text, color = 0x627bad)
    emb.set_image(url = 'https://acegif.com/wp-content/uploads/anime-kissin-10.gif')
    await ctx.send(embed = emb)

@client.command()
async def hug(ctx, *, text):
    emb = discord.Embed(title = 'Обійми🤗', description = text, color = 0x627bad)
    emb.set_image(url = 'https://acegif.com/wp-content/gif/anime-hug-52.gif')
    await ctx.send(embed = emb)

@client.command()
async def slap(ctx, *, text):
    emb = discord.Embed(title = "Схоже на початок бійки!", description = text, color = 0x627bad)
    emb.set_image(url = 'https://tenor.com/view/slap-jjk-nicevagg-anime-gif-22368283')

@client.command()
async def kill(ctx):
    author = ctx.author.mention
    emb = discord.Embed(title = f'Як бажаєте, {author} !', color = 0x627bad)
    emb.set_image(url = 'https://i.gifer.com/DU2.gif')
    await ctx.send(embed = emb)

@client.command()
async def worldmap(ctx):
    emb = discord.Embed(title = 'Карта світу', color = 0x627bad)
    emb.set_image(url = 'https://images.ua.prom.st/2152301041_w640_h640_karta-mira-anglijskaya.jpg')
    await ctx.send(embed = emb)

@client.command()
async def ukrainemap(ctx):
    emb = discord.Embed(title = 'Карта України', color = 0x627bad)
    emb.set_image(url = 'https://artside.com.ua/tmp/cache/images/2b/de8/25002522-630x422-r.jpg')
    await ctx.send(embed = emb)

print('піздец робе')
client.run('OTIzMjYwNTA5NzI0MjEzMjg4.YcNbWg.D_b14LzIocpJAEi3X8wK7vmrW9M')
