# import logging
#
# import discord
# from discord import app_commands
# from mcstatus import JavaServer
#
# from main import server_host, api_token
#
#
# class MinecraftClient(discord.Client):
#     async def on_ready(self):
#         logging.info(f"MinecraftClient is UP as {self.user}")
#
#     async def on_connect(self):
#         logging.debug(f"MinecraftClient successfully connected to server")
#
#
# intents = discord.Intents.default()
# intents.message_content = True
# minecraftClient = MinecraftClient(intents=intents)
# minecraftCommandTree = app_commands.CommandTree(minecraftClient)
#
#
# def getServerStatus(host):
#     server = JavaServer.lookup(host)
#
#     try:
#         server.status()
#         return server.status()
#     except (TimeoutError, ConnectionRefusedError):
#         return []
#
#
# @minecraftCommandTree.command(name="players", description="Check players count")
# async def players(interaction: discord.Interaction):
#     server = JavaServer.lookup(server_host)
#     status = server.status()
#     await interaction.response.send_message(f"Сейчас на сервере {status.players.online} chelovek")
#
#
# @minecraftCommandTree.command(name="online", description="Check online")
# async def check_online(interaction: discord.Interaction):
#     server = JavaServer.lookup(server_host)
#     try:
#         await interaction.response.defer()
#         server.status()
#         msg = "Сервер онлайн!"
#     except (TimeoutError, ConnectionRefusedError):
#         msg = "Сервер оффлайн((("
#     await interaction.followup.send(msg)
#
#
# @minecraftCommandTree.command(name="ip", description="Check online")
# async def ip_command(interaction: discord.Interaction):
#     await interaction.response.send_message(server_host)
#
#
# minecraftClient.run(api_token)
