import logging

import discord


class SusunClient(discord.Client):

    async def on_ready(self):
        logging.info(f"Bot is UP as {self.user}")
        await tree.sync()

    async def on_connect(self):
        logging.debug(f"Bot successfully connected to server")
