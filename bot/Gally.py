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

########################################
#              Arthur                  #
########################################

	if any([message.content.startswith (item) for item in ['Arth','FeuArth','TopArth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557209668171202574/ArthurpendragonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#36 Arthur (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557209668171202574/ArthurpendragonR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%, (Donjons)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Défense réduite 70% 3 tours\n(???)\n**PV**: 27948\n**Attaque**: 3466\n**Défense**: 2717\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arth','EauArth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326391658086421/ArthurpendragonB_large.jpg", color=0xffffff)
		embed.set_author(name="#37 Arthur (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326391658086421/ArthurpendragonB_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Boost de moral 100% 50% of de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Attaque réduite 70% 3 tours\n(???)\n**PV**: 32453\n**Attaque**: 2784\n**Défense**: 2930\n**Récupération**:2644", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arth','BoisArth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551565345554433/ArthurpendragonG_large.jpeg", color=0xffffff)
		embed.set_author(name="#38 Arthur (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551565345554433/ArthurpendragonG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Siphon de PV (soi-même)\n(Dmg +25%)\n**Actif**: Étourdissement 60% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**PV**: 28166\n**Attaque**: 3766\n**Défense**: 2479\n**Récupération**:2288", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arth','LightArth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551549591617611/Arthurpendragon_large.jpeg", color=0xffffff)
		embed.set_author(name="#39 Arthur (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551549591617611/Arthurpendragon_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Choc 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Chasseur 50% \n(No skillbooks)\n**PV**: 26416\n**Attaque**: 3936\n**Défense**: 2411\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arth','DarkArth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551561923002368/ArthurpendragonD_large.jpeg", color=0xffffff)
		embed.set_author(name="#40 Arthur (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551561923002368/ArthurpendragonD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45% (Donjons)\n**Passif**: Agression (PV)\n(Dmg +30%)\n**Actif**: Nécrose x3 100% 1 tour\n(Dmg +25%, tour: +1)\n**PV**: 49696\n**Attaque**: 1976\n**Défense**: 2487\n**Récupération**:2024", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Balrona ##################
		###########################	

	if any([message.content.startswith (item) for item in ['Bal','FeuBal']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551642940178442/Balrakaris_large.jpeg", color=0xffffff)
		embed.set_author(name="#41 Balrona (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551642940178442/Balrakaris_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Siphon de PV\n(Dmg +25%)\n**Actif**: Avantage élémentaire\n(Dmg +20%)\n**PV**: 25684\n**Attaque**: 3152\n**Défense**: 3216\n**Récupération**:2999", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bal','EauBal','TopBal']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551647943852052/BalrakarisB_large.jpeg", color=0xffffff)
		embed.set_author(name="#42 Balrona (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551647943852052/BalrakarisB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 28813\n**Attaque**: 3562\n**Défense**: 2452\n**Récupération**:2390", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bal','BoisBal']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551656152367118/BalrakarisG_large.jpeg", color=0xffffff)
		embed.set_author(name="#43 Balrona (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551656152367118/BalrakarisG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Att +35~40%\n**Passif**: Boost de moral 100% 50% of de ses PA \n(Dmg +10%, +Effect.: +10%)\n**Actif**: Sceau 60% 2 tours \n(Dmg +10%, Taux: +20%)\n**PV**: 31115\n**Attaque**: 2683\n**Défense**: 3466\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bal','LightBal']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551675655618562/Balrakarisw_large.jpeg", color=0xffffff)
		embed.set_author(name="#44 Balrona (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551675655618562/Balrakarisw_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Choc 100% 1 tour \n(Dmg +20%, tour: +1)\n**Actif**: Avantage élémentaire\n(Dmg +20%)\n**PV**: 32698\n**Attaque**: 2866\n**Défense**: 2842\n**Récupération**:1963", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bal','DarkBal']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551650644983819/BalrakarisD_large.jpeg", color=0xffffff)
		embed.set_author(name="#45 Balrona (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551650644983819/BalrakarisD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +35~40%\n**Passif**: Boost de moral (Allies) 20% SP \n(Dmg +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV \n(Dmg +25%)\n**PV**: 48212\n**Attaque**: 2133\n**Défense**: 2507\n**Récupération**:2017", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Banshee ##################
		###########################	

	if any([message.content.startswith (item) for item in ['Ban','FeuBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556797349593096/MorrighanR_large.jpeg", color=0xffffff)
		embed.set_author(name="#46 Banshee (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556797349593096/MorrighanR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +10%, Taux: +20%)\n**Actif**: Malédiction foudroyante\n(Dmg: +30%)\n**PV**: 29382\n**Attaque**: 2362\n**Défense**: 2433\n**Récupération**:2147", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ban','EauBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556766131388416/MorrighanB_large.jpeg", color=0xffffff)
		embed.set_author(name="#47 Banshee (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556766131388416/MorrighanB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%, \n**Passif**: Abondance d'âmes rouges\n(Dmg +35%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 40040\n**Attaque**: 2364\n**Défense**: 1976\n**Récupération**:1887", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ban','BoisBan','TopBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556767108792321/MorrighanG_large.jpeg", color=0xffffff)
		embed.set_author(name="#48 Banshee (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556767108792321/MorrighanG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Boost de moral 30% de ses PA \n(???)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 29760\n**Attaque**: 3092\n**Défense**: 2152\n**Récupération**:1968", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ban','LightBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607326992823615498/MorrighanW_large.jpg", color=0xffffff)
		embed.set_author(name="#49 Banshee (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607326992823615498/MorrighanW_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Choc 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Choc 70% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 31575\n**Attaque**: 2321\n**Défense**: 2631\n**Récupération**:2311", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ban','DarkBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556762058850305/Morrighan_large.jpeg", color=0xffffff)
		embed.set_author(name="#50 Banshee (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556762058850305/Morrighan_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Nécrose x3 100% 1 tours\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +25%)\n**PV**: 42001\n**Attaque**: 2405\n**Défense**: 1744\n**Récupération**:1847", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Banshee S Evo ##################
		###########################	

	if any([message.content.startswith (item) for item in ['FeuBan','SBan','FeuSBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707493851698430012/20200506_092733.jpg", color=0xffffff)
		embed.set_author(name="#828 Banshee SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707493851698430012/20200506_092733.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +10%, Taux: +20%)\n**Actif**: Malédiction foudroyante\n(Dmg: +30%)\n**PV**: 32343\n**Attaque**: 3121\n**Défense**: 2684\n**Récupération**:2371", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauBan','SBan','EauSBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494654911709214/20200506_092902.jpg", color=0xffffff)
		embed.set_author(name="#829 Banshee SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494654911709214/20200506_092902.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%, \n**Passif**: Abondance d'âmes rouges\n(Dmg +35%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 44206\n**Attaque**: 2821\n**Défense**: 2249\n**Récupération**:2078", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisBan','SBan','BoisSBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494655079612536/20200506_092921.jpg", color=0xffffff)
		embed.set_author(name="#830 Banshee SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494655079612536/20200506_092921.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Boost de moral 30% de ses PA \n(???)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 32742\n**Attaque**: 3759\n**Défense**: 2377\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightBan','SBan','LightSBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707495450969899038/20200506_093405.jpg", color=0xffffff)
		embed.set_author(name="#831 Banshee SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707495450969899038/20200506_093405.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Choc 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Choc 70% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 38207\n**Attaque**: 2563\n**Défense**: 2902\n**Récupération**:2555", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkBan','SBan','DarkSBan']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707494655469551687/20200506_093037.jpg", color=0xffffff)
		embed.set_author(name="#832 Banshee SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707494655469551687/20200506_093037.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Nécrose x3 100% 1 tours\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +25%)\n**PV**: 48626\n**Attaque**: 2650\n**Défense**: 2085\n**Récupération**:2038", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Bast ##################
		###########################	

	if any([message.content.startswith (item) for item in ['Bast','FeuBast']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551797122793484/Bastet_large.jpeg", color=0xffffff)
		embed.set_author(name="#51 Bast (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551797122793484/Bastet_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Récupération\n**Lead**: CR +20~25%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Domination 3 tours\n(Dmg +25%)\n**PV**: 30591\n**Attaque**: 2343\n**Défense**: 3201\n**Récupération**:3255", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bast','EauBast','TopBast']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551798490136591/BastetB_large.jpeg", color=0xffffff)
		embed.set_author(name="#52 Bast (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551798490136591/BastetB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: CR +20~25%\n**Passif**: Affaiblissement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%)\n**PV**: 43662\n**Attaque**: 2705\n**Défense**: 2112\n**Récupération**:2228", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bast','BoisBast','TopBast']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551804236464137/BastetG_large.jpeg", color=0xffffff)
		embed.set_author(name="#53 Bast (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551804236464137/BastetG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Récupération\n**Lead**: CR +20~25%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque augmentée  3 tours\n(Dmg +25%)\n**PV**: 31973\n**Attaque**: 1914\n**Défense**: 2581\n**Récupération**:3303", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bast','LightBast']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551805310074881/BastetW_large.jpeg", color=0xffffff)
		embed.set_author(name="#54 Bast (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551805310074881/BastetW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25%\n**Passif**: Siphon de PA 30%\n(No skillbooks)\n**Actif**: Vigueur 3 tours\n(No skillbooks)\n**PV**: 28779\n**Attaque**: 2860\n**Défense**: 3562\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bast','DarkBast']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551801132548097/BastetD_large.jpeg", color=0xffffff)
		embed.set_author(name="#55 Bast (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551801132548097/BastetD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: CR +20~25%\n**Passif**: Boost de moral 30% (de ses PA)\n(Dmg +25%)\n**Actif**: Bouclier (PV) 3 tours\n(Dmg +25%)\n**PV**: 42546\n**Attaque**: 2487\n**Défense**: 2487\n**Récupération**:2487", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Scarabo ##################
		###########################	

	if any([message.content.startswith (item) for item in ['Scar','FeuScar']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554775711842304/HerculeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#56 Scarabo (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554775711842304/HerculeR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 100% 1 tour \n(No skillbooks)\n**PV**: 27172\n**Attaque**: 2588\n**Défense**: 3099\n**Récupération**:2234", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Scar','EauScar']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554769105813530/HerculeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#57 Scarabo (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554769105813530/HerculeB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 60% 2 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 41374\n**Attaque**: 2105\n**Défense**: 2037\n**Récupération**:2051", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Scar','BoisScar','TopScar']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554769189699584/Hercule_large.jpeg", color=0xffffff)
		embed.set_author(name="#58 Scarabo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554769189699584/Hercule_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 60% 2 Truns \n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour \n(No skillbooks)\n**PV**: 29998\n**Attaque**: 2377\n**Défense**: 3221\n**Récupération**:1832", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Scar','LightScar']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554784729727037/HerculeW_large.jpeg", color=0xffffff)
		embed.set_author(name="#59 Scarabo (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554784729727037/HerculeW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Siphon de PV ,Greatly)\n(No skillbooks)\n**PV**: 30223\n**Attaque**: 2166\n**Défense**: 3133\n**Récupération**:2016", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Scar','DarkScar']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554771760939021/HerculeD_large.jpeg", color=0xffffff)
		embed.set_author(name="#60 Scarabo (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554771760939021/HerculeD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 24148\n**Attaque**: 3194\n**Défense**: 2234\n**Récupération**:1839", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Zabeille ##################
		###########################	

	if any([message.content.startswith (item) for item in ['Zab','LightZab']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552142364475402/BumblekingW_large.jpeg", color=0xffffff)
		embed.set_author(name="#64 Zabeille (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552142364475402/BumblekingW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Défense réduite 60% 2 tours \n(No skillbooks)\n**Actif**: Attaque augmentée de 50% 2 tours \n(No skillbooks)\n**PV**: 28731\n**Attaque**: 2356\n**Défense**: 1559\n**Récupération**:1437", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zab','DarkZab']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552139411685376/Bumbleking_large.jpeg", color=0xffffff)
		embed.set_author(name="#65 Zabeille (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552139411685376/Bumbleking_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 40% 1 tour \n(No skillbooks)\n**Actif**: Attaque augmentée de 50% 2 tours \n(No skillbooks)\n**PV**: 34837\n**Attaque**: 1404\n**Défense**: 1683\n**Récupération**:1588", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Rubani ##################
		###########################

	if any([message.content.startswith (item) for item in ['Ruba','FeuRuba']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558359937548300/Ribonia_large.jpeg", color=0xffffff)
		embed.set_author(name="#66 Rubani (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558359937548300/Ribonia_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Abondance d'âmes rouges\n(Dmg +30%)\n**Actif**: Zèle 3 tours\n(Dmg +30%)\n**PV**: 23685\n**Attaque**: 1696\n**Défense**: 1559\n**Récupération**:2472", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ruba','EauRuba']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558362290683944/RiboniaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#67 Rubani (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558362290683944/RiboniaB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Attaque réduite 50% 2 tours \n(Dmg +10%,Taux: +15%)\n**Actif**: Récupération augmentée 3 tours\n(Dmg +30%)\n**PV**: 26222\n**Attaque**: 2001\n**Défense**: 1991\n**Récupération**:1923", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ruba','BoisRuba']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558364136046593/RiboniaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#68 Rubani (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558364136046593/RiboniaG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Étourdissement 60% 1 tour \n(Dmg +10%, Taux: +20%)\n**Actif**: Vigueur 3 tours\n(Dmg +30%)\n**PV**: 31026\n**Attaque**: 1566\n**Défense**: 1444\n**Récupération**:2472", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Benjabuton ##################
		###########################

	if any([message.content.startswith (item) for item in ['Ben','FeuBen','TopBen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033120484589591/Benjamin1.png", color=0xffffff)
		embed.set_author(name="#71 Benjabuton (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033120484589591/Benjamin1.png")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%, \n**Passif**: Traqueur +30% CR\n(Dmg +20%, Taux: +10%)\n**Actif**: Traqueur +30% CR\n(Dmg +20%, Taux: +10%)\n**PV**: 30556\n**Attaque**: 3085\n**Défense**: 1907\n**Récupération**:2050", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ben','EauBen','TopBen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033123835707393/Benjamin2.png", color=0xffffff)
		embed.set_author(name="#72 Benjabuton (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033123835707393/Benjamin2.png")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30454\n**Attaque**: 1920\n**Défense**: 3187\n**Récupération**:2206", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ben','BoisBen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033127316455454/Benjamin3.png", color=0xffffff)
		embed.set_author(name="#73 Benjabuton (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033127316455454/Benjamin3.png")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 41388\n**Attaque**: 2085\n**Défense**: 2439\n**Récupération**:1704", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ben','LightBen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033136103260160/Benjamin5.png", color=0xffffff)
		embed.set_author(name="#74 Benjabuton (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033136103260160/Benjamin5.png")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Persévérance 10 tours\n(Dmg +20%)\n**Actif**: Persévérance 10 tours\n(Dmg +20%)\n**PV**: 26389\n**Attaque**: 3364\n**Défense**: 2343\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ben','DarkBen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033131238653962/Benjamin4.png", color=0xffffff)
		embed.set_author(name="#75 Benjabuton (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033131238653962/Benjamin4.png")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Persévérance 10 tours\n(Dmg +20%)\n**PV**: 27243\n**Attaque**: 2886\n**Défense**: 2774\n**Récupération**:2386", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Beth ##################
		###########################

	if any([message.content.startswith (item) for item in ['Bet','FeuBet','TopBeth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551923698368513/BethanyR_large.jpeg", color=0xffffff)
		embed.set_author(name="#76 Beth (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551923698368513/BethanyR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (bois) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (bois) 100%\n(Dmg: +35%)\n**PV**: 28871\n**Attaque**: 1994\n**Défense**: 1793\n**Récupération**: 1691", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bet','EauBet','TopBeth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551918807810060/Bethany_large.jpeg", color=0xffffff)
		embed.set_author(name="#77 Beth (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551918807810060/Bethany_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (feu) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (feu) 100%\n(Dmg: +35%)\n**PV**: 25367\n**Attaque**: 2595\n**Défense**: 1818\n**Récupération**: 1580", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bet','BoisBet''TopBeth']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551921584439298/BethanyG_large.jpeg", color=0xffffff)
		embed.set_author(name="#78 Beth (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551921584439298/BethanyG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (League)\n**Passif**: Prédateur (eau) 30%\n(Dmg: +35%)\n**Actif**: Prédateur (eau) 100%\n(Dmg: +35%)\n**PV**: 43901\n**Attaque**: 1676\n**Défense**: 1295\n**Récupération**: 1513", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Piou ##################
		###########################

	if any([message.content.startswith (item) for item in ['Pio','FeuPio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560068093018114/SwiftR_large.jpeg", color=0xffffff)
		embed.set_author(name="#81 Piou (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560068093018114/SwiftR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Provocation 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 28752\n**Attaque**: 1784\n**Défense**: 2527\n**Récupération**:1355", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pio','EauPio','TopPiou']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560053186723882/SwiftB_large.jpeg", color=0xffffff)
		embed.set_author(name="#82 Piou (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560053186723882/SwiftB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30451\n**Attaque**: 1763\n**Défense**: 1943\n**Récupération**:1705", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pio','BoisPio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560050309300225/Swift_large.jpeg", color=0xffffff)
		embed.set_author(name="#83 Piou (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560050309300225/Swift_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Nécrose 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 36812\n**Attaque**: 1758\n**Défense**: 1247\n**Récupération**:1336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pio','LightPio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560069754093586/SwiftW_large.jpeg", color=0xffffff)
		embed.set_author(name="#84 Piou (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560069754093586/SwiftW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Boost de moral 20% (de ses PA)\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 27029\n**Attaque**: 3133\n**Défense**: 2159\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pio','DarkPio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560064679116820/SwiftD_large.jpeg", color=0xffffff)
		embed.set_author(name="#85 Piou (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560064679116820/SwiftD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%(Donjons)\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 44643\n**Attaque**: 2010\n**Défense**: 1942\n**Récupération**:1915", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### tipiaf ##########
		###########################

	if any([message.content.startswith (item) for item in ['Tip','FeuTip','TopTip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557838963179521/Phoenix_large.jpeg", color=0xffffff)
		embed.set_author(name="#86 Tipiaf (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557838963179521/Phoenix_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%,Taux: +20%)\n**Actif**: Attaque réduite 70% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 24291\n**Attaque**: 3058\n**Défense**: 2138\n**Récupération**:2288", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tip','EauTip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557856696827969/PhoenixB_large.jpeg", color=0xffffff)
		embed.set_author(name="#87 Tipiaf (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557856696827969/PhoenixB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +15%, Taux: +10%, tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(???)\n**PV**: 24250\n**Attaque**: 2424\n**Défense**: 3173\n**Récupération**:1948", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tip','BoisTip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557861427871770/PhoenixG_large.jpeg", color=0xffffff)
		embed.set_author(name="#88 Tipiaf (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557861427871770/PhoenixG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PV \n(Dmg +15%, Taux: +10%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +15%, Taux: +10%)\n**PV**: 26096\n**Attaque**: 3085\n**Défense**: 2281\n**Récupération**:1628", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tipiaf','LightTipiaf']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569195048337524/Screenshot_20200907-183739_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#1000 Tipiaf (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569195048337524/Screenshot_20200907-183739_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques 40-45%\n**Passif**: Frappe courageuse\n(Dmg +25%)\n**Actif**: Faiblesse exposée\n(Dmg +20%, Taux: +10%)\n**PV**: 30029\n**Attaque**: 2812\n**Défense**: 2610\n**Récupération**:2161", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tipiaf','DarkTipiaf']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569195186880622/Screenshot_20200907-183853_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#1001 Tipiaf (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569195186880622/Screenshot_20200907-183853_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques 40-45%\n**Passif**: Boost de moral 10% PA Alliés\n(Dmg +20%, efficacité +5%)\n**Actif**: Nécrose x3 80% 2 tours\n(Dmg +20%, Taux +10%)\n**PV**: 29603\n**Attaque**: 2206\n**Défense**: 3099\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed) 

		###########################
		######### Bron ##################
		###########################

	if any([message.content.startswith (item) for item in ['Bro','FeuBro']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg", color=0xffffff)
		embed.set_author(name="#97 Bron (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Prédateur (bois) 30%\n(no skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(no skillbooks)\n**PV**: 28568\n**Attaque**: 2404\n**Défense**: 1512\n**Récupération**: 1396", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bro','EauBro']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg", color=0xffffff)
		embed.set_author(name="#97 Bron (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557003684315146/MustangB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Prédateur (feu) 30%\n(No skillbooks)\n**Actif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**PV**: 29048\n**Attaque**: 1681\n**Défense**: 1807\n**Récupération**:1596", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bro','BoisBro']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557011636584463/MustangG_large.jpeg", color=0xffffff)
		embed.set_author(name="#98 Bron (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557011636584463/MustangG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Prédateur (eau) 30%\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 29331\n**Attaque**: 1321\n**Défense**: 2554\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### bulbie ##################
		###########################

	if any([message.content.startswith (item) for item in ['Bul','FeuBul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327107101753376/BarometzR_large.jpg", color=0xffffff)
		embed.set_author(name="#101 Bulbie (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327107101753376/BarometzR_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 33032\n**Attaque**: 1881\n**Défense**: 1874\n**Récupération**:1806", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bul','EauBul','TopBul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327101481254918/BarometzB_large.jpg", color=0xffffff)
		embed.set_author(name="#102 Bulbie (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327101481254918/BarometzB_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Brise bouclier 100%\n(Dmg +30%)\n**Actif**: Frappe indéfectible \n(Dmg +25%)\n**PV**: 21499\n**Attaque**: 3357\n**Défense**: 2363\n**Récupération**:1777", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bul','BoisBul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327097999982613/Barometz_large.jpg", color=0xffffff)
		embed.set_author(name="#103 Bulbie (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327097999982613/Barometz_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +30%)\n**Actif**: Brise-Bonus 100%\n(Dmg +30%)\n**PV**: 27427\n**Attaque**: 2192\n**Défense**: 2372\n**Récupération**:1671", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bul','LightBul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327109634850817/BarometzW_large.jpg", color=0xffffff)
		embed.set_author(name="#104 Bulbie (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327109634850817/BarometzW_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Récupération réduite 80% 2 tour\n(Dmg +30%)\n**Actif**: Récupération réduite 100% 2 tour\n(Dmg +30%)\n**PV**: 32225\n**Attaque**: 2023\n**Défense**: 3139\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Bul','DarkBul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327104186581002/BarometzD_large.jpg", color=0xffffff)
		embed.set_author(name="#105 Bulbie (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327104186581002/BarometzD_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Faiblesse exposée 100% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 24475\n**Attaque**: 3378\n**Défense**: 2349\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Lumignon ##################
		###########################

	if any([message.content.startswith (item) for item in ['Lumignon','FeuLumi','TopLumi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555572877197322/Lantra_large.jpeg", color=0xffffff)
		embed.set_author(name="#106 Lumignon (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555572877197322/Lantra_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28813\n**Attaque**: 2595\n**Défense**: 1975\n**Récupération**:1825", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lumignon','EauLumi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555575649632296/LantraB_large.jpeg", color=0xffffff)
		embed.set_author(name="#107 Lumignon (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555575649632296/LantraB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Traqueur +20% CR\n(Dmg +20%, Taux: +10%)\n**Actif**: Traqueur +20% CR\n(Dmg +15%, Taux: +10%)\n**PV**: 24795\n**Attaque**: 2601\n**Défense**: 1832\n**Récupération**:1811", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lumignon','BoisLumi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555577016844300/LantraG_large.jpeg", color=0xffffff)
		embed.set_author(name="#108 Lumignon (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555577016844300/LantraG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Donjons)\n**Passif**: Chasseur (eau) 50%\n(Dmg +15%, Taux: +10%)\n**Actif**: Chasseur (eau) 50%\n(???)\n**PV**: 29457\n**Attaque**: 1742\n**Défense**: 1963\n**Récupération**:1861", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### canna ##################
		###########################

	if any([message.content.startswith (item) for item in ['Canna','FeuCanna']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552232940208140/CanariaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#111 Canna (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552232940208140/CanariaR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Pétrification 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 80% -20% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 34053\n**Attaque**: 2267\n**Défense**: 2277\n**Récupération**:2277", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Canna','EauCanna']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552226124464139/CanariaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#112 Canna (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552226124464139/CanariaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28752\n**Attaque**: 1948\n**Défense**: 3235\n**Récupération**:2254", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Canna','BoisCanna','TopCanna']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552230591660050/CanariaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#113 Canna (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552230591660050/CanariaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 70% 1 tour\n(Dmg +10%, Taux: +5%, tour: +1)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 29484\n**Attaque**: 2396\n**Défense**: 2447\n**Récupération**:2352", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Canna','LightCanna']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552224300072980/Canaria_large.jpeg", color=0xffffff)
		embed.set_author(name="#114 Canna (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552224300072980/Canaria_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%\n**Passif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 35443\n**Attaque**: 1956\n**Défense**: 2316\n**Récupération**:2187", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Canna','DarkCanna']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552228615880715/CanariaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#115 Canna (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552228615880715/CanariaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV \n(Dmg +20%)\n**Actif**: Siphon de PV ,Greatly)\n(Dmg +20%)\n**PV**: 25776\n**Attaque**: 3262\n**Défense**: 2349\n**Récupération**:1907", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Cerise ##################
		###########################

	if any([message.content.startswith (item) for item in ['Ceri','FeuCeri','TopCeri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033505872838686/Cherry1.png", color=0xffffff)
		embed.set_author(name="#796 Cerise (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033505872838686/Cherry1.png")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (clan)\n**Passif**: Nécrose 80% 2 tours\n(Dmg: +10% Taux +20%)\n**Actif**: Défense augmentée 2 tours\n(Dmg: +25% tour: +1)\n**PV**: 23501\n**Attaque**: 2036\n**Défense**: 2969\n**Récupération**: 2009", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ceri','EauCeri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033508372774912/Cherry2.png", color=0xffffff)
		embed.set_author(name="#797 Cerise (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033508372774912/Cherry2.png")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Défense réduite 60% 1 tour\n(Dmg: +10% Taux +20%)\n**Actif**: Bouclier 2 tours\n(Dmg: +25% tour +1)\n**PV**: 28643\n**Attaque**: 1743\n**Défense**: 1580\n**Récupération**: 2540", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ceri','BoisCeri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033511829405736/Cherry3.png", color=0xffffff)
		embed.set_author(name="#798 Cerise (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033511829405736/Cherry3.png")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35% (clan)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +30%)\n**Actif**: Bouclier (PV) 2 tours\n(Dmg: +25% tour: +1)\n**PV**: 30553\n**Attaque**: 1656\n**Défense**: 1826\n**Récupération**: 2180", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ceri','LightCeri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033520024944650/Cherry5.png", color=0xffffff)
		embed.set_author(name="#799 Cerise (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033520024944650/Cherry5.png")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Nécrose x2 60% 2 tours\n(Dmg: +15% Taux: +20%)\n**Actif**: Défense augmentée 2 tours\n(Dmg: +20% tour +1)\n**PV**: 24645\n**Attaque**: 2458\n**Défense**: 1948\n**Récupération**: 2792", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ceri','DarkCeri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772033515268079626/Cherry4.png", color=0xffffff)
		embed.set_author(name="#800 Cerise (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772033515268079626/Cherry4.png")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Att +30~35% (clan)\n**Passif**: Défense réduite 60% 1 tour\n(Dmg: +15% Taux: +20%)\n**Actif**: Attaque augmentée  2 tours\n(Dmg: +20% tour: +1)\n**PV**: 25715\n**Attaque**: 1982\n**Défense**: 1920\n**Récupération**: 3153", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### chiroptie ##################
		###########################

	if any([message.content.startswith (item) for item in ['Chir','FeuChir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552787842564109/CloakR_large.jpeg", color=0xffffff)
		embed.set_author(name="#116 Chiroptie (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552787842564109/CloakR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 40% 2 tours\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2527\n**Défense**: 1403\n**Récupération**:1478", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chir','EauChir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557210231248125963/Cloak_large.jpeg", color=0xffffff)
		embed.set_author(name="#117 Chiroptie (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557210231248125963/Cloak_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Récupération réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 36675\n**Attaque**: 1710\n**Défense**: 1206\n**Récupération**:1343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chir','BoisChir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552782914256897/CloakG_large.jpeg", color=0xffffff)
		embed.set_author(name="#118 Chiroptie (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552782914256897/CloakG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**PV**: 29334\n**Attaque**: 1933\n**Défense**: 1895\n**Récupération**:1691", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chir','LightChir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552795610546176/CloakW_large.jpeg", color=0xffffff)
		embed.set_author(name="#119 Chiroptie (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552795610546176/CloakW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Prédateur (light) 50%\n(No skillbooks)\n**Actif**: Choc 80% 1 tour\n(No skillbooks)\n**PV**: 29249\n**Attaque**: 1321\n**Défense**: 2527\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chir','DarkChir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552774186041344/CloakD_large.jpeg", color=0xffffff)
		embed.set_author(name="#120 Chiroptie (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552774186041344/CloakD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Prédateur (dark) 50%\n(No skillbooks)\n**Actif**: Silence 80% 1 tour\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Chloe ##################
		###########################

	if any([message.content.startswith (item) for item in ['Chlo','FeuChlo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553694080663562/FateR_large.jpeg", color=0xffffff)
		embed.set_author(name="#121 Chloe (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553694080663562/FateR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Adrénaline 50% 50% de ses PV\n(Dmg +10%, Taux: +20%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**PV**: 39873\n**Attaque**: 1976\n**Défense**: 2323\n**Récupération**:1915", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chlo','EauChlo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553689555009557/FateB_large.jpeg", color=0xffffff)
		embed.set_author(name="#122 Chloe (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553689555009557/FateB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +30%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 26675\n**Attaque**: 2240\n**Défense**: 3173\n**Récupération**:2384", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chlo','BoisChlo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553692314992653/FateG_large.jpeg", color=0xffffff)
		embed.set_author(name="#123 Chloe (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553692314992653/FateG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**PV**: 23712\n**Attaque**: 3323\n**Défense**: 2309\n**Récupération**:1948", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chlo','LightChlo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553696224083989/FateW_large.jpeg", color=0xffffff)
		embed.set_author(name="#124 Chloe (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553696224083989/FateW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Boost de moral 30%  100% (de ses PA)\n(Dmg +15%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 30175\n**Attaque**: 2261\n**Défense**: 3323\n**Récupération**:1811", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chlo','DarkChlo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553685998370820/Fate_large.jpeg", color=0xffffff)
		embed.set_author(name="#125 Chloe (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553685998370820/Fate_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe Courageuse\n(Dmg +25%)\n**PV**: 26733\n**Attaque**: 2716\n**Défense**: 2658\n**Récupération**:2522", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### cocomaru ##################
		###########################

	if any([message.content.startswith (item) for item in ['Coco','FeuCoco']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552911675064325/CocoemongR_large.jpeg", color=0xffffff)
		embed.set_author(name="#126 Cocomaru (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552911675064325/CocoemongR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (Même élément)\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 40% 1 tour\n(Taux: +30%)\n**PV**: 29419\n**Attaque**: 1437\n**Défense**: 2847\n**Récupération**:1702", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coco','EauCoco']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552903211089922/CocoemongB_large.jpeg", color=0xffffff)
		embed.set_author(name="#127 Cocomaru (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552903211089922/CocoemongB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +30%, tour: +1)\n**Actif**: Pétrification 40% 1 tour\n(Taux: +30%)\n**PV**: 23706\n**Attaque**: 2384\n**Défense**: 1709\n**Récupération**:1866", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coco','BoisCoco','TopCoco']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552801033650176/Cocoemong_large.jpeg", color=0xffffff)
		embed.set_author(name="#128 Cocomaru (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552801033650176/Cocoemong_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Même élément)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 31646\n**Attaque**: 2642\n**Défense**: 1784\n**Récupération**:1716", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coco','LightCoco']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552970559160342/CocoemongW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#129 Cocomaru (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552970559160342/CocoemongW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Agression (PV)\n(Dmg +20%)\n**PV**: 37520\n**Attaque**: 2235\n**Défense**: 1751\n**Récupération**:2385", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coco','DarkCoco']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552906637967386/CocoemongD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#130 Cocomaru (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552906637967386/CocoemongD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +10%, Taux: +10%)\n**PV**: 33141\n**Attaque**: 2812\n**Défense**: 2365\n**Récupération**:1970", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Poulichon ##################
		###########################

	if any([message.content.startswith (item) for item in ['Poul','LightPoul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558022694666240/Ponicon_large.jpeg", color=0xffffff)
		embed.set_author(name="#134 Poulichon (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558022694666240/Ponicon_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Choc 80% 2 tours\n(Dmg: +20% Taux: +15%)\n**PV**: 30417\n**Attaque**: 1749\n**Défense**: 1895\n**Récupération**: 1807", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Poul','DarkPoul']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558034140790846/PoniconD_large.jpeg", color=0xffffff)
		embed.set_author(name="#135 Poulichon (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558034140790846/PoniconD_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Défense réduite 70% 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Prédateur (light) 100%\n(Dmg: +35%)\n**PV**: 26430\n**Attaque**: 2384\n**Défense**: 1818\n**Récupération**: 1600", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### cosmo ##################
		###########################

	if any([message.content.startswith (item) for item in ['Cosmo','LightCosmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558953041756160/Shootingstar_large.jpeg", color=0xffffff)
		embed.set_author(name="#139 Cosmo (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558953041756160/Shootingstar_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Adrénaline (Allies) 10% de ses PV  (On crit)\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Nécrose x2 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 32991\n**Attaque**: 2076\n**Défense**: 2106\n**Récupération**:1786", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cosmo','DarkCosmo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558983840399361/ShootingstarD_large.jpeg", color=0xffffff)
		embed.set_author(name="#140 Cosmo (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558983840399361/ShootingstarD_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Brise bouclier 100%\n(Dmg +30%)\n**Actif**: Silence 60% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 45522\n**Attaque**: 1411\n**Défense**: 1445\n**Récupération**:1281", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### cotonou ##################
		###########################

	if any([message.content.startswith (item) for item in ['Coto','FeuCoto']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553079292035082/CottonsongR_large.jpeg", color=0xffffff)
		embed.set_author(name="#141 Cotonou (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553079292035082/CottonsongR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Nécrose 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Attaque augmentée  3 tours\n(Dmg +25%)\n**PV**: 27696\n**Attaque**: 1362\n**Défense**: 1702\n**Récupération**:2574", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coto','EauCoto']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553075357909014/Cottonsong_large.jpeg", color=0xffffff)
		embed.set_author(name="#142 Cotonou (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553075357909014/Cottonsong_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Brise bouclier 100%\n(Dmg +25%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%)\n**PV**: 30216\n**Attaque**: 1457\n**Défense**: 1730\n**Récupération**:2492", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coto','BoisCoto']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553077203533826/CottonsongG_large.jpeg", color=0xffffff)
		embed.set_author(name="#143 Cotonou (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553077203533826/CottonsongG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Provocation 40% 1 tour \n(Dmg +10%, Taux: +20%)\n**Actif**: Purification 100%\n(Dmg +25%)\n**PV**: 31054\n**Attaque**: 1532\n**Défense**: 1430\n**Récupération**:2574", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coto','LightCoto']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541347722592369/CotoL.png", color=0xffffff)
		embed.set_author(name="#142 Cotonou (Light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541347722592369/CotoL.png")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +10~15%\n**Passif**: Nécrose 60%\n(Dmg +20%, Taux: +10%)\n**Actif**: Bouclier 2 tours\n(Dmg +20%, +1 tour)\n**PV**: 26314\n**Attaque**: 1362\n**Défense**: 1968\n**Récupération**:2663", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Coto','DarkCoto']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541425467949056/CotoD.png", color=0xffffff)
		embed.set_author(name="#143 Cotonou (Dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541425467949056/CotoD.png")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: SP Rec +10~15%\n**Passif**: Résistance réduite 100% 1 tour \n(Dmg +20%, +1 tour)\n**Actif**: Domination 2 tours\n(Dmg +20%, +1 tour)\n**PV**: 25483\n**Attaque**: 1607\n**Défense**: 2411\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)



@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
