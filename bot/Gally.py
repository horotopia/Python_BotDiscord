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

########################################
#                Help                  #
########################################	

	if any([message.content ==(item) for item in ['Help','help']]):
		await message.author.send("__- - > Astromons__\nEcrivez le nom d'un astromons sans espaces et avec la première lettre en majuscule pour montrer tous les éléments de l'astromons.\nExemple : Miho\nLa plupart du temps Athéna a seulement besoin des 3 ou 4 premières lettres. 'Shivobi' sera compris par 'Shiva' et non 'Shinobi'\nPour trouver un astromon Super Evo, veuillez rajouter devant son nom la lettre 'S'\nExemple: SYuki ou SLeo\n\n__- - > ePV__\nEcrivez ePV puis vos statistiques PV puis vos statistiques DEF\nExemple: ePV 30245 2461\n\n__- - > Dégâts__\nEcrivez 'D' puis vos statistiques ATQ, le % dégâts critiques puis le % taux critique.\nExemple: D 3240 50 10\nNB : Dégâts critiques et Taux Critique s'expriment en %. Si la valeur entrée est > 100 les résultats seront incohérents.\n\n__- - > Horaires des Batailles de Clan__\nEcrivez la timezone de votre clan pour avoir toutes les timezones.\nExemple: UTC+3\nLa plupart des formats de timezone sont pris en compte (JST,MST...) vous ne devriez pas avoir besoin de convertir vous-même au format UTC.\n\n__- - > Boss__\n'dragon' ou 'dragons', 'golem' ou 'golems' pour avoir  une vue globale des statistiques de ces boss.\n'DB' ou 'GB' suivi d'un nombre pour avoir le descriptif d'un niveau précis. Exemple : GB8, DB5...\n\n__- - > Compétences__\nEcrivez le nom d'une compétence sans espace ni majuscule pour en avoir une description ainsi que les astromons possédant cette compétence. \nExemple: siphondepv\n\n__- - > Events__\nEcrivez 'Rebirth3', 'Rebirth4' ou 'exotique' pour faire apparaître une liste des renaissances 3*, 4* ou exotique\n\n__- - > Divers__\n'Help' pour voir ce message en version courte, entrez 'Ath' ou 'Athena'\n'Titan' ou 'Titans' pour voir les attaques des titans et leurs HP.\n'TitanPV' ou 'TitansPV' pour les PV des titans\n'Toc' ou 'ToC' pour la liste des boss et les récompenses associées")

########################################
#               Sony                   #
########################################	

	if message.content.startswith('Knuc'):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634702953611285/Knuckles3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#1 Knuckles (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634702953611285/Knuckles3Evo_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Persévérance\n(Dmg : +20%)\n**Actif**: Persévérance\n(Dmg : +20%)\n**PV**: 27996\n**Attaque**: 3344\n**Défense**: 2009\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

	if message.content.startswith("Soni"):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634807807279104/Sonic3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#2 Sonic (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634807807279104/Sonic3Evo_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Dégâts -50% 1 tour\n(Dmg : +20% +1 tour)\n**Actif**: Attaque augmentée +50%  2 tours (soi-même)\n(Dmg : +25%)\n**PV**: 26927\n**Attaque**: 3344\n**Défense**: 2384\n**Récupération**:2159", inline=False)

		await message.channel.send(embed=embed)

	if message.content.startswith("Tail"):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634818213085194/Tails3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#3 Tails (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634818213085194/Tails3Evo_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg : +25%)\n**Actif**: Faiblesse exposée 80% 2 tours\n(Dmg : +20% Effect : +10%)\n**PV**: 26440\n**Attaque**: 2812\n**Défense**: 2856\n**Récupération**:2692", inline=False)

		await message.channel.send(embed=embed)

	if message.content.startswith("Tail"):
		return

	if message.content.startswith("Silv"):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634795052269689/Silver3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#4 Silver (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634795052269689/Silver3Evo_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%\n(Dmg : +20% Effect : +5%)\n**Actif**: Réduction de dégâts 2 tours (allies)\n(Dmg : +20% +1tour)\n**PV**: 32160\n**Attaque**: 2696\n**Défense**: 3128\n**Récupération**:1889", inline=False)

		await message.channel.send(embed=embed)


	if message.content.startswith("Shad"):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634767080456202/Shadow3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#5 Shadow (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634767080456202/Shadow3Evo_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Vague martiale 10% (allies)\n(Dmg +25%)\n**Actif**: Attaque augmentée  2 tours\n(Dmg +20% +1tour)\n**PV**: 24380\n**Attaque**: 3916\n**Défense**: 2377\n**Récupération**:1880", inline=False)

		await message.channel.send(embed=embed)

	if message.content.startswith("Shad"):
		return

