import discord
import logging

from SusunClient import SusunClient
from mcstatus import JavaServer

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = SusunClient(intents=intents)


    @client.event
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return
        if message.content.startswith("$online"):
            server = JavaServer.lookup("212.12.14.7:25505")
            status = server.status()
            logging.info(status)
            await message.channel.send(f"Сейчас на сервере {status.players.online} chelovek")


    client.run("")
