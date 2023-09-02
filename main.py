import discord
import os

from SusunClient import SusunClient
from discord import app_commands
from dotenv import load_dotenv

dotenv_path = os.path.join('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

server_host = os.getenv("SERVER_HOST")
api_token = os.getenv("APIKEY")

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = SusunClient(intents=intents)
    tree = app_commands.CommandTree(client)


    @client.event
    async def on_ready():
        await tree.sync()


    client.run(api_token)