########################################
#                Alpaga                #
########################################

	if any([message.content.startswith (item) for item in ['Alp','FeuAlp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559613791174668/StrangeAlpacaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#6 Alpaca (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559613791174668/StrangeAlpacaR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Brise-Bonus 100%\n(Dmg +25%)\n**Actif**: Sceau 80% 3 tours\n(Dmg +20% Effect +10%)\n**PV**: 30921\n**Attaque**: 1826\n**Défense**: 1942\n**Récupération**:1533", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Alp','EauAlp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559608523128862/StrangeAlpacaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#7 Alpaca (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559608523128862/StrangeAlpacaB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Boost de moral 100% (de ses PA, on crit)\n(Dmg +25%)\n**Actif**: Siphon de PA 30% (On crit)\n(Dmg +20% Effect +10%)\n**PV**: 24965\n**Attaque**: 3051\n**Défense**: 1648\n**Récupération**:1444", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Alp','BoisAlp','TopAlp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559602701697029/StrangeAlpaca_large.jpeg", color=0xffffff)
		embed.set_author(name="#8 Alpaca (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559602701697029/StrangeAlpaca_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +25%)\n**Actif**: Frappe indéfectible (On crit) \n(Dmg +25%)\n**PV**: 26893\n**Attaque**: 2847\n**Défense**: 1498\n**Récupération**:1355", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Alp','LightAlp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559616010223628/StrangeAlpacaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#9 Alpaca (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559616010223628/StrangeAlpacaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Choc 50% 2 tours\n(Dmg +20% Taux +20%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +20% Taux + 20%)\n**PV**: 32024\n**Attaque**: 2389\n**Défense**: 2685\n**Récupération**:1752", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Alp','DarkAlp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559612277030931/StrangeAlpacaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#10 Alpaca (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559612277030931/StrangeAlpacaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Tc +15~20%(Même élément)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20% +1tour)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 22555\n**Attaque**: 3173\n**Défense**: 2670\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

########################################
#              Ammonore                #
########################################

	if any([message.content.startswith (item) for item in ['Ammo','FeuAmmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556861866508314/MortArchleR_large.jpeg", color=0xffffff)
		embed.set_author(name="#11 Ammonore (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556861866508314/MortArchleR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 41143\n**Attaque**: 1506\n**Défense**: 1125\n**Récupération**:1329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ammo','EauAmmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556816991649812/MortArchle_large.jpeg", color=0xffffff)
		embed.set_author(name="#12 Ammonore (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556816991649812/MortArchle_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 29484\n**Attaque**: 1742\n**Défense**: 1800\n**Récupération**:1732", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ammo','BoisAmmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556860650029077/MortArchleG_large.jpeg", color=0xffffff)
		embed.set_author(name="#13 Ammonore (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556860650029077/MortArchleG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tour\n(No skillbooks)\n**PV**: 25272\n**Attaque**: 1784\n**Défense**: 2813\n**Récupération**:1355", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ammo','LightAmmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556862235607049/MortArchleW_large.jpeg", color=0xffffff)
		embed.set_author(name="#14 Ammonore (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556862235607049/MortArchleW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 30403\n**Attaque**: 1892\n**Défense**: 1889\n**Récupération**:1119", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ammo','DarkAmmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556839519125504/MortArchleD_large.jpeg", color=0xffffff)
		embed.set_author(name="#15 Ammonore (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556839519125504/MortArchleD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 26327\n**Attaque**: 2615\n**Défense**: 1573\n**Récupération**:1457", inline=False)

		await message.channel.send(embed=embed)

########################################
#               Anubis                 #
########################################

	if any([message.content.startswith (item) for item in ['Anu','FeuAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551381249032192/AnubisR_large.jpeg", color=0xffffff)
		embed.set_author(name="#16 Anu (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551381249032192/AnubisR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 38684\n**Attaque**: 2112\n**Défense**: 2439\n**Récupération**:1772", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Anu','EauAnu','TopAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551368997470218/AnubisB_large.jpeg", color=0xffffff)
		embed.set_author(name="#18 Anu (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551368997470218/AnubisB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Prédateur 50%\n(No skillbooks)\n**PV**: 22739\n**Attaque**: 3296\n**Défense**: 2111\n**Récupération**:1920", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Anu','BoisAnu','TopAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551378271207424/AnubisG_large.jpeg", color=0xffffff)
		embed.set_author(name="#20 Anu (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551378271207424/AnubisG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 23494\n**Attaque**: 3092\n**Défense**: 2322\n**Récupération**:1948", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Anu','LightAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551366741196820/Anubis_large.jpeg", color=0xffffff)
		embed.set_author(name="#22 Anu (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551366741196820/Anubis_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 39604\n**Attaque**: 2351\n**Défense**: 1772\n**Récupération**:1915", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Anu','DarkAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326188053987328/AnubisD_large.jpg", color=0xffffff)
		embed.set_author(name="#24 Anu (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326188053987328/AnubisD_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 29617\n**Attaque**: 2288\n**Défense**: 3296\n**Récupération**:1709", inline=False)

		await message.channel.send(embed=embed)

########################################
#             Anubis S Evo             #
########################################

	if any([message.content.startswith (item) for item in ['FeuAnu','SAnu','FeuSAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559766572892191/SuperAnubisR_large.jpeg", color=0xffffff)
		embed.set_author(name="#17 Anu SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559766572892191/SuperAnubisR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 42722\n**Attaque**: 2324\n**Défense**: 2684\n**Récupération**:1949", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauAnu','SAnu','EauSAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559755193876501/SuperAnubisB_large.jpeg", color=0xffffff)
		embed.set_author(name="#19 Anu SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559755193876501/SuperAnubisB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Prédateur 50%\n(No skillbooks)\n**PV**: 25020\n**Attaque**: 3657\n**Défense**: 2329\n**Récupération**:2118", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisAnu','SAnu','BoisSAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559761200119823/SuperAnubisG_large.jpeg", color=0xffffff)
		embed.set_author(name="#21 Anu SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559761200119823/SuperAnubisG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25851\n**Attaque**: 3432\n**Défense**: 2561\n**Récupération**:2152", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightAnu','SAnu','LightSAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559733983412273/SuperAnubis_large.jpeg", color=0xffffff)
		embed.set_author(name="#23 Anu SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559733983412273/SuperAnubis_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 43730\n**Attaque**: 2589\n**Défense**: 1949\n**Récupération**:2112", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkAnu','SAnu','DarkSAnu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559752039890964/SuperAnubisD_large.jpeg", color=0xffffff)
		embed.set_author(name="#25 Anu SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559752039890964/SuperAnubisD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 32586\n**Attaque**: 2527\n**Défense**: 3657\n**Récupération**:1886", inline=False)

		await message.channel.send(embed=embed)

########################################
#               Arch                   #
########################################

	if any([message.content.startswith (item) for item in ['Arch','FeuArch']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551455308120064/Archhelon_large.jpeg", color=0xffffff)
		embed.set_author(name="#26 Arch (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551455308120064/Archhelon_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**:  Provocation intrépide 60% 2 tours\n(Dmg: +25%, Taux: +20%)\n**PV**: 29412\n**Attaque**: 1321\n**Défense**: 2642\n**Récupération**:1628", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arch','EauArch']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551458386477076/ArchhelonB_large.jpeg", color=0xffffff)
		embed.set_author(name="#27 Arch (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551458386477076/ArchhelonB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Etourdissement 60% 2 tours \n(Dmg: +25%, Taux: +20%)\n**PV**: 28439\n**Attaque**: 1668\n**Défense**: 2486\n**Récupération**:1192", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arch','BoisArch']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551468025118722/ArchhelonG_large.jpeg", color=0xffffff)
		embed.set_author(name="#28 Arch (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551468025118722/ArchhelonG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Reduction dégâts 50% 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Chasseur 50%\n(Dmg: +30%)\n**PV**: 33737\n**Attaque**: 2152\n**Défense**: 1328\n**Récupération**:1362", inline=False)

		await message.channel.send(embed=embed)

########################################
#               Artemis                #
########################################

	if any([message.content.startswith (item) for item in ['Arte','FeuArte','TopArte']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558810489683978/SeleneR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#31 Artemis (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558810489683978/SeleneR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Étourdissement 80% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15% Taux: +20%)\n**PV**: 37247\n**Attaque**: 2746\n**Défense**: 2807\n**Récupération**:2316", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arte','EauArte']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558776893440013/SeleneB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#32 Artemis (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558776893440013/SeleneB_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Nécrose x2 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose x2 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30856\n**Attaque**: 3173\n**Défense**: 2833\n**Récupération**:2486", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arte','BoisArte']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558775291346980/Selene_Large.jpeg", color=0xffffff)
		embed.set_author(name="#33 Artemis (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558775291346980/Selene_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PV (Allies)\n(Dmg +20%)\n**Actif**: Siphon de PV (Allies) \n(Dmg +20%)\n**PV**: 28016\n**Attaque**: 3575\n**Défense**: 2492\n**Récupération**:2281", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arte','LightArte']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558807260069891/SeleneW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#34 Artemis (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558807260069891/SeleneW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Vague Martiale 10% pv/pa (alliés)\n(Dmg +30%)\n**Actif**: Prédateur 50% \n(Dmg +20%)\n**PV**: 29222\n**Attaque**: 3575\n**Défense**: 2588\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arte','DarkArte']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558779636514836/SeleneD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#35 Artemis (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558779636514836/SeleneD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +15%; +Effect.: +5%)\n**Actif**: Silence 80% 2 tours\n(Dmg +15%, Taux: +20%, +1tour)\n**PV**: 31946\n**Attaque**: 2533\n**Défense**: 3650\n**Récupération**:2206", inline=False)

		await message.channel.send(embed=embed)


@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
