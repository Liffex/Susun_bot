import discord
import os

from SusunClient import SusunClient
from mcstatus import JavaServer
from discord import app_commands
from dotenv import load_dotenv

dotenv_path = os.path.join('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = SusunClient(intents=intents)
    tree = app_commands.CommandTree(client)


    @tree.command(name="players", description="Check players count")
    async def testCommand(interaction: discord.Interaction):
        server = JavaServer.lookup("212.12.14.7:25505")
        status = server.status()
        await interaction.response.send_message(f"Сейчас на сервере {status.players.online} chelovek")


    @tree.command(name="online", description="Check online")
    async def check_online(interaction: discord.Interaction):
        server = JavaServer.lookup("212.12.14.7:25565")
        try:
            await interaction.response.defer()
            server.status()
            msg = "Сервер онлайн!"
        except TimeoutError:
            print("ХУЙ")
            msg = "Сервер оффлайн((("
        await interaction.followup.send(msg)


    @tree.command(name="ip", description="Check online")
    async def ip_command(interaction: discord.Interaction):
        await interaction.response.send_message("212.12.14.7:25505")


    @client.event
    async def on_ready():
        await tree.sync()


    # client.run("MTEzMzc3NjM4MTg2NDU3OTA4Mg.Gumz-O.Uspf3tsJvkbFD7Vb4jhd8E0-69sSv1bOPygTzY")
    client.run(os.getenv("APIKEY"))
