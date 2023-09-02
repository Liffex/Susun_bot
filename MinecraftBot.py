import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from mcstatus import JavaServer

from mcstatus.status_response import JavaStatusResponse

description = 'Бот майнкрафт сервера'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

dotenv_path = os.path.join('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

server_host = os.getenv("SERVER_HOST")
api_token = os.getenv("APIKEY")

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


def get_server_status(host):
    server = JavaServer.lookup(host)

    try:
        server.status()
        return server.status()
    except (TimeoutError, ConnectionRefusedError):
        return False


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.hybrid_command(description='Количество игроков онлайн')
async def online(interaction: discord.ext.commands.Context):
    server_status = get_server_status(server_host)
    if isinstance(server_status, JavaStatusResponse):
        await interaction.send(
            f"Сейчас на сервере {server_status.players.online} из {server_status.players.max} игроков")
    else:
        await interaction.send('Сервер оффлайн(')


@bot.hybrid_command(description='Список игроков на сервере')
async def players(interaction: discord.ext.commands.Context):
    server_status = get_server_status(server_host)
    if isinstance(server_status, JavaStatusResponse):
        sample = server_status.players.sample
        if sample is None:
            await interaction.send('Сервер пуст')
        else:
            player_list = []
            for player in sample:
                player_list.append(player.name)
            await interaction.send(f"Игроки на сервере: {', '.join(player_list)}")
    else:
        await interaction.send('Сервер оффлайн')


@bot.hybrid_command(description='Статус сервера')
async def server(interaction: discord.ext.commands.Context):
    server_status = get_server_status(server_host)
    if isinstance(server_status, JavaStatusResponse):
        await interaction.send('Сервер онлайн')
    else:
        await interaction.send('Сервер оффлайн')


@bot.hybrid_command(description='Адрес сервера')
async def ip(interaction: discord.ext.commands.Context):
    await interaction.send(f"Подключиться к серверу можно по адресу {server_host}")


bot.run(api_token)
