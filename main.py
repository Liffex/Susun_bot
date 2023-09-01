import discord
import logging

import mcstatus

from SusunClient import SusunClient
from mcstatus import JavaServer

if __name__ == '__main__':
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter("")

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
