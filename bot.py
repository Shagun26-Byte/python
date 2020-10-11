import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!!")

@client.event
async def on_ready():
	print("Bot is ready")

@client.command()
async def hi(ctx):
	await ctx.send("toh kese ho aap")

client.run("NzY0ODYzODY2OTA2NjA3NjU2.X4Mc_A.Y4q5hdqTEyR2vtMiP5DFwAj9VR8")
