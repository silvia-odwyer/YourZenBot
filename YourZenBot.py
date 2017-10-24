import discord
import asyncio
import random
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!', description = "YourZenBot: Bringing wisdom to you from the universe. !!! For entertainment purposes only.")

@bot.event
async def on_ready():
	print("Logged in as")
	print(bot.user.name)

@client.event
async def on_ready():
	print("Logged in as: ")
	print("Your client username is: ", client.user.name)
	print("Your client user ID is: ", client.user.id)
	print("------")
	print("Has the client logged in?", client.is_logged_in)
	
@bot.command()
async def howareyou():
	await bot.say("I am good, thanks! I'm only a bot, I don't have feelings, but maybe I will someday :D")
	
@bot.command()
async def hello():
	await bot.say("Hello! I am YourZenBot, a Discord bot that tries to add some positivity to your life. :) But enough talking. Time for you to talk to me! I'm waiting :)")
	
@bot.command()
async def whatislife():
	await bot.say("I'm only a robot :( I don't have the answers to everything. But if I had to, I'd say: You are life. ;)")
	
@bot.command
async def _bot():
	"""Is the bot cool?"""
	await bot.say("I'm not cool yet, but maybe I will be someday. :) ")

@client.event
async def on_message(message):
	userMessage = message.content.lower()
	if userMessage == "!hithere":
		await client.send_message(message.channel, "Hi! :D")
		
	elif userMessage == "!talktome":
		await client.send_message(message.channel, "I'm always open to talk. But first you have to talk to me :)")
		
	elif userMessage == "!future" or userMessage == "!fortune":
		await client.send_message(message.channel, "You want a small prediction on what's lying in the stars? YourZenBot will do so!")
		random_number = random.randint(0, 1)
		fortune_list = ["The future looks bright for you!", "The future looks bleak for you. :("]
		prediction = fortune_list[random_number]
		await client.send_message(message.channel, "Your prediction is: " + prediction)
		await client.send_message(message.channel, "If you would like some wise words, just type !wisewords ")
		
	elif userMessage == "!wisewords":
		random_number = random.randint(0, 4)
		wise_words_list = ["Take a look behind you. Therein lies a clue.", "The greatest things in life are the things you accomplish.", 
						   "Don't be worried about tomorrow. That'll fall into place after you work on today. ;)", "Listen to your favourite music. It's transcending.",
						   "All you have to do is look to the sky and listen.", "Let the rain of the cosmos fall on you. Be at peace with yourself."]
		wise_message = wise_words_list[random_number]				
		await client.send_message(message.channel, wise_message)
		
	elif userMessage == "!question":
		random_number = random.randint(0, 2)
		answers = ["Hell yeah!", "Sorry, not for now. But try again in a few minutes. Maybe your luck will change ;)", 
		"Maybe, maybe. Hmmm . . . ", 
		"My readings aren't great right now. There must be some electrical short circuiting going on right now. I'm frazzled. :("]
		final_answer = answers[random_number]
		await client.send_message(message.channel, final_answer)
		
	await bot.process_commands(message)
		
client.run("YOUR CLIENT ID GOES HERE")
