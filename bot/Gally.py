import discord
from discord.ext import commands
import os


TOKEN = os.getenv("DiscordBotToken")


client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

########################################
##############  Epv  ###################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

	if message.content.startswith("ePV "):
		a = 0
		b = 0
		x = ""
		invalid = False
		spacerequired = True
		info = message.content.replace("ePV ", "")
		for i in range(0,len(info)):
			if spacerequired == True and info[i] == " ":
				spacerequired = False
			elif list(info)[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
				invalid = True
		if spacerequired == True:
			invalid = True
		if invalid == False:

			for i in range(0,info.find(" ")):
				x += info[i]

			a = int(x)
			x = ""

			for i in range(info.find(" ") + 1, len(info)):
				x += info[i]

			b = int(x)

			c = round(a/(1-(b/(b+1500))))

			embed=discord.Embed(title="", description=" ", url="", color=0xffffff)
			embed.set_author(name=" ")
			embed.set_thumbnail(url="")
			embed.add_field(name="Calculs effectués avec:", value="\nPV: " + str(a) +"\nDéfense: " + str(b) + "\n\n__**ePV**__: " + str(c), inline=False)
			await message.channel.send(embed=embed)


		else:
			await message.channel.send("Ecrivez ePV suivi des PV et de la Def")

########################################
## Choisir ses gemmes (2 Def ou 2 Pv) ##
########################################

	ListElementInMessage = message.content.split()
	if ListElementInMessage[0] == "EpvGem":
		if len(ListElementInMessage) == 3 and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round((a * 2.36) / (1 - ((b * 1.68) / ((b * 1.68) + 1200))))
			d = round((a * 1.68) / (1 - ((b * 2.36) / ((b * 2.36) + 1200))))
			embed = discord.Embed(title="", description=" ", url="", color=0xffffff)
			embed.set_author(name=" ")
			embed.set_thumbnail(url="")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base: " + str(a) + "\nDéfense de base: " + str(b) + "\n\nEpv avec 2Pv + 1Def: " + str(c) + "\nEpv avec 1Pv + 2Def: " + str(d), inline=False)
			await message.channel.send(embed=embed)

		else:
			await message.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")




@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
