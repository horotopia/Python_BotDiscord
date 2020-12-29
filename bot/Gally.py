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
#            Split du message          #
########################################

	ListElementInMessage = message.content.split()

########################################
##############  Epv  ###################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

	if ListElementInMessage[0] == "Epv":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(a/(1-(b/(b+1200))))
			embed = discord.Embed(title="Epv", color=0xffffff)
			embed.set_thumbnail(url="https://img.pngio.com/bar-development-game-health-video-game-icon-video-game-health-png-512_204.png")
			embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(a) + "\nDéfense : " + str(b) + "\n\n**Epv : " + str(c) + "**", inline=False)
			await message.channel.send(embed=embed)
 
		else:
			await message.channel.send ("Erreur, Ecrivez Epv suivi des PV et de la Def. (ex : Epv 20000 2000)")

########################################
## Choisir ses gemmes (2 Def ou 2 Pv) ##
########################################

	if ListElementInMessage[0] == "EpvGem":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1] and ListElementInMessage[2].isnumeric():
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

########################################
#############  Dégats   ################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

	if ListElementInMessage[0] == "D":
		if len(ListElementInMessage) == 4 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric and ListElementInMessage[3].isnumeric:
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = int(ListElementInMessage[3])
			d = round(a*5.5)
			e = round(a*5.5*(1+(b/100)*(c/100)))
			f = round(a*5.5*(1+(c/100)))
			embed = discord.Embed(title="", color=0xffffff)
			embed.set_thumbnail(url = "https://img2.pngio.com/markeus-b-ui-buttons-opengameartorg-attack-png-187_207.png")
			embed.add_field(name="Calculs effectués avec : ", value="\nAttaque : " + str(a) + "\nTaux critique : " + str(b) + "\nDommages critiques : " + str(c) +
					"\n\n__**Dégâts moyens__ : "+ str(e)+ "**" + " (75k recomandé)" +
					"\n\n__Dégâts min :__ " + str(d)+ " (no crit)" +
					"\n__Dégâts crit :__ "+ str(f)+ " (crit)",inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez D suivi de l'attaque, du taux critique et des dégats critique")

########################################
###########  Agression Def   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression def 
#appel avec "AgrDef"

########################################
###########  Agression pv   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression pv 
# appel avec "AgrPv"

########################################
###########  Agression Rec   ###########
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

#faire un calcul d'agression recup 
# Appel avec "AgrRec"

########################################
###############  heal   ################
########################################
#   mettre un message d'erreur en cas  #
#        d'oublie de la commande       #
########################################

# faire un calcul de heal

# recup du heal x 4 + recup du soigné x 2
# demander la récup du heal + soigné





@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
