import json
import discord
import os
import time
from discord import embeds
from discord import emoji
from discord import guild
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



colors = [0x627bad]

intents = discord.Intents().all()
client = commands.Bot( command_prefix = 'h!' )
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
    notificationChannel = client.get_channel(874970041609769000)
    await notificationChannel.send(embed = discord.Embed(description = f"**перезапуск хоста**\n доброго ранку, не звертайте уваги на це повідомлення.", color = 0x627bad))
    while True:
         time = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
         await client.change_presence(status=discord.Status.dnd, activity=discord.Game(f"h!help | {time}"))
         await sleep(5)
         await client.change_presence(status=discord.Status.dnd, activity=discord.Game(f"{len(client.guilds)} servers "))
         await sleep(5)
    

@client.event
async def on_guild_join(guild):
    await guild.text_channels[0].send(embed = discord.Embed(description = f'**Вдячний за те що додали на сервер!**\n Всім привіт, мене звуть Хінн. Я україномовний дискорд бот, трошки крінжовий але з непоганим функціоналом. В моєму ассортименті команд присутні модераційні, утилітні, інформаційні та розважальні. Якщо ви вперше користуєтесь мною або підзабули мій функціонал то напишіть команду `h!help. Бажаю приємного спілкування<:tomokoSip:783387311840034839> ` '))

@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", color = 0x627bad).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)

@client.command()
async def hello(ctx):
  author = ctx.message.author
  await ctx.send( f'Привіт {author.mention}!' )

@client.command()

@commands.has_permissions(manage_messages=True)
@commands.has_permissions( administrator = True )

async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed = discord.Embed(description = f'**Очистка чату пройшла успішно.**', color = 0x627bad))

@client.command()
@commands.has_permissions(administrator = True)
async def kick( ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(embed = discord.Embed(description = f'**Користувача {member} вигнали за причиною** ' + reason + '**'))

@client.command()
@commands.has_permissions(administrator = True)
async def warn(ctx, member: discord.Member, *, reason=None):
	await ctx.send(embed = discord.Embed(description = f'**Користувача {member} попереджено .**'))

@client.command()
@commands.has_permissions(administrator = True)
async def ban( ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(embed = discord.Embed(description = f'Користувача {member} заблоковано за причиною ' + reason + '.'))

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Користувача {user} розблоковано.")
            return

@client.command()
async def userinfo(ctx,member:discord.Member):
    emb = discord.Embed(title=f'Інформація про користувача {member}',color=wuw(colors))
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
async def avatar(ctx, *,  avamember:discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(title = 'Шукаєте аватар?', color = 0x627bad)
    embed.set_image(userAvatarUrl)


@client.command()
@commands.has_permissions(administrator = True)
async def delete_channels(ctx):
    [await channel.delete() for channel in ctx.guild.text_channels]
    [await channel.delete() for channel in ctx.guild.voice_channels]

@client.command()
async def hinn(ctx):
  emb = discord.Embed(title = 'Інформація про бота Хінн:', colour = 0x627bad)
  emb.add_field(name = 'Розробники',value = 'klancyidk#7110, частково !! Yuk1ch#7849')
  emb.add_field(name = 'Стан:',value = 'у розробці, сира версія')
  emb.add_field(name = 'Сімейство:', value = 'Посилання: https://discord.gg/trJZmZhAKb ')
  emb.add_field(name = 'ОС, на якій розроблюється бот', value = 'Не знаю для кого це потрібно але Windows 10, іноді Ubuntu 20.04')
  emb.add_field(name = 'Мова програмування:', value = 'Python')
  emb.add_field(name = 'Мова інтерфейсу:', value = 'Українська, але в планах і англійська.')
  emb.add_field(name = 'Хостинг бота:',value = 'ПК Розробника, але при релізі планується Heroku')
  emb.add_field(name = 'Додати мене на свій сервер:', value = 'https://discord.com/api/oauth2/authorize?client_id=918929924277043240&permissions=8&scope=bot')
  emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/918929924277043240/bf90bee409d69ea9184fbd409190ec8e.webp?size=1024')
  emb.set_footer(text=f"klancyidk ©️ | всі права зафіксовані.",icon_url= 'https://cdn.discordapp.com/avatars/748185779733266474/a_5cf15f71e322a74e53e04e5cc84d7d32.gif?size=1024')

  await ctx.send(embed=emb)

@client.command()
async def poll(ctx, *,message):

    emb = discord.Embed(title="<a:Tamiko_news:904314834869432371>Опитування:",description=f"{message}", colour = wuw(colors))
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@client.command()
async def say(ctx, *, text):
    await ctx.send(embed = discord.Embed(description = text,  colour = wuw(colors)))

@client.command()
async def action(ctx,*, text):
    author = ctx.message.author
    embed = discord.Embed(title = f'Цитата від {author} :pinched_fingers:', color = 0x627bad)
    embed.add_field(name = text, value = 'прислухайтесь!')
    await ctx.send(embed = embed)


@client.command()
async def help(ctx):
    await ctx.send(embed = discord.Embed(description = f'**Вас вітає навігаційне меню Хінна! Розпочнемо подорож!**\n **💻Модераційні команди:**\n`ban`, `unban`, `kick`, `warn`, `mute`\n **📄Інформаційні комаанди:**\n `hinn`, `userinfo`, `serverinfo`\n **💽Утилітні команди:**\n `clear`, `avatar`, `delete_channels`, `ping`, `say`, `action`, `poll`, `find`, `invite`, `nitro`, `weather` \n☠Таймкіллери: \n `minesweeper`, `calc`, `answer`, `ppsize` ', color = 0x627bad))


@client.command()
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.message.guild
    roles =[role for role in guild.roles]
    text_channels = [text_channels for text_channels in guild.text_channels]
    embed = discord.Embed(title=f'{guild.name} ', description="Про сервер", timestamp=ctx.message.created_at, color=wuw(colors))
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
async def ping(ctx):
     await ctx.send(embed = discord.Embed(description = f'**Понг!** {round(client.latency * 1000)} ms', color = 0x627bad))


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
        emoji = '🤨'
        await ctx.message.add_reaction(emoji)


@client.command()      
async def dota(ctx):
    await ctx.reply('https://tenor.com/view/intel-dead-inside-logo-gif-16821712')

@client.command()
async def nitro(ctx):
    await ctx.reply('тримай друже. \n ||https://bit.ly/3FjXsFu||')

@client.command()
async def invite(ctx):
    await ctx.reply('Радий бачити, що хтось хоче отримати мій інвайт. \n https://discord.com/api/oauth2/authorize?client_id=923260509724213288&permissions=8&scope=bot ')


@client.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(embed = discord.Embed(description =f"\nОсь результати твого пошуку, {author} \n {j}", color =0x627bad))


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



print('аддеба!')
client.run('OTIzMjYwNTA5NzI0MjEzMjg4.YcNbWg.D_b14LzIocpJAEi3X8wK7vmrW9M')
