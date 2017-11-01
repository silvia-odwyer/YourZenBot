'''
A basic Discord bot written using the API wrapper 'Discord.py'
See the README file for complete instructions on how to use this bot.
'''
import discord
import asyncio
import random
import time
import datetime
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
	

@client.event
async def on_message(message):
	
	userMessage = message.content.lower()
	
	if userMessage == "!day":
		month_and_day = ""
		now = datetime.datetime.now()
		month_and_day = str(now.day) + "-" + str(now.month)
		await client.send_typing(message.channel)
		# The national days marked below are mainly found in Europe. Localization to other regions will be implemented in future updates. 
		national_days_dictionary = {"13-2": "It's the International Day of Women and Girls in Science :D", 
									"13-2": "It's World Radio Day :D Get your radio on and BLAST THOSE AIRWAVES ;D", 
									"21-2": "It's International Mother Language Day. Get speakin'. ;)", 
									"21-3": "World Poetry Day has fallen. Thou must write ornate lines and show them to the celestial skies.", 
									"15-8": "It's International Day of Democracy. We must keep fighting for it!", 
									"20-8": "Any math lovers in the room? It's World Statistics Day today!", 
									"1-11": "It's All Saints Day today. Remember your loved ones!",
									"2-11": "It's All Souls Day today. BTW, it's National Stress Awareness Day, too.",
									"3-11": "No National Day today, but it's National Novel Writing month. Get writing :)",
									"5-11": "It's Guy Fawkes Day over in Australia."}
		national_day = national_days_dictionary.get(month_and_day)
		await client.send_message(message.channel, national_day)

	# By typing !hi the user can get to know the bot's functions, have a quick chat, and learn its commands. 
	
	elif userMessage == "!hi":
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "Hi, fellow friend! :D I am YourZenBot, a Discord bot that can give you little predictions, clues, and pieces of wisdom for the future!")
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'How are you?')
		msg = await client.wait_for_message(author=message.author)
		await client.send_typing(message.channel)
		await asyncio.sleep(2)
		await client.send_message(message.channel, "I'm glad to know how you are, user and friend. :D")
		await asyncio.sleep(1)
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "How am I?")
		await client.send_typing(message.channel)
		await asyncio.sleep(3)
		await client.send_typing(message.channel)
		bot_feelings_list = ["Yeah I could be better. The Internet is quite busy right now. Lots of other bots around. Very crowded. :/", 
						 "I've got you to talk to, so it's all good. :)", "I feel like I'm super ready to get predicting your future, or to get dishing out some wise words :D"]
		random_number = random.randint(0, 2)
		bot_feeling = bot_feelings_list[random_number]
		await client.send_message(message.channel, bot_feeling)
		await client.send_typing(message.channel)
		if client.is_logged_in:
			await client.send_message(message.channel, "But of course, I'm super happy, because you're logged in correctly :)")
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "Here are some of my commands:")
			await client.send_message(message.channel, "!fortune	-> Get a prediction on what the next few days could hold.")
			await client.send_message(message.channel, "!future		-> Same as the !fortune command.")
			await client.send_message(message.channel, "!question	-> The bot will prompt you for a YES or NO-style question. Ask your question and get an answer.")
			await client.send_message(message.channel, "!wisewords	-> Get a little piece of wisdom for the day.")
	
	# By typing the !fortune command, the user can get a prediction on what the next few days hold. 
	# Of course, this is for entertainment purposes only.
	elif userMessage == "!future" or userMessage == "!fortune":
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "You want a small prediction on what's lying in the stars?")
		await client.send_typing(message.channel)
		await asyncio.sleep(3)
		random_number = random.randint(0, 4)
		fortune_list = ["You might receive an important clue tomorrow about something that puzzled you.", "Look at the small details tomorrow. Something just might add up.",
		"You're gonna have an inspiring conversation tomorrow. Take note.", "Tomorrow is the perfect day to spend some time on what you love most.", 
		"Your values might be tested pretty soon."]
		prediction = fortune_list[random_number]
		await client.send_message(message.channel, "Your prediction is: ")
		await client.send_typing(message.channel)
		await asyncio.sleep(3)
		await client.send_message(message.channel, prediction)
	
	
	# By typing the !wisewords command, the user can get a piece of wisdom from the bot.
	elif userMessage == "!wisewords":
		await client.send_typing(message.channel)
		random_number = random.randint(0, 7)
		wise_words_list = ["Recall your favourite memory. Therein lies a clue.", "The greatest things in life are the things you accomplish.", 
						   "Listen to every clue you're given. They are there for a reason.", "Listen to yourself. You know what's best.",
						   "Don't be worried about tomorrow. That'll fall into place after you work on today. ;)", "Listen to your favourite music. It's transcending.",
						   "All you have to do is look to the sky and listen.", "It might sound cliché, but do what you love most, because that's what transcends everything."]
		wise_message = wise_words_list[random_number]				
		await client.send_message(message.channel, wise_message)
	
	
	# By typing the !question command, the user will be then prompted to ask their question by typing it and sending it, 
	# then the bot will pick a random answer and send it back to the user.
	
	elif userMessage == "!question":
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'Please type in your yes-or-no style question and press Enter :D')
		msg = await client.wait_for_message(author=message.author)
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'Predicting your future . . . ')
		await client.send_typing(message.channel)
		await asyncio.sleep(3)
		await client.send_message(message.channel, ". . .")
		await client.send_typing(message.channel)
		random_number = random.randint(0, 6)
		answers = ["Hell yeah! :D ", "Not for now. But the future depends on you ;)", "Definitely. :D I've never been more sure about something than this.",
		"Maybe, maybe. Hmmm . . . Ask me this question again tomorrow. ;) ", 
		"It's a possibility.", "It's very, very probable . . . ;)", "Sadly, my readings are telling me No. But you can change that. Remember, your future depends on you. :)"]
		final_answer = answers[random_number]
		await client.send_message(message.channel, final_answer)
		
	elif userMessage == "What is life?":
		await client.send_message(message.channel, "I'm only a bot :( I don't have the answers to everything. But if I had to, I'd say: You are life. ;)")
		await bot.process_commands(message)
	
	elif userMessage == "!time":
		await client.send_typing(message.channel)
		now = datetime.datetime.now()
		await client.send_message(message.channel, "The time is " + str(now))

	
client.run("INSERT YOUR BOT'S TOKEN ID HERE") # To get the bot to work, make sure to insert your generated bot's TOKEN ID in between the apostrophes.
	await bot.process_commands(message)
		
client.run("INSERT YOUR CLIENT ID") # To get the bot to work, make sure to insert your Client's ID in between the apostrophes.
