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

		########################################
		#############  Dégats   ################
		########################################
		#   mettre un message d'erreur en cas  #
		#        d'oublie de la commande       #
		########################################

	if message.content.startswith("D "):
		a = 0
		b = 0
		c = 0
		x = ""
		y = ""
		invalid = False
		spacerequired = 2
		info = message.content.replace("D ", "")
		for i in range(0,len(info)):
			if spacerequired > 0 and info[i] == " ":
			spacerequired -= 1
		elif list(info)[i] not in [".","0","1","2","3","4","5","6","7","8","9"]:
			invalid = True
		if spacerequired != 0:
			invalid = True
		if invalid == False:

		for i in range(0,info.find(" ")):
			x += info[i]
			y += "x"
		try:
			a = float(x)
		except:
			invalid = True
		x = ""
		for i in range(info.find(" ") + 1, len(info)):
			y += info[i]
		for i in range(info.find(" ") + 1, y.find(" ") + 1):
			x += info[i]
		try:
			b = float(x)
		except:
			invalid = True
		x = ""

		for i in range(y.find(" ") + 1, len(info)):
			x += info[i]

		try:
			c = float(x)
		except:
			invalid = True

		d = round(( 5.5 * a *( 1 + (b / 100 ) * (c/100))))

		print(a,b,c)

		if invalid == False:
			embed=discord.Embed(title="", description=" ", url="", color=0xffffff)
			embed.set_author(name=" ")
			embed.set_thumbnail(url="")
			embed.add_field(name="Calculs effectués avec:", value="\nAttaque: " + str(a) + "\nDommages critiques: " + str(b) + "\nTaux critique: " + str(c) + "\n\n__**Dégâts moyens**__: " + str(d) + "\n__**Dégâts Min**__: " + str(round(5.5 * a)) + " (no crit)\n__**Dégâts Max**__ : " + str(round(( 5.5 * a *( 1 + (b / 100 ) * (1)))))+ " (crit)", inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send("Ecrivez 'D' suivi de l'attaque, du dommage critique et du taux critique")
		else:
			await message.channel.send("Ecrivez 'D' suivi de l'attaque, du dommage critique et du taux critique")



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


########################################
######  activation de commandes   ######
########################################		

	if " " in message.content:
		return

	if "." in message.content:
		return

	if "?" in message.content:
		return

	if "/" in message.content:
		return


########################################
##############   Menu   ################
########################################
#   Mettre un message pour expliquer   #
#   toutes les commandes disponible    #
#         un peu comme Help            #
########################################

	if any([message.content ==(item) for item in ['Athena','Ath','athena']]):
		embed=discord.Embed(title="", url="https://vignette.wikia.nocookie.net/saint-seiya-cosmo-fantasy/images/f/f9/Athena_armure_divine.png/revision/latest/top-crop/width/360/height/450?cb=20171204120613&path-prefix=fr", color=0xffffff)
		embed.set_author(name="'Ath' ou 'Athena' Pour faire apparaître ce message.\n'Help' Pour obtenir en MP une version plus détaillée")
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/saint-seiya-cosmo-fantasy/images/f/f9/Athena_armure_divine.png/revision/latest/top-crop/width/360/height/450?cb=20171204120613&path-prefix=fr")
		embed.add_field(name="★★★★★★★★★★", value="__>Astromons__\nEcrivez le nom d'un astromon sans espace et avec la première lettre en majuscule pour montrer tous les éléments de l'astromons.\nExemple : Miho\nPour faire apparaître un astomon précis, veuillez préciser son élément avant le nom.\nExemple : FeuMiho\n__>ePV__\nEcrivez ePV puis vos statistiques PV suivi des statistiques DEF\nExemple: ePV 30245 2461\n__>Dégâts__\nEcrivez 'D' puis vos statistiques ATQ, le % dégâts critiques puis le % taux critique.\nExemple: D 3240 50 10\nNB : Si la valeur du taux critique est > 100 les résultats seront incohérents.\n__>Boss__\nDragons, Golems : 'Dragon' ou 'Dragons', 'Golem' ou 'Golems' pour avoir une vue globale des statistiques de ces boss.\n__>Compétences__\nEcrivez le nom d'une compétence sans espace ni majuscule pour en avoir une description ainsi que les astromons possédant cette compétence.\nExemple: siphondepv", inline=False)
		await message.channel.send(embed=embed)

	if message.content.startswith("Ath"):
		return

###########################
######### Help ##################
###########################	

	if any([message.content ==(item) for item in ['Help','help']]):
		await message.author.send("__- - > Astromons__\nEcrivez le nom d'un astromons sans espaces et avec la première lettre en majuscule pour montrer tous les éléments de l'astromons.\nExemple : Miho\nLa plupart du temps Athéna a seulement besoin des 3 ou 4 premières lettres. 'Shivobi' sera compris par 'Shiva' et non 'Shinobi'\nPour trouver un astromon Super Evo, veuillez rajouter devant son nom la lettre 'S'\nExemple: SYuki ou SLeo\n\n__- - > ePV__\nEcrivez ePV puis vos statistiques PV puis vos statistiques DEF\nExemple: ePV 30245 2461\n\n__- - > Dégâts__\nEcrivez 'D' puis vos statistiques ATQ, le % dégâts critiques puis le % taux critique.\nExemple: D 3240 50 10\nNB : Dégâts critiques et Taux Critique s'expriment en %. Si la valeur entrée est > 100 les résultats seront incohérents.\n\n__- - > Horaires des Batailles de Clan__\nEcrivez la timezone de votre clan pour avoir toutes les timezones.\nExemple: UTC+3\nLa plupart des formats de timezone sont pris en compte (JST,MST...) vous ne devriez pas avoir besoin de convertir vous-même au format UTC.\n\n__- - > Boss__\n'dragon' ou 'dragons', 'golem' ou 'golems' pour avoir  une vue globale des statistiques de ces boss.\n'DB' ou 'GB' suivi d'un nombre pour avoir le descriptif d'un niveau précis. Exemple : GB8, DB5...\n\n__- - > Compétences__\nEcrivez le nom d'une compétence sans espace ni majuscule pour en avoir une description ainsi que les astromons possédant cette compétence. \nExemple: siphondepv\n\n__- - > Events__\nEcrivez 'Rebirth3', 'Rebirth4' ou 'exotique' pour faire apparaître une liste des renaissances 3*, 4* ou exotique\n\n__- - > Divers__\n'Help' pour voir ce message en version courte, entrez 'Ath' ou 'Athena'\n'Titan' ou 'Titans' pour voir les attaques des titans et leurs HP.\n'TitanPV' ou 'TitansPV' pour les PV des titans\n'Toc' ou 'ToC' pour la liste des boss et les récompenses associées")

###########################
######### Sony ##################
###########################	



@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
