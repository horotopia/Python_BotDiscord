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

		###########################
		######### croquignol ##################
		###########################

	if any([message.content.startswith (item) for item in ['Croq','FeuCroq']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327215167733829/CaptainCroR_large.jpg", color=0xffffff)
		embed.set_author(name="#146 Croquignol (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327215167733829/CaptainCroR_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (League)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +30%, Taux: +20%)\n**Actif**: Nécrose x2 80% 1 tour\n(Dmg: 20%, +1 tour)\n**PV**: 29368\n**Attaque**: 2015\n**Défense**: 1684\n**Récupération**:1664", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Croq','EauCroq','TopCroq']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327218745475082/CaptainCro_large.jpg", color=0xffffff)
		embed.set_author(name="#147 Croquignol (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327218745475082/CaptainCro_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (League)\n**Passif**: Chasseur 50%\n(Dmg: +35%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg: +20%, +1 tour)\n**PV**: 25926\n**Attaque**: 2581\n**Défense**: 1777\n**Récupération**:1682", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Croq','BoisCroq']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607327223275323402/CaptainCroG_large.jpg", color=0xffffff)
		embed.set_author(name="#148 Croquignol (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607327223275323402/CaptainCroG_large.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(League)\n**Passif**: Chasseur 50%\n(Dmg: +35%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 25565\n**Attaque**: 2717\n**Défense**: 1784\n**Récupération**:1226", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### cupidon ##################
		###########################

	if any([message.content.startswith (item) for item in ['Cupi','FeuCupi','TopCupi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553671330889754/ErosR_large.jpeg", color=0xffffff)
		embed.set_author(name="#151 Cupidon (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553671330889754/ErosR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 60% 1 tour\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 32456\n**Attaque**: 2159\n**Défense**: 1989\n**Récupération**:3323", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cupi','EauCupi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553664129138710/ErosB_large.jpeg", color=0xffffff)
		embed.set_author(name="#152 Cupidon (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553664129138710/ErosB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Purification 100%\n(No skillbooks)\n**PV**: 30693\n**Attaque**: 2036\n**Défense**: 2452\n**Récupération**:3003", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cupi','BoisCupi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553668583489536/ErosG_large.jpeg", color=0xffffff)
		embed.set_author(name="#153 Cupidon (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553668583489536/ErosG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Abondance d'âmes rouges\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours\n(No skillbooks)\n**PV**: 29875\n**Attaque**: 2179\n**Défense**: 1989\n**Récupération**:3099", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cupi','LightCupi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553662711332866/Eros_large.jpeg", color=0xffffff)
		embed.set_author(name="#154 Cupidon (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553662711332866/Eros_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV +30~35%\n**Passif**: Agression (Def)\n(No skillbooks)\n**Actif**: Zèle 3 tours \n(No skillbooks)\n**PV**: 29630\n**Attaque**: 2023\n**Défense**: 3303\n**Récupération**:2731", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cupi','DarkCupi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553666050129921/ErosD_large.jpeg", color=0xffffff)
		embed.set_author(name="#155 Cupidon (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553666050129921/ErosD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Bouclier (PV) 3 tours\n(No skillbooks)\n**PV**: 37731\n**Attaque**: 1806\n**Défense**: 2323\n**Récupération**:2153", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### cura ##################
		###########################

	if any([message.content.startswith (item) for item in ['Cura','FeuCura','TopCura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557601397669908/PandoraR_large.jpeg", color=0xffffff)
		embed.set_author(name="#156 Cura (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557601397669908/PandoraR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (Allies)10% SP\n(No skillbooks)\n**Actif**: Bouclier (Level) 3 tours\n(No skillbooks)\n**PV**: 30679\n**Attaque**: 2036\n**Défense**: 2452\n**Récupération**:2996", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cura','EauCura','TopCura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557593608847370/PandoraB_large.jpeg", color=0xffffff)
		embed.set_author(name="#157 Cura (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557593608847370/PandoraB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral 25% de ses PA\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 38378\n**Attaque**: 1928\n**Défense**: 2024\n**Récupération**:2133", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cura','BoisCura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557598805590016/PandoraG_large.jpeg", color=0xffffff)
		embed.set_author(name="#158 Cura (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557598805590016/PandoraG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Volonté 2 tours\n(No skillbooks)\n**PV**: 37533\n**Attaque**: 1962\n**Défense**: 2316\n**Récupération**:2194", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cura','LightCura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557591276945408/Pandora_large.jpeg", color=0xffffff)
		embed.set_author(name="#159 Cura (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557591276945408/Pandora_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Choc 60% 2 tours\n(No skillbooks)\n**Actif**: Domination 2 tours\n(No skillbooks)\n**PV**: 26178\n**Attaque**: 2281\n**Défense**: 3194\n**Récupération**:2050", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cura','DarkCura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557595852800000/PandoraD_large.jpeg", color=0xffffff)
		embed.set_author(name="#160 Cura (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557595852800000/PandoraD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Boost de moral 2 tours\n(No skillbooks)\n**PV**: 29014\n**Attaque**: 2532\n**Défense**: 2345\n**Récupération**:2100", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### d'artagnan ##################
		###########################

	if any([message.content.startswith (item) for item in ["D'art","FeuD'art","Dart","FeuDart"]]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553332091387914/DartagnanR_large.jpeg", color=0xffffff)
		embed.set_author(name="#161 D'artagnan (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553332091387914/DartagnanR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Soif 100% -20% 2 tours\n(No skillbooks)\n**PV**: 27220\n**Attaque**: 3092\n**Défense**: 2418\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ["D'art","EauD'art","Dart","EauDart"]]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553327485779970/DartagnanB_large.jpeg", color=0xffffff)
		embed.set_author(name="#162 D'artagnan (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553327485779970/DartagnanB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Fatigue 100% 3 tours\n(No skillbooks)\n**PV**: 35579\n**Attaque**: 2282\n**Défense**: 2058\n**Récupération**:2010", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ["D'art","BoisD'art","Dart","BoisDart"]]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553329314496522/DartagnanG_large.jpeg", color=0xffffff)
		embed.set_author(name="#163 D'artagnan (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553329314496522/DartagnanG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 100% 1 tour\n(No skillbooks)\n**PV**: 29933\n**Attaque**: 2253\n**Défense**: 2386\n**Récupération**:2311", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ["D'art","LightD'art","Dart","LightDart"]]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553339238481922/DartagnanW_large.jpeg", color=0xffffff)
		embed.set_author(name="#164 D'artagnan (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553339238481922/DartagnanW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 40%%\n(No skillbooks)\n**PV**: 24734\n**Attaque**: 3269\n**Défense**: 2254\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ["D'art","DarkD'art","Dart","DarkDart"]]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553326928199710/Dartagnan_large.jpeg", color=0xffffff)
		embed.set_author(name="#165 D'artagnan (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553326928199710/Dartagnan_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Nécrose x2 100% 1 tour\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 26736\n**Attaque**: 2322\n**Défense**: 3194\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### draka ##################
		###########################

	if any([message.content.startswith (item) for item in ['Drak','FeuDrak','TopDrak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553542011846692/Drakoness_large.jpeg", color=0xffffff)
		embed.set_author(name="#166 Draka (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553542011846692/Drakoness_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Boost de moral 15% (Allies SP)\n(No skillbooks)\n**Actif**: Perforation 100% 2 tours\n(No skillbooks)\n**PV**: 24856\n**Attaque**: 3902\n**Défense**: 2520\n**Récupération**:2125", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Drak','EauDrak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553546072195091/DrakonessB_large.jpeg", color=0xffffff)
		embed.set_author(name="#167 Draka (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553546072195091/DrakonessB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Affaiblissement 60% 3 tours\n(No skillbooks)\n**PV**: 28643\n**Attaque**: 3568\n**Défense**: 2622\n**Récupération**:2213", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Drak','BoisDrak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553553454170113/DrakonessG_large.jpeg", color=0xffffff)
		embed.set_author(name="#168 Draka (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553553454170113/DrakonessG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 50098\n**Attaque**: 2010\n**Défense**: 2827\n**Récupération**:1840", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Drak','LightDrak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553560928157696/DrakonessW_large.jpeg", color=0xffffff)
		embed.set_author(name="#169 Draka (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553560928157696/DrakonessW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 30556\n**Attaque**: 4038\n**Défense**: 2206\n**Récupération**:1852", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Drak','DarkDrak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553556293451797/DrakonessD_large.jpeg", color=0xffffff)
		embed.set_author(name="#170 Draka (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553556293451797/DrakonessD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**Actif**: Sceau 80% 2 tours\n(No skillbooks)\n**PV**: 28946\n**Attaque**: 3104\n**Défense**: 3162\n**Récupération**:2454", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### somnol ##################
		###########################

	if any([message.content.startswith (item) for item in ['Somn','FeuSomn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554918968295429/HypnosR_large.jpeg", color=0xffffff)
		embed.set_author(name="#171 Somnol (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554918968295429/HypnosR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 25% de ses PV\n(No skillbooks)\n**Actif**: Sommeil 90% 1 tours\n(No skillbooks)\n**PV**: 41688\n**Attaque**: 2126\n**Défense**: 2487\n**Récupération**:1751", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Somn','EauSomn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554914027536417/HypnosB_large.jpeg", color=0xffffff)
		embed.set_author(name="#172 Somnol (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554914027536417/HypnosB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Sommeil 90% 1 tours\n(No skillbooks)\n**PV**: 26971\n**Attaque**: 2682\n**Défense**: 2672\n**Récupération**:2501", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Somn','BoisSomn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554916955160576/HypnosG_large.jpeg", color=0xffffff)
		embed.set_author(name="#173 Somnol (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554916955160576/HypnosG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 25394\n**Attaque**: 3255\n**Défense**: 2261\n**Récupération**:2118", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Somn','LightSomn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554938102841344/HypnosW_large.jpeg", color=0xffffff)
		embed.set_author(name="#174 Somnol (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554938102841344/HypnosW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27492\n**Attaque**: 3194\n**Défense**: 2206\n**Récupération**:2363", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Somn','DarkSomn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554911980716033/Hypnos_large.jpeg", color=0xffffff)
		embed.set_author(name="#175 Somnol (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554911980716033/Hypnos_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(No skillbooks)\n**Actif**: Chasseur 40%\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 3323\n**Défense**: 2281\n**Récupération**:2254", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### fennec ##################
		###########################

	if any([message.content.startswith (item) for item in ['Fenn','FeuFenn','TopFenn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558622144593948/SandhiefR_large.jpeg", color=0xffffff)
		embed.set_author(name="#176 Fennec (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558622144593948/SandhiefR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Chasseur (bois) 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%Taux: +20%)\n**PV**: 27179\n**Attaque**: 2527\n**Défense**: 1566\n**Récupération**:1628", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenn','EauFenn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558617488785433/SandhiefB_large.jpeg", color=0xffffff)
		embed.set_author(name="#177 Fennec (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558617488785433/SandhiefB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Feu Chasseur 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26940\n**Attaque**: 2629\n**Défense**: 1525\n**Récupération**:1607", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenn','BoisFenn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558616155258890/Sandhief_large.jpeg", color=0xffffff)
		embed.set_author(name="#178 Fennec (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558616155258890/Sandhief_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%, (Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +20%)\n**Actif**: Attaque réduite 80%(On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 23733\n**Attaque**: 2574\n**Défense**: 1818\n**Récupération**:1805", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenn','LightFenn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558623381913610/SandhiefW_large.jpeg", color=0xffffff)
		embed.set_author(name="#179 Fennec (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558623381913610/SandhiefW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 26293\n**Attaque**: 3269\n**Défense**: 2281\n**Récupération**:1668", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenn','DarkFenn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558619623948298/SandhiefD_large.jpeg", color=0xffffff)
		embed.set_author(name="#180 Fennec (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558619623948298/SandhiefD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Vague martiale (On crit) 20%\n(Dmg +20%)\n**Actif**: Silence 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 45951\n**Attaque**: 1874\n**Défense**: 1874\n**Récupération**:1717", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### flora ##################
		###########################

	if any([message.content.startswith (item) for item in ['Flor','BoisFlor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558079909298225/Primavera_large.jpeg", color=0xffffff)
		embed.set_author(name="#183 Flora (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558079909298225/Primavera_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Sommeil 80% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 30866\n**Attaque**: 2131\n**Défense**: 2032\n**Récupération**:1351", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Flor','LightFlor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558086003621889/PrimaveraW_large.jpeg", color=0xffffff)
		embed.set_author(name="#184 Flora (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558086003621889/PrimaveraW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 37527\n**Attaque**: 2133\n**Défense**: 1874\n**Récupération**:2065", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Flor','DarkFlor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558083969384469/PrimaveraD_large.jpeg", color=0xffffff)
		embed.set_author(name="#185 Flora (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558083969384469/PrimaveraD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Même élément)\n**Passif**: Nécrose x3 80% 1 tour\n(Dmg : +10%, Taux : +20%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg : +20%, Taux : +10%)\n**PV**: 29675\n**Attaque**: 2389\n**Défense**: 2535\n**Récupération**:2474", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### gargor ##################
		###########################

	if any([message.content.startswith (item) for item in ['Garg','FeuGarg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554134377857026/GagolosR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#186 Gargor (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554134377857026/GagolosR_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: -10/15% resistance ennemie\n**Passif**: Pétrification 80% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**: Adrénaline 30% de ses PV\n(Dmg: +20%, Taux: +20%)\n**PV**: 32923\n**Attaque**: 1593\n**Défense**: 1521\n**Récupération**:1412", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garg','EauGarg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554106233946147/Gagolos_Large.jpeg", color=0xffffff)
		embed.set_author(name="#187 Gargor (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554106233946147/Gagolos_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: -10/15% resistance ennemie\n**Passif**: Adrénaline 20% de ses PV\n(Dmg: +20%, Taux: +10%)\n**Actif**: Adrénaline 20% PV (Allies)\n(Dmg: +20%)\n**PV**: 33488\n**Attaque**: 1452\n**Défense**: 1670\n**Récupération**:1336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garg','BoisGarg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554130753847326/GagolosG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#188 Gargor (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554130753847326/GagolosG_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: -10/15% resistance ennemie\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +20%, Taux: +20%)\n**Actif**: Pétrification 80% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 25374\n**Attaque**: 1702\n**Défense**: 2581\n**Récupération**:1362", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### félinelame ##################
		###########################

	if any([message.content.startswith (item) for item in ['Feli','FeuFeli']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329066328129553/MastercatR_large.jpg", color=0xffffff)
		embed.set_author(name="#191 Félinelame (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329066328129553/MastercatR_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35% (ToC)\n**Passif**: Récupération réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Pétrification 100% 1 tour\n(No skillbooks)\n**PV**: 28272\n**Attaque**: 2267\n**Défense**: 2106\n**Récupération**:1691", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Feli','EauFeli']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329056559595520/MastercatB_large.jpg", color=0xffffff)
		embed.set_author(name="#192 Félinelame (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329056559595520/MastercatB_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (ToC)\n**Passif**: Attaque réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 80% 2 tours\n(No skillbooks)\n**PV**: 24210\n**Attaque**: 1730\n**Défense**: 2697\n**Récupération**:1648", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Feli','BoisFeli']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329061882036225/MastercatG_large.jpg", color=0xffffff)
		embed.set_author(name="#193 Félinelame (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329061882036225/MastercatG_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35% (ToC)\n**Passif**: Défense réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Fatigue 100% 3 tours\n(No skillbooks)\n**PV**: 26212\n**Attaque**: 2588\n**Défense**: 1737\n**Récupération**:1566", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Feli','LightFeli']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329054106058762/Mastercat_large.jpg", color=0xffffff)
		embed.set_author(name="#194 Félinelame (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329054106058762/Mastercat_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (ToC)\n**Passif**: Nécrose 100% 2 tours\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 34203\n**Attaque**: 2221\n**Défense**: 2391\n**Récupération**:1881", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Feli','DarkFeli']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607329059239624714/MastercatD_large.jpg", color=0xffffff)
		embed.set_author(name="#195 Félinelame (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607329059239624714/MastercatD_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%(ToC)\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 23283\n**Attaque**: 3255\n**Défense**: 2363\n**Récupération**:1948", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### garuda ##################
		###########################

	if any([message.content.startswith (item) for item in ['Garu','FeuGaru']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556066714681347/MahagarudaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#196 Garuda (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556066714681347/MahagarudaR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25%\n**Passif**: Sceau 100% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 80% 1 tour\n(???)\n**PV**: 30965\n**Attaque**: 2247\n**Défense**: 3609\n**Récupération**:1968", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garu','EauGaru']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556035668181005/MahagarudaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#197 Garuda (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556035668181005/MahagarudaB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Avantage élémentaire\n(Dmg +35%)\n**PV**: 24938\n**Attaque**: 3643\n**Défense**: 2901\n**Récupération**:2213", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garu','BoisGaru','TopGaru']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556034820931595/Mahagaruda_large.jpeg", color=0xffffff)
		embed.set_author(name="#198 Garuda (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556034820931595/Mahagaruda_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%\n**Passif**: Affaiblissement 70% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Frappe Courageuse\n(Dmg +30%)\n**PV**: 31976\n**Attaque**: 3036\n**Défense**: 2787\n**Récupération**:2181", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garu','LightGaru']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556068534747136/MahagarudaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#199 Garuda (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556068534747136/MahagarudaW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Choc 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(???)\n**PV**: 25367\n**Attaque**: 3616\n**Défense**: 2670\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Garu','DarkGaru']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556061941432353/MahagarudaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#200 Garuda (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556061941432353/MahagarudaD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%\n**Passif**: Avantage élémentaire\n(Dmg +40%)\n**Actif**: Avantage élémentaire\n(Dmg +40%)\n**PV**: 28207\n**Attaque**: 4018\n**Défense**: 2635\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### gemini cricket ##################
		###########################

	if any([message.content.startswith (item) for item in ['Gem','FeuGem']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554192645128212/GemMiaR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#201 Gemini (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554192645128212/GemMiaR_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PV   \n(No skillbooks)\n**Actif**: Siphon de PV (Allies)  \n(No skillbooks)\n**PV**: 28881\n**Attaque**: 2615\n**Défense**: 1777\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gem','LightGem']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554188228263960/GemMia_Large.jpeg", color=0xffffff)
		embed.set_author(name="#204 Gemini (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554188228263960/GemMia_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 36301\n**Attaque**: 2221\n**Défense**: 2432\n**Récupération**:1853", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gem','DarkGem']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554190753234961/GemMiaD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#205 Gemini (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554190753234961/GemMiaD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PA (On crit) 30%\n(No skillbooks)\n**Actif**: Sommeil (On crit) 100%\n(No skillbooks)\n**PV**: 30832\n**Attaque**: 2362\n**Défense**: 2481\n**Récupération**:2352", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### spectros ##################
		###########################

	if any([message.content.startswith (item) for item in ['Spectro','LightSpectro']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557824001966091/PhantomW_large.jpeg", color=0xffffff)
		embed.set_author(name="#209 Spectros (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557824001966091/PhantomW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Étourdissement 100% (On crit) 1 tour\n(Dmg: +25%, +1 tour)\n**Actif**: Sommeil 100% (On crit) 1 tour\n(Dmg: +30%)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Spectro','DarkSpectro']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557820390932500/Phantom_large.jpeg", color=0xffffff)
		embed.set_author(name="#210 Spectros (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557820390932500/Phantom_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### sacstère ##################
		###########################

	if any([message.content.startswith (item) for item in ['Sac','FeuSac']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557581956485873677/Musuri_large.jpeg", color=0xffffff)
		embed.set_author(name="#211 Sacstère (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557581956485873677/Musuri_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(No skillbooks)\n**Actif**: Vigueur 2 tours \n(No skillbooks)\n**PV**: 28878\n**Attaque**: 2137\n**Défense**: 1923\n**Récupération**:1854", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sac','EauSac']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556913166909440/MusuriB_large.jpeg", color=0xffffff)
		embed.set_author(name="#212 Sacstère (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556913166909440/MusuriB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Adrénaline (On crit)(Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Zèle 2 tours \n(No skillbooks)\n**PV**: 33802\n**Attaque**: 1704\n**Défense**: 1881\n**Récupération**:1704", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sac','BoisSac']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556902652051476/MusuriG_large.jpeg", color=0xffffff)
		embed.set_author(name="#213 Sacstère (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556902652051476/MusuriG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Nécrose 70% 1 tour\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 26327\n**Attaque**: 1873\n**Défense**: 1580\n**Récupération**:2492", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sac','LightSac']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556908092063747/MusuriW_large.jpeg", color=0xffffff)
		embed.set_author(name="#214 Sacstère (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556908092063747/MusuriW_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 37459\n**Attaque**: 1384\n**Défense**: 1881\n**Récupération**:1744", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sac','DarkSac']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556943722545167/MusuriD_large.jpeg", color=0xffffff)
		embed.set_author(name="#215 Sacstère (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556943722545167/MusuriD_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%(Même élément)\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours\n(No skillbooks)\n**PV**: 34292\n**Attaque**: 1663\n**Défense**: 1697\n**Récupération**:1799", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### gupp ##################
		###########################

	if any([message.content.startswith (item) for item in ['Gupp','EauGupp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555792293953578/Longchu_large.jpeg", color=0xffffff)
		embed.set_author(name="#217 Gupp (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555792293953578/Longchu_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 60% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 26225\n**Attaque**: 2343\n**Défense**: 1696\n**Récupération**:1566", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### hades ##################
		###########################

	if any([message.content.startswith (item) for item in ['Hade','FeuHade']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553436533620736/DisPaterR_large.jpeg", color=0xffffff)
		embed.set_author(name="#221 Hades (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553436533620736/DisPaterR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Malédiction 80% 2 tours\n(Dmg: +15% tour: +1)\n**Actif**: Malédiction foudroyante\n(Dmg: +25%)\n**PV**: 27281\n**Attaque**: 3480\n**Défense**: 2492\n**Récupération**:2622", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hade','EauHade','TopHade']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553423887794207/DisPaterB_large.jpeg", color=0xffffff)
		embed.set_author(name="#222 Hades (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553423887794207/DisPaterB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg: +25% Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 31922\n**Attaque**: 2703\n**Défense**: 2747\n**Récupération**:2644", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hade','BoisHade']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553426559565855/DisPaterG_large.jpeg", color=0xffffff)
		embed.set_author(name="#223 Hades (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553426559565855/DisPaterG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist -20~25%\n**Passif**: Soif 80% -30% 2 tour\n(Dmg: +20%tour: +1)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 41109\n**Attaque**: 2296\n**Défense**: 2609\n**Récupération**:2521", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hade','LightHade']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553439352061952/DisPaterW_large.jpeg", color=0xffffff)
		embed.set_author(name="#224 Hades (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553439352061952/DisPaterW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Prédateur 40%\n(Dmg: +25%)\n**Actif**: Prédateur 50%\n(Dmg: +30%)\n**PV**: 33137\n**Attaque**: 3718\n**Défense**: 2418\n**Récupération**:2159", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hade','DarkHade']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553421815676929/DisPater_large.jpeg", color=0xffffff)
		embed.set_author(name="#225 Hades (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553421815676929/DisPater_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Malédiction 80% 3 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Malédiction foudroyante\n(Dmg: +20%)\n**PV**: 32967\n**Attaque**: 3677\n**Défense**: 2595\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### hana ##################
		###########################

	if any([message.content.startswith (item) for item in ['Hana','FeuHana']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554558396694528/HanahimeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#226 Hana (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554558396694528/HanahimeR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Sommeil 70% 1 tour\n(???)\n**Actif**: Boost de moral 3 tours\n(Dmg +25%+Effect.: +10%)\n**PV**: 30468\n**Attaque**: 2036\n**Défense**: 2431\n**Récupération**:2881", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hana','EauHana']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554554244202516/HanahimeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#227 Hana (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554554244202516/HanahimeB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Nécrose x2 60% 1 tour\n(Taux: +20%, tour: +1)\n**Actif**: Volonté 3 tours\n(Dmg +25%, Taux: +20%)\n**PV**: 32463\n**Attaque**: 2125\n**Défense**: 1954\n**Récupération**:3310", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hana','BoisHana','TopHana']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554551585275905/Hanahime_large.jpeg", color=0xffffff)
		embed.set_author(name="#228 Hana (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554551585275905/Hanahime_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Attaque réduite 70% 2 tour\n(Dmg +10%, Taux: +10%)\n**Actif**: Défense augmentée 3 tours\n(Dmg +25%, Taux: +10%)\n**PV**: 32443\n**Attaque**: 2138\n**Défense**: 1989\n**Récupération**:3364", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hana','LightHana']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554561467056139/HanahimeW_large.jpeg", color=0xffffff)
		embed.set_author(name="#229 Hana (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554561467056139/HanahimeW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%\n**Passif**: Agression (PV)\n(Dmg +20%)\n**Actif**: Bouclier (PV) 3 tours\n(Dmg +25%)\n**PV**: 36805\n**Attaque**: 1976\n**Défense**: 1996\n**Récupération**:2357", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hana','DarkHana']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554555599093760/HanahimeD_large.jpeg", color=0xffffff)
		embed.set_author(name="#230 Hana (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554555599093760/HanahimeD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35%\n**Passif**: Abondance d'âmes rouges \n(Dmg +30%)\n**Actif**: Bouclier (Level) 3 tours\n(Dmg +25%)\n**PV**: 29624\n**Attaque**: 2125\n**Défense**: 1982\n**Récupération**:3058", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### lermite ##################
		###########################

	if any([message.content.startswith (item) for item in ['Lerm','EauLerm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555361773682718/Komorix_large.jpeg", color=0xffffff)
		embed.set_author(name="#232 Lermite (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555361773682718/Komorix_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +15%, Taux: +10%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 29787\n**Attaque**: 2343\n**Défense**: 3139\n**Récupération**:1750", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### hohenheim ##################
		###########################

	if any([message.content.startswith (item) for item in ['Hohe','FeuHohe','TopHohe']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635465113305099/ParacelsusR_large.jpg", color=0xffffff)
		embed.set_author(name="#236 Hohenheim (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635465113305099/ParacelsusR_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +35~40%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg: +25% Taux: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg: +25% Taux: +10)\n**PV**: 43213\n**Attaque**: 2378\n**Défense**: 2630\n**Récupération**:2412", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hohe','EauHohe']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635473526947885/ParacelsusB_large.jpg", color=0xffffff)
		embed.set_author(name="#237 Hohenheim (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635473526947885/ParacelsusB_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +35~40%\n**Passif**: Vague martiale 20%\n(Dmg: +20% Effect.: +5%)\n**Actif**: Taux critique augmenté 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 32242\n**Attaque**: 3009\n**Défense**: 2999\n**Récupération**:2556", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hohe','BoisHohe']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635470511505439/Paracelsus_large.jpg", color=0xffffff)
		embed.set_author(name="#238 Hohenheim (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635470511505439/Paracelsus_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg: +30% )\n**Actif**: Nécrose x3 80% 2 tour\n(Dmg: +10% Taux: +20%)\n**PV**: 27233\n**Attaque**: 3582\n**Défense**: 2901\n**Récupération**:2561", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hohe','LightHohe']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635467797790729/ParacelsusW_large.jpg", color=0xffffff)
		embed.set_author(name="#239 Hohenheim (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635467797790729/ParacelsusW_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Siphon de PA 30%\n(No skillbooks)\n**Actif**: Attaque augmentée 2 tours\n(No skillbooks)\n**PV**: 28105\n**Attaque**: 3841\n**Défense**: 2499\n**Récupération**:2418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Hohe','DarkHohe']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607635462743654423/ParacelsusD_large.jpg", color=0xffffff)
		embed.set_author(name="#240 Hohenheim (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607635462743654423/ParacelsusD_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +35~40%\n**Passif**: Prédateur 40%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 28357\n**Attaque**: 3718\n**Défense**: 2567\n**Récupération**:2370", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### chasseur ##################
		###########################

	if any([message.content.startswith (item) for item in ['Chas','FeuChas']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560671754027032/VanhelsingR_large.jpeg", color=0xffffff)
		embed.set_author(name="#241 Chasseur (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560671754027032/VanhelsingR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20(League)\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(Dmg +25%)\n**Actif**: Étourdissement 80% (On crit) 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 25776\n**Attaque**: 2595\n**Défense**: 1573\n**Récupération**:1737", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chas','EauChas']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560665756434453/Vanhelsing_large.jpeg", color=0xffffff)
		embed.set_author(name="#242 Chasseur (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560665756434453/Vanhelsing_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20(League)\n**Passif**: Siphon de PV\n(Dmg +30%)\n**Actif**: Siphon de PV\n(Dmg +30%)\n**PV**: 29164\n**Attaque**: 1960\n**Défense**: 1684\n**Récupération**:1664", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chas','BoisChas']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560669648617482/VanhelsingG_large.jpeg", color=0xffffff)
		embed.set_author(name="#243 Chasseur (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560669648617482/VanhelsingG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20(League)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +20%, Taux: +5%)\n**Actif**: Nécrose x3 50% 1 tour\n(Dmg +10%Taux: +10%, tour: +1)\n**PV**: 30420\n**Attaque**: 1539\n**Défense**: 2554\n**Récupération**:1832", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chas','LightChas']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560673993916417/VanhelsingW_large.jpeg", color=0xffffff)
		embed.set_author(name="#244 Chasseur (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560673993916417/VanhelsingW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20(League)\n**Passif**: Choc 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Siphon de PV\n(Dmg +30%)\n**PV**: 30808\n**Attaque**: 3064\n**Défense**: 1873\n**Récupération**:2070", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chas','DarkChas']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560667505459251/VanhelsingD_large.jpeg", color=0xffffff)
		embed.set_author(name="#245 Chasseur (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560667505459251/VanhelsingD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20(League)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30114\n**Attaque**: 2309\n**Défense**: 3139\n**Récupération**:1832", inline=False)

		await message.channel.send(embed=embed)

###########################
######### incubus ##################
###########################

	if any([message.content.startswith (item) for item in ['Incu','FeuIncu','TopIncu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551634056642589/AzazelR_large.jpeg", color=0xffffff)
		embed.set_author(name="#246 Incubus (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551634056642589/AzazelR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours (on crit)\n(???)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 31711\n**Attaque**: 2648\n**Défense**: 2535\n**Récupération**:1732", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Incu','EauIncu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557576304405512192/AzazelB_large.jpeg", color=0xffffff)
		embed.set_author(name="#247 Incubus (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557576304405512192/AzazelB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 36505\n**Attaque**: 2180\n**Défense**: 2432\n**Récupération**:1874", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Incu','BoisIncu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551631116435457/AzazelG_large.jpeg", color=0xffffff)
		embed.set_author(name="#248 Incubus (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551631116435457/AzazelG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 25095\n**Attaque**: 3173\n**Défense**: 2547\n**Récupération**:1771", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Incu','LightIncu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551638858989576/AzazelW_large.jpeg", color=0xffffff)
		embed.set_author(name="#249 Incubus (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551638858989576/AzazelW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV (Allies)\n(Dmg +20%)\n**Actif**: Choc 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 27962\n**Attaque**: 3167\n**Défense**: 2254\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Incu','DarkIncu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551623755563008/Azazel_large.jpeg", color=0xffffff)
		embed.set_author(name="#250 Incubus (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551623755563008/Azazel_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV , Greatly)\n(Dmg +20%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 24822\n**Attaque**: 3221\n**Défense**: 2492\n**Récupération**:2111", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### indra ##################
		###########################

	if any([message.content.startswith (item) for item in ['Indr','FeuIndr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555001113739296/IndrasakraR_large.jpeg", color=0xffffff)
		embed.set_author(name="#251 Indra (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555001113739296/IndrasakraR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Avantage élémentaire\n(Dmg +30%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**PV**: 31694\n**Attaque**: 3650\n**Défense**: 2288\n**Récupération**:2329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Indr','EauIndr','TopIndr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554997502705694/IndrasakraB_large.jpeg", color=0xffffff)
		embed.set_author(name="#252 Indra (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554997502705694/IndrasakraB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%\n**Passif**: Attaque réduite 80% 3 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 27768\n**Attaque**: 3043\n**Défense**: 3033\n**Récupération**:2876", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Indr','BoisIndr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555002154188838/IndrasakraG_large.jpeg", color=0xffffff)
		embed.set_author(name="#253 Indra (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555002154188838/IndrasakraG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%\n**Passif**: Étourdissement 100% 1 tour \n(Dmg +15%, tour: +1)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 32841\n**Attaque**: 2846\n**Défense**: 2910\n**Récupération**:1929", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Indr','LightIndr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555003815002112/IndrasakraW_large.jpeg", color=0xffffff)
		embed.set_author(name="#254 Indra (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555003815002112/IndrasakraW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Boost Moral regen 20% PA\n(Dmg +30%)\n**Actif**: prédateur 50%\n(Dmg +30%)\n**PV**: 27281\n**Attaque**: 3977\n**Défense**: 2663\n**Récupération**:2240", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Indr','DarkIndr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554996357529610/Indrasakra_large.jpeg", color=0xffffff)
		embed.set_author(name="#255 Indra (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554996357529610/Indrasakra_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 28166\n**Attaque**: 3677\n**Défense**: 2554\n**Récupération**:2295", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### citrouillon ##################
		###########################

	if any([message.content.startswith (item) for item in ['Citr','FeuCitr','TopCitr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555117426114590/JacquelynR_large.jpeg", color=0xffffff)
		embed.set_author(name="#256 Citrouillon (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555117426114590/JacquelynR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 37091\n**Attaque**: 2391\n**Défense**: 2099\n**Récupération**:1956", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Citr','EauCitr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555097419284499/JacquelynB_large.jpeg", color=0xffffff)
		embed.set_author(name="#257 Citrouillon (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555097419284499/JacquelynB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Sceau 70% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Provocation 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 25374\n**Attaque**: 1954\n**Défense**: 2894\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Citr','BoisCitr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555113470754841/JacquelynG_large.jpeg", color=0xffffff)
		embed.set_author(name="#258 Citrouillon (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555113470754841/JacquelynG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Prédateur 30%\n(Dmg +10%, Taux: +15%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 23781\n**Attaque**: 2418\n**Défense**: 1696\n**Récupération**:1818", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Citr','LightCitr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555119665741825/JacquelynW_large.jpeg", color=0xffffff)
		embed.set_author(name="#259 Citrouillon (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555119665741825/JacquelynW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Boost de moral (On crit) 30% de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Chasseur 50%\n(Dmg +20%, Taux: +5%)\n**PV**: 25143\n**Attaque**: 3173\n**Défense**: 2281\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Citr','DarkCitr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555093002813458/Jacquelyn_large.jpeg", color=0xffffff)
		embed.set_author(name="#260 Citrouillon (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555093002813458/Jacquelyn_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV Rec +20~25%\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 38759\n**Attaque**: 1813\n**Défense**: 2316\n**Récupération**:2133", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### jeanne ! Au secours !! ##################
		###########################

	if any([message.content.startswith (item) for item in ['Jean','FeuJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553975396827195/FreyjaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#261 Jeanne (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553975396827195/FreyjaR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Abondance d'âmes rouges\n(No skillbooks)\n**PV**: 37942\n**Attaque**: 2194\n**Défense**: 1853\n**Récupération**:2058", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jean','EauJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553955138338847/FreyjaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#262 Jeanne (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553955138338847/FreyjaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Sommeil 100% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2220\n**Défense**: 3208\n**Récupération**:2050", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jean','BoisJean','TopJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213220709072906/FreyjaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#263 Jeanne (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213220709072906/FreyjaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Traqueur +30% CR\n(No skillbooks)\n**Actif**: Traqueur +30% CR\n(No skillbooks)\n**PV**: 23842\n**Attaque**: 3262\n**Défense**: 2091\n**Récupération**:1839", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jean','LightJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553920019300384/Freyja_large.jpeg", color=0xffffff)
		embed.set_author(name="#264 Jeanne (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553920019300384/Freyja_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 43560\n**Attaque**: 1472\n**Défense**: 2337\n**Récupération**:1874", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jean','DarkJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553955897376768/FreyjaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#265 Jeanne (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553955897376768/FreyjaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 31544\n**Attaque**: 2206\n**Défense**: 3153\n**Récupération**:2138", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Jeanne S Evo ##################
		###########################

	if any([message.content.startswith (item) for item in ['SJean','FeuJean','FeuSJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107143728955534/20200521_210719.jpg", color=0xffffff)
		embed.set_author(name="#824 Jeanne SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107143728955534/20200521_210719.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Abondance d'âmes rouges\n(No skillbooks)\n**PV**: 41905\n**Attaque**: 2419\n**Défense**: 1853\n**Récupération**: 2269", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SJean','EauJean','EauSJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107143959511151/20200521_210739.jpg", color=0xffffff)
		embed.set_author(name="#825 Jeanne SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107143959511151/20200521_210739.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Sommeil 100% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**PV**: 29760\n**Attaque**: 2452\n**Défense**: 3562\n**Récupération**: 2261", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SJean','BoisJean','BoisSJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144240660580/20200521_210757.jpg", color=0xffffff)
		embed.set_author(name="#826 Jeanne SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144240660580/20200521_210757.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Traqueur +30% CR\n(No skillbooks)\n**Actif**: Traqueur +30% CR\n(No skillbooks)\n**PV**: 28854\n**Attaque**: 3800\n**Défense**: 2309\n**Récupération**: 2029", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SJean','LightJean','LightSJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144668348456/20200521_210814.jpg", color=0xffffff)
		embed.set_author(name="#827 Jeanne SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144668348456/20200521_210814.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Agression (PV)\n(No skillbooks)\n**Actif**: Agression (PV)\n(No skillbooks)\n**PV**: 48081\n**Attaque**: 1622\n**Défense**: 2576\n**Récupération**: 2065", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SJean','DarkJean','DarkSJean']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/706455947987386369/713107144945303695/20200521_210833.jpg", color=0xffffff)
		embed.set_author(name="#828 Jeanne SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/706455947987386369/713107144945303695/20200521_210833.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 34704\n**Attaque**: 2431\n**Défense**: 3500\n**Récupération**: 2356", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Médusine ##################
		###########################

	if any([message.content.startswith (item) for item in ['Medusi','FeuMedusi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555220014596136/JellionR_large.jpeg", color=0xffffff)
		embed.set_author(name="#266 Médusine (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555220014596136/JellionR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(ToC)\n**Passif**: Siphon de PV \n(Dmg: +30%)\n**Actif**: Pétrification 40% 1 tour\n(Taux: +30%)\n**PV**: 25306\n**Attaque**: 2615\n**Défense**: 1784\n**Récupération**:1267", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusi','EauMedusi','TopMedusi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555191816290304/Jellion_large.jpeg", color=0xffffff)
		embed.set_author(name="#267 Médusine (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555191816290304/Jellion_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: PV +30~35%(ToC)\n**Passif**: Brise bouclier 100%\n(Dmg: +30%)\n**Actif**: Adrénaline (Allies) 5% de ses PV\n(Dmg: +20% Effect.: +5%)\n**PV**: 35599\n**Attaque**: 1717\n**Défense**: 1915\n**Récupération**:1465", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusi','BoisMedusi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555219054231559/JellionG_large.jpeg", color=0xffffff)
		embed.set_author(name="#268 Médusine (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555219054231559/JellionG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(ToC)\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg: +15% Taux: +10% tour: +1)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg: +10% Taux: +10% tour: +1)\n**PV**: 30206\n**Attaque**: 1763\n**Défense**: 1929\n**Récupération**:1752", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusi','LightMedusi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555221620883477/JellionW_large.jpeg", color=0xffffff)
		embed.set_author(name="#269 Médusine (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555221620883477/JellionW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(ToC)\n**Passif**: Sceau 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 22793\n**Attaque**: 3405\n**Défense**: 2077\n**Récupération**:1914", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusi','DarkMedusi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555215572697119/JellionD_large.jpeg", color=0xffffff)
		embed.set_author(name="#270 Médusine (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555215572697119/JellionD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(ToC)\n**Passif**: Adrénaline (Allies) 5% de ses PV\n(Dmg: +20% Effect.: +5%)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 32698\n**Attaque**: 2267\n**Défense**: 2311\n**Récupération**:2134", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Jiangshi ##################
		###########################

	if any([message.content.startswith (item) for item in ['Jiang','FeuJiang']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210252976324639/Jiangshi3EvoR_large.jpg", color=0xffffff)
		embed.set_author(name="#271 Jiangshi (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210252976324639/Jiangshi3EvoR_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Provocation intrépide -50% damage 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 60% 2 tours\n(No skillbooks)\n**PV**: 24918\n**Attaque**: 1832\n**Défense**: 2772\n**Récupération**:1594", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jiang','EauJiang']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210250979704835/Jiangshi3EvoB_large.jpg", color=0xffffff)
		embed.set_author(name="#272 Jiangshi (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210250979704835/Jiangshi3EvoB_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Malédiction 80% 2 tours\n(No skillbooks)\n**Actif**: Malédiction 80% 2 tours\n(No skillbooks)\n**PV**: 38855\n**Attaque**: 1799\n**Défense**: 1806\n**Récupération**:1622", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jiang','BoisJiang']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210252204703744/Jiangshi3EvoG_large.jpg", color=0xffffff)
		embed.set_author(name="#273 Jiangshi (Bois)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210252204703744/Jiangshi3EvoG_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Sommeil 80% 1 tours\n(No skillbooks)\n**Actif**: Frappe indéfectible \n(No skillbooks)\n**PV**: 26345\n**Attaque**: 2219\n**Défense**: 2358\n**Récupération**:1657", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jiang','LightJiang']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210254725480457/Jiangshi3EvoW_large.jpg", color=0xffffff)
		embed.set_author(name="#274 Jiangshi (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210254725480457/Jiangshi3EvoW_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Boost de moral (soi-même) 20% SP\n(No skillbooks)\n**Actif**: Siphon de PV (Allies, Greatly)\n(No skillbooks)\n**PV**: 26552\n**Attaque**: 3201\n**Défense**: 2247\n**Récupération**:1961", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jiang','DarkJiang']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/553210249843048461/Jiangshi3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#275 Jiangshi (dark)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/553210249843048461/Jiangshi3Evo_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Malédiction 80% 2 tours\n(No skillbooks)\n**Actif**: Malédiction foudroyante\n(No skillbooks)\n**PV**: 27322\n**Attaque**: 3255\n**Défense**: 2309\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Djinn ##################
		###########################

	if any([message.content.startswith (item) for item in ['Djinn','FeuDjinn','TopDjinn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554941957406785/Ifrit_large.jpeg", color=0xffffff)
		embed.set_author(name="#276 Djinn (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554941957406785/Ifrit_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Boost de moral\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 26927\n**Attaque**: 3337\n**Défense**: 2193\n**Récupération**:1982", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Djinn','EauDjinn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554941974183958/IfritB_large.jpeg", color=0xffffff)
		embed.set_author(name="#277 Djinn (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554941974183958/IfritB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(No skillbooks)\n**PV**: 29957\n**Attaque**: 2322\n**Défense**: 2595\n**Récupération**:2206", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Djinn','BoisDjinn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554946260893714/IfritG_large.jpeg", color=0xffffff)
		embed.set_author(name="#278 Djinn (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554946260893714/IfritG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x3 80% 1 tour\n(No skillbooks)\n**PV**: 28919\n**Attaque**: 3018\n**Défense**: 1976\n**Récupération**:1996", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Djinn','LightDjinn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554948643127296/IfritW_large.jpeg", color=0xffffff)
		embed.set_author(name="#279 Djinn (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554948643127296/IfritW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25156\n**Attaque**: 3296\n**Défense**: 2704\n**Récupération**:2077", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Djinn','DarkDjinn']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554944339902536/IfritD_large.jpeg", color=0xffffff)
		embed.set_author(name="#280 Djinn (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554944339902536/IfritD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Résistance réduite 100% 2 tours\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tour\n(No skillbooks)\n**PV**: 38827\n**Attaque**: 2294\n**Défense**: 1889\n**Récupération**:2140", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### kiki ##################
		###########################

	if any([message.content.startswith (item) for item in ['Kiki','FeuKiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213368314888192/KikimoraR_large.jpeg", color=0xffffff)
		embed.set_author(name="#281 Kiki (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213368314888192/KikimoraR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(ToC)\n**Passif**: Brise bouclier 100%\n(Dmg +25%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25316\n**Attaque**: 2335\n**Défense**: 2345\n**Récupération**:2038", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Kiki','EauKiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555271101218816/KikimoraB_large.jpeg", color=0xffffff)
		embed.set_author(name="#282 Kiki (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555271101218816/KikimoraB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(ToC)\n**Passif**: Brise-Bonus 100%\n(Dmg +25%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28742\n**Attaque**: 1885\n**Défense**: 2038\n**Récupération**:2004", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Kiki','BoisKiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555266462187520/Kikimora_large.jpeg", color=0xffffff)
		embed.set_author(name="#283 Kiki (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555266462187520/Kikimora_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(ToC)\n**Passif**: Pétrification (On crit) 1 tour\n(Dmg +20%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 25897\n**Attaque**: 2751\n**Défense**: 1621\n**Récupération**:1730", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Kiki','LightKiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555287530438656/KikimoraW_large.jpeg", color=0xffffff)
		embed.set_author(name="#284 Kiki (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555287530438656/KikimoraW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(ToC)\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 26246\n**Attaque**: 2452\n**Défense**: 3568\n**Récupération**:1941", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Kiki','DarkKiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555282191089686/KikimoraD_large.jpeg", color=0xffffff)
		embed.set_author(name="#285 Kiki (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555282191089686/KikimoraD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(ToC)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%)\n**PV**: 27744\n**Attaque**: 3357\n**Défense**: 2309\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### kiloptère ##################
		###########################

	if any([message.content.startswith (item) for item in ['Kilo','LightKilo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560481378893864/UltrabatW_large.jpeg", color=0xffffff)
		embed.set_author(name="#289 Kiloptère (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560481378893864/UltrabatW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: CR +10~15%\n**Passif**: Attaque réduite 100% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 29249\n**Attaque**: 1321\n**Défense**: 2527\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Kilo','DarkKilo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560476828205056/Ultrabat_large.jpeg", color=0xffffff)
		embed.set_author(name="#290 Kiloptère (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560476828205056/Ultrabat_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Traqueur (Dark) 20%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 25776\n**Attaque**: 2302\n**Défense**: 1471\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Latt ##################
		###########################

	if any([message.content.startswith (item) for item in ['Latt','FeuLatt']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552058390052879/BlizzardR_large.jpeg", color=0xffffff)
		embed.set_author(name="#291 Latt (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552058390052879/BlizzardR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(League)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 26838\n**Attaque**: 2622\n**Défense**: 1532\n**Récupération**:1600", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Latt','EauLatt','TopLatt']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552051075317780/Blizzard_large.jpeg", color=0xffffff)
		embed.set_author(name="#292 Latt (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552051075317780/Blizzard_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(League)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 38140\n**Attaque**: 1574\n**Défense**: 1506\n**Récupération**:1887", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Latt','BoisLatt']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552056536301588/BlizzardG_large.jpeg", color=0xffffff)
		embed.set_author(name="#293 Latt (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552056536301588/BlizzardG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(League)\n**Passif**: Nécrose 40% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Fatigue 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 30015\n**Attaque**: 1620\n**Défense**: 1766\n**Récupération**:1623", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Latt','LightLatt']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557584671039422474/BlizzardW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#294 Latt (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557584671039422474/BlizzardW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(League)\n**Passif**: Choc 60% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 29688\n**Attaque**: 2389\n**Défense**: 2501\n**Récupération**:2474", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Latt','DarkLatt']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552053319270426/BlizzardD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#295 Latt (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552053319270426/BlizzardD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (League)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 30652\n**Attaque**: 2996\n**Défense**: 1907\n**Récupération**:2002", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Léo ##################
		###########################

	if any([message.content.startswith (item) for item in ['Leo','FeuLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555628963561473/Leon_large.jpeg", color=0xffffff)
		embed.set_author(name="#296 Leo (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555628963561473/Leon_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 26348\n**Attaque**: 3173\n**Défense**: 2281\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)


	if any([message.content.startswith (item) for item in ['Leo','EauLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555634298716162/LeonB_large.jpeg", color=0xffffff)
		embed.set_author(name="#298 Leo (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555634298716162/LeonB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Provocation intrépide 90% 2 tour\n(???)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 36941\n**Attaque**: 2364\n**Défense**: 1813\n**Récupération**:1922", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Leo','BoisLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555655307722797/LeonG_large.jpeg", color=0xffffff)
		embed.set_author(name="#300 Leo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555655307722797/LeonG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30059\n**Attaque**: 2363\n**Défense**: 3139\n**Récupération**:1880", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Leo','LightLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555657581035527/LeonW_large.jpeg", color=0xffffff)
		embed.set_author(name="#302 Leo (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555657581035527/LeonW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(Dmg +10%, +Effect.: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 27281\n**Attaque**: 3139\n**Défense**: 2261\n**Récupération**:2118", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Leo','DarkLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555651872849930/LeonD_large.jpeg", color=0xffffff)
		embed.set_author(name="#304 Leo (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555651872849930/LeonD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 100% 2 tours\n(Dmg +15%, tour: +1)\n**Actif**: Silence 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28091\n**Attaque**: 3276\n**Défense**: 2002\n**Récupération**:2070", inline=False)

		await message.channel.send(embed=embed)


		###########################
		######### Léo S Evo ##################
		###########################

	if any([message.content.startswith (item) for item in ['FeuLeo','SLeo','FeuSLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559867416805376/SuperLionking_large.jpeg", color=0xffffff)
		embed.set_author(name="#297 Leo SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559867416805376/SuperLionking_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 28990\n**Attaque**: 3521\n**Défense**: 2520\n**Récupération**:1811", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauLeo','SLeo','EauSLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559870100897812/SuperLionkingB_large.jpeg", color=0xffffff)
		embed.set_author(name="#299 Leo SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559870100897812/SuperLionkingB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Provocation 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 40801\n**Attaque**: 2603\n**Défense**: 1997\n**Récupération**:2119", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisLeo','SLeo','BoisSLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559889382113295/SuperLionkingG_large.jpeg", color=0xffffff)
		embed.set_author(name="#301 Leo SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559889382113295/SuperLionkingG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 33069\n**Attaque**: 2608\n**Défense**: 3487\n**Récupération**:2077", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightLeo','SLeo','LightSLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559892381040640/SuperLionkingW_large.jpeg", color=0xffffff)
		embed.set_author(name="#303 Leo SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559892381040640/SuperLionkingW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50% de ses PA\n(Dmg +10%, +Effect.: +10%)\n**Actif**: Étourdissement 50% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30018\n**Attaque**: 3487\n**Défense**: 2492\n**Récupération**:2336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkLeo','SLeo','DarkSLeo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559885582204928/SuperLionkingD_large.jpeg", color=0xffffff)
		embed.set_author(name="#305 Leo SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559885582204928/SuperLionkingD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 100% 2 tours\n(Dmg +15%, tour: +1)\n**Actif**: Silence 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30911\n**Attaque**: 3637\n**Défense**: 2206\n**Récupération**:2281", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Loki ##################
		###########################

	if any([message.content.startswith (item) for item in ['Loki','FeuLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560415549423619/TricksterlokiR_large.jpeg", color=0xffffff)
		embed.set_author(name="#306 Loki (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560415549423619/TricksterlokiR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Nécrose 80% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 33856\n**Attaque**: 2253\n**Défense**: 2229\n**Récupération**:2066", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','EauLoki','TopLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560403012517889/TricksterlokiB_large.jpeg", color=0xffffff)
		embed.set_author(name="#307 Loki (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560403012517889/TricksterlokiB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Prédateur 40%\n(Dmg +25%, Effect: +10%)\n**PV**: 30556\n**Attaque**: 3357\n**Défense**: 2118\n**Récupération**:1907", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','BoisLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560400420569099/Tricksterloki_large.jpeg", color=0xffffff)
		embed.set_author(name="#308 Loki (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560400420569099/Tricksterloki_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Boost moral 40%PA\n(Dmg +20%, Effect: +10%)\n**Actif**: Agression (Def)\n(Dmg +25%)\n**PV**: 30611\n**Attaque**: 2418\n**Défense**: 3391\n**Récupération**:1900", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','LightLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557586319992291339/TricksterlokiW_large.jpeg", color=0xffffff)
		embed.set_author(name="#309 Loki (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557586319992291339/TricksterlokiW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Boost moral 10% PA\n(Dmg +20%, Effect: +5%)\n**Actif**: Provoc (réduit 50%dmg) 70% 2tours\n(Dmg +20%, Taux: +10%)\n**PV**: 29732\n**Attaque**: 2418\n**Défense**: 3221\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','DarkLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560407211147275/TricksterlokiD_large.jpeg", color=0xffffff)
		embed.set_author(name="#310 Loki (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560407211147275/TricksterlokiD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 80% 3 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 38548\n**Attaque**: 2180\n**Défense**: 2405\n**Récupération**:1853", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### Loki S Evo ############
		###########################

	if any([message.content.startswith (item) for item in ['Loki','FeuLoki','SLoki','FeuSLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/783271918329397258/Screenshot_20201201-110053_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#306 Loki SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/783271918329397258/Screenshot_20201201-110053_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Nécrose 80% 2 tours\n(Dmg +15%, Taux: +10%, tour: +1)\n**Actif**: Nécrose x2 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 37267\n**Attaque**: 2488\n**Défense**: 2459\n**Récupération**:2282", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','EauLoki','TopLoki','SLoki','EauSLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/783271918177353728/Screenshot_20201201-110120_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#307 Loki SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/783271918177353728/Screenshot_20201201-110120_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Prédateur 40%\n(Dmg +25%, Effect: +10%)\n**PV**: 33621\n**Attaque**: 3725\n**Défense**: 2336\n**Récupération**:2104", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','BoisLoki','SLoki','BoisSLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/783271918014562304/Screenshot_20201201-110145_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#308 Loki SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/783271918014562304/Screenshot_20201201-110145_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Boost moral 40%PA\n(Dmg +20%, Effect: +10%)\n**Actif**: Agression (Def)\n(Dmg +25%)\n**PV**: 33682\n**Attaque**: 2670\n**Défense**: 3759\n**Récupération**:2097", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','LightLoki','SLoki','LightSLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/783271917825163294/Screenshot_20201201-110206_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#309 Loki SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/783271917825163294/Screenshot_20201201-110206_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Boost moral 10% PA\n(Dmg +20%, Effect: +5%)\n**Actif**: Provoc (réduit 50%dmg) 70% 2tours\n(Dmg +20%, Taux: +10%)\n**PV**: 32715\n**Attaque**: 2670\n**Défense**: 3575\n**Récupération**:2581", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Loki','DarkLoki','SLoki','DarkSLoki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/783271917661978644/Screenshot_20201201-110228_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#310 Loki SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/783271917661978644/Screenshot_20201201-110228_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Sceau 80% 3 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 42572\n**Attaque**: 2398\n**Défense**: 2650\n**Récupération**:2044", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### lucy ##################
		###########################

	if any([message.content.startswith (item) for item in ['Lucy','FeuLucy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559334324830219/SnowwhiteR_large.jpeg", color=0xffffff)
		embed.set_author(name="#311 Lucy (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559334324830219/SnowwhiteR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Siphon de PV \n(Dmg +25%)\n**Actif**: Sceau 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 23494\n**Attaque**: 3378\n**Défense**: 2349\n**Récupération**:1900", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lucy','EauLucy','TopLucy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559321473482764/Snowwhite_large.jpeg", color=0xffffff)
		embed.set_author(name="#312 Lucy (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559321473482764/Snowwhite_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 28098\n**Attaque**: 3276\n**Défense**: 2009\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lucy','BoisLucy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559324556427267/SnowwhiteG_large.jpeg", color=0xffffff)
		embed.set_author(name="#313 Lucy (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559324556427267/SnowwhiteG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%(League)\n**Passif**: Nécrose 90% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 30689\n**Attaque**: 2376\n**Défense**: 2481\n**Récupération**:2331", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lucy','LightLucy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559383763222588/SnowwhiteW_large.jpeg", color=0xffffff)
		embed.set_author(name="#314 Lucy (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559383763222588/SnowwhiteW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%(League)\n**Passif**: Choc 70% 1 tour\n(Dmg +15%)\n**Actif**: Choc 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 38984\n**Attaque**: 2084\n**Défense**: 2405\n**Récupération**:1853", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lucy','DarkLucy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559322496761866/SnowwhiteD_large.jpeg", color=0xffffff)
		embed.set_author(name="#315 Lucy (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559322496761866/SnowwhiteD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%(League)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Faiblesse exposée 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 27349\n**Attaque**: 3439\n**Défense**: 2288\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### lumo ##################
		###########################

	if any([message.content.startswith (item) for item in ['Lumo','FeuLumo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213503161892894/LuminaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#316 Lumo (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213503161892894/LuminaR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Récupération augmentée 2 tours\n(No skillbooks)\n**PV**: 25497\n**Attaque**: 1648\n**Défense**: 1682\n**Récupération**:2315", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lumo','EauLumo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555923709886484/LuminaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#317 Lumo (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555923709886484/LuminaB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Récupération réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Attaque augmentée  2 tours\n(No skillbooks)\n**PV**: 28977\n**Attaque**: 1743\n**Défense**: 2384\n**Récupération**:1301", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lumo','BoisLumo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555924376518678/Lumina_large.jpeg", color=0xffffff)
		embed.set_author(name="#318 Lumo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555924376518678/Lumina_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 40% 1 tours\n(No skillbooks)\n**Actif**: Blue souls SP up 2 tours\n(No skillbooks)\n**PV**: 29290\n**Attaque**: 1410\n**Défense**: 1832\n**Récupération**:2288", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### lupin ##################
		###########################

	if any([message.content.startswith (item) for item in ['Lupin','FeuLupin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556893927899138/MysteriousLupinR_large.jpeg", color=0xffffff)
		embed.set_author(name="#321 Lupin (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556893927899138/MysteriousLupinR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Prédateur 30%\n(No skillbooks)\n**Actif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 25122\n**Attaque**: 3262\n**Défense**: 2295\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lupin','EauLupin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556905772482580/MysteriousLupinB_large.jpeg", color=0xffffff)
		embed.set_author(name="#322 Lupin (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556905772482580/MysteriousLupinB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 25% de ses PV\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 41402\n**Attaque**: 2391\n**Défense**: 1785\n**Récupération**:1922", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lupin','BoisLupin','TopLupin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556898126135297/MysteriousLupinG_large.jpeg", color=0xffffff)
		embed.set_author(name="#323 Lupin (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556898126135297/MysteriousLupinG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 30151\n**Attaque**: 2614\n**Défense**: 2440\n**Récupération**:2311", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lupin','DarkLupin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607328062346100736/BossMysteriousLupin_large.jpg", color=0xffffff)
		embed.set_author(name="#325 Lupin (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607328062346100736/BossMysteriousLupin_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Siphon de PA 25%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 27451\n**Attaque**: 3310\n**Défense**: 2261\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

	if message.content.startswith('Lupina'):
		return

	if message.content.startswith('DarkLupina'):
		return

	if message.content.startswith('BoisLupina'):
		return

	if message.content.startswith('EauLupina'):
		return

	if message.content.startswith('FeuLupina'):
		return

	if message.content.startswith('LightLupina'):
		return

		###########################
		######### mammont ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mam','FeuMam']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556260046667777/MaroudonR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#326 Mammont (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556260046667777/MaroudonR_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Rec +30~35%\n**Passif**: Provocation 80% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 35313\n**Attaque**: 2364\n**Défense**: 2092\n**Récupération**:2017", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mam','EauMam','TopMam']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556255621939201/Maroudon_Large.jpeg", color=0xffffff)
		embed.set_author(name="#327 Mammont (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556255621939201/Maroudon_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Rec +30~35%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 22793\n**Attaque**: 3126\n**Défense**: 1989\n**Récupération**:2138", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mam','BoisMam']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556258184527873/MaroudonG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#328 Mammont (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556258184527873/MaroudonG_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Rec +30~35%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 30134\n**Attaque**: 1907\n**Défense**: 3173\n**Récupération**:2220", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mam','LightMam']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556267126652931/MaroudonW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#329 Mammont (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556267126652931/MaroudonW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Rec +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 80% 2 tours\n(No skillbooks)\n**PV**: 34115\n**Attaque**: 2253\n**Défense**: 2195\n**Récupération**:2059", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mam','DarkMam']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556256762658816/MaroudonD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#330 Mammont (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556256762658816/MaroudonD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Rec +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 30611\n**Attaque**: 3017\n**Défense**: 1982\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mandragore ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mand','FeuMand','TopMand']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556758892281870/MoonflowerR_large.jpeg", color=0xffffff)
		embed.set_author(name="#331 Mandragore (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556758892281870/MoonflowerR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Sommeil (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Chasseur 30%\n(Dmg +20%)\n**PV**: 29385\n**Attaque**: 2608\n**Défense**: 1886\n**Récupération**:1559", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mand','EauMand']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556750818115585/MoonflowerB_large.jpeg", color=0xffffff)
		embed.set_author(name="#332 Mandragore (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556750818115585/MoonflowerB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%,(Même élément)\n**Passif**: Fatigue 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Récupération réduite 60% 2 tours\n(Dmg +10%, Taux: +10%, tour: +1)\n**PV**: 26838\n**Attaque**: 2622\n**Défense**: 1512\n**Récupération**:1580", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mand','BoisMand']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556750705000448/Moonflower_large.jpeg", color=0xffffff)
		embed.set_author(name="#333 Mandragore (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556750705000448/Moonflower_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Nécrose 60% 1 tour\n(Dmg +10%, Taux: +10%, tour: +1)\n**Actif**: Sommeil 40% 1 tour\n(Taux: +30%)\n**PV**: 29603\n**Attaque**: 1430\n**Défense**: 2833\n**Récupération**:1702", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mand','LightMand']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556759823155220/MoonflowerW_large.jpeg", color=0xffffff)
		embed.set_author(name="#334 Mandragore (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556759823155220/MoonflowerW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Nécrose x3 90% 1 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30611\n**Attaque**: 1907\n**Défense**: 3439\n**Récupération**:2159", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mand','DarkMand']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556754228084739/MoonflowerD_large.jpeg", color=0xffffff)
		embed.set_author(name="#335 Mandragore (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556754228084739/MoonflowerD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 30441\n**Attaque**: 3187\n**Défense**: 1880\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### végédalle ##################
		###########################

	if any([message.content.startswith (item) for item in ['Vege','FeuVege']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556196398366720/VégédalleR_large.jpeg", color=0xffffff)
		embed.set_author(name="#336 Végédalle (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556196398366720/VégédalleR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**PV**: 27049\n**Attaque**: 2527\n**Défense**: 1403\n**Récupération**:1478", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vege','EauVege']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556173111590966/VégédalleB_large.jpeg", color=0xffffff)
		embed.set_author(name="#337 Végédalle (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556173111590966/VégédalleB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Sommeil 60% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 36675\n**Attaque**: 1710\n**Défense**: 1206\n**Récupération**:1343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vege','BoisVege']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556172411142144/Végédalle_large.jpeg", color=0xffffff)
		embed.set_author(name="#338 Végédalle (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556172411142144/Végédalle_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 29334\n**Attaque**: 1933\n**Défense**: 1895\n**Récupération**:1691", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mari ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mari','FeuMari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551483875524614/AriaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#341 Mari (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551483875524614/AriaR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(No skillbooks)\n**PV**: 20219\n**Attaque**: 3037\n**Défense**: 2036\n**Récupération**:1559", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mari','EauMari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551473771184149/Aria_Large.jpeg", color=0xffffff)
		embed.set_author(name="#342 Mari (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551473771184149/Aria_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Attaque réduite 70% 1 tour\n(No skillbooks)\n**PV**: 28749\n**Attaque**: 2521\n**Défense**: 2473\n**Récupération**:2432", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mari','BoisMari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557213757726785557/AriaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#343 Mari (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557213757726785557/AriaG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite (On crit) 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 70% 2 tours\n(No skillbooks)\n**PV**: 26825\n**Attaque**: 2581\n**Défense**: 1907\n**Récupération**:1607", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mari','LightMari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551487277105152/AriaW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#344 Mari (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551487277105152/AriaW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Agression (Def)\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 27649\n**Attaque**: 2009\n**Défense**: 3568\n**Récupération**:1989", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mari','DarkMari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557587010664267789/AriaD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#345 Mari (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557587010664267789/AriaD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Vague martiale\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 29549\n**Attaque**: 3092\n**Défense**: 2118\n**Récupération**:2009", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### médusa ##################
		###########################

	if any([message.content.startswith (item) for item in ['Medusa','FeuMedusa','TopMedusa']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559575547641887/Sthenno_large.jpeg", color=0xffffff)
		embed.set_author(name="#346 Médusa (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559575547641887/Sthenno_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Pétrification 60% 1 tour\n(No skillbooks)\n**PV**: 34523\n**Attaque**: 1642\n**Défense**: 1942\n**Récupération**:1336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusa','EauMedusa']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559577225363477/SthennoB_large.jpeg", color=0xffffff)
		embed.set_author(name="#347 Médusa (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559577225363477/SthennoB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Sommeil 80% 1 tour\n(No skillbooks)\n**Actif**: Soif 60% -10% 1 tour\n(No skillbooks)\n**PV**: 30403\n**Attaque**: 2049\n**Défense**: 2025\n**Récupération**:1225", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusa','BoisMedusa']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559581746954240/SthennoG_large.jpeg", color=0xffffff)
		embed.set_author(name="#348 Médusa (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559581746954240/SthennoG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Nécrose 60% 3 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 1 tour\n(No skillbooks)\n**PV**: 29732\n**Attaque**: 1580\n**Défense**: 2472\n**Récupération**:1811", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusa','LightMedusa']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559604802912307/SthennoW_large.jpeg", color=0xffffff)
		embed.set_author(name="#349 Médusa (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559604802912307/SthennoW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Étourdissement (On crit) 1 tour\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27546\n**Attaque**: 2956\n**Défense**: 2288\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Medusa','DarkMedusa']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559579305869332/SthennoD_large.jpeg", color=0xffffff)
		embed.set_author(name="#350 Médusa (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559579305869332/SthennoD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Même élément)\n**Passif**: Aveuglement 70% 2 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 36056\n**Attaque**: 1942\n**Défense**: 2432\n**Récupération**:2010", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mera ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mera','FeuMera','TopMera']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552527086878733/Chimaira_large.jpeg", color=0xffffff)
		embed.set_author(name="#351 Mera (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552527086878733/Chimaira_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%)\n**PV**: 26212\n**Attaque**: 3187\n**Défense**: 2261\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mera','EauMera']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552530798968832/ChimairaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#352 Mera (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552530798968832/ChimairaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Sceau 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 24445\n**Attaque**: 2812\n**Défense**: 2828\n**Récupération**:2658", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mera','BoisMera']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552561224187918/ChimairaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#353 Mera (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552561224187918/ChimairaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Fatigue 80% 3 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg +25%)\n**PV**: 36757\n**Attaque**: 2228\n**Défense**: 1881\n**Récupération**:2051", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mera','LightMera']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552562847383554/ChimairaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#354 Mera (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552562847383554/ChimairaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Sceau 60% 2 tours\n(Dmg  +15%, Taux: +15%)\n**PV**: 30822\n**Attaque**: 2043\n**Défense**: 2962\n**Récupération**:2322", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mera','DarkMera']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552558334443521/ChimairaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#355 Mera (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552558334443521/ChimairaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Récupération réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 100% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 39059\n**Attaque**: 1853\n**Défense**: 2303\n**Récupération**:2187", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### merlin ##################
		###########################

	if any([message.content.startswith (item) for item in ['Merl','FeuMerl']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556391848476672/MerlinusR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#356 Merlin (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556391848476672/MerlinusR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25% \n**Passif**: Boost de moral 50% de ses PA\n(Dmg +20%, +Effect.: +10%)\n**Actif**: Chasseur 50%%\n(Dmg +30%)\n**PV**: 28037\n**Attaque**: 3398\n**Défense**: 2554\n**Récupération**:2384", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Merl','EauMerl']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556388795023365/Merlinus_Large.jpeg", color=0xffffff)
		embed.set_author(name="#357 Merlin (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556388795023365/Merlinus_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist -20~25%\n**Passif**: Boost de moral (Allies) 15% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 31537\n**Attaque**: 3494\n**Défense**: 2213\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Merl','BoisMerl','TopMerl']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556390053576734/MerlinusG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#358 Merlin (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556390053576734/MerlinusG_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Frappe Courageuse\n(Dmg +30%)\n**Actif**: Frappe Courageuse\n(Dmg +30%)\n**PV**: 31037\n**Attaque**: 2982\n**Défense**: 2787\n**Récupération**:2576", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Merl','LightMerl']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556393345974282/MerlinusW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#359 Merlin (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556393345974282/MerlinusW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Resist -20~25%\n**Passif**: Choc 70% 2 tours\n(Dmg: +15% Taux: +10%)\n**Actif**: Avantage élémentaire\n(Dmg: +30%)\n**PV**: 32222\n**Attaque**: 3213\n**Défense**: 2924\n**Récupération**:1977", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Merl','DarkMerl']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556388769988608/MerlinusD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#360 Merlin (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556388769988608/MerlinusD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist -20~25%\n**Passif**: Siphon de PA 30%\n(Dmg +15%, Taux: +5%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 40298\n**Attaque**: 2398\n**Défense**: 2834\n**Récupération**:1996", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### miho ##################
		###########################

	if any([message.content.startswith (item) for item in ['Miho','FeuMiho','TopMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554848990789667/Horan_large.jpeg", color=0xffffff)
		embed.set_author(name="#361 Miho (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554848990789667/Horan_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%, Taux: +20%)\n**PV**: 37363\n**Attaque**: 2180\n**Défense**: 1806\n**Récupération**:1397", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','EauMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554851318628373/HoranB_large.jpeg", color=0xffffff)
		embed.set_author(name="#363 Miho (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554851318628373/HoranB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Nécrose 100% 2 tours\n(Dmg +30%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 31234\n**Attaque**: 2096\n**Défense**: 2072\n**Récupération**:1827", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','BoisMiho','TopMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554855798013974/HoranG_large.jpeg", color=0xffffff)
		embed.set_author(name="#365 Miho (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554855798013974/HoranG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28207\n**Attaque**: 2676\n**Défense**: 1798\n**Récupération**:1900", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','LightMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554858708860949/HoranW_large.jpeg", color=0xffffff)
		embed.set_author(name="#367 Miho (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554858708860949/HoranW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Attaque réduite 60% 3 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 31701\n**Attaque**: 2023\n**Défense**: 3085\n**Récupération**:2329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','DarkMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554853897994253/HoranD_large.jpeg", color=0xffffff)
		embed.set_author(name="#370 Miho (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554853897994253/HoranD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Agression (PV)\n(Dmg: +20%)\n**Actif**: Agression (PV)\n(Dmg: +20%)\n**PV**: 37261\n**Attaque**: 1806\n**Défense**: 2303\n**Récupération**: 2167", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### miho S Evo ##################
		###########################

	if any([message.content.startswith (item) for item in ['Miho','FeuMiho','SMiho','FeuSMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559814811713548/SuperHoran_large.jpeg", color=0xffffff)
		embed.set_author(name="#362 Miho SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559814811713548/SuperHoran_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +20%, Taux: +20%)\n**PV**: 41265\n**Attaque**: 2398\n**Défense**: 1990\n**Récupération**:1540", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','EauMiho','SMiho','EauSMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559818963943445/SuperHoranB_large.jpeg", color=0xffffff)
		embed.set_author(name="#364 Miho SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559818963943445/SuperHoranB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Nécrose 100% 2 tours\n(Dmg +30%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 34380\n**Attaque**: 2318\n**Défense**: 2289\n**Récupération**:2024", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','BoisMiho','SMiho','BoisSMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559824123199498/SuperHoranG_large.jpeg", color=0xffffff)
		embed.set_author(name="#366 Miho SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559824123199498/SuperHoranG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 31033\n**Attaque**: 2976\n**Défense**: 1982\n**Récupération**:2097", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','LightMiho','SMiho','LightSMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559829718401036/SuperHoranW_large.jpeg", color=0xffffff)
		embed.set_author(name="#368 Miho SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559829718401036/SuperHoranW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Resist +15~20%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Attaque réduite 60% 3 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 34881\n**Attaque**: 2234\n**Défense**: 3425\n**Récupération**:2567", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Miho','DarkMiho','SMiho','DarkSMiho']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559821338050580/SuperHoranD_large.jpeg", color=0xffffff)
		embed.set_author(name="#371 Miho SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559821338050580/SuperHoranD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Agression (PV)\n(no skillbooks)\n**Actif**: Agression (PV)\n(no skillbooks)\n**PV**: 41156\n**Attaque**: 1990\n**Défense**: 2535\n**Récupération**: 2385", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mildeu ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mild','FeuMild']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554096197107733/FungusR_large.jpeg", color=0xffffff)
		embed.set_author(name="#371 Mildeu (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554096197107733/FungusR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Nécrose 60% 1 tour\n\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 26498\n**Attaque**: 1730\n**Défense**: 1444\n**Récupération**:2485", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mild','EauMild']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554093449838602/FungusB_large.jpeg", color=0xffffff)
		embed.set_author(name="#372 Mildeu (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554093449838602/FungusB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Rec +20~25%\n**Passif**: Brise bouclier 100%\n(No skillbooks)\n**Actif**: Défense augmentée 3 tours\n(No skillbooks)\n**PV**: 25953\n**Attaque**: 1614\n**Défense**: 2343\n**Récupération**:1771", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mild','BoisMild']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554090236870676/Fungus_large.jpeg", color=0xffffff)
		embed.set_author(name="#373 Mildeu (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554090236870676/Fungus_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Purification 100%\n(No skillbooks)\n**PV**: 28003\n**Attaque**: 1342\n**Défense**: 1702\n**Récupération**:2697", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mild','LightMild']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554098432540672/FungusW_large.jpeg", color=0xffffff)
		embed.set_author(name="#374 Mildeu (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554098432540672/FungusW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Rec +20~25%\n**Passif**: Adrénaline 10% de ses PV (Allies)\n(No skillbooks)\n**Actif**: Domination 3 tours\n(No skillbooks)\n**PV**: 27975\n**Attaque**: 1491\n**Défense**: 2499\n**Récupération**:1485", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mild','DarkMild']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554093772537887/FungusD_large.jpeg", color=0xffffff)
		embed.set_author(name="#375 Mildeu (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554093772537887/FungusD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Récupération\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Bouclier (Flat) 2 tours \n(No skillbooks)\n**PV**: 24768\n**Attaque**: 1777\n**Défense**: 1662\n**Récupération**:2574", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mimic ##################
		###########################

	if any([message.content.startswith (item) for item in ['Mimi','FeuMimi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554274010169364/GoldmickR_large.jpeg", color=0xffffff)
		embed.set_author(name="#376 Mimic (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554274010169364/GoldmickR_large.jpeg")
		embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Provocation 20% 1 tour\n(No skillbooks)\n**Actif**: Provocation 60% 1 tour\n(No skillbooks)\n**PV**: 26246\n**Attaque**: 2206\n**Défense**: 1607\n**Récupération**:1559", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mimi','EauMimi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554270839537664/GoldmickB_large.jpeg", color=0xffffff)
		embed.set_author(name="#377 Mimic (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554270839537664/GoldmickB_large.jpeg")
		embed.add_field(name="★", value="**Type**: Tank\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 38555\n**Attaque**: 1193\n**Défense**: 1792\n**Récupération**:1343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mimi','BoisMimi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554264698945567/Goldmick_large.jpeg", color=0xffffff)
		embed.set_author(name="#378 Mimic (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554264698945567/Goldmick_large.jpeg")
		embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 28881\n**Attaque**: 1668\n**Défense**: 2404\n**Récupération**:1273", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mimi','LightMimi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554275079847937/GoldmickW_large.jpeg", color=0xffffff)
		embed.set_author(name="#379 Mimic (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554275079847937/GoldmickW_large.jpeg")
		embed.add_field(name="★", value="**Type**: Récupération\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Récupération réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Récupération réduite 60% 2 tours\n(No skillbooks)\n**PV**: 27955\n**Attaque**: 1403\n**Défense**: 1662\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mimi','DarkMimi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554271824936962/GoldmickD_large.jpeg", color=0xffffff)
		embed.set_author(name="#380 Mimic (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554271824936962/GoldmickD_large.jpeg")
		embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: TC +10~15%(Donjons)\n**Passif**: Fatigue 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 60% 2 tours\n(No skillbooks)\n**PV**: 27816\n**Attaque**: 1831\n**Défense**: 1664\n**Récupération**:1534", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### chapillon ##################
		###########################

	if any([message.content.startswith (item) for item in ['Chapi','FeuChapi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556529417715737/ChapillonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#381 Chapillon (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556529417715737/ChapillonR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg: +10% Taux: +20%)\n**Actif**: Purification 100%\n(Dmg: +30%)\n**PV**: 35279\n**Attaque**: 1744\n**Défense**: 1452\n**Récupération**: 1642", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chapi','EauChapi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556527693725707/ChapillonB_large.jpeg", color=0xffffff)
		embed.set_author(name="#382 Chapillon (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556527693725707/ChapillonB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Boost de moral 30% de ses PA\n(???)\n**Actif**: Bouclier (Flat) 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 28561\n**Attaque**: 1648\n**Défense**: 1525\n**Récupération**: 2595", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Chapi','BoisChap','TopChapi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556526770847754/Chapillon_large.jpeg", color=0xffffff)
		embed.set_author(name="#383 Chapillon (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556526770847754/Chapillon_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Rec +30~35% (ToC)\n**Passif**: Faiblesse exposée 80% 1 tour\n(???)\n**Actif**: Attaque augmentée  2 tours\n(???)\n**PV**: 23563\n**Attaque**: 1818\n**Défense**: 1668\n**Récupération**: 2663", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mini camilla ##################
		###########################

	if any([message.content.startswith (item) for item in ['MiniC','LightMiniC','Minicam','LightMinicam','Camilla','LightCami']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728588644974592/MiniCamilla3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#389 Mini Camilla (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728588644974592/MiniCamilla3Evo_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Choc 80% 1 tour\n(no skillbooks)\n**Actif**: Faiblesse exposée 80% 1 tours\n(no skillbooks)\n**PV**: 40046\n**Attaque**: 2105\n**Défense**: 2242\n**Récupération**: 2037", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['MiniC','DarkMiniC','Minicam','DarkMinicam','Camilla','DarkCami']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728590691794954/MiniCamilla3EvoD_large.jpg", color=0xffffff)
		embed.set_author(name="#390 Mini Camilla (dark)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728590691794954/MiniCamilla3EvoD_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Siphon de PA 25%\n(no skillbooks)\n**Actif**: Agression (PV)\n(no skillbooks)\n**PV**: 41272\n**Attaque**: 2119\n**Défense**: 2167\n**Récupération**: 1983", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mini seira ##################
		###########################

	if any([message.content.startswith (item) for item in ['MiniS','LightMiniS','Minis','LightMinis','Seira','LightSeira']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557103714402306/NavigatorSeira_large.jpeg", color=0xffffff)
		embed.set_author(name="#394 Mini Seira light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557103714402306/NavigatorSeira_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24216\n**Attaque**: 3425\n**Défense**: 2390\n**Récupération**:2479", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['MiniS','DarkMiniS','Minis','DarkMinis','Seira','DarkSeira']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557106322997249/NavigatorSeiraD_large.jpeg", color=0xffffff)
		embed.set_author(name="#395 Mini Seira (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557106322997249/NavigatorSeiraD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24216\n**Attaque**: 3425\n**Défense**: 2390\n**Récupération**:2479", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mini tina ##################
		###########################

	if any([message.content.startswith (item) for item in ['MiniT','LightMiniT','Minit','LightMinit','Tina','LightTina']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557596216792317967/GemsmithTina_large.jpeg", color=0xffffff)
		embed.set_author(name="#399 Mini Tina (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557596216792317967/GemsmithTina_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +30%)\n**Actif**: Avantage élémentaire\n(Dmg +30%)\n**PV**: 21492\n**Attaque**: 3357\n**Défense**: 2384\n**Récupération**:2853", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['MiniT','DarkMiniT','Minit','DarkMinit','Tina','DarkTina']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554235573698591/GemsmithTinaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#400 Mini Tina (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554235573698591/GemsmithTinaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Chasseur 40%\n(Dmg +35%)\n**PV**: 24816\n**Attaque**: 3378\n**Défense**: 2479\n**Récupération**:2384", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Mini Zephyros ############
		#######################################

	if any([message.content.startswith (item) for item in ['Mini Zephyros','DarkMiniZephy','DarkZephyr','Zephyr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569194846879904/Screenshot_20200907-183823_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#1002 Mini Zephyros (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569194846879904/Screenshot_20200907-183823_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Taux critique 15-20%\n**Passif**: Vague martiale 20% PA/PV\n(Dmg +20%, taux +5%)\n**Actif**: Persévérance\n(Dmg +25%)\n**PV**: 26811\n**Attaque**: 3473\n**Défense**: 2377\n**Récupération**:1941", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mini Zephyros','LightMiniZephy','LightZephyr','Zephyr']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569194465460254/Screenshot_20200907-183711_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#1003 Mini Zephyros (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569194465460254/Screenshot_20200907-183711_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Taux critique 15-20%\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +30%)\n**Actif**: Choc 60% 2 tours\n(Dmg +20%, Taux +10%)\n**PV**: 40639\n**Attaque**: 1928\n**Défense**: 2432\n**Récupération**:2044", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mino ############
		###########################

	if any([message.content.startswith (item) for item in ['Mino','FeuMino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560144970416130/TaurusR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#401 Mino (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560144970416130/TaurusR_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (bois) 100%\n(No skillbooks)\n**PV**: 24713\n**Attaque**: 2452\n**Défense**: 1682\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mino','EauMino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560130055602189/Taurus_Large.jpeg", color=0xffffff)
		embed.set_author(name="#402 Mino (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560130055602189/Taurus_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Feu Chasseur 100%\n(No skillbooks)\n**PV**: 25885\n**Attaque**: 2370\n**Défense**: 1498\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mino','BoisMino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560142860681264/TaurusG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#403 Mino (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560142860681264/TaurusG_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (eau) 100%\n(No skillbooks)\n**PV**: 26246\n**Attaque**: 2172\n**Défense**: 1696\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mino','LightMino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560164453089280/TaurusW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#404 Mino (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560164453089280/TaurusW_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (dark) 100%\n(No skillbooks)\n**PV**: 22384\n**Attaque**: 2642\n**Défense**: 1539\n**Récupération**:1702", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mino','DarkMino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560140684099587/TaurusD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#405 Mino (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560140684099587/TaurusD_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Rec +20~25%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(No skillbooks)\n**Actif**: Chasseur (light) 100%\n(No skillbooks)\n**PV**: 29188\n**Attaque**: 2336\n**Défense**: 1308\n**Récupération**:1498", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### misha ############
		###########################

	if any([message.content.startswith (item) for item in ['Mish','FeuMish']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558515118538756/Runeclaw_large.jpeg", color=0xffffff)
		embed.set_author(name="#406 Misha (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558515118538756/Runeclaw_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Adrénaline 30% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 35395\n**Attaque**: 1922\n**Défense**: 1622\n**Récupération**:1486", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mish','EauMish']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558529266057278/RuneclawB_large.jpeg", color=0xffffff)
		embed.set_author(name="#407 Misha (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558529266057278/RuneclawB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Nécrose x2 50% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Frappe impitoyable\n(Dmg +30%)\n**PV**: 29293\n**Attaque**: 2083\n**Défense**: 2011\n**Récupération**:1732", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mish','BoisMish']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558532088561695/RuneclawG_large.jpeg", color=0xffffff)
		embed.set_author(name="#408 Misha (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558532088561695/RuneclawG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Provocation 80% 1 tour\n(Dmg +30%)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25476\n**Attaque**: 1866\n**Défense**: 2969\n**Récupération**:1512", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mish','LightMish']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558534160678935/RuneclawW_large.jpeg", color=0xffffff)
		embed.set_author(name="#409 Misha (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558534160678935/RuneclawW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35% (Même élément)\n**Passif**: Vague martiale 20% (On crit)\n(Dmg +30%)\n**Actif**: Choc 70%(On crit) 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 40312\n**Attaque**: 2221\n**Défense**: 2364\n**Récupération**:1874", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mish','DarkMish']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558521913311242/RuneclawD_large.jpeg", color=0xffffff)
		embed.set_author(name="#410 Misha (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558521913311242/RuneclawD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%(Même élément)\n**Passif**: Vengeance\n(Dmg +35%)\n**Actif**: Vengeance\n(Dmg +35%)\n**PV**: 26287\n**Attaque**: 2663\n**Défense**: 3105\n**Récupération**:2009", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### taupinou ############
		###########################
	if any([message.content.startswith (item) for item in ['Taup','FeuTaup']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#411 Taupinou (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV Rec +10~15%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 28731\n**Attaque**: 1709\n**Défense**: 2486\n**Récupération**:1192", inline=False)

		await message.channel.send(embed=embed)
		###########################     

	if any([message.content.startswith (item) for item in ['Taup','EauTaup']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553564493578270/DrillmonB_large.jpeg", color=0xffffff)
		embed.set_author(name="#412 Taupinou (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553564493578270/DrillmonB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV Rec +10~15%\n**Passif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 36069\n**Attaque**: 1622\n**Défense**: 1329\n**Récupération**:1506", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Taup','BoisTaup']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553561985122337/Drillmon_large.jpeg", color=0xffffff)
		embed.set_author(name="#413 Taupinou (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553561985122337/Drillmon_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV Rec +10~15%\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 28857\n**Attaque**: 1831\n**Défense**: 1637\n**Récupération**:1596", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Taup','FeuTaup']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#411 Taupinou (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553566196203520/DrillmonR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV Rec +10~15%\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 1 tour\n(No skillbooks)\n**PV**: 28731\n**Attaque**: 1709\n**Défense**: 2486\n**Récupération**:1192", inline=False)

		await message.channel.send(embed=embed)

		###########################
		######### mona ############
		###########################

	if any([message.content.startswith (item) for item in ['Mona','FeuMona','mona','MonaFeu', 'MonaF']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556697726746634/MonArchh_large.jpeg", color=0xffffff)
		embed.set_author(name="#416 Mona (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556697726746634/MonArchh_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank \n**Lead**: Att +30~35% (Même élément)\n**Passif**: Siphon de PA 20%\n(dmg +20%, Taux : +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 42627\n**Attaque**: 1431\n**Défense**: 1785\n**Récupération**:1411", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaEau','EauMona', 'MonaE', 'TopMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556704307347466/MonArchhB_large.jpeg", color=0xffffff)
		embed.set_author(name="#417 Mona (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556704307347466/MonArchhB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 25081\n**Attaque**: 2853\n**Défense**: 2016\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaBois','BoisMona', 'MonaB']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214074111262720/MonArchhG_large.jpeg", color=0xffffff)
		embed.set_author(name="#418 Mona (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214074111262720/MonArchhG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 27860\n**Attaque**: 1491\n**Défense**: 2554\n**Récupération**:1839", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona', 'mona', 'MonaLight','LightMona', 'MonaL']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556709810274319/MonArchhW_large.jpeg", color=0xffffff)
		embed.set_author(name="#419 Mona (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556709810274319/MonArchhW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 25% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Agression (Def)\n(Dmg +40%)\n**PV**: 30686\n**Attaque**: 2486\n**Défense**: 3255\n**Récupération**:1771", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona','mona', 'MonaDark', 'MonaD','DarkMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556707352412185/MonArchhD_large.jpeg", color=0xffffff)
		embed.set_author(name="#420 Mona (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556707352412185/MonArchhD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Chasseur(Dc) 30%\n(Dmg +25%, +Effect.: +10%)\n**PV**: 28030\n**Attaque**: 3391\n**Défense**: 2070\n**Récupération**:2077", inline=False)

		await message.channel.send(embed=embed)

		###################################
		########### Mona S Evo ############
		###################################


	if any([message.content.startswith (item) for item in ['Mona','mona','FeuMona','MonaF','MonaFeu','SMonaF','SMona','FeuSMona','SMonaFeu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222143410236/Screenshot_20200907-183956_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#362 Mona SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222143410236/Screenshot_20200907-183956_Monster_Super_League.jpg")
		embed.add_field(name="★★★", value="**Type**: Tank \n**Lead**: Att +30~35% (Même élément)\n**Passif**: Siphon de PA 20%\n(dmg +20%, Taux : +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**PV**: 47053\n**Attaque**: 1474\n**Défense**: 1969\n**Récupération**:1554", inline=False)

		await message.channel.send(embed=embed)     

	if any([message.content.startswith (item) for item in ['Mona','mona','MonaEau','MonaE','EauMona','SMonaE','Smona','SmonaEau','EauSMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569221883363409/Screenshot_20200907-183923_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#364 Mona SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569221883363409/Screenshot_20200907-183923_Monster_Super_League.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 27594\n**Attaque**: 3173\n**Défense**: 2227\n**Récupération**:1811", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona','mona','MonaBois','MonaB','BoisMona','SMonaB','Smona','SmonaBois','BoisSMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222294536274/Screenshot_20200907-184021_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#366 Mona SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222294536274/Screenshot_20200907-184021_Monster_Super_League.jpg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Provocation intrépide 80% 1 tour\n(???)\n**PV**: 30652\n**Attaque**: 1648\n**Défense**: 2840\n**Récupération**:2029", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona','mona','MonaLight','MonaL','LightMona','SMonaL','Smona','SmonaLight','LightSMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222491799573/Screenshot_20200907-184043_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#368 Mona SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222491799573/Screenshot_20200907-184043_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Adrénaline 25% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Agression (Def)\n(Dmg +40%)\n**PV**: 33764\n**Attaque**: 2744\n**Défense**: 3609\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mona','mona','MonaDark','MonaD','DarkMona','SMonaD','Smona','SmonaDark','DarkSMona']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/752449210422525962/752569222772555816/Screenshot_20200907-184103_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#371 Mona SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752449210422525962/752569222772555816/Screenshot_20200907-184103_Monster_Super_League.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Chasseur(Dc) 30%\n(Dmg +25%, +Effect.: +10%)\n**PV**: 30842\n**Attaque**: 3759\n**Défense**: 2281\n**Récupération**:2295", inline=False)

		await message.channel.send(embed=embed)     

		###################################
		############ Monkiki ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Monk','FeuMonk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552082805358612/Bluemong_large.jpeg", color=0xffffff)
		embed.set_author(name="#421 Monkiki (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552082805358612/Bluemong_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +25~30%\n**Passif**: Sommeil (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Sommeil (On crit) 2 tours\n(Dmg +25%)\n**PV**: 27676\n**Attaque**: 2867\n**Défense**: 1914\n**Récupération**:1382", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Monk','EauMonk','TopMonkiki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552085267283968/BluemongB_large.jpeg", color=0xffffff)
		embed.set_author(name="#422 Monkiki (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552085267283968/BluemongB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +25~30%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**Actif**: Soif 80% -10% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 28697\n**Attaque**: 1852\n**Défense**: 2588\n**Récupération**:1328", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Monk','BoisMonk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552097451737091/BluemongG_large.jpeg", color=0xffffff)
		embed.set_author(name="#423 Monkiki (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552097451737091/BluemongG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Att +25~30%\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +10%, Taux: +20%, tour: +1)\n**Actif**: Étourdissement 100% 1 tour\n(Dmg +25%)\n**PV**: 28476\n**Attaque**: 1892\n**Défense**: 1963\n**Récupération**:1725", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Monk','LightMonk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552099897147403/BluemongW_large.jpeg", color=0xffffff)
		embed.set_author(name="#424 Monkiki (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552099897147403/BluemongW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +25~30%\n**Passif**: Chasseur 50%\n(Dmg +20%)\n**Actif**: Aveuglement (On crit) 3 tours\n(Dmg +25%)\n**PV**: 26917\n**Attaque**: 2662\n**Défense**: 2658\n**Récupération**:2488", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Monk','DarkMonk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552088807276544/BluemongD_large.jpeg", color=0xffffff)
		embed.set_author(name="#425 Monkiki (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552088807276544/BluemongD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +25~30%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Défense 100% 2 tours\n(Dmg +15%, tour: +1)\n**PV**: 28731\n**Attaque**: 1941\n**Défense**: 3167\n**Récupération**:2309", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Mowgli ###############
		################################### 

	if any([message.content.startswith (item) for item in ['Mowg','FeuMowg','TopMowg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556868510285825/MowgliaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#426 Mowgli (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556868510285825/MowgliaR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (bois) 50%\n(Dmg +25%)\n**Actif**: Prédateur (bois) 40%\n(Dmg +25%)\n**PV**: 26900\n**Attaque**: 2717\n**Défense**: 1525\n**Récupération**:1580", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mowg','EauMowg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557085313859602/MowgliaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#427 Mowgli (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557085313859602/MowgliaB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Feu Chasseur 50%\n(Dmg +25%)\n**Actif**: Prédateur (feu) 40%\n(Dmg +25%)\n**PV**: 28670\n**Attaque**: 2615\n**Défense**: 1648\n**Récupération**:1566", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mowg','BoisMowg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556869877760002/Mowglia_large.jpeg", color=0xffffff)
		embed.set_author(name="#428 Mowgli (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556869877760002/Mowglia_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (eau) 50%\n(Dmg +25%)\n**Actif**: Prédateur (eau) 40%\n(Dmg +25%)\n**PV**: 26900\n**Attaque**: 2847\n**Défense**: 1532\n**Récupération**:1580", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mowg','LightMowg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556869768445972/MowgliaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#429 Mowgli (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556869768445972/MowgliaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (dark) 40%\n(Dmg +25%)\n**Actif**: Prédateur (dark) 30%\n(Dmg +25%)\n**PV**: 28016\n**Attaque**: 3133\n**Défense**: 2036\n**Récupération**:1989", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Mowg','DarkMowg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556868711743510/MowgliaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#430 Mowgli (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556868711743510/MowgliaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Même élément)\n**Passif**: Chasseur (light) 40%\n(Dmg +25%)\n**Actif**: Prédateur (light) 30%\n(Dmg +25%)\n**PV**: 27288\n**Attaque**: 3085\n**Défense**: 2193\n**Récupération**:1968", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ champi ###############
		################################### 

	if any([message.content.startswith (item) for item in ['Champ','FeuChamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559527850147843/SporeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#431 Champi (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559527850147843/SporeR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Provocation 100% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 29092\n**Attaque**: 1321\n**Défense**: 2540\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Champ','EauChamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559525757190164/SporeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#432 Champi (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559525757190164/SporeB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Provocation 40% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Prédateur (eau) 20%\n(Dmg +20%)\n**PV**: 28054\n**Attaque**: 1879\n**Défense**: 1725\n**Récupération**:1555", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Champ','BoisChamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559523706044417/Spore_large.jpeg", color=0xffffff)
		embed.set_author(name="#433 Champi (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559523706044417/Spore_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 23862\n**Attaque**: 2785\n**Défense**: 1702\n**Récupération**:1662", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Nezha ###############
		################################### 


	if any([message.content.startswith (item) for item in ['Nez','FeuNez','TopNez']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556889733464064/Nalakuvara_large.jpeg", color=0xffffff)
		embed.set_author(name="#436 Nezha (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556889733464064/Nalakuvara_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 70% 3 tours\n(No skillbooks)\n**PV**: 38643\n**Attaque**: 2323\n**Défense**: 1806\n**Récupération**:1922", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Nez','EauNez','TopNez']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557093924765706/NalakuvaraB_large.jpeg", color=0xffffff)
		embed.set_author(name="#437 Nezha (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557093924765706/NalakuvaraB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 70% 2 tours\n(No skillbooks)\n**PV**: 30199\n**Attaque**: 2444\n**Défense**: 2542\n**Récupération**:2774", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Nez','BoisNez']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557099780145163/NalakuvaraG_large.jpeg", color=0xffffff)
		embed.set_author(name="#438 Nezha (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557099780145163/NalakuvaraG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Sceau 60% 1 tour\n(No skillbooks)\n**PV**: 27696\n**Attaque**: 3092\n**Défense**: 2329\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Nez','LightNez']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214207414894632/Nalakuvaraw_large.jpeg", color=0xffffff)
		embed.set_author(name="#439 Nezha (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214207414894632/Nalakuvaraw_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Aveuglement 80% 3 tours\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**PV**: 38752\n**Attaque**: 1853\n**Défense**: 2323\n**Récupération**:2133", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Nez','DarkNez']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552557097187803167/NalakuvaraD_large.jpeg", color=0xffffff)
		embed.set_author(name="#440 Nezha (dark)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552557097187803167/NalakuvaraD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Siphon de PV , Greatly)\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 25640\n**Attaque**: 3153\n**Défense**: 2431\n**Récupération**:2111", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############## Nifa ###############
		################################### 

	if any([message.content.startswith (item) for item in ['Nif','LightNif']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551351289118721/Angelmon_Large.jpeg", color=0xffffff)
		embed.set_author(name="#444 Nifa (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551351289118721/Angelmon_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Chasseur 50%\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 25292\n**Attaque**: 3024\n**Défense**: 2288\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Nif','DarkNif']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551357824106537/AngelmonD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#445 Nifa (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551357824106537/AngelmonD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 47027\n**Attaque**: 1853\n**Défense**: 1915\n**Récupération**:1751", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Cauchemar ############
		################################### 

	if any([message.content.startswith (item) for item in ['Cauc','FeuCauc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557419897683968/NyxR_large.jpeg", color=0xffffff)
		embed.set_author(name="#446 Cauchemar (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557419897683968/NyxR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Soif 80% -30% 2 tours\n(No skillbooks)\n**PV**: 32000\n**Attaque**: 3616\n**Défense**: 2172\n**Récupération**:2424", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cauc','EauCauc','TopCauc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557413228609557/NyxB_large.jpeg", color=0xffffff)
		embed.set_author(name="#447 Cauchemar (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557413228609557/NyxB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Sceau 100% 3 tours\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 27247\n**Attaque**: 2601\n**Défense**: 3514\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cauc','BoisCauc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557418219962388/NyxG_large.jpeg", color=0xffffff)
		embed.set_author(name="#448 Cauchemar (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557418219962388/NyxG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**PV**: 26906\n**Attaque**: 2595\n**Défense**: 3602\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cauc','LightCauc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557421390856192/NyxW_large.jpeg", color=0xffffff)
		embed.set_author(name="#449 Cauchemar (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557421390856192/NyxW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Agression (Def)\n(Dmg +25%)\n**Actif**: Provocation intrépide 80% 2 tours\n(Dmg + 20%, Taux: +20%)\n**PV**: 32456\n**Attaque**: 2561\n**Défense**: 3875\n**Récupération**:2254", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cauc','DarkCauc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557389174538252/Nyx_large.jpeg", color=0xffffff)
		embed.set_author(name="#450 Cauchemar (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557389174538252/Nyx_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Boost de moral 40% de ses PA\n(No skillbooks)\n**Actif**: Sceau 80% 3 tours\n(No skillbooks)\n**PV**: 41143\n**Attaque**: 2316\n**Défense**: 2534\n**Récupération**:2916", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############## Odin ###############
		################################### 

	if any([message.content.startswith (item) for item in ['Odin','FeuOdin','TopOdin']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558094786363394/PrimeodinR_large.jpeg", color=0xffffff)
		embed.set_author(name="#451 Odin (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558094786363394/PrimeodinR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Défense réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 43077\n**Attaque**: 2010\n**Défense**: 3066\n**Récupération**:2432", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Odin','EauOdin','TopOdin']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558094077526026/PrimeodinB_large.jpeg", color=0xffffff)
		embed.set_author(name="#452 Odin (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558094077526026/PrimeodinB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +30%)\n**PV**: 25378\n**Attaque**: 3172\n**Défense**: 3155\n**Récupération**:3012", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Odin','BoisOdin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558094253555745/PrimeodinG_large.jpeg", color=0xffffff)
		embed.set_author(name="#453 Odin (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558094253555745/PrimeodinG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Siphon de PV ,  Greatly))\n(Dmg +25%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 28473\n**Attaque**: 3909\n**Défense**: 2595\n**Récupération**:2152", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Odin','LightOdin']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558098632540170/PrimeodinW_large.jpeg", color=0xffffff)
		embed.set_author(name="#454 Odin (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558098632540170/PrimeodinW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(Dmg +25%)\n**Actif**: Adrénaline (Allies) 10% de ses PV par mob attaqué\n(Dmg +25%)\n**PV**: 48048\n**Attaque**: 2099\n**Défense**: 2916\n**Récupération**:2677", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Odin','DarkOdin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558087924351006/Primeodin_large.jpeg", color=0xffffff)
		embed.set_author(name="#455 Odin (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558087924351006/Primeodin_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45%\n**Passif**: Vague martiale 20%\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Défense réduite 80% 3 tours\n(Dmg +25%)\n**PV**: 32024\n**Attaque**: 2975\n**Défense**: 2828\n**Récupération**:1889", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Onmyoji ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Onm','FeuOnm','TopOnm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558730898571288/SeimeiR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#456 Onmyoji (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558730898571288/SeimeiR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 80% 2 tours\n(Dmg +25%)\n**PV**: 37772\n**Attaque**: 2521\n**Défense**: 2705\n**Récupération**:2494", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Onm','EauOnm','TopOnm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558724070244352/Seimei_Large.jpeg", color=0xffffff)
		embed.set_author(name="#457 Onmyoji (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558724070244352/Seimei_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Chasseur 50%\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 31626\n**Attaque**: 3677\n**Défense**: 2070\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Onm','BoisOnm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558729330032651/SeimeiG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#458 Onmyoji (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558729330032651/SeimeiG_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Sceau 100% 2 tours\n(Dmg +30%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 29569\n**Attaque**: 2363\n**Défense**: 3562\n**Récupération**:2588", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Onm','LightOnm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558753854259201/SeimeiW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#459 Onmyoji (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558753854259201/SeimeiW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PA 30%%\n(Dmg +20%, Taux: +10%)\n**Actif**: Choc 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 25068\n**Attaque**: 2792\n**Défense**: 3609\n**Récupération**:2254", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Onm','DarkOnm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558727438401537/SeimeiD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#460 Onmyoji (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558727438401537/SeimeiD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Resist +20~25%\n**Passif**: Siphon de PV \n(Dmg +30%)\n**Actif**: Siphon de PV (Allies) Greatly\n(Dmg +30%)\n**PV**: 25878\n**Attaque**: 3698\n**Défense**: 2479\n**Récupération**:2452", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############## Otari ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Ota','FeuOta']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558815204212758/SelkieR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#461 Otari (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558815204212758/SelkieR_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 2 tours\n(No skillbooks)\n**PV**: 35048\n**Attaque**: 1635\n**Défense**: 1302\n**Récupération**:1486", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ota','EauOta']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558803640385584/Selkie_Large.jpeg", color=0xffffff)
		embed.set_author(name="#462 Otari (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558803640385584/Selkie_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Resistance réduite  100% 2 tours\n(Dmg: +30%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 28687\n**Attaque**: 1742\n**Défense**: 1854\n**Récupération**:1807", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ota','BoisOta']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558813245472771/SelkieG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#463 Otari (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558813245472771/SelkieG_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 28820\n**Attaque**: 1478\n**Défense**: 2336\n**Récupération**:1614", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ota','LightOta']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557607503815376906/SelkieW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#464 Otari (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557607503815376906/SelkieW_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 30%\n(No skillbooks)\n**PV**: 25667\n**Attaque**: 2574\n**Défense**: 1709\n**Récupération**:1614", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ota','DarkOta']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558799148285964/SelkieD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#465 Otari (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558799148285964/SelkieD_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Aveuglement 100% 2 tours\n(No skillbooks)\n**PV**: 28473\n**Attaque**: 1873\n**Défense**: 2724\n**Récupération**:1362", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############## Cayou ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Cayou','FeuCayou']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556020711292943/Magton_large.jpeg", color=0xffffff)
		embed.set_author(name="#466 Cayou (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556020711292943/Magton_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(No skillbooks)\n**Actif**: Provocation 80% 1 tour\n(No skillbooks)\n**PV**: 29773\n**Attaque**: 2240\n**Défense**: 3058\n**Récupération**:1852", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Pégase ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Pega','FeuPega']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551852319703080/BellerophonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#471 Pégase (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551852319703080/BellerophonR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Chasseur 40%\n(No skillbooks)\n**PV**: 25619\n**Attaque**: 3208\n**Défense**: 2309\n**Récupération**:1893", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pega','EauPega']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551844161912867/BellerophonB_large.jpeg", color=0xffffff)
		embed.set_author(name="#472 Pégase (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551844161912867/BellerophonB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 27666\n**Attaque**: 2328\n**Défense**: 2610\n**Récupération**:2263", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pega','BoisPega']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551849719496724/BellerophonG_large.jpeg", color=0xffffff)
		embed.set_author(name="#473 Pégase (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551849719496724/BellerophonG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 80% 2 tour\n(No skillbooks)\n**Actif**: Soif 60% -30% 2 tours\n(No skillbooks)\n**PV**: 30522\n**Attaque**: 2261\n**Défense**: 3099\n**Récupération**:2016", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pega','LightPega']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551841762770945/Bellerophon_large.jpeg", color=0xffffff)
		embed.set_author(name="#474 Pégase (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551841762770945/Bellerophon_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%\n**Passif**: Choc 80% 1 tour\n(No skillbooks)\n**Actif**: Adrénaline 10% de ses PV (Allies)\n(No skillbooks)\n**PV**: 30849\n**Attaque**: 2036\n**Défense**: 3221\n**Récupération**:2152", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pega','DarkPega']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551846833684480/BellerophonD_large.jpeg", color=0xffffff)
		embed.set_author(name="#475 Pégase (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551846833684480/BellerophonD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Chasseur 30%\n(No skillbooks)\n**PV**: 27560\n**Attaque**: 3242\n**Défense**: 2193\n**Récupération**:2084", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Penpen ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Pen','FeuPen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557687053877255/PenkingR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#476 Penpen (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557687053877255/PenkingR_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Boost de moral (On crit) 100% de ses PA\n(No skillbooks)\n**Actif**: Attaque réduite (On crit) 2 tours\n(No skillbooks)\n**PV**: 31033\n**Attaque**: 1199\n**Défense**: 2581\n**Récupération**:1491", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pen','EauPen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557680087138304/Penking_Large.jpeg", color=0xffffff)
		embed.set_author(name="#477 Penpen (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557680087138304/Penking_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 80% 1 tours\n(No skillbooks)\n**Actif**: Aveuglement 60% 2 tours\n(No skillbooks)\n**PV**: 27969\n**Attaque**: 1342\n**Défense**: 2506\n**Récupération**:1580", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pen','BoisPen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557684235436054/PenkingG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#478 Penpen (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557684235436054/PenkingG_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Fatigue 60% 2 tours\n(No skillbooks)\n**Actif**: Récupération réduite 80% 1 tour\n(No skillbooks)\n**PV**: 39951\n**Attaque**: 1506\n**Défense**: 1145\n**Récupération**:1295", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pen','LightPen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557690346274828/PenkingW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#479 Penpen (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557690346274828/PenkingW_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Provocation 80% 2 tours\n(No skillbooks)\n**Actif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**PV**: 28806\n**Attaque**: 1866\n**Défense**: 2418\n**Récupération**:1410", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pen','DarkPen']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557682301730836/PenkingD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#480 Penpen (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557682301730836/PenkingD_Large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Boost de moral (On crit) 40% de ses PA\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2588\n**Défense**: 1696\n**Récupération**:1539", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Persephone ###########
		################################### 

	if any([message.content.startswith (item) for item in ['Pers','FeuPers']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558136058314752/QueenPerseponeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#481 Persephone (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558136058314752/QueenPerseponeR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Nécrose x2 80% 1 tour\n(???)\n**Actif**: Nécrose x2 100% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 30110\n**Attaque**: 3077\n**Défense**: 2801\n**Récupération**:2617", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pers','EauPers','TopPerse']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558136326619136/QueenPerseponeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#482 Persephone (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558136326619136/QueenPerseponeB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +10%, Taux: +20%)\n**PV**: 32494\n**Attaque**: 2784\n**Défense**: 2883\n**Récupération**:2624", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pers','BoisPers']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558134594371586/QueenPerseponeG_large.jpeg", color=0xffffff)
		embed.set_author(name="#483 Persephone (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558134594371586/QueenPerseponeG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Nécrose x3 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Attaque réduite 100% 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 32800\n**Attaque**: 2737\n**Défense**: 2903\n**Récupération**:2610", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pers','LightPers']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558136893112321/QueenPerseponeW_large.jpeg", color=0xffffff)
		embed.set_author(name="#484 Persephone (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558136893112321/QueenPerseponeW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: CR +20~25% (Donjons)\n**Passif**: Boost de moral (Allies) 20% SP\n(Dmg +30%)\n**Actif**: Choc 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 31094\n**Attaque**: 2649\n**Défense**: 3548\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pers','DarkPers']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558131624935424/QueenPersepone_large.jpeg", color=0xffffff)
		embed.set_author(name="#485 Persephone (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558131624935424/QueenPersepone_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: CR +20~25%(Donjons)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg +25%)\n**Actif**: Prédateur 50%\n(Dmg +25%)\n**PV**: 27151\n**Attaque**: 3834\n**Défense**: 2704\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Peyote ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Peyo','FeuPeyo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557781618524180/PeyotesR_large.jpeg", color=0xffffff)
		embed.set_author(name="#486 Peyote (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557781618524180/PeyotesR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Pétrification 80% 1 tour\n(No skillbooks)\n**Actif**: Adrénaline 30% de ses PV \n(No skillbooks)\n**PV**: 36451\n**Attaque**: 1418\n**Défense**: 1411\n**Récupération**:1704", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Peyo','EauPeyo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557775247376403/PeyotesB_large.jpeg", color=0xffffff)
		embed.set_author(name="#487 Peyote (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557775247376403/PeyotesB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Adrénaline 20% de ses PV \n(No skillbooks)\n**Actif**: Adrénaline 20% de ses PV (allies)\n(No skillbooks)\n**PV**: 24090\n**Attaque**: 2171\n**Défense**: 2147\n**Récupération**:2100", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Peyo','BoisPeyo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557772651233346/Peyotes_large.jpeg", color=0xffffff)
		embed.set_author(name="#488 Peyote (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557772651233346/Peyotes_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Boost de moral 30%\n(No skillbooks)\n**Actif**: Pétrification 80% 2 tour\n(No skillbooks)\n**PV**: 29453\n**Attaque**: 1342\n**Défense**: 2445\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Peyo','LightPeyo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557807480602625/PeyotesW_large.jpeg", color=0xffffff)
		embed.set_author(name="#489 Peyote (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557807480602625/PeyotesW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 100% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 27972\n**Attaque**: 1892\n**Défense**: 1725\n**Récupération**:1562", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Peyo','DarkPeyo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557776547741697/PeyotesD_large.jpeg", color=0xffffff)
		embed.set_author(name="#490 Peyote (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557776547741697/PeyotesD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Att +20~25%\n**Passif**: Traqueur (Dark) 20%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Phibian ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Phib','FeuPhib','TopPhib']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554042300039168/FroskeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#491 Phibian (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554042300039168/FroskeR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Clan)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +20%)\n**Actif**: Aveuglement 80% 2 tours\n(Dmg +25%)\n**PV**: 29889\n**Attaque**: 2860\n**Défense**: 1709\n**Récupération**:1764", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Phib','EauPhib']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554033261576212/Froske_large.jpeg", color=0xffffff)
		embed.set_author(name="#492 Phibian (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554033261576212/Froske_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35%(Clan)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 46993\n**Attaque**: 1499\n**Défense**: 1479\n**Récupération**:1404", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Phib','BoisPhib','TopPhib']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554044896313348/FroskeG_large.jpeg", color=0xffffff)
		embed.set_author(name="#493 Phibian (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554044896313348/FroskeG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%(Clan)\n**Passif**: Défense réduite 80% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 35974\n**Attaque**: 1953\n**Défense**: 1889\n**Récupération**:1786", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Phib','LightPhib']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554049355120671/FroskeW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#494 Phibian (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554049355120671/FroskeW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Clan)\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 26096\n**Attaque**: 2424\n**Défense**: 3269\n**Récupération**:1914", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Phib','DarkPhib']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554035396214806/FroskeD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#495 Phibian (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554035396214806/FroskeD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%(Clan)\n**Passif**: Vague martiale 20% (On crit)\n(Dmg +25%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +30%)\n**PV**: 32017\n**Attaque**: 2580\n**Défense**: 2576\n**Récupération**:1664", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Pincemi ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Pinc','FeuPinc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553117510795309/CrabigR_large.jpeg", color=0xffffff)
		embed.set_author(name="#496 Pincemi (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553117510795309/CrabigR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: 20%, +1 tour)\n**Actif**: Persévérance\n(Dmg: +25%)\n**PV**: 38678\n**Attaque**: 1247\n**Défense**: 1683\n**Récupération**:1547", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pinc','EauPinc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553087177588756/Crabig_large.jpeg", color=0xffffff)
		embed.set_author(name="#497 Pincemi (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553087177588756/Crabig_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: 20%, +1 tour)\n**Actif**: Prédateur 30%\n(Dmg: +20%, Taux: +10%)\n**PV**: 29147\n**Attaque**: 2302\n**Défense**: 1328\n**Récupération**:1444", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pinc','BoisPinc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553089673199616/CrabigG_large.jpeg", color=0xffffff)
		embed.set_author(name="#498 Pincemi (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553089673199616/CrabigG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Def +20~25%\n**Passif**: Reduction des dégâts 50% 1 tour\n(Dmg: +20%, +1 tour)\n**Actif**: Pétrification 80% 1 tour\n(Dmg: +20%, +1 tour)\n**PV**: 29930\n**Attaque**: 1471\n**Défense**: 2275\n**Récupération**:1743", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Pinolo ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Pino','BoisPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557873591222310/Pinocchio_large.jpeg", color=0xffffff)
		embed.set_author(name="#503 Pinolo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557873591222310/Pinocchio_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Frappe indéfectible\n(No skillbooks)\n**PV**: 21308\n**Attaque**: 2315\n**Défense**: 1730\n**Récupération**:1730", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557905673453588/PinocchioW_large.jpeg", color=0xffffff)
		embed.set_author(name="#504 Pinolo (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557905673453588/PinocchioW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Choc 60% - 2 tours\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 23433\n**Attaque**: 2683\n**Défense**: 1614\n**Récupération**:1668", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557883984707584/PinocchioD_large.jpeg", color=0xffffff)
		embed.set_author(name="#505 Pinolo (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557883984707584/PinocchioD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Clan)\n**Passif**: Frappe indéfectible\n**Actif**: Attaque réduite 60% - 1 tour\n**PV**: 26195\n**Attaque**: 2103\n**Défense**: 2113\n**Récupération**:2011", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Pinolo Lie ###########
		################################### 

	if any([message.content.startswith (item) for item in ['Pino','BoisPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557895871365120/Pinocchiofake_large.jpeg", color=0xffffff)
		embed.set_author(name="#508 Pinolo Lie (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557895871365120/Pinocchiofake_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Frappe Courageuse\n(No skillbooks)\n**PV**: 2152\n**Attaque**: 402\n**Défense**: 197\n**Récupération**:197", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pino','LightPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557903957983305/PinocchiofakeW_large.jpeg", color=0xffffff)
		embed.set_author(name="#509 Pinolo Lie (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557903957983305/PinocchiofakeW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: CR +15~20%(Clan)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(No skillbooks)\n**Actif**: Aveuglement 100% 2 tours\n(No skillbooks)\n**PV**: 2149\n**Attaque**: 103\n**Défense**: 103\n**Récupération**:103", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pino','DarkPino']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557901286211584/PinocchiofakeD_large.jpeg", color=0xffffff)
		embed.set_author(name="#510 Pinolo Lie (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557901286211584/PinocchiofakeD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%(Clan)\n**Passif**: Chasseur 100%\n(No skillbooks)\n**Actif**: Chasseur 100%\n(No skillbooks)\n**PV**: 1195\n**Attaque**: 142\n**Défense**: 152\n**Récupération**:152", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############   Fée   ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Fee','FeuFee','TopFee']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553317029642250/DaphneR_large.jpeg", color=0xffffff)
		embed.set_author(name="#511 Fée (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553317029642250/DaphneR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense augmentée 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 33202\n**Attaque**: 2099\n**Défense**: 2180\n**Récupération**:2528", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fee','EauFee']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553304765235202/DaphneB_large.jpeg", color=0xffffff)
		embed.set_author(name="#512 Fée (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553304765235202/DaphneB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Nécrose x2 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Domination 2 tours\n(Dmg +30%)\n**PV**: 29753\n**Attaque**: 2125\n**Défense**: 2002\n**Récupération**:3133", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fee','BoisFee']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553300948680763/Daphne_large.jpeg", color=0xffffff)
		embed.set_author(name="#513 Fée (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553300948680763/Daphne_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Vigueur 2 tours\n(Dmg +20%, Taux: +5%)\n**PV**: 28262\n**Attaque**: 2431\n**Défense**: 2138\n**Récupération**:2881", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fee','LightFee']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214559467864074/DaphneW_large.jpeg", color=0xffffff)
		embed.set_author(name="#514 Fée (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214559467864074/DaphneW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Vigueur 2 tours\n(Dmg +20%, Taux: +5%)\n**PV**: 29113\n**Attaque**: 1907\n**Défense**: 2322\n**Récupération**:3139", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fee','DarkFee']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553315062251520/DaphneD_large.jpeg", color=0xffffff)
		embed.set_author(name="#515 Fée (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553315062251520/DaphneD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: CR +15~20%\n**Passif**: Vague martiale\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Volonté 3 tours\n(Dmg +30%)\n**PV**: 24543\n**Attaque**: 2343\n**Défense**: 2125\n**Récupération**:3173", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Poséïdon #############
		################################### 

	if any([message.content.startswith (item) for item in ['Pose','FeuPose','TopPose']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557157216682012/NeptunegodR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#516 Poseidon (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557157216682012/NeptunegodR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45% (Clan)\n**Passif**:Frappe Courageuse\n(No skillbooks)\n**Actif**: Affaiblissement 70% 2 tours\n(No skillbooks)\n**PV**: 40312\n**Attaque**: 2187\n**Défense**: 2677\n**Récupération**:2534", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pose','EauPose']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557151705628693/Neptunegod_Large.jpeg", color=0xffffff)
		embed.set_author(name="#517 Poseidon (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557151705628693/Neptunegod_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de moral (Allies) 10% SP\n(No skillbooks)\n**Actif**: Prédateur 40%\n(No skillbooks)\n**PV**: 28513\n**Attaque**: 3391\n**Défense**: 2588\n**Récupération**:2329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pose','BoisPose']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557155165667338/NeptunegodG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#518 Poseidon (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557155165667338/NeptunegodG_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%(Clan)\n**Passif**:  Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 27281\n**Attaque**: 2792\n**Défense**: 3773\n**Récupération**:2206", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pose','LightPose']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557172412776448/NeptunegodW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#519 Poseidon (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557172412776448/NeptunegodW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 24216\n**Attaque**: 3854\n**Défense**: 2635\n**Récupération**:2240", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pose','DarkPose']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607337948358115329/NeptunegodD_Large.jpg", color=0xffffff)
		embed.set_author(name="#520 Poseidon (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607337948358115329/NeptunegodD_Large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%(Clan)\n**Passif**: Vague martiale\n(No skillbooks)\n**Actif**: Attaque réduite 80% 3 tours\n(No skillbooks)\n**PV**: 29732\n**Attaque**: 2281\n**Défense**: 3602\n**Récupération**:2561", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############# Torpin ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Torpin','BoisTorpin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558137807470592/Rabbeatles_large.jpeg", color=0xffffff)
		embed.set_author(name="#523 Torpin (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558137807470592/Rabbeatles_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (Donjons)\n**Passif**: Attaque réduite 70% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 50% 2 tours \n(No skillbooks)\n**PV**: 28840\n**Attaque**: 1784\n**Défense**: 2717\n**Récupération**:1355", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Torpin','LightTorpin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558166039199765/RabbeatlesW_large.jpeg", color=0xffffff)
		embed.set_author(name="#524 Torpin (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558166039199765/RabbeatlesW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%(Donjons)\n**Passif**: Vengeance\n(No skillbooks)\n**Actif**: Vengeance\n(No skillbooks)\n**PV**: 29208\n**Attaque**: 3139\n**Défense**: 2152\n**Récupération**:2193", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Torpin','DarkTorpin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558139518615555/RabbeatlesD_large.jpeg", color=0xffffff)
		embed.set_author(name="#525 Torpin (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558139518615555/RabbeatlesD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%(Donjons)\n**Passif**: Nécrose x2 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose x2 80% 2 tours\n(No skillbooks)\n**PV**: 35906\n**Attaque**: 2439\n**Défense**: 2146\n**Récupération**:2092", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############   Raic  ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Radi','FeuRadi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558210452815892/RadiossR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#526 Radic (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558210452815892/RadiossR_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%)\n**PV**: 26709\n**Attaque**: 2527\n**Défense**: 1811\n**Récupération**:1607", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Radi','EauRadi']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558180689772548/RadiossB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#527 Radic (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558180689772548/RadiossB_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 34353\n**Attaque**: 1874\n**Défense**: 1540\n**Récupération**:1588", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Radi','BoisRadi','TopRadi']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558183160217650/RadiossG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#528 Radic (Bois)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558183160217650/RadiossG_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Attaque réduite 30% 3 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Attaque réduite 70% 1 tour\n(Dmg +15%, tour: +1)\n**PV**: 28936\n**Attaque**: 1832\n**Défense**: 2411\n**Récupération**:1437", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Radi','LightRadi']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558214349062157/RadiossW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#529 Radic (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558214349062157/RadiossW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Nécrose 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +10%, Taux: +15%)\n**PV**: 24380\n**Attaque**: 3126\n**Défense**: 2581\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Radi','DarkRadi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558178467053574/Radioss_Large.jpeg", color=0xffffff)
		embed.set_author(name="#530 Radic (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558178467053574/Radioss_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: SP Rec +20~25%(Donjons)\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 29998\n**Attaque**: 2111\n**Défense**: 3187\n**Récupération**:1839", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############   Ramu  ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Ramu','FeuRamu','TopRamu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554283472781334/GoldonRamsayR_large.jpeg", color=0xffffff)
		embed.set_author(name="#531 Ramu (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554283472781334/GoldonRamsayR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Siphon de PA (On crit) 20%\n(Dmg +20%, Taux: +5%)\n**Actif**: Adrénaline (On crit)(Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**PV**: 26552\n**Attaque**: 2792\n**Défense**: 1682\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ramu','EauRamu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554279181746176/GoldonRamsayB_large.jpeg", color=0xffffff)
		embed.set_author(name="#532 Ramu (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554279181746176/GoldonRamsayB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Provocation 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Soif 60% -30% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 25204\n**Attaque**: 1954\n**Défense**: 2983\n**Récupération**:1491", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ramu','BoisRamu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554277135056898/GoldonRamsay_large.jpeg", color=0xffffff)
		embed.set_author(name="#533 Ramu (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554277135056898/GoldonRamsay_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%(Donjons)\n**Passif**: Étourdissement 40% 2 tours\n(Dmg +10%, Taux: +25%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28817\n**Attaque**: 2137\n**Défense**: 1970\n**Récupération**:1875", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ramu','LightRamu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554317941309450/GoldonRamsayW_large.jpeg", color=0xffffff)
		embed.set_author(name="#534 Ramu (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554317941309450/GoldonRamsayW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20% (Donjons)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 30335\n**Attaque**: 2784\n**Défense**: 2399\n**Récupération**:2100", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ramu','DarkRamu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554280700215327/GoldonRamsayD_large.jpeg", color=0xffffff)
		embed.set_author(name="#535 Ramu (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554280700215327/GoldonRamsayD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20% (Donjons)\n**Passif**: Silence 80% 2 tours\n(Dmg +20%, tour: +1)\n**Actif**: Provocation 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**PV**: 37281\n**Attaque**: 2044\n**Défense**: 2487\n**Récupération**:1717", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Robobot ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Robo','LightRobo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556427697324034/Metalion_large.jpeg", color=0xffffff)
		embed.set_author(name="#539 Robobot (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556427697324034/Metalion_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Def +20~25%\n**Passif**: Attaque réduite 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 27165\n**Attaque**: 2547\n**Défense**: 1403\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Robo','DarkRobo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556423486242847/MetalionD_large.jpeg", color=0xffffff)
		embed.set_author(name="#540 Robobot (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556423486242847/MetalionD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Def +20~25%\n**Passif**: Provocation 40% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**PV**: 27972\n**Attaque**: 1892\n**Défense**: 1725\n**Récupération**:1562", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############  Pottus ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Pottus','FeuPottus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557214830839463946/DePottusR_large.jpeg", color=0xffffff)
		embed.set_author(name="#541 Pottus (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557214830839463946/DePottusR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Nécrose 40% 2 tours\n(No skillbooks)\n**Actif**: Étourdissement 40% 1 tour\n(No skillbooks)\n**PV**: 36451\n**Attaque**: 1418\n**Défense**: 1411\n**Récupération**:1704", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pottus','EauPottus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553360528637954/DePottusB_large.jpeg", color=0xffffff)
		embed.set_author(name="#542 Pottus (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553360528637954/DePottusB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Récupération réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 24090\n**Attaque**: 2171\n**Défense**: 2147\n**Récupération**:2100", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pottus','BoisPottus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553359018819592/DePottus_large.jpeg", color=0xffffff)
		embed.set_author(name="#543 Pottus (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553359018819592/DePottus_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Attaque réduite 50% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**PV**: 29453\n**Attaque**: 1342\n**Défense**: 2445\n**Récupération**:1573", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Gravel  ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Grav','LightGrav']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555580645048330/Lemstone_large.jpeg", color=0xffffff)
		embed.set_author(name="#549 Gravel (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555580645048330/Lemstone_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Boost de moral 30% de ses PA\n(No skillbooks)\n**Actif**: Choc 50% 2 tours\n(No skillbooks)\n**PV**: 24271\n**Attaque**: 2458\n**Défense**: 3187\n**Récupération**:1914", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Grav','DarkGrav']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555592972107834/LemstoneD_large.jpeg", color=0xffffff)
		embed.set_author(name="#550 Gravel (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555592972107834/LemstoneD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Fatigue 80% 3 tours\n(No skillbooks)\n**Actif**: Silence 80% 2 tours\n(No skillbooks)\n**PV**: 24414\n**Attaque**: 3024\n**Défense**: 2138\n**Récupération**:2247", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############   Buis  ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Buis','BoisBuis']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560396255494155/Treebear_large.jpeg", color=0xffffff)
		embed.set_author(name="#553 Buis (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560396255494155/Treebear_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Rec +20~25%\n**Passif**: Sommeil 60% 1 tour\n(Dmg: +20%, Taux: +20%, +1 tour)\n**Actif**: Zèle 2 tours\n(Recup: +35%, +1 tour)\n**PV**: 37602\n**Attaque**: 1193\n**Défense**: 1840\n**Récupération**:1343", inline=False)

		await message.channel.send(embed=embed)

		###################################
		############ Rudolph ##############
		################################### 

	if any([message.content.startswith (item) for item in ['Rudo','BoisRudo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557285763711001/Noelle_large.jpeg", color=0xffffff)
		embed.set_author(name="#558 Rudolph (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557285763711001/Noelle_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Boost de moral 50% de ses PA\n(No skillbooks)\n**Actif**: Prédateur 20%\n(No skillbooks)\n**PV**: 26389\n**Attaque**: 2642\n**Défense**: 1539\n**Récupération**:1512", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Rudo','LightRudo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557370304233491/NoelleW_large.jpeg", color=0xffffff)
		embed.set_author(name="#559 Rudolph (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557370304233491/NoelleW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Siphon de PA 25%\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 26470\n**Attaque**: 2492\n**Défense**: 3269\n**Récupération**:2070", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Rudo','DarkRudo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557295930966039/NoelleD_large.jpeg", color=0xffffff)
		embed.set_author(name="#560 Rudolph (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557295930966039/NoelleD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Attaque réduite (On crit) 3 tours\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 28084\n**Attaque**: 3208\n**Défense**: 2023\n**Récupération**:2043", inline=False)

		await message.channel.send(embed=embed)

		###################################
		####### Spectre des sables ########
		################################### 

	if any([message.content.startswith (item) for item in ['Spectre','FeuSpectre','TopSpectre']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560820429651969/Void_large.jpeg", color=0xffffff)
		embed.set_author(name="#561 Spectre des sables (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560820429651969/Void_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Faiblesse exposée 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 22568\n**Attaque**: 2077\n**Défense**: 2935\n**Récupération**:1559", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Spectre','EauSpectre','TopSpectre']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560825961807872/VoidB_large.jpeg", color=0xffffff)
		embed.set_author(name="#562 Spectre des sables (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560825961807872/VoidB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Frappe indéfectible (On crit)\n(Dmg +25%)\n**Actif**: Vengeance\n(Dmg +35%)\n**PV**: 23566\n**Attaque**: 2362\n**Défense**: 2331\n**Récupération**:1725", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Spectre','BoisSpectre']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560829095084052/VoidG_large.jpeg", color=0xffffff)
		embed.set_author(name="#563 Spectre des sables (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560829095084052/VoidG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Sceau 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**PV**: 31391\n**Attaque**: 1942\n**Défense**: 2092\n**Récupération**:1411", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Spectre','LightSpectre']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560832521699341/VoidW_large.jpeg", color=0xffffff)
		embed.set_author(name="#564 Spectre des sables (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560832521699341/VoidW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Frappe indéfectible (On crit)\n(Dmg +25%)\n**PV**: 37493\n**Attaque**: 2473\n**Défense**: 2214\n**Récupération**:1915", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Spectre','DarkSpectre']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560826616381461/VoidD_large.jpeg", color=0xffffff)
		embed.set_author(name="#565 Spectre des sables (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560826616381461/VoidD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Même élément)\n**Passif**: Siphon de PA 20%\n(Dmg +15%, Taux: +5%)\n**Actif**: Persévérance\n(Dmg +20%)\n**PV**: 26634\n**Attaque**: 3391\n**Défense**: 2424\n**Récupération**:1784", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sanzang ##################
		#######################################	 

	if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangFeu','FeuSanzang','SanzFeu','SanzF','FeuSanz']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554508555780106/GuemtsaiziR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#566 Sanzang (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554508555780106/GuemtsaiziR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +35~40%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Sceau 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 29671\n**Attaque**: 2520\n**Défense**: 3562\n**Récupération**:2622", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangEau','EauSanzang','SanzEau','SanzE','EauSanz']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554499881959446/GuemtsaiziB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#567 Sanzang (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554499881959446/GuemtsaiziB_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +35~40%\n**Passif**: Agression (Def)\n(Dmg +25%)\n**Actif**: Agression (Def)\n(Dmg +10%, Taux: +20%)\n**PV**: 24611\n**Attaque**: 2492\n**Défense**: 3698\n**Récupération**:2690", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangBois','BoisSanzang','SanzBois','SanzB','BoisSanz']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554503652638740/Guemtsaizi_Large.jpeg", color=0xffffff)
		embed.set_author(name="#568 Sanzang (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554503652638740/Guemtsaizi_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Def +35~40%\n**Passif**: Attaque réduite 90% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 35770\n**Attaque**: 2739\n**Défense**: 2568\n**Récupération**:2316", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangLight','LightSanzang','SanzLight','SanzL','LightSanz']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554511407906826/GuemtsaiziW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#569 Sanzang (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554511407906826/GuemtsaiziW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Def +40%~45%\n**Passif**: Vague martiale 20%\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Choc 70% 2 tours\n(Dmg +20%, Taux : +10%)\n**PV**: 34803\n**Attaque**: 2716\n**Défense**: 2917\n**Récupération**:2787", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sanz','sanz','Sanzang','sanzang','SanzangDark','DarkSanzang','SanzDark','SanzD','DarkSanz']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554506383130645/GuemtsaiziD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#570 Sanzang (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554506383130645/GuemtsaiziD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +35~40%\n**Passif**: Siphon de PV \n(Dmg +20%)\n**Actif**: Chasseur 50%\n(Dmg +20%)\n**PV**: 24141\n**Attaque**: 3848\n**Défense**: 2601\n**Récupération**:2384", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Stella ###################
		#######################################

	if any([message.content.startswith (item) for item in ['Stella','FeuStella','TopStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553268417396766/DagonR_large.jpeg", color=0xffffff)
		embed.set_author(name="#571 Stella (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553268417396766/DagonR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Prédateur 30%\n(???)\n**Actif**: Étourdissement 100% 1 tour\n(???)\n**PV**: 22650\n**Attaque**: 2622\n**Défense**: 1852\n**Récupération**:1491", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Stella','EauStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553259466752011/Dagon_large.jpeg", color=0xffffff)
		embed.set_author(name="#572 Stella (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553259466752011/Dagon_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Nécrose x2 50% 1 tour\n(???)\n**Actif**: Nécrose 80% 2 tours\n(???)\n**PV**: 24346\n**Attaque**: 2472\n**Défense**: 1771\n**Récupération**:1696", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Stella','BoisStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553263841673216/DagonG_large.jpeg", color=0xffffff)
		embed.set_author(name="#573 Stella (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553263841673216/DagonG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Soif 80% -20% 1 tour\n(???)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28687\n**Attaque**: 1981\n**Défense**: 1773\n**Récupération**:1691", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Stella','LightStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553293172310026/DagonW_large.jpeg", color=0xffffff)
		embed.set_author(name="#574 Stella (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553293172310026/DagonW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Choc (On crit) 2 tour\n(Dmg +25%)\n**Actif**: Attaque réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 38174\n**Attaque**: 2017\n**Défense**: 1983\n**Récupération**:2364", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Stella','DarkStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553261710704671/DagonD_large.jpeg", color=0xffffff)
		embed.set_author(name="#575 Stella (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553261710704671/DagonD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 31442\n**Attaque**: 2036\n**Défense**: 2962\n**Récupération**:2343", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Stella S Evo #############
		#######################################

	if any([message.content.startswith (item) for item in ['FeuStella','SStella','FeuSStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496845814923264/20200506_093822.jpg", color=0xffffff)
		embed.set_author(name="#823 Stella SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496845814923264/20200506_093822.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Prédateur 30%\n(???)\n**Actif**: Étourdissement 100% 1 tour\n(???)\n**PV**: 24925\n**Attaque**: 3330\n**Défense**: 2043\n**Récupération**:1648", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauStella','SStella','EauSStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846054129664/20200506_093841.jpg", color=0xffffff)
		embed.set_author(name="#824 Stella SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846054129664/20200506_093841.jpg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +13~18%\n**Passif**: Nécrose x2 50% 1 tour\n(???)\n**Actif**: Nécrose 80% 2 tours\n(???)\n**PV**: 26791\n**Attaque**: 2751\n**Défense**: 2152\n**Récupération**:1873", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisStella','SStella','BoisSStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496845517258822/20200506_093744.jpg", color=0xffffff)
		embed.set_author(name="#825 Stella SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496845517258822/20200506_093744.jpg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: CR +13~18%\n**Passif**: Soif 80% -20% 1 tour\n(???)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 31581\n**Attaque**: 2188\n**Défense**: 2357\n**Récupération**:1874", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightStella','SStella','LightSStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846351794216/20200506_093900.jpg", color=0xffffff)
		embed.set_author(name="#826 Stella SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846351794216/20200506_093900.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +13~18%\n**Passif**: Choc (On crit) 2 tour\n(Dmg +25%)\n**Actif**: Attaque réduite (On crit) 2 tours\n(Dmg +20%)\n**PV**: 42157\n**Attaque**: 2221\n**Défense**: 2187\n**Récupération**:2603", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkStella','SStella','DarkSStella']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/686241946586316803/707496846670692422/20200506_093919.jpg", color=0xffffff)
		embed.set_author(name="#827 Stella SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/686241946586316803/707496846670692422/20200506_093919.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +13~18%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 34595\n**Attaque**: 2247\n**Défense**: 3609\n**Récupération**:2336", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Gren  ###################
		#######################################

	if any([message.content.startswith (item) for item in ['Gren','FeuGren']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560815924969475/VitaminR_large.jpeg", color=0xffffff)
		embed.set_author(name="#576 Gren (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560815924969475/VitaminR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Sceau 70% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Nécrose 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 28030\n**Attaque**: 1873\n**Défense**: 2676\n**Récupération**:1301", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gren','EauGren','TopGren']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560773814026241/VitaminB_large.jpeg", color=0xffffff)
		embed.set_author(name="#577 Gren (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560773814026241/VitaminB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 27931\n**Attaque**: 2165\n**Défense**: 2066\n**Récupération**:1432", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gren','BoisGren']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560771758948377/Vitamin_large.jpeg", color=0xffffff)
		embed.set_author(name="#578 Gren (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560771758948377/Vitamin_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Nécrose x2 60% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Nécrose x2 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 37173\n**Attaque**: 1792\n**Défense**: 1976\n**Récupération**:1540", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gren','LightGren']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560817414078465/VitaminW_large.jpeg", color=0xffffff)
		embed.set_author(name="#579 Gren (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560817414078465/VitaminW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28806\n**Attaque**: 1954\n**Défense**: 3344\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gren','DarkGren']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560811793448967/VitaminD_large.jpeg", color=0xffffff)
		embed.set_author(name="#580 Gren (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560811793448967/VitaminD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Avantage élémentaire (On crit)\n(Dmg +20%)\n**Actif**: Défense réduite (On crit)\n(Dmg +25%)\n**PV**: 27560\n**Attaque**: 3064\n**Défense**: 2159\n**Récupération**:2002", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sirène ###################
		#######################################

	if any([message.content.startswith (item) for item in ['Sire','FeuSire']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557184706281474/NereidR_large.jpeg", color=0xffffff)
		embed.set_author(name="#581 Sirène (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557184706281474/NereidR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Nécrose 30% 2 tours\n(Taux: +25%)\n**Actif**: Volonté 2 tours\n(Dmg +25%, Taux: +20%)\n**PV**: 30822\n**Attaque**: 1696\n**Défense**: 1525\n**Récupération**:2751", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sire','EauSire','TopSire']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557181543645204/Nereid_large.jpeg", color=0xffffff)
		embed.set_author(name="#582 Sirène (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557181543645204/Nereid_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Vigueur 2 tours\n(Dmg +25%, Taux: +5%)\n**PV**: 27982\n**Attaque**: 1920\n**Défense**: 2016\n**Récupération**:2867", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sire','BoisSire']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557183951306753/NereidG_large.jpeg", color=0xffffff)
		embed.set_author(name="#583 Sirène (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557183951306753/NereidG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Abondance d'âmes rouges\n(Dmg +25%)\n**Actif**: Récupération augmentée 2 tours\n(Dmg +25%, tour: +1)\n**PV**: 26327\n**Attaque**: 1900\n**Défense**: 1559\n**Récupération**:2458", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sire','LightSire']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557187432579073/NereidW_large.jpeg", color=0xffffff)
		embed.set_author(name="#584 Sirène (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557187432579073/NereidW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Boost de moral 20% de ses PA\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Bouclier (Level) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 24713\n**Attaque**: 2424\n**Défense**: 3337\n**Récupération**:1914", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sire','DarkSire']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557610553732890632/NereidD_large.jpeg", color=0xffffff)
		embed.set_author(name="#585 Sirène (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557610553732890632/NereidD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Récupération\n**Lead**: Def +30~35%(Même élément)\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Domination 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 24523\n**Attaque**: 2322\n**Défense**: 2118\n**Récupération**:3344", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sha Wujing ###############
		#######################################

	if any([message.content.startswith (item) for item in ['ShaW','FeuShaW', 'Sha', 'FeuSha','TopSha']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634748415934464/Sha3EvoR_large.jpg", color=0xffffff)
		embed.set_author(name="#591 Sha wujing (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634748415934464/Sha3EvoR_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Tc +20~25%\n**Passif**: Faiblesse exposée 80% 2 tours\n(No skillbooks)\n**Actif**: Frappe Courageuse\n(No skillbooks)\n**PV**: 30059\n**Attaque**: 3596\n**Défense**: 2206\n**Récupération**:2240", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['ShaW','EauShaW', 'Sha', 'EauSha']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634734813806615/Sha3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#592 Sha wujing (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634734813806615/Sha3Evo_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Tc +20~25%\n**Passif**: Résistance réduite 2 tours\n(No skillbooks)\n**Actif**: Sceau 70% 2 tours\n(No skillbooks)\n**PV**: 31295\n**Attaque**: 2934\n**Défense**: 2944\n**Récupération**:2181", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['ShaW','BoisShaW', 'Sha', 'BoisSha']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634744225824774/Sha3EvoG_large.jpg", color=0xffffff)
		embed.set_author(name="#593 Sha wujing (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634744225824774/Sha3EvoG_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Tc +20~25%\n**Passif**: Vague martiale 20%\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 32698\n**Attaque**: 2907\n**Défense**: 2856\n**Récupération**:2011", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['ShaW','LightShaW', 'Sha', 'LightSha']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634753482653716/Sha3EvoW_large.jpg", color=0xffffff)
		embed.set_author(name="#594 Sha wujing (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634753482653716/Sha3EvoW_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Tc +20~25%\n**Passif**: Sceau 100% 3 tours\n(dmg +25%)\n**Actif**: Réduction de dégâts 2 tours\n(dmg +25%)\n**PV**: 30883\n**Attaque**: 2622\n**Défense**: 3596\n**Récupération**:2479", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['ShaW','DarkShaW', 'Sha', 'DarkSha']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607634739678937103/Sha3EvoD_large.jpg", color=0xffffff)
		embed.set_author(name="#595 Sha wujing (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607634739678937103/Sha3EvoD_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Tc +20~25%\n**Passif**: Frappe Courageuse\n(No skillbooks)\n**Actif**: Affaiblissement 80% 2 tours\n(No skillbooks)\n**PV**: 28643\n**Attaque**: 3732\n**Défense**: 2465\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Clamy ###################
		#######################################

	if any([message.content.startswith (item) for item in ['Clamy','FeuClamy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558861177978910/ShellkingR_large.jpeg", color=0xffffff)
		embed.set_author(name="#586 Clamy (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558861177978910/ShellkingR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV Rec +20~25%\n**Passif**: Provocation 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (feu) 100%\n(Dmg: +35%)\n**PV**: 29293\n**Attaque**: 2001\n**Défense**: 1705\n**Récupération**: 1671", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Clamy','EauClamy','TopClamy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558855821852673/Shellking_large.jpeg", color=0xffffff)
		embed.set_author(name="#587 Clamy (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558855821852673/Shellking_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV Rec +20~25%\n**Passif**: Défense réduite 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (eau) 100%\n(Dmg: +35%)\n**PV**: 29440\n**Attaque**: 2996\n**Défense**: 1641\n**Récupération**: 1764", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Clamy','BoisClamy']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558857717809165/ShellkingG_large.jpeg", color=0xffffff)
		embed.set_author(name="#588 Clamy (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558857717809165/ShellkingG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV Rec +20~25%\n**Passif**: Nécrose 100% 2 tours\n(Dmg: +20% tour: +1)\n**Actif**: Prédateur (bois) 100%\n(Dmg: +35%)\n**PV**: 25360\n**Attaque**: 1784\n**Défense**: 2663\n**Récupération**: 1566", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sherlock #################
		#######################################

	if any([message.content.startswith (item) for item in ['Sher','FeuSher']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553372243329025/DetectiveSherlockR_large.jpeg", color=0xffffff)
		embed.set_author(name="#596 Sherlock (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553372243329025/DetectiveSherlockR_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20% (Clan)\n**Passif**: Traqueur (bois) 50%\n(Dmg : +35%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg : +20%, Taux : +10%)\n**PV**: 25878\n**Attaque**: 2724\n**Défense**: 1580\n**Récupération**:1750", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sher','EauSher']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553366559916043/DetectiveSherlockB_large.jpeg", color=0xffffff)
		embed.set_author(name="#597 Sherlock (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553366559916043/DetectiveSherlockB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Traqueur (feu) 50%\n(Dmg : +35%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg : +20%, Taux : +10%)\n**PV**: 28507\n**Attaque**: 2622\n**Défense**: 1641\n**Récupération**:1566", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sher','BoisSher']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553369210716171/DetectiveSherlockG_large.jpeg", color=0xffffff)
		embed.set_author(name="#598 Sherlock (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553369210716171/DetectiveSherlockG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Traqueur (eau) 50%\n(Dmg : +35%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg : +20%, Taux : +10%)\n**PV**: 26300\n**Attaque**: 2813\n**Défense**: 1696\n**Récupération**:1525", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sher','LightSher']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553364995440660/DetectiveSherlock_large.jpeg", color=0xffffff)
		embed.set_author(name="#599 Sherlock (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553364995440660/DetectiveSherlock_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%(Clan)\n**Passif**: Faiblesse exposée 80% 2 tours\n(Dmg : +10%, Taux : +20%)\n**Actif**: Faiblesse exposée 80% 2 tours\n(Dmg : +10%, Taux : +20%)\n**PV**: 29794\n**Attaque**: 3221\n**Défense**: 2309\n**Récupération**:1989", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Shinobi ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Shin','FeuShin','TopShin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554694837403670/HattoriHanzoR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#601 Shinobi (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554694837403670/HattoriHanzoR_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: PV +40~45% (Clan)\n**Passif**: Frappe Courageuse\n(Dmg +20%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 32106\n**Attaque**: 3057\n**Défense**: 2883\n**Récupération**:2072", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shin','EauShin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554677200486401/HattoriHanzoB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#602 Shinobi (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554677200486401/HattoriHanzoB_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Avantage élémentaire \n(Dmg +25%)\n**Actif**: Siphon de PA 50% \n(Dmg +25%)\n**PV**: 25483\n**Attaque**: 3303\n**Défense**: 3071\n**Récupération**:2547", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shin','BoisShin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554675162054666/HattoriHanzo_Large.jpeg", color=0xffffff)
		embed.set_author(name="#603 Shinobi (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554675162054666/HattoriHanzo_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Clan)\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +10%)\n**Actif**: Étourdissement 100% 2 tours\n(Dmg +30%)\n**PV**: 41436\n**Attaque**: 2017\n**Défense**: 2807\n**Récupération**:2228", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shin','LightShin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554710520037382/HattoriHanzoW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#604 Shinobi (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554710520037382/HattoriHanzoW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Boost de Moral +100% PA\n(Dmg +30%)\n**Actif**: Prédateur 50%\n(Dmg +30%)\n**PV**: 28977\n**Attaque**: 3889\n**Défense**: 2935\n**Récupération**:2247", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shin','DarkShin']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554690584248335/HattoriHanzoD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#605 Shinobi (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554690584248335/HattoriHanzoD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Clan)\n**Passif**: Siphon de PA 40%\n(Dmg +25%, +Effect.: +10%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 28949\n**Attaque**: 3957\n**Défense**: 2704\n**Récupération**:2309", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Shiva  ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Shiv','FeuShiv','TopShiv']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556070690881536/Mahakala_large.jpeg", color=0xffffff)
		embed.set_author(name="#606 Shiva (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556070690881536/Mahakala_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%,(Donjons)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg: +15% tour: +1)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +25%)\n**PV**: 27689\n**Attaque**: 2295\n**Défense**: 3494\n**Récupération**:2309", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shiv','EauShiv']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556073115058187/MahakalaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#607 Shiva (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556073115058187/MahakalaB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Siphon de PA 30%\n(Dmg: +20% Effect.: +10%)\n**Actif**: Soif 80% -30% 2 tours\n(Dmg: +20% tour: +1)\n**PV**: 49104\n**Attaque**: 2214\n**Défense**: 2398\n**Récupération**:2228", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shiv','BoisShiv']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556087392469022/MahakalaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#608 Shiva (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556087392469022/MahakalaG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Prédateur 50%\n(Dmg: +25%)\n**Actif**: Sceau 80% 2 tours\n(???)\n**PV**: 28541\n**Attaque**: 3902\n**Défense**: 2819\n**Récupération**:2138", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shiv','LightShiv']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556088625594384/MahakalaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#609 Shiva (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556088625594384/MahakalaW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Vague martiale 20%\n(Dmg: +20% Effect.: +5%)\n**Actif**: Agression (PV)\n(Dmg: +25%)\n**PV**: 49376\n**Attaque**: 2568\n**Défense**: 2126\n**Récupération**:1915", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Shiv','DarkShiv']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552556081721638914/MahakalaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#610 Shiva (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552556081721638914/MahakalaD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%(Donjons)\n**Passif**: Sceau 100% 2 tours\n(???)\n**Actif**: Étourdissement 80% 2 tour\n(???)\n**PV**: 32273\n**Attaque**: 2349\n**Défense**: 3562\n**Récupération**:2588", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Siegfried ################
		#######################################

	if any([message.content.startswith (item) for item in ['Sieg','FeuSieg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553469253386243/Dragonslayer_large.jpeg", color=0xffffff)
		embed.set_author(name="#611 Siegfried (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553469253386243/Dragonslayer_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +40~45%(Clan)\n**Passif**: Boost de moral 30% de ses PA\n(Dmg: +25%)\n**Actif**: Avantage élémentaire\n(Dmg: +30%)\n**PV**: 24625\n**Attaque**: 4018\n**Défense**: 2629\n**Récupération**:2179", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sieg','EauSieg','TopSieg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553498735018034/DragonslayerB_large.jpeg", color=0xffffff)
		embed.set_author(name="#612 Siegfried (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553498735018034/DragonslayerB_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Def +40~45%(Clan)\n**Passif**: Faiblesse exposée 80% 2 tours\n(Dmg: +15% tour: +1)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 28221\n**Attaque**: 3269\n**Défense**: 2629\n**Récupération**:2329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sieg','BoisSieg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553503533301778/DragonslayerG_large.jpeg", color=0xffffff)
		embed.set_author(name="#613 Siegfried (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553503533301778/DragonslayerG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Def +40~45%(Clan)\n**Passif**: Défense réduite 80% 3 tours\n(Dmg: +25% )\n**Actif**: Étourdissement 80% 1 tour\n(Dmg: +15% Taux: +10%)\n**PV**: 39747\n**Attaque**: 2677\n**Défense**: 2235\n**Récupération**:2194", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sieg','LightSieg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553503814320128/DragonslayerW_large.jpeg", color=0xffffff)
		embed.set_author(name="#614 Siegfried (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553503814320128/DragonslayerW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Def +40~45%(Clan)\n**Passif**: Frappe Courageuse\n(Dmg: +20%)\n**Actif**: Frappe Courageuse\n(Dmg: +20%)\n**PV**: 31295\n**Attaque**: 3023\n**Défense**: 2692\n**Récupération**:2672", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sieg','DarkSieg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553499968143373/DragonslayerD_large.jpeg", color=0xffffff)
		embed.set_author(name="#615 Siegfried (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553499968143373/DragonslayerD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Def +40~45%(Clan)\n**Passif**: Agression (Def)\n(Dmg: +25%)\n**Actif**: Agression (Def)\n(Dmg: +25%)\n**PV**: 31578\n**Attaque**: 2213\n**Défense**: 3807\n**Récupération**:2465", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Soldat Slime #############
		#######################################

	if any([message.content.startswith (item) for item in ['SoldatSlime','FeuSoldatSlime','SoldatSlime','FeuSoldatSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559134994596086/Slimeknight3Evo_large.jpeg", color=0xffffff)
		embed.set_author(name="#621 Soldat Slime (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559134994596086/Slimeknight3Evo_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Attaque réduite 60% 2 tour\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 25783\n**Attaque**: 3044\n**Défense**: 2029\n**Récupération**:1246", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SoldatSlime','EauSoldatSlime','SoldatSlime','EauSoldatSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559205337399296/Slimeknight3EvoB_large.jpeg", color=0xffffff)
		embed.set_author(name="#622 Soldat Slime (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559205337399296/Slimeknight3EvoB_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 24182\n**Attaque**: 2370\n**Défense**: 3064\n**Récupération**:1226", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SoldatSlime','BoisSoldatSlime','SoldatSlime','BoisSoldatSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557610727095926799/Slimeknight3EvoG_large.jpeg", color=0xffffff)
		embed.set_author(name="#623 Soldat Slime (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557610727095926799/Slimeknight3EvoG_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Nécrose x2 60% 2 tours\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27117\n**Attaque**: 2738\n**Défense**: 2179\n**Récupération**:1301", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SoldatSlime','LightSoldatSlime','SoldatSlime','LightSoldatSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559213012844566/Slimeknight3EvoW_large.jpeg", color=0xffffff)
		embed.set_author(name="#624 Soldat Slime (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559213012844566/Slimeknight3EvoW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Boost de moral 50%\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 27070\n**Attaque**: 3058\n**Défense**: 2275\n**Récupération**:2118", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['SoldatSlime','DarkSoldatSlime','SoldatSlime','DarkSoldatSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559202183151616/Slimeknight3EvoD_large.jpeg", color=0xffffff)
		embed.set_author(name="#625 Soldat Slime (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559202183151616/Slimeknight3EvoD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Avantage élémentaire\n(No skillbooks)\n**PV**: 37288\n**Attaque**: 1887\n**Défense**: 2180\n**Récupération**:2037", inline=False)

		await message.channel.send(embed=embed)


	if message.content.startswith("SoldatSlime"):
		return

	if message.content.startswith("FeuSoldatSlime"):
		return

	if message.content.startswith("EauSoldatSlime"):
		return

	if message.content.startswith("BoisSoldatSlime"):
		return

	if message.content.startswith("LightSoldatSlime"):
		return

	if message.content.startswith("DarkSoldatSlime"):
		return

	if message.content.startswith("SoldatSlime"):
		return

	if message.content.startswith("FeuSoldatSlime"):
		return

	if message.content.startswith("EauSoldatSlime"):
		return

	if message.content.startswith("BoisSoldatSlime"):
		return

	if message.content.startswith("LightSoldatSlime"):
		return

	if message.content.startswith("DarkSoldatSlime"):
		return

		#######################################
		############  Slime  ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Slime','FeuSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555350977544192/KingslimeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#616 Slime (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555350977544192/KingslimeR_large.jpeg")
		embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 35177\n**Attaque**: 2017\n**Défense**: 1574\n**Récupération**:1554", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Slime','EauSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555344438624257/KingslimeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#617 Slime (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555344438624257/KingslimeB_large.jpeg")
		embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +30%)\n**Actif**: Etourdissement 60% 1 tour\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 24516\n**Attaque**: 1777\n**Défense**: 2574\n**Récupération**:1396", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Slime','BoisSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555321399312395/Kingslime_large.jpeg", color=0xffffff)
		embed.set_author(name="#618 Slime (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555321399312395/Kingslime_large.jpeg")
		embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +25%, Taux: 10%, tour: +1)\n**PV**: 26144\n**Attaque**: 2322\n**Défense**: 1525\n**Récupération**:1430", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Slime','LightSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555351954817026/KingslimeW_large.jpeg", color=0xffffff)
		embed.set_author(name="#619 Slime (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555351954817026/KingslimeW_large.jpeg")
		embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Choc 60% 1 tour\n(Dmg +25%, Taux: +10%)\n**Actif**: Choc 60% 1 tour\n(Dmg +25%, tour: +1)\n**PV**: 28946\n**Attaque**: 1708\n**Défense**: 1766\n**Récupération**:1562", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Slime','DarkSlime']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608935531241406475/KingslimeD_large.jpg", color=0xffffff)
		embed.set_author(name="#620 Slime (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608935531241406475/KingslimeD_large.jpg")
		embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +20~25%(Même élément)\n**Passif**: Agression (PV)\n(Dmg +30%)\n**Actif**: Agression (PV)\n(Dmg +30%)\n**PV**: 37792\n**Attaque**: 1411\n**Défense**: 1370\n**Récupération**:1710", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Givri  ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Givri','EauGivri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557225747415040/nicole_large.jpeg", color=0xffffff)
		embed.set_author(name="#627 Givri (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557225747415040/nicole_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: SP Rec +20~25%\n**Passif**: Provocation 80% 1 tour\n(No skillbooks)\n**Actif**: Nécrose x2 60% 1 tours\n(No skillbooks)\n**PV**: 43240\n**Attaque**: 1622\n**Défense**: 1261\n**Récupération**:1465\n**Nord**", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Givri','LightGivri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557217327511240763/nicoleW_large.jpeg", color=0xffffff)
		embed.set_author(name="#629 Givri (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557217327511240763/nicoleW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: SP Rec +20~25%\n**Passif**: Siphon de PV\n(No skillbooks)\n**Actif**: Siphon de PV (Allies) \n(No skillbooks)\n**PV**: 26368\n**Attaque**: 3276\n**Défense**: 2247\n**Récupération**:1682", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Givri','DarkGivri']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557226523361290/nicoleD_large.jpeg", color=0xffffff)
		embed.set_author(name="#630 Givri (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557226523361290/nicoleD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: SP Rec +20~25%\n**Passif**: Attaque réduite 80% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 80% 1 tour\n(No skillbooks)\n**PV**: 32337\n**Attaque**: 2614\n**Défense**: 2672\n**Récupération**:1739", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sparkitt #################
		#######################################

	if any([message.content.startswith (item) for item in ['Sparki','FeuSparki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555509366915082/LaidenR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#631 Sparkitt (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555509366915082/LaidenR_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Étourdissement (On crit) 2 tours\n(Dmg +25%)\n**Actif**: Aveuglement 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 36587\n**Attaque**: 1962\n**Défense**: 2316\n**Récupération**:2214", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sparki','EauSparki','TopSparki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555498851926071/LaidenB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#632 Sparkitt (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555498851926071/LaidenB_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 30672\n**Attaque**: 3173\n**Défense**: 1900\n**Récupération**:2002", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sparki','BoisSparki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557612523306745858/LaidenG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#633 Sparkitt (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557612523306745858/LaidenG_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Avantage élémentaire\n(Dmg +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 24737\n**Attaque**: 2805\n**Défense**: 2576\n**Récupération**:2488", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sparki','LightSparki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555496243200010/Laiden_Large.jpeg", color=0xffffff)
		embed.set_author(name="#634 Sparkitt (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555496243200010/Laiden_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Choc (On crit) 1 tour\n(Dmg +25%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30815\n**Attaque**: 3303\n**Défense**: 1920\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sparki','DarkSparki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555501116719115/LaidenD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#635 Sparkitt (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555501116719115/LaidenD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 37152\n**Attaque**: 2024\n**Défense**: 2432\n**Récupération**:1976", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Tincel  ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Tincel','FeuTincell']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561027070296064/WispkingR_large.jpeg", color=0xffffff)
		embed.set_author(name="#636 Tincel (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561027070296064/WispkingR_large.jpeg")
		embed.add_field(name="★", value="**Type**: Tank\n**Lead**: PV +10~15%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Défense réduite 60% 2 tours\n(No skillbooks)\n**PV**: 35531\n**Attaque**: 1363\n**Défense**: 1772\n**Récupération**:1418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tincel','EauTincel']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561016165367828/Wispking_large.jpeg", color=0xffffff)
		embed.set_author(name="#637 Tincel (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561016165367828/Wispking_large.jpeg")
		embed.add_field(name="★", value="**Type**: Équilibré\n**Lead**: PV +10~15%\n**Passif**: Fatigue 40% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 60% 2 tours\n(No skillbooks)\n**PV**: 29082\n**Attaque**: 1538\n**Défense**: 1793\n**Récupération**:1684", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tincel','BoisTincel']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561022146314240/WispkingG_large.jpeg", color=0xffffff)
		embed.set_author(name="#638 Tincel (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561022146314240/WispkingG_large.jpeg")
		embed.add_field(name="★", value="**Type**: Récupération\n**Lead**: PV +10~15%\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 60% 2 tours\n(No skillbooks)\n**PV**: 25102\n**Attaque**: 1682\n**Défense**: 1600\n**Récupération**:2418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tincel','LightTincel']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561045592604672/WispkingW_large.jpeg", color=0xffffff)
		embed.set_author(name="#639 Tincel (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561045592604672/WispkingW_large.jpeg")
		embed.add_field(name="★", value="**Type**: Défenseur\n**Lead**: PV +10~15%\n**Passif**: Étourdissement 20% 1 tour\n(No skillbooks)\n**Actif**: Étourdissement 60% 1 tour\n(No skillbooks)\n**PV**: 27860\n**Attaque**: 1355\n**Défense**: 2418\n**Récupération**:1628", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tincel','DarkTincel']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561019277279238/WispkingD_large.jpeg", color=0xffffff)
		embed.set_author(name="#640 Tincel (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561019277279238/WispkingD_large.jpeg")
		embed.add_field(name="★", value="**Type**: Attaquant\n**Lead**: PV +10~15%\n**Passif**: Silence 20% 1 tour\n(No skillbooks)\n**Actif**: Silence 60% 1 tour\n(No skillbooks)\n**PV**: 23433\n**Attaque**: 2275\n**Défense**: 1662\n**Récupération**:1362", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############ Sphinx  ##################
		#######################################

	if any([message.content.startswith (item) for item in ['Sph','FeuSph','TopSph']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552209552900156/CairoR_large.jpeg", color=0xffffff)
		embed.set_author(name="#641 Sphinx (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552209552900156/CairoR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe indéfectible \n(Dmg +30%)\n**PV**: 35586\n**Attaque**: 2494\n**Défense**: 2044\n**Récupération**:1881", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sph','EauSph']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552202804396083/CairoB_large.jpeg", color=0xffffff)
		embed.set_author(name="#642 Sphinx (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552202804396083/CairoB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Frappe indéfectible\n(Dmg +30%)\n**Actif**: Siphon de PV \n(Dmg +30%)\n**PV**: 25442\n**Attaque**: 2390\n**Défense**: 3235\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sph','BoisSph','TopSph']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552207573057546/CairoG_large.jpeg", color=0xffffff)
		embed.set_author(name="#643 Sphinx (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552207573057546/CairoG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Faiblesse exposée 70% 2 tours\n(Dmg +10%, Taux: +30%)\n**Actif**: Frappe indéfectible\n(Dmg +30%)\n**PV**: 25415\n**Attaque**: 3221\n**Défense**: 2452\n**Récupération**:1873", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sph','LightSph']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552179563626506/Cairo_large.jpeg", color=0xffffff)
		embed.set_author(name="#644 Sphinx (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552179563626506/Cairo_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Avantage élémentaire (On crit)\n(Dmg +30%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30890\n**Attaque**: 3391\n**Défense**: 1968\n**Récupération**:1920", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sph','DarkSph']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557612911468740619/CairoD_large.jpeg", color=0xffffff)
		embed.set_author(name="#645 Sphinx (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557612911468740619/CairoD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Aveuglement 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Frappe indéfectible (On crit)\n(Dmg +30%)\n**PV**: 27768\n**Attaque**: 3002\n**Défense**: 2753\n**Récupération**:1854", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Ecurrix   ##############
		#######################################

	if any([message.content.startswith (item) for item in ['Ecur','FeuEcur']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559563027513367/SqusquR_large.jpeg", color=0xffffff)
		embed.set_author(name="#646 Ecurrix (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559563027513367/SqusquR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Att +20~25%\n**Passif**: Attaque réduite 60% 1 tour\n(Dmg +10%, Taux: +10%tour: +1)\n**Actif**: Attaque réduite 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 29906\n**Attaque**: 1654\n**Défense**: 1752\n**Récupération**:1623", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ecur','EauEcur']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559553175224320/SqusquB_large.jpeg", color=0xffffff)
		embed.set_author(name="#647 Ecurrix (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559553175224320/SqusquB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: Att +20~25%\n**Passif**: Récupération réduite 60% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Nécrose 40% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 24720\n**Attaque**: 1607\n**Défense**: 2322\n**Récupération**:1491", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Ecur','BoisEcur']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559549060481024/Squsqu_large.jpeg", color=0xffffff)
		embed.set_author(name="#648 Ecurrix (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559549060481024/Squsqu_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Att +20~25%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Défense réduite 40% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 22514\n**Attaque**: 2574\n**Défense**: 1539\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Crustarov   ############
		#######################################

	if any([message.content.startswith (item) for item in ['Crus','FeuCrus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558472173060109/RocknRollR_large.jpeg", color=0xffffff)
		embed.set_author(name="#651 Crustarov (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558472173060109/RocknRollR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Boost de moral 20% PA\n(Dmg: +20%, Taux: +10%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 26041\n**Attaque**: 2486\n**Défense**: 1457\n**Récupération**:1628", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Crus','EauCrus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558468675010563/RocknRoll_large.jpeg", color=0xffffff)
		embed.set_author(name="#652 Crustarov (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558468675010563/RocknRoll_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: CR +10~15%\n**Passif**: Provocation intrépide 60% 1 tour\n(Dmg: +20%, Taux: +20%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 29947\n**Attaque**: 1593\n**Défense**: 1766\n**Récupération**:1623", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Crus','BoisCrus']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558470344212490/RocknRollG_large.jpeg", color=0xffffff)
		embed.set_author(name="#653 Crustarov (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558470344212490/RocknRollG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: CR +10~15%\n**Passif**: Adrenaline 20% PV\n(Dmg: +20%, Taux: +10%)\n**Actif**: Perforation 70% défense ennemie\n(Dmg: +30%)\n**PV**: 26518\n**Attaque**: 2377\n**Défense**: 1696\n**Récupération**:1457", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Succube    ############
		#######################################

	if any([message.content.startswith (item) for item in ['Succ','FeuSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557218097015029761/LilithR_large.jpeg", color=0xffffff)
		embed.set_author(name="#656 Succube (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557218097015029761/LilithR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: PV +30~35%\n**Passif**: Siphon de PV  (On crit)\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 26327\n**Attaque**: 3167\n**Défense**: 2288\n**Récupération**:1682", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Succ','EauSucc','TopSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555663763439616/LilithB_large.jpeg", color=0xffffff)
		embed.set_author(name="#658 Succube (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555663763439616/LilithB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +25%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**PV**: 37057\n**Attaque**: 2146\n**Défense**: 2473\n**Récupération**:1710", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Succ','BoisSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555665948672000/LilithG_large.jpeg", color=0xffffff)
		embed.set_author(name="#660 Succube (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555665948672000/LilithG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: PV +30~35%\n**Passif**: Sommeil 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**Actif**: Brise bouclier 100%\n(Dmg +30%)\n**PV**: 31329\n**Attaque**: 2321\n**Défense**: 2352\n**Récupération**:2045", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Succ','LightSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555669300183051/LilithW_large.jpeg", color=0xffffff)
		embed.set_author(name="#662 Succube (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555669300183051/LilithW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +25%)\n**PV**: 36812\n**Attaque**: 1976\n**Défense**: 2323\n**Récupération**:2214", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Succ','DarkSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555661851099150/Lilith_large.jpeg", color=0xffffff)
		embed.set_author(name="#664 Succube (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555661851099150/Lilith_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: PV +30~35%\n**Passif**: Sommeil 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Sommeil 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 30012\n**Attaque**: 2343\n**Défense**: 3173\n**Récupération**:1866", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Succube S Evo  ##########
		#######################################

	if any([message.content.startswith (item) for item in ['FeuSucc','SSucc','FeuSSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338087747682334/SuperLilithR_large.jpg", color=0xffffff)
		embed.set_author(name="#657 Succube SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338087747682334/SuperLilithR_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Siphon de PV  (On crit)\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite (On crit) 2 tours\n(Dmg +20%, tour: +1)\n**PV**: 28970\n**Attaque**: 3514\n**Défense**: 2527\n**Récupération**:1859", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauSucc','SSucc','EauSSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338082563522571/SuperLilithB_large.jpg", color=0xffffff)
		embed.set_author(name="#659 Succube SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338082563522571/SuperLilithB_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral (On crit) 50% de ses PA\n(Dmg +25%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**PV**: 40931\n**Attaque**: 2364\n**Défense**: 2725\n**Récupération**:1888", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisSucc','SSucc','BoisSSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338084765270030/SuperLilithG_large.jpg", color=0xffffff)
		embed.set_author(name="#661 Succube SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338084765270030/SuperLilithG_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Sommeil 60% 2 tours\n(Dmg +20%, Taux: +15%)\n**Actif**: Brise bouclier 100%\n(Dmg +30%)\n**PV**: 34488\n**Attaque**: 2563\n**Défense**: 2596\n**Récupération**:2262", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightSucc','SSucc','LightSSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338090083909652/SuperLilithW_large.jpg", color=0xffffff)
		embed.set_author(name="#663 Succube SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338090083909652/SuperLilithW_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Boost de moral (Allies) 10% SP\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +25%)\n**PV**: 40658\n**Attaque**: 2174\n**Défense**: 2562\n**Récupération**:2439", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkSucc','SSucc','DarkSSucc']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/607338079501549570/SuperLilith_large.jpg", color=0xffffff)
		embed.set_author(name="#665 Succube SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/607338079501549570/SuperLilith_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: PV +30~35%\n**Passif**: Sommeil 80% 2 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Sommeil 80% 1 tour\n(Dmg +20%, tour: +1)\n**PV**: 33022\n**Attaque**: 2581\n**Défense**: 3521\n**Récupération**:2057", inline=False)

		await message.channel.send(embed=embed)


		#######################################
		############   Sun Wukong  ############
		#######################################

	if any([message.content.startswith (item) for item in ['Sun','FeuSun','Wukong','FeuWukong','TopSun']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558099710607360/Qitiandasheng_Large.jpeg", color=0xffffff)
		embed.set_author(name="#666 Sun Wukong (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558099710607360/Qitiandasheng_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Défense réduite  70% 2 tours\n(???)\n**Actif**: Frappe Courageuse\n(Dmg +25%)\n**PV**: 28262\n**Attaque**: 3473\n**Défense**: 2479\n**Récupération**:2418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sun','EauSun','Wukong','EauWukong']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558101430272000/QitiandashengB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#667 Sun Wukong (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558101430272000/QitiandashengB_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%,(Clan)\n**Passif**: Siphon de PV  \n(Dmg +30%)\n**Actif**: Siphon de PV (Allies) \n(Dmg +30%)\n**PV**: 29801\n**Attaque**: 3323\n**Défense**: 2799\n**Récupération**:2363", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sun','BoisSun','Wukong','BoisWukong']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/552558126969126927/QitiandashengG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#668 Sun Wukong (Bois)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/552558126969126927/QitiandashengG_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +50~55%,(Clan)\n**Passif**: Défense réduite 70% 3 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 33328\n**Attaque**: 3405\n**Défense**: 2213\n**Récupération**:2329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sun','LightSun','Wukong','LightWukong']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558121621651537/QitiandashengW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#669 Sun Wukong (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558121621651537/QitiandashengW_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Défense réduite 100% 2 tours\n(Dmg +20%, +1 tour)\n**Actif**: Choc 70% 2 tour\n(Dmg +25%, Taux : +10%)\n**PV**: 43118\n**Attaque**: 2705\n**Défense**: 2494\n**Récupération**:2269", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sun','DarkSun','Wukong','DarkWukong']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558128588128277/QitiandashengD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#670 Sun Wukong (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558128588128277/QitiandashengD_Large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +50~55%, (Clan)\n**Passif**: Sceau 100% 3 tours\n(Dmg +30%)\n**Actif**: Étourdissement 70% 2 tour\n(Dmg +25%, Taux: +10%)\n**PV**: 32153\n**Attaque**: 2743\n**Défense**: 2747\n**Récupération**:2576", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Sura     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Sura','FeuSura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560713479094282/Varuna_large.jpeg", color=0xffffff)
		embed.set_author(name="#671 Sura (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560713479094282/Varuna_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Boost de moral 20% SP\n(Dmg +15%, +Effect.: +10%)\n**Actif**: Adrénaline (Allies) 20% de ses PV\n(Dmg +30%)\n**PV**: 22984\n**Attaque**: 3262\n**Défense**: 2084\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sura','EauSura','TopSura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560720391438336/VarunaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#672 Sura (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560720391438336/VarunaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR +15~20%\n**Passif**: Étourdissement (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Prédateur 40%\n(Dmg +30%)\n**PV**: 38412\n**Attaque**: 2044\n**Défense**: 2017\n**Récupération**:2303", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sura','BoisSura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557613238137651201/VarunaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#673 Sura (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557613238137651201/VarunaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR +15~20%\n**Passif**: Sceau 70% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Nécrose 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 29787\n**Attaque**: 2288\n**Défense**: 3105\n**Récupération**:1771", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sura','LightSura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560752620470292/VarunaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#674 Sura (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560752620470292/VarunaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR +15~20%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Adrénaline (Allies) 20% de ses PV\n(Dmg +30%)\n**PV**: 31772\n**Attaque**: 2532\n**Défense**: 2542\n**Récupération**:1671", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Sura','DarkSura']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560725671804947/VarunaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#675 Sura (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560725671804947/VarunaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR +15~20%\n**Passif**: Siphon de PV \n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 25367\n**Attaque**: 3126\n**Défense**: 2343\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Tai      #############
		#######################################

	if any([message.content.startswith (item) for item in ['Tai','LightTai']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559448187469824/Spark_large.jpeg", color=0xffffff)
		embed.set_author(name="#679 Tai (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559448187469824/Spark_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Choc 60% 1 tour\n(Dmg: +25%, Taux: +10%, +1 tour)\n**Actif**: Choc 80% 1 tour\n(Dmg: +25%, +1 tour)\n**PV**: 28667\n**Attaque**: 1722\n**Défense**: 1854\n**Récupération**:1664", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tai','DarkTai']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559450104528907/SparkD_large.jpeg", color=0xffffff)
		embed.set_author(name="#680 Tai (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559450104528907/SparkD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +30~35%\n**Passif**: Silence 60% 1 tour\n(Dmg: +25%, Taux: +10%, +1 tour)\n**Actif**: Chasseur 50%\n(Dmg: +30%)\n**PV**: 24931\n**Attaque**: 2486\n**Défense**: 2036\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Tanya    ##############
		#######################################

	if any([message.content.startswith (item) for item in ['Tany','FeuTany']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560089752404003/Talia_large.jpeg", color=0xffffff)
		embed.set_author(name="#681 Tanya (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560089752404003/Talia_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Dungeon)\n**Passif**: Prédateur (bois) 50%\n(No skillbooks)\n**Actif**: Prédateur (bois) 100%\n(No skillbooks)\n**PV**: 24414\n**Attaque**: 2622\n**Défense**: 1832\n**Récupération**:1696", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tany','LightTany']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560093690986506/TaliaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#684 Tanya (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560093690986506/TaliaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35% (Dungeon)\n**Passif**: Merciless  Strike\n(No skillbooks)\n**Actif**: Merciless  Strike\n(No skillbooks)\n**PV**: 27608\n**Attaque**: 3058\n**Défense**: 2309\n**Récupération**:2050", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tany','DarkTany']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560091874721803/TaliaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#685 Tanya (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560091874721803/TaliaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%(Dungeon)\n**Passif**: Provocation intrépide 80% 2 tours\n(No skillbooks)\n**Actif**: Silence 100% 1 tour\n(No skillbooks)\n**PV**: 30822\n**Attaque**: 2050\n**Défense**: 3099\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Thor     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Thor','FeuThor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560207851552800/ThunderthorR_large.jpeg", color=0xffffff)
		embed.set_author(name="#686 Thor (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560207851552800/ThunderthorR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**Actif**: Défense réduite 50% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 26865\n**Attaque**: 2220\n**Défense**: 3037\n**Récupération**:2411", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Thor','EauThor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560182400385064/ThunderthorB_large.jpeg", color=0xffffff)
		embed.set_author(name="#687 Thor (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560182400385064/ThunderthorB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Boost de moral 20% SP\n(Dmg +15%, +Effect.: +5%)\n**Actif**: Prédateur 30%\n(Dmg +20%, Taux: +20%)\n**PV**: 26484\n**Attaque**: 3003\n**Défense**: 2111\n**Récupération**:2179", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Thor','BoisThor','TopThor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560189275111424/ThunderthorG_large.jpeg", color=0xffffff)
		embed.set_author(name="#688 Thor (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560189275111424/ThunderthorG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Def +30~35%\n**Passif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**Actif**: Aveuglement (On crit) 2 tours\n(Dmg +25%)\n**PV**: 30819\n**Attaque**: 2648\n**Défense**: 2535\n**Récupération**:1603", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Thor','LightThor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560180529725450/Thunderthor_large.jpeg", color=0xffffff)
		embed.set_author(name="#689 Thor (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560180529725450/Thunderthor_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Def +30~35%\n**Passif**: Choc 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 41374\n**Attaque**: 1717\n**Défense**: 2494\n**Récupération**:1894", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Thor','DarkThor']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560187173765121/ThunderthorD_large.jpeg", color=0xffffff)
		embed.set_author(name="#690 Thor (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560187173765121/ThunderthorD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Def +30~35%\n**Passif**: Défense réduite (On crit) 2 tours\n(Dmg +25%)\n**Actif**: Frappe Courageuse (On crit)\n(Dmg +20%)\n**PV**: 25538\n**Attaque**: 2887\n**Défense**: 2411\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Tigar    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Tig','FeuTig']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560257759445013/Tigris_large.jpeg", color=0xffffff)
		embed.set_author(name="#691 Tigar (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560257759445013/Tigris_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 3 tours\n(Dmg +25%, Taux: +10%)\n**Actif**: Nécrose 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 24445\n**Attaque**: 2832\n**Défense**: 2862\n**Récupération**:2685", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tig','EauTig']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560270409728010/TigrisB_large.jpeg", color=0xffffff)
		embed.set_author(name="#692 Tigar (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560270409728010/TigrisB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Provocation 70% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Défense réduite 70% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26729\n**Attaque**: 2193\n**Défense**: 3051\n**Récupération**:2411", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tig','BoisTig','TopTig']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560280023072779/TigrisG_large.jpeg", color=0xffffff)
		embed.set_author(name="#693 Tigar (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560280023072779/TigrisG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Talent Var**: Att +30~35%\n**Passif**: Predateur 30%\n(Dgt +30%)\n**Actif**: Etourdissement 60% 1 tour\n(Dgt +15%, Taux: +10%)\n**PV**: 30625\n**Attaque**: 3139\n**Défense**: 1900\n**Recuperation**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tig','LightTig']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560283395031054/TigrisW_large.jpeg", color=0xffffff)
		embed.set_author(name="#694 Tigar (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560283395031054/TigrisW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Sommeil (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 29521\n**Attaque**: 3126\n**Défense**: 2118\n**Récupération**:2002", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Tig','DarkTig']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560274083676160/TigrisD_large.jpeg", color=0xffffff)
		embed.set_author(name="#695 Tigar (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560274083676160/TigrisD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Vague martiale\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Attaque réduite 80% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 37009\n**Attaque**: 1983\n**Défense**: 2010\n**Récupération**:2316", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Crapora    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Crapo','LightCrapo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560349400793109/ToadkingW_large.jpeg", color=0xffffff)
		embed.set_author(name="#699 Crapora (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560349400793109/ToadkingW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Boost de moral 25% SP\n(No skillbooks)\n**Actif**: Nécrose x3 60% 1 tours\n(No skillbooks)\n**PV**: 28817\n**Attaque**: 2491\n**Défense**: 2311\n**Récupération**:2147", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Crapo','DarkCrapo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560347240988702/Toadking_large.jpeg", color=0xffffff)
		embed.set_author(name="#700 Crapora (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560347240988702/Toadking_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**Actif**: Nécrose x2 70% 2 tours\n(No skillbooks)\n**PV**: 30761\n**Attaque**: 1920\n**Défense**: 3187\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Truffel    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Truf','FeuTruf']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558611822542862/Rutella_large.jpeg", color=0xffffff)
		embed.set_author(name="#701 Truffel (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558611822542862/Rutella_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Def +30~35% (Clan)\n**Passif**: Adrénaline 30% de ses PV\n(No skillbooks)\n**Actif**: Pétrification 60% 1 tour\n(No skillbooks)\n**PV**: 34898\n**Attaque**: 1499\n**Défense**: 1806\n**Récupération**:1724", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Truf','DarkTruf']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558615517593600/RutellaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#705 Truffel (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558615517593600/RutellaD_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Def +30~35% (Clan)\n**Passif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**Actif**: Attaque réduite 60% 2 tours\n(No skillbooks)\n**PV**: 28387\n**Attaque**: 1750\n**Défense**: 2744\n**Récupération**:1410", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Valkyrie   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Valk','FeuValk','TopValk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559037137420298/SigrunR_large.jpeg", color=0xffffff)
		embed.set_author(name="#706 Valkyrie (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559037137420298/SigrunR_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Boost de moral 50% SP\n(Dmg +20%)\n**Actif**: Étourdissement 80% 1 tour\n(Dmg +25%, Taux: +10%)\n**PV**: 35443\n**Attaque**: 2703\n**Défense**: 2842\n**Récupération**:2372", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Valk','EauValk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559025477386242/Sigrun_large.jpeg", color=0xffffff)
		embed.set_author(name="#707 Valkyrie (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559025477386242/Sigrun_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Att +40~45%(League)\n**Passif**: Prédateur 50%\n(Dmg +20%)\n**Actif**: Défense réduite 100% 2 tour\n(Dmg +25%)\n**PV**: 25408\n**Attaque**: 3671\n**Défense**: 2581\n**Récupération**:2397", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Valk','BoisValk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559035199782928/SigrunG_large.jpeg", color=0xffffff)
		embed.set_author(name="#708 Valkyrie (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559035199782928/SigrunG_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg +15%, +Effect.: +10%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 30288\n**Attaque**: 2893\n**Défense**: 2937\n**Récupération**:2624", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Valk','LightValk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559039393824786/SigrunW_large.jpeg", color=0xffffff)
		embed.set_author(name="#709 Valkyrie (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559039393824786/SigrunW_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Att +40~45%(League)\n**Passif**: Choc 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Réduction de dégâts 50% 2 tours (allies)\n(???)\n**PV**: 31003\n**Attaque**: 3104\n**Défense**: 2808\n**Récupération**:2515", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Valk','DarkValk']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559034394345474/SigrunD_large.jpeg", color=0xffffff)
		embed.set_author(name="#710 Valkyrie (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559034394345474/SigrunD_large.jpeg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Att +40~45%(League)\n**Passif**: Étourdissement 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Silence 100% 2 tours\n(???)\n**PV**: 48498\n**Attaque**: 2167\n**Défense**: 2357\n**Récupération**:2194", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Vampire    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Vamp','FeuVamp','TopVamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557375907692584/NosferatuR_large.jpeg", color=0xffffff)
		embed.set_author(name="#711 Vampire (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557375907692584/NosferatuR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline (On crit) 50% de ses PV\n(No skillbooks)\n**Actif**: Chasseur 50%\n(No skillbooks)\n**PV**: 26368\n**Attaque**: 3024\n**Défense**: 2254\n**Récupération**:1662", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vamp','EauVamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557372388933643/NosferatuB_large.jpeg", color=0xffffff)
		embed.set_author(name="#712 Vampire (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557372388933643/NosferatuB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Prédateur 30%\n(No skillbooks)\n**Actif**: Sommeil 80% 1 tour\n(No skillbooks)\n**PV**: 26416\n**Attaque**: 3262\n**Défense**: 2043\n**Récupération**:2159", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vamp','BoisVamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557374204936192/NosferatuG_large.jpeg", color=0xffffff)
		embed.set_author(name="#713 Vampire (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557374204936192/NosferatuG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Resist +15~20%\n**Passif**: Boost de moral 20% SP\n(No skillbooks)\n**Actif**: Nécrose x2 80% 1 tour\n(No skillbooks)\n**PV**: 31629\n**Attaque**: 2205\n**Défense**: 2352\n**Récupération**:2236", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vamp','LightVamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557377837334548/NosferatuW_large.jpeg", color=0xffffff)
		embed.set_author(name="#714 Vampire (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557377837334548/NosferatuW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Resist +15~20%\n**Passif**: Siphon de PV \n(No skillbooks)\n**Actif**: Défense réduite 70% 2 tours\n(No skillbooks)\n**PV**: 27969\n**Attaque**: 3310\n**Défense**: 2002\n**Récupération**:2036", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vamp','DarkVamp']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552557370476068867/Nosferatu_large.jpeg", color=0xffffff)
		embed.set_author(name="#715 Vampire (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552557370476068867/Nosferatu_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Nécrose x3 80% 1 tour\n(No skillbooks)\n**Actif**: Attaque réduite 70% 2 tours\n(No skillbooks)\n**PV**: 30672\n**Attaque**: 1873\n**Défense**: 3167\n**Récupération**:2179", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Venus    ##############
		#######################################

	if any([message.content.startswith (item) for item in ['Venu','LightVenu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551394285060106/Aphrodite_large.jpeg", color=0xffffff)
		embed.set_author(name="#719 Venus (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551394285060106/Aphrodite_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Resist +15~20%\n**Passif**: Adrénaline 20% de ses PV\n(No skillbooks)\n**Actif**: Bouclier (PV) 3 tours\n(No skillbooks)\n**PV**: 37452\n**Attaque**: 1881\n**Défense**: 2521\n**Récupération**:2024", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Venu','DarkVenu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551398823165973/AphroditeD_large.jpeg", color=0xffffff)
		embed.set_author(name="#720 Venus (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551398823165973/AphroditeD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Resist +15~20%\n**Passif**: Attaque réduite 80% 2 tours\n(No skillbooks)\n**Actif**: Attaque augmentée  3 tours\n(No skillbooks)\n**PV**: 26859\n**Attaque**: 2118\n**Défense**: 3153\n**Récupération**:2479", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Verde     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Verde','FeuVerde','TopVerde']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553575427866650/DruidR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#721 Verde (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553575427866650/DruidR_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Aveuglement 70% 2 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Frappe Courageuse\n(Dmg +20%)\n**PV**: 27713\n**Attaque**: 2573\n**Défense**: 2576\n**Récupération**:2311", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Verde','EauVerde']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553571829153792/DruidB_Large.jpeg", color=0xffffff)
		embed.set_author(name="#722 Verde (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553571829153792/DruidB_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Pétrification 100% 1 tour\n(Dmg +25%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +20%)\n**PV**: 32051\n**Attaque**: 2491\n**Défense**: 2501\n**Récupération**:1671", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Verde','BoisVerde']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553568457064448/Druid_Large.jpeg", color=0xffffff)
		embed.set_author(name="#723 Verde (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553568457064448/Druid_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Attaque réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +15%)\n**PV**: 44160\n**Attaque**: 1894\n**Défense**: 1881\n**Récupération**:1717", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Verde','LightVerde']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553598832082948/DruidW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#724 Verde (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553598832082948/DruidW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Siphon de PA 30%\n(Dmg +20%, Taux: +5%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%)\n**PV**: 38848\n**Attaque**: 1813\n**Défense**: 2337\n**Récupération**:2194", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Verde','DarkVerde']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553575994359848/DruidD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#725 Verde (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553575994359848/DruidD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Nécrose x3 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Silence 80% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 30979\n**Attaque**: 2813\n**Défense**: 2533\n**Récupération**:1737", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Victoria   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Vic','FeuVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551619422846983/AthenaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#726 Victoria (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551619422846983/AthenaR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Provocation intrépide 100% 1 tour\n(???)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 30516\n**Attaque**: 1900\n**Défense**: 3310\n**Récupération**:2172", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vic','EauVic','TopVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551603689750532/AthenaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#728 Victoria (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551603689750532/AthenaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 27097\n**Attaque**: 3126\n**Défense**: 2213\n**Récupération**:1989", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vic','BoisVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551611847933953/AthenaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#730 Victoria (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551611847933953/AthenaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Att +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +10%, Taux: +30%)\n**PV**: 42478\n**Attaque**: 2085\n**Défense**: 1860\n**Récupération**:1853", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vic','LightVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551588372152343/Athena_large.jpeg", color=0xffffff)
		embed.set_author(name="#732 Victoria (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551588372152343/Athena_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 29889\n**Attaque**: 2295\n**Défense**: 3296\n**Récupération**:1777", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Vic','DarkVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552551609352060982/AthenaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#734 Victoria (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552551609352060982/AthenaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Att +30~35%\n**Passif**: Étourdissement (On crit) 1 tour\n(Dmg +30%)\n**Actif**: Défense réduite 60% 3 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 30580\n**Attaque**: 2165\n**Défense**: 2481\n**Récupération**:2304", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		########### Victoria S Evo ############
		#######################################

	if any([message.content.startswith (item) for item in ['FeuVic','SVic','FeuSVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557613575087194154/SuperNikeR_large.jpeg", color=0xffffff)
		embed.set_author(name="#727 Victoria SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557613575087194154/SuperNikeR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Provocation 100% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**PV**: 33573\n**Attaque**: 2097\n**Défense**: 3671\n**Récupération**:2397", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauVic','SVic','EauSVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559897544228899/SuperNikeB_large.jpeg", color=0xffffff)
		embed.set_author(name="#729 Victoria SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559897544228899/SuperNikeB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 29814\n**Attaque**: 3473\n**Défense**: 2445\n**Récupération**:2193", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisVic','SVic','BoisSVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559900488630283/SuperNikeG_large.jpeg", color=0xffffff)
		embed.set_author(name="#731 Victoria SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559900488630283/SuperNikeG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Étourdissement 70% 1 tour\n(Dmg +20%, tour: +1)\n**Actif**: Étourdissement 70% 1 tour\n(Dmg +10%, Taux: +30%)\n**PV**: 46890\n**Attaque**: 2296\n**Défense**: 2051\n**Récupération**:2044", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightVic','SVic','LightSVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559894490775553/SuperNike_large.jpeg", color=0xffffff)
		embed.set_author(name="#733 Victoria SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559894490775553/SuperNike_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Agression (Def)\n(Dmg +20%)\n**Actif**: Agression (Def)\n(Dmg +20%)\n**PV**: 32885\n**Attaque**: 2533\n**Défense**: 3657\n**Récupération**:1961", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkVic','SVic','DarkSVic']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559898974617612/SuperNikeD_large.jpeg", color=0xffffff)
		embed.set_author(name="#735 Victoria SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559898974617612/SuperNikeD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Att +30~35%\n**Passif**: Étourdissement (On crit) 1 tour\n(Dmg +30%)\n**Actif**: Défense réduite 60% 3 tours\n(Dmg +15%, Taux: +10%)\n**PV**: 33664\n**Attaque**: 2392\n**Défense**: 2739\n**Récupération**:2548", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Wendigo   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Wend','FeuWend']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557221589649850368/GargantuanR_Large.jpeg", color=0xffffff)
		embed.set_author(name="#736 Wendigo (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557221589649850368/GargantuanR_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Prédateur 30%\n(Dmg: +35%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg: +35%)\n**PV**: 27077\n**Attaque**: 2547\n**Défense**: 1559\n**Récupération**: 1784", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Wend','EauWend','TopWendi']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554143064129537/Gargantuan_Large.jpeg", color=0xffffff)
		embed.set_author(name="#737 Wendigo (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554143064129537/Gargantuan_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Adrénaline 20% de ses PV\n(Dmg: +20% Effect.: +5%)\n**Actif**: Provocation 50% 2 tours\n(Dmg: +15% Taux: +30%)\n**PV**: 27758\n**Attaque**: 1668\n**Défense**: 2615\n**Récupération**: 2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Wend','BoisWend']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554147136798731/GargantuanG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#738 Wendigo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554147136798731/GargantuanG_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Boost de moral 20%\n(Dmg: +15% Effect.: +10%)\n**Actif**: Étourdissement 60% 1 tour\n(Dmg: +15% Taux: +30%)\n**PV**: 27182\n**Attaque**: 2396\n**Défense**: 1582\n**Récupération**: 1807", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Wend','LightWend']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554150475595786/GargantuanW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#739 Wendigo (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554150475595786/GargantuanW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Frappe Courageuse (On crit)\n(Dmg: +20%)\n**Actif**: Attaque réduite 60% 2 tours\n(Dmg: +10% Taux: +20%)\n**PV**: 27063\n**Attaque**: 3105\n**Défense**: 2247\n**Récupération**: 2125", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Wend','DarkWend']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554144934789150/GargantuanD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#740 Wendigo (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554144934789150/GargantuanD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45% (Même élément)\n**Passif**: Vengeance\n(Dmg: +35%)\n**Actif**: Adrénaline (Allies) 10% de ses PV\n(Dmg: +35%)\n**PV**: 30492\n**Attaque**: 2478\n**Défense**: 2406\n**Récupération**: 2331", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Fenrir    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Fenrir','FeuFenrir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557221260476678162/LunaticFenrirR_large.jpeg", color=0xffffff)
		embed.set_author(name="#741 Fenrir (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557221260476678162/LunaticFenrirR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Siphon de PV (allies)\n(Dmg +35%)\n**Actif**: Siphon de PV , Greatly)\n(Dmg +35%)\n**PV**: 27015\n**Attaque**: 3058\n**Défense**: 2295\n**Récupération**:2138", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenrir','EauFenrir','TopFenrir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555961504497674/LunaticFenrir_large.jpeg", color=0xffffff)
		embed.set_author(name="#743 Fenrir (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555961504497674/LunaticFenrir_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +10%, Taux: +10%tour: +1)\n**Actif**: Pétrification 80% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 39611\n**Attaque**: 2221\n**Défense**: 1840\n**Récupération**:2058", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenrir','BoisFenrir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555970912452608/LunaticFenrirG_large.jpeg", color=0xffffff)
		embed.set_author(name="#745 Fenrir (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555970912452608/LunaticFenrirG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR -15~20%\n**Passif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux +20%)\n**PV**: 31496\n**Attaque**: 2036\n**Défense**: 2921\n**Récupération**: 2322", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenrir','LightFenrir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555974851035137/LunaticFenrirW_large.jpeg", color=0xffffff)
		embed.set_author(name="#747 Fenrir (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555974851035137/LunaticFenrirW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%\n**Passif**: Défense réduite 100% 2 tours\n(Dmg +15%, Taux: +20%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 30730\n**Attaque**: 2607\n**Défense**: 2488\n**Récupération**:2066", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Fenrir','DarkFenrir']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555968890667018/LunaticFenrirD_large.jpeg", color=0xffffff)
		embed.set_author(name="#749 Fenrir (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555968890667018/LunaticFenrirD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: CR -15~20%\n**Passif**: Traqueur 30%\n(Dmg +20%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +20%, Taux: +20%)\n**PV**: 29964\n**Attaque**: 3295\n**Défense**: 2509\n**Récupération**:2300", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Fenir S Evo  ############
		#######################################

	if any([message.content.startswith (item) for item in ['FeuFenrir','SFenrir','FeuSFenrir']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728599722131457/SuperLunaticFenrirR_large.jpg", color=0xffffff)
		embed.set_author(name="#742 Fenrir SE (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728599722131457/SuperLunaticFenrirR_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Siphon de PV \n(no skillbooks)\n**Actif**: Siphon de PV , Greatly)\n(no skillbooks)\n**PV**: 29726\n**Attaque**: 3398\n**Défense**: 2533\n**Récupération**: 2356", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauFenrir','SFenrir','EauSFenrir']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728594302828554/SuperLunaticFenrir_large.jpg", color=0xffffff)
		embed.set_author(name="#744 Fenrir SE (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728594302828554/SuperLunaticFenrir_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: CR -15~20%\n**Passif**: Étourdissement 80% 1 tour\n(no skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(no skillbooks)\n**PV**: 43737\n**Attaque**: 2446\n**Défense**: 2024\n**Récupération**: 2269", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisFenrir','SFenrir','BoisSFenrir']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728597876375552/SuperLunaticFenrirG_large.jpg", color=0xffffff)
		embed.set_author(name="#746 Fenrir SE (Bois)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728597876375552/SuperLunaticFenrirG_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: CR -15~20%\n**Passif**: Pétrification 80% 1 tour\n(Dmg +15%, Taux: +20%)\n**Actif**: Sommeil 70% 2 tours\n(Dmg +20%, Taux +20%)\n**PV**: 34646\n**Attaque**: 2486\n**Défense**: 3248\n**Récupération**: 2336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightFenrir','SFenrir','LightSFenrir']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728601361973248/SuperLunaticFenrirW_large.jpg", color=0xffffff)
		embed.set_author(name="#748 Fenrir SE (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728601361973248/SuperLunaticFenrirW_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: CR -15~20%\n**Passif**: Défense réduite 100% 2 tours\n(no skillbooks)\n**Actif**: Choc 70% 1 tour\n(no skillbooks)\n**PV**: 33828\n**Attaque**: 2876\n**Défense**: 2745\n**Récupération**: 2282", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkFenrir','SFenrir','DarkSFenrir']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/552550283885019166/626728596160905218/SuperLunaticFenrirD_large.jpg", color=0xffffff)
		embed.set_author(name="#701 Fenrir SE (dark)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/552550283885019166/626728596160905218/SuperLunaticFenrirD_large.jpg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: CR -15~20%\n**Passif**: Traqueur 30%\n(no skillbooks)\n**Actif**: Traqueur 30%\n(no skillbooks)\n**PV**: 29971\n**Attaque**: 3330\n**Défense**: 2520\n**Récupération**: 2309", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Lupio    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Lupio','LightLupio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552319598854144/CanisW_large.jpeg", color=0xffffff)
		embed.set_author(name="#754 Lupio (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552319598854144/CanisW_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Att +30~35% (ToC)\n**Passif**: Brise-Bonus 100%\n(Dmg: +35%)\n**Actif**: Choc 80% 1 tour\n(Dmg: +20% Taux: +15%)\n**PV**: 28731\n**Attaque**: 1873\n**Défense**: 2765\n**Récupération**: 1342", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lupio','DarkLupio']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552552318323654666/Canis_large.jpeg", color=0xffffff)
		embed.set_author(name="#755 Lupio (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552552318323654666/Canis_large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Att +30~35% (ToC)\n**Passif**: Agression (PV)\n(Dmg: +35%)\n**Actif**: Agression (PV)\n(Dmg: +35%)\n**PV**: 35817\n**Attaque**: 1676\n**Défense**: 1996\n**Récupération**: 1295", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Lombrix   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Lombrix','FeuLombrix']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554864539074560/HorntailR_large.jpeg", color=0xffffff)
		embed.set_author(name="#756 Lombrix (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554864539074560/HorntailR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Étourdissement 50% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 34898\n**Attaque**: 1404\n**Défense**: 1445\n**Récupération**:1758", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lombrix','EauLombrix']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554862555168778/HorntailB_large.jpeg", color=0xffffff)
		embed.set_author(name="#757 Lombrix (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554862555168778/HorntailB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: Resist +10~15%\n**Passif**: Nécrose 50% 2 tours\n(No skillbooks)\n**Actif**: Pétrification 80% 1 tour\n(No skillbooks)\n**PV**: 37792\n**Attaque**: 1132\n**Défense**: 1853\n**Récupération**:1363", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Lombrix','BoisLombrix']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552554860990562325/Horntail_large.jpeg", color=0xffffff)
		embed.set_author(name="#758 Lombrix (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552554860990562325/Horntail_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: Resist +10~15%\n**Passif**: Attaque réduite 60% 2 tour\n(No skillbooks)\n**Actif**: Récupération réduite 80% 2 tours\n(No skillbooks)\n**PV**: 25742\n**Attaque**: 2281\n**Défense**: 1525\n**Récupération**:1607", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Poulpo    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Poulpo','FeuPoulpo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561157995495449/WumewraR_large.jpeg", color=0xffffff)
		embed.set_author(name="#761 Poulpo (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561157995495449/WumewraR_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Feu Chasseur 50%\n(No skillbooks)\n**Actif**: Nécrose 40% 2 tours\n(No skillbooks)\n**PV**: 28377\n**Attaque**: 1696\n**Défense**: 2615\n**Récupération**:1219", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Poulpo','EauPoulpo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561154195456020/Wumewra_large.jpeg", color=0xffffff)
		embed.set_author(name="#762 Poulpo (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561154195456020/Wumewra_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Chasseur (eau) 50%\n(No skillbooks)\n**Actif**: Soif 40% -10% 1 tour\n(No skillbooks)\n**PV**: 28561\n**Attaque**: 1737\n**Défense**: 2404\n**Récupération**:1287", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Poulpo','BoisPoulpo']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561155378380801/WumewraG_large.jpeg", color=0xffffff)
		embed.set_author(name="#763 Poulpo (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561155378380801/WumewraG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Chasseur (bois) 50%\n(No skillbooks)\n**Actif**: Pétrification 40% 1 tour\n(No skillbooks)\n**PV**: 35838\n**Attaque**: 1275\n**Défense**: 1751\n**Récupération**:1574", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Yaksha    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Yak','FeuYak','TopYak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555400504016906/Kubera_large.jpeg", color=0xffffff)
		embed.set_author(name="#766 Yaksha (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555400504016906/Kubera_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Attaque réduite 80% 2 tour\n(Dmg +20%, Taux: +10%)\n**Actif**: Aveuglement 70% 3 tours\n(Dmg +10%, Taux: +30%)\n**PV**: 30093\n**Attaque**: 2322\n**Défense**: 3037\n**Récupération**:1852", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yak','EauYak','TopYak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555403435573261/KuberaB_large.jpeg", color=0xffffff)
		embed.set_author(name="#767 Yaksha (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555403435573261/KuberaB_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Traqueur 30%\n(Dmg +15%, Taux: +20%)\n**Actif**: Traqueur 30%\n(Dmg +10%, Taux: +20%)\n**PV**: 29589\n**Attaque**: 3153\n**Défense**: 2152\n**Récupération**:1982", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yak','BoisYak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555467264491551/KuberaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#768 Yaksha (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555467264491551/KuberaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Sommeil (On crit) 2 tours\n(Dmg +30%)\n**Actif**: Chasseur 50%\n(Dmg +30%)\n**PV**: 29869\n**Attaque**: 3126\n**Défense**: 2125\n**Récupération**:2002", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yak','LightYak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555468766052404/KuberaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#769 Yaksha (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555468766052404/KuberaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 3 tours\n(Dmg +15%, Taux: +10%)\n**Actif**: Prédateur 30%\n(Dmg +30%)\n**PV**: 26559\n**Attaque**: 3269\n**Défense**: 2084\n**Récupération**:2193", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yak','DarkYak']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552555464580399104/KuberaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#770 Yaksha (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552555464580399104/KuberaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Adrénaline (Allies) 10% de ses PV\n(Dmg +20%, +Effect.: +5%)\n**Actif**: Silence 80% 2 tours\n(Dmg +10%, Taux: +20%)\n**PV**: 30696\n**Attaque**: 2641\n**Défense**: 2542\n**Récupération**:2331", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Yeti     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Yeti','FeuYeti']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772034028252954635/Yeti1.png", color=0xffffff)
		embed.set_author(name="#771 Yeti (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772034028252954635/Yeti1.png")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%,(Donjons)\n**Passif**: Chasseur 40%\n(Dmg +25%)\n**Actif**: Aveuglement 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28200\n**Attaque**: 2785\n**Défense**: 1614\n**Récupération**:1682", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yeti','EauYeti','TopYeti']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772034031234842624/Yeti2.png", color=0xffffff)
		embed.set_author(name="#772 Yeti (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772034031234842624/Yeti2.png")
		embed.add_field(name="★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45% (Donjons)\n**Passif**: Attaque réduite 60% 2 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 28840\n**Attaque**: 1989\n**Défense**: 2581\n**Récupération**:1457", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yeti','BoisYeti']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558664381366283/SasquatchG_Large.jpeg", color=0xffffff)
		embed.set_author(name="#773 Yeti (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558664381366283/SasquatchG_Large.jpeg")
		embed.add_field(name="★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Provocation 80% 1 tour\n(Dmg +15%, tour: +1)\n**Actif**: Nécrose x2 60% 1 tours\n(Dmg +20%, tour: +1)\n**PV**: 33434\n**Attaque**: 1894\n**Défense**: 1976\n**Récupération**:1499", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yeti','LightYeti']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558670659977266/SasquatchW_Large.jpeg", color=0xffffff)
		embed.set_author(name="#774 Yeti (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558670659977266/SasquatchW_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Boost de moral 30%\n(Dmg +25%)\n**Actif**: Choc 70% 1 tour\n(Dmg +20%, Taux: +10%)\n**PV**: 28241\n**Attaque**: 2418\n**Défense**: 3133\n**Récupération**:1941", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yeti','DarkYeti']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552558628142448642/SasquatchD_Large.jpeg", color=0xffffff)
		embed.set_author(name="#775 Yeti (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552558628142448642/SasquatchD_Large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%(Donjons)\n**Passif**: Étourdissement 80% 1 tour\n(Dmg +15%, Taux: +10%)\n**Actif**: Sceau 70% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 35245\n**Attaque**: 2192\n**Défense**: 2134\n**Récupération**:2025", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Yuki     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Yuki','FeuYuki','TopYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561323419107342/YukiR_large.jpeg", color=0xffffff)
		embed.set_author(name="#776 Yuki (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561323419107342/YukiR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +30%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 26947\n**Attaque**: 3105\n**Défense**: 2240\n**Récupération**:2118", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yuki','EauYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561274509197332/Yuki_large.jpeg", color=0xffffff)
		embed.set_author(name="#778 Yuki (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561274509197332/Yuki_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Nécrose x2 70% 1 tour\n(Taux: +25%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 36982\n**Attaque**: 2024\n**Défense**: 1976\n**Récupération**:2316", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yuki','BoisYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561278695243786/YukiG_large.jpeg", color=0xffffff)
		embed.set_author(name="#780 Yuki (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561278695243786/YukiG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Faiblesse exposée 80% 2 tour\n(???)\n**Actif**: Faiblesse exposée 80% 2 tours\n(???)\n**PV**: 28857\n**Attaque**: 2546\n**Défense**: 2345\n**Récupération**:2140", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yuki','LightYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561325142966302/YukiW_large.jpeg", color=0xffffff)
		embed.set_author(name="#782 Yuki (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561325142966302/YukiW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Choc 80% 2 Turm\n(???)\n**Actif**: Choc 70% 2 tours\n(???)\n**PV**: 25156\n**Attaque**: 3153\n**Défense**: 2309\n**Récupération**:2138", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Yuki','DarkYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559989881831464/SuperYukinaD_large.jpeg", color=0xffffff)
		embed.set_author(name="#785 Yuki (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559989881831464/SuperYukinaD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PA 30%\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Taux: +20%, tour: +1)\n**PV**: 44023\n**Attaque**: 2603\n**Défense**: 1949\n**Récupération**:2065", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Yuki S Evo  #############
		#######################################

	if any([message.content.startswith (item) for item in ['FeuYuki','SYuki','FeuSYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559994025934878/SuperYukinaR_large.jpeg", color=0xffffff)
		embed.set_author(name="#777 Yuki SE (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559994025934878/SuperYukinaR_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Défense réduite 70% 2 tours\n(Dmg +30%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 29651\n**Attaque**: 3446\n**Défense**: 2472\n**Récupération**:2336", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['EauYuki','SYuki','EauSYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559987629490176/SuperYukina_large.jpeg", color=0xffffff)
		embed.set_author(name="#779 Yuki SE (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559987629490176/SuperYukina_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Nécrose x2 70% 1 tour\n(Taux: +25%)\n**Actif**: Nécrose x2 60% 2 tours\n(Dmg +15%, Taux: +20%)\n**PV**: 40849\n**Attaque**: 2228\n**Défense**: 2174\n**Récupération**:2548", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['BoisYuki','SYuki','BoisSYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552559992348213268/SuperYukinaG_large.jpeg", color=0xffffff)
		embed.set_author(name="#781 Yuki SE (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552559992348213268/SuperYukinaG_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Faiblesse exposée 80% 2 tour\n(???)\n**Actif**: Faiblesse exposée 80% 2 tours\n(???)\n**PV**: 31764\n**Attaque**: 2808\n**Défense**: 2589\n**Récupération**:2364", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['LightYuki','SYuki','LightSYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552560018860408842/SuperYukinaW_large.jpeg", color=0xffffff)
		embed.set_author(name="#783 Yuki SE (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552560018860408842/SuperYukinaW_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: \n**Lead**: Dégâts critiques +40~45%\n**Passif**: Choc 80% 2 Turm\n(???)\n**Actif**: Choc 70% 2 tours\n(???)\n**PV**: 27676\n**Attaque**: 3500\n**Défense**: 2547\n**Récupération**:2356", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['DarkYuki','SYuki','DarkSYuki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561270834987008/YukiD_large.jpeg", color=0xffffff)
		embed.set_author(name="#784 Yuki SE (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561270834987008/YukiD_large.jpeg")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégâts critiques +40~45%\n**Passif**: Siphon de PA 30%\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Taux: +20%, tour: +1)\n**PV**: 39869\n**Attaque**: 2364\n**Défense**: 1772\n**Récupération**:1874", inline=False)

		await message.channel.send(embed=embed)	 

		#######################################
		############     Zarid    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Zari','FeuZari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561371620048896/Zalisk_large.jpeg", color=0xffffff)
		embed.set_author(name="#786 Zarid (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561371620048896/Zalisk_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Sommeil 60% 1 tour\n(No skillbooks)\n**Actif**: Fatigue 80% 2 tours\n(No skillbooks)\n**PV**: 22514\n**Attaque**: 2574\n**Défense**: 1539\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zari','EauZari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561373020946433/ZaliskB_large.jpeg", color=0xffffff)
		embed.set_author(name="#787 Zarid (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561373020946433/ZaliskB_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Défenseur\n**Lead**: PV +20~25%\n**Passif**: Pétrification 60% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 29092\n**Attaque**: 1321\n**Défense**: 2540\n**Récupération**:1641", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zari','BoisZari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561378267758622/ZaliskG_large.jpeg", color=0xffffff)
		embed.set_author(name="#788 Zarid (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561378267758622/ZaliskG_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Équilibré\n**Lead**: PV +20~25%\n**Passif**: Étourdissement 50% 1 tour\n(No skillbooks)\n**Actif**: Défense réduite 80% 2 tours\n(No skillbooks)\n**PV**: 28054\n**Attaque**: 1879\n**Défense**: 1725\n**Récupération**:1555", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zari','LightZari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561380318773250/ZaliskW_large.jpeg", color=0xffffff)
		embed.set_author(name="#789 Zarid (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561380318773250/ZaliskW_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Tank\n**Lead**: PV +20~25%\n**Passif**: Défense réduite 40% 2 tours\n(No skillbooks)\n**Actif**: Sommeil 60% 1 tour\n(No skillbooks)\n**PV**: 35375\n**Attaque**: 1554\n**Défense**: 1758\n**Récupération**:1329", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zari','DarkZari']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552561376040845332/ZaliskD_large.jpeg", color=0xffffff)
		embed.set_author(name="#790 Zarid (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552561376040845332/ZaliskD_large.jpeg")
		embed.add_field(name="★★", value="**Type**: Attaquant\n**Lead**: PV +20~25%\n**Passif**: Nécrose 40% 1 tour\n(No skillbooks)\n**Actif**: Nécrose 80% 2 tours\n(No skillbooks)\n**PV**: 26041\n**Attaque**: 2343\n**Défense**: 1566\n**Récupération**:1403", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Zhu Bajie  #############
		#######################################

	if any([message.content.startswith (item) for item in ['Zhu','FeuZhu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608737954910830613/Zhu3EvoR_large.jpg", color=0xffffff)
		embed.set_author(name="#791 Zhu Bajie  (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608737954910830613/Zhu3EvoR_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: PV +40~45%\n**Passif**: Prédateur 40%\n(Dmg: +25% )\n**Actif**: Prédateur 40%\n(Dmg: +25% )\n**PV**: 35201\n**Attaque**: 3664\n**Défense**: 2390\n**Récupération**:2663", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zhu','EauZhu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553821356818483/Zhu3EvoB_large.jpg", color=0xffffff)
		embed.set_author(name="#792 Zhu Bajie  (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553821356818483/Zhu3EvoB_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(Dmg: +20% Taux: +10%)\n**Actif**: Étourdissement 80% 2 tours\n(Dmg: +15% Taux: +15%)\n**PV**: 29971\n**Attaque**: 2860\n**Défense**: 3848\n**Récupération**:2574", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zhu','BoisZhu','TopZhu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/557222726306365449/Zhu3Evo_large.jpg", color=0xffffff)
		embed.set_author(name="#793 Zhu Bajie  (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/557222726306365449/Zhu3Evo_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Frappe Courageuse\n(Dmg: +20%)\n**Actif**: Aveuglement 80% 3 tours\n(Dmg: +20% Taux: +10%)\n**PV**: 29596\n**Attaque**: 2928\n**Défense**: 3943\n**Récupération**:2581", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zhu','LightZhu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/608737957133942818/Zhu3EvoW_large.jpg", color=0xffffff)
		embed.set_author(name="#794 Zhu Bajie  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/608737957133942818/Zhu3EvoW_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: PV +40~45%\n**Passif**: Provocation intrépide -50% dégâts 1 tour 80% Provocation 2 tours\n(No skillbooks)\n**Actif**: Agression (Def)\n(No skillbooks)\n**PV**: 29521\n**Attaque**: 2813\n**Défense**: 3957\n**Récupération**:2622", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Zhu','DarkZhu']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/552550283885019166/552553822174838814/Zhu3EvoD_large.jpg", color=0xffffff)
		embed.set_author(name="#795 Zhu Bajie  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/552550283885019166/552553822174838814/Zhu3EvoD_large.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: PV +40~45%\n**Passif**: Agression (PV)\n(Dmg: +25% )\n**Actif**: Agression (PV)\n(Dmg: +25% )\n**PV**: 51998\n**Attaque**: 2548\n**Défense**: 2786\n**Récupération**:2902", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Enkidu   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Enki','FeuEnki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146670273462312/Enkidu3EvoR.png", color=0xffffff)
		embed.set_author(name="#800 Enkidu  (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146670273462312/Enkidu3EvoR.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Siphon de PV\n**Actif**: Sommeil 100% 1 tour\n**PV**: 29392\n**Attaque**: 3596\n**Défense**: 2343\n**Récupération**:2125", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Enki','EauEnki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146663449591838/Enkidu3Evo.png", color=0xffffff)
		embed.set_author(name="#801 Enkidu  (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146663449591838/Enkidu3Evo.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Attaque réduite 80% - 2 tours\n**Actif**: Chasseur 50%\n**PV**: 26089\n**Attaque**: 3909\n**Défense**: 2683\n**Récupération**:2023", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Enki','BoisEnki','TopEnki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146659339042867/EnkiB.png", color=0xffffff)
		embed.set_author(name="#802 Enkidu  (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146659339042867/EnkiB.png")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense +40~45%\n**Passif**: Frappe courageuse\n**Actif**: Réduction dégâts- 2 tours\n**PV**: 31466\n**Attaque**: 3036\n**Défense**: 2842\n**Récupération**:2433", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Enki','LightEnki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146672807084082/Enkidu3EvoW.png", color=0xffffff)
		embed.set_author(name="#803 Enkidu  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146672807084082/Enkidu3EvoW.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Affaiblissement 80% - 2 tours\n**Actif**: Frappe courageuse\n**PV**: 27798\n**Attaque**: 3534\n**Défense**: 2629\n**Récupération**:1852", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Enki','DarkEnki']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707146667006230588/Enkidu3EvoD.png", color=0xffffff)
		embed.set_author(name="#804 Enkidu  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707146667006230588/Enkidu3EvoD.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense +40~45%\n**Passif**: Chasseur 50%\n**Actif**: Persévérance\n**PV**: 26927\n**Attaque**: 3596\n**Défense**: 2431\n**Récupération**:1880", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############    Griffon   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Griffon','FeuGriffon']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698266710046/20200505_122858.jpg", color=0xffffff)
		embed.set_author(name="#805 Griffon  (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698266710046/20200505_122858.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**: Attaque +40~45%\n**Passif**: Agression (Def)\n**Actif**: Agression (Def)\n**PV**: 35991\n**Attaque**: 2159\n**Défense**: 3936\n**Récupération**:2254", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Griffon','EauGriffon','TopGriffon']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698027503626/20200505_122844.jpg", color=0xffffff)
		embed.set_author(name="#806 Griffon  (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698027503626/20200505_122844.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Attaque +40~45%\n**Passif**: Contre attaque 100%\n**Actif**: Agression (PV)\n**PV**: 41647\n**Attaque**: 2603\n**Défense**: 2658\n**Récupération**:2725", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Griffon','BoisGriffon']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698501328976/20200505_122915.jpg", color=0xffffff)
		embed.set_author(name="#807 Griffon  (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698501328976/20200505_122915.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Attaque +40~45%\n**Passif**: Prédateur 40%\n**Actif**: Prédateur 50%\n**PV**: 28922\n**Attaque**: 3977\n**Défense**: 2595\n**Récupération**:2349", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Griffon','LightGriffon']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177698820227112/20200505_122929.jpg", color=0xffffff)
		embed.set_author(name="#808 Griffon  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177698820227112/20200505_122929.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Attaque +40~45%\n**Passif**: Boost de moral 50% PA\n**Actif**: Résistance réduite 100% - 2 tours\n**PV**: 33372\n**Attaque**: 3084\n**Défense**: 2842\n**Récupération**:2345", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Griffon','DarkGriffon']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177699151708170/20200505_122942.jpg", color=0xffffff)
		embed.set_author(name="#809 Griffon  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177699151708170/20200505_122942.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Attaque +40~45%\n**Passif**: Chasseur 40%\n**Actif**: Chasseur 50%\n**PV**: 27792\n**Attaque**: 3548\n**Défense**: 2513\n**Récupération**:2513", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Arlequin   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Arle','FeuArle']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159778035761223/Clown3EvoR.png", color=0xffffff)
		embed.set_author(name="#810 Arlequin  (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159778035761223/Clown3EvoR.png")
		embed.add_field(name="★★★★", value="**Type**: Tank\n**Lead**: Dégats critiques +40~45%\n**Passif**: Soif 80% - 2 tours\n**Actif**: Attaque réduite 60% - 2 tours\n**PV**: 40809\n**Attaque**: 2051\n**Défense**: 1887\n**Récupération**:1976", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arle','EauArle','TopArle']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159771790180423/Clown3EvoB.png", color=0xffffff)
		embed.set_author(name="#811 Arlequin  (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159771790180423/Clown3EvoB.png")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégats critiques +40~45%\n**Passif**: Frappe courageuse (Crit)\n**Actif**: Attaque réduite 80% - 2 tours (Crit)\n**PV**: 29593\n**Attaque**: 2730\n**Défense**: 2399\n**Récupération**:1766", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arle','BoisArle']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159775020056606/Clown3EvoG.png", color=0xffffff)
		embed.set_author(name="#812 Arlequin  (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159775020056606/Clown3EvoG.png")
		embed.add_field(name="★★★★", value="**Type**: Équilibré\n**Lead**: Dégats critiques +40~45%\n**Passif**: Siphon PA 20%\n**Actif**: Petrification 80% - 1 tour\n**PV**: 30846\n**Attaque**: 2389\n**Défense**: 2556\n**Récupération**:2433", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arle','LightArle']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159781177294919/Clown3EvoW.png", color=0xffffff)
		embed.set_author(name="#813 Arlequin  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159781177294919/Clown3EvoW.png")
		embed.add_field(name="★★★★", value="**Type**: Défenseur\n**Lead**: Dégats critiques +40~45%\n**Passif**: Réduction dégâts 50% - 1 tour\n**Actif**: Provocation intrépide 80% - 1 tour\n**PV**: 30713\n**Attaque**: 2070\n**Défense**: 3173\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Arle','DarkArle']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707159765490597939/Clown3Evo.png", color=0xffffff)
		embed.set_author(name="#814 Arlequin  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707159765490597939/Clown3Evo.png")
		embed.add_field(name="★★★★", value="**Type**: Attaquant\n**Lead**: Dégats critiques +40~45%\n**Passif**: Avantage élementaire (Crit)\n**Actif**: Prédateur 40%\n**PV**: 27063\n**Attaque**: 3194\n**Défense**: 2043\n**Récupération**:1954", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############  Gilgamesh   #############
		#######################################

	if any([message.content.startswith (item) for item in ['Gilg','FeuGilg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696396050462/20200505_122711.jpg", color=0xffffff)
		embed.set_author(name="#815 Gilgamesh  (feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696396050462/20200505_122711.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Étourdissement 100% - 1 tour\n**Actif**: Siphon PV\n**PV**:  29058\n**Attaque**: 3936\n**Défense**: 2635\n**Récupération**: 2384", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gilg','EauGilg','TopGilg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696693583872/20200505_122730.jpg", color=0xffffff)
		embed.set_author(name="#816 Gilgamesh  (eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696693583872/20200505_122730.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Affaiblissement 70% - 2 tours\n**Actif**: Frappe courageuse\n**PV**: 31139\n**Attaque**:  3070\n**Défense**: 2821\n**Récupération**:2535", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gilg','BoisGilg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177696916013186/20200505_122743.jpg", color=0xffffff)
		embed.set_author(name="#817 Gilgamesh  (bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177696916013186/20200505_122743.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Prédateur 50%\n**Actif**: Persévérance\n**PV**: 28336\n**Attaque**: 3814\n**Défense**: 2806\n**Récupération**:2418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gilg','LightGilg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177697188642846/20200505_122802.jpg", color=0xffffff)
		embed.set_author(name="#818 Gilgamesh  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177697188642846/20200505_122802.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Frappe courageuse\n**Actif**: Attaque augmentée - 2 tours\n**PV**: 33243\n**Attaque**: 3111\n**Défense**: 3080\n**Récupération**:2583", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Gilg','DarkGilg']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707177697796948058/20200505_122819.jpg", color=0xffffff)
		embed.set_author(name="#819 Gilgamesh  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707177697796948058/20200505_122819.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Vague martiale 20%\n**Actif**: Perforation 90% def ennemie\n**PV**: 28970\n**Attaque**: 3902\n**Défense**: 2670\n**Récupération**:2091", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		##########  Imperio Armani    #########
		#######################################

	if any([message.content.startswith (item) for item in ['Imper','LightImper']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707238669706330122/20200505_163013.jpg", color=0xffffff)
		embed.set_author(name="#820 Imperio  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707238669706330122/20200505_163013.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Défenseur\n**Lead**:  Attaque ennemie -35/40%\n**Passif**: Vague martiale 10%\n**Actif**: Choc - 60% - 2 tours\n**PV**: 30073\n**Attaque**: 2704\n**Défense**: 3616\n**Récupération**:2247", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Imper','DarkImper']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/707146231008460800/707238669513130004/20200505_162949.jpg", color=0xffffff)
		embed.set_author(name="#821 Imperio  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/707146231008460800/707238669513130004/20200505_162949.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**:  Attaque ennemie -35/40%\n**Passif**: Vague martiale - 10%\n**Actif**: Chasseur - 40%\n**PV**: 28421\n**Attaque**: 4004\n**Défense**: 2670\n**Récupération**:2322", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############     Shark    #############
		#######################################

	if any([message.content.startswith (item) for item in ['Shark','LightShark']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/707241241716195428/3181164-6019923722-baby-.png", color=0xffffff)
		embed.set_author(name="#822 Shark  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/707241241716195428/3181164-6019923722-baby-.png")
		embed.add_field(name="★★★", value="**Type**: Récupération\n**Lead**:  PV +30-35% (light)\n**Passif**: Attaque réduite 70% - 1 tour\n**Actif**: Attaque augmentée - 2 tours\n**PV**: 30345\n**Attaque**: 1941\n**Défense**: 1989\n**Récupération**:2881", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############      Pip     #############
		#######################################

	if any([message.content.startswith (item) for item in ['Pip','FeuPip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543372451282976/PipF.png", color=0xffffff)
		embed.set_author(name="#823 Pip (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543372451282976/PipF.png")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Résistance réduite 100% 2 tours\n(Dmg +25%)\n**Actif**: Défense réduite 60% 2 tours\n(Dmg +20%, Taux: +10%)\n**PV**: 25027\n**Attaque**: 1989\n**Défense**: 2751\n**Récupération**:1512", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pip','EauPip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543367405535242/PipE.png", color=0xffffff)
		embed.set_author(name="#824 Pip (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543367405535242/PipE.png")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Sommeil 80% 1 tour\n(Dmg +20%, Taux: +10%, +1 tour)\n**Actif**: Prédateur 30%\n(Dmg +20%, Taux: +10%)\n**PV**: 26416\n**Attaque**: 2813\n**Défense**: 2050\n**Récupération**:1512", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pip','BoisPip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731543362473164870/PipB.png", color=0xffffff)
		embed.set_author(name="#825 Pip (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731543362473164870/PipB.png")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Chasseur 50%\n(Dmg +30%)\n**Actif**: Avantage élémentaire\n(Dmg +25%)\n**PV**: 24496\n**Attaque**: 2956\n**Défense**: 2036\n**Récupération**:1437", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pip','LightPip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731541471747899593/lightp.png", color=0xffffff)
		embed.set_author(name="#826 Pip (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731541471747899593/lightp.png")
		embed.add_field(name="★★★", value="**Type**: Attaquant\n**Lead**: PV +30% (Donjons)\n**Passif**: Siphon de PA\n(Dmg +20%, Taux: +5%)\n**Actif**: Prédateur 40%\n(Dmg +20%, Taux: +10%)\n**PV**: 27628\n**Attaque**: 3255\n**Défense**: 2390\n**Récupération**:1818", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Pip','DarkPip']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/684370413958332436/731540053687533608/Darkp.png", color=0xffffff)
		embed.set_author(name="#827 Pip (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684370413958332436/731540053687533608/Darkp.png")
		embed.add_field(name="★★★", value="**Type**: Équilibré\n**Lead**: PV +30% (Donjons)\n**Passif**: Vague martiale 20% de ses PV et PA\n(Dmg +30%)\n**Actif**: Nécrose x3 80% 1 tour\n(Dmg +20%, Taux: +20%)\n**PV**: 31091\n**Attaque**: 2607\n**Défense**: 2386\n**Récupération**:1773", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Cernunnos  #############
		#######################################

	if any([message.content.startswith (item) for item in ['Cern','FeuCern']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793529880636/Screenshot_20200924-155113_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#828 Cernunnos  (Feu)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793529880636/Screenshot_20200924-155113_Monster_Super_League.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Defenseur\n**Lead**: Défense réduite 35/40%\n**Passif**: Affaiblissement 70% 2 tours\n**Actif**: Attaque augmentée 3 tours\n**PV**: 27744\n**Attaque**: 2840\n**Défense**: 3432\n**Récupération**:2424", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cern','EauCern']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793802248222/Screenshot_20200924-155142_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#829 Cernunnos  (Eau)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793802248222/Screenshot_20200924-155142_Monster_Super_League.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Défense réduite 35/40%\n**Passif**: Siphon de PA 30%\n**Actif**: Domination 3 tours\n**PV**: 41306\n**Attaque**: 2534\n**Défense**: 2364\n**Récupération**:2466", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cern','BoisCern']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687793974607882/Screenshot_20200924-155212_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#830 Cernunnos  (Bois)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687793974607882/Screenshot_20200924-155212_Monster_Super_League.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Nécrose x3 100% 1 tour\n**Actif**: Volonté immortelle 4 tours\n**PV**: 31513\n**Attaque**: 3145\n**Défense**: 2815\n**Récupération**:3033", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cern','LightCern']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687794184192060/Screenshot_20200924-155237_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#831 Cernunnos  (light)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687794184192060/Screenshot_20200924-155237_Monster_Super_League.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Défense réduite 35/40%\n**Passif**: Frappe courageuse\n**Actif**: Bouclier basé sur l'attaque 3 tours\n**PV**: 27689\n**Attaque**: 3718\n**Défense**: 2424\n**Récupération**:3044", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Cern','DarkCern']]):
		embed=discord.Embed(title="", url="https://media.discordapp.net/attachments/758071281219272775/758687794343444480/Screenshot_20200924-155305_Monster_Super_League.jpg", color=0xffffff)
		embed.set_author(name="#832 Cernunnos  (dark)")
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/758071281219272775/758687794343444480/Screenshot_20200924-155305_Monster_Super_League.jpg")
		embed.add_field(name="★★★★★", value="**Type**: Équilibré\n**Lead**: Défense réduite 35/40%\n**Passif**: Traqueur 50%\n**Actif**: Volonté immortelle 4 tours\n**PV**: 28541\n**Attaque**: 3807\n**Défense**: 2629\n**Récupération**:3180", inline=False)

		await message.channel.send(embed=embed)

		#######################################
		############   Jormungandr  ###########
		#######################################

	if any([message.content.startswith (item) for item in ['Jorm','FeuJorm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032243219824660/Jormungandfeu.png", color=0xffffff)
		embed.set_author(name="#833 Jormungandr  (Feu)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032243219824660/Jormungandfeu.png")
		embed.add_field(name="★★★★★", value="**Type**: Defenseur\n**Lead**: Résistance -20/25%\n**Passif**: Boost de moral 50% PA\n(Dmg: +20%, effet: +10%)\n**Actif**: Taux critique augmenté (Alliés))\n(Dmg: +20%, +1 tour)\n**PV**: 29773\n**Attaque**: 2901\n**Défense**: 3902\n**Récupération**:2418", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jorm','EauJorm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032302255308840/Jormungandeau.png", color=0xffffff)
		embed.set_author(name="#834 Jormungandr  (Eau)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032302255308840/Jormungandeau.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Résistance -20/25%\n**Passif**: Bouclier proportionnel à l'attaque 1 tour\n(Dmg: +20%, +1 tour\n**Actif**: Malédiction x2 2 tours\n(Dmg: +20%, +1 tour)\n**PV**: 27676\n**Attaque**: 3773\n**Défense**: 2758\n**Récupération**:2411", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jorm','BoisJorm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032329203449857/Jormungandbois.png", color=0xffffff)
		embed.set_author(name="#835 Jormungandr  (Bois)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032329203449857/Jormungandbois.png")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Résistance -20/25%\n**Passif**: Boost de moral 40% PA\n(Dmg: 20%, effet: +10%)\n**Actif**: Nécrose x2 90% 2 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 40557\n**Attaque**: 2494\n**Défense**: 2466\n**Récupération**:2555", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jorm','LightJorm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032370911346709/Jormungandlight.png", color=0xffffff)
		embed.set_author(name="#836 Jormungandr  (light)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032370911346709/Jormungandlight.png")
		embed.add_field(name="★★★★★", value="**Type**: Tank\n**Lead**: Résistance -20/25%\n**Passif**: Vague martiale 10% PA\n(Dmg: +25%)\n**Actif**: Nécrose x3 90% 2 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 46938\n**Attaque**: 2391\n**Défense**: 2637\n**Récupération**:2568", inline=False)

		await message.channel.send(embed=embed)

	if any([message.content.startswith (item) for item in ['Jorm','DarkJorm']]):
		embed=discord.Embed(title="", url="https://cdn.discordapp.com/attachments/758071281219272775/772032350568579082/Jormunganddark.png", color=0xffffff)
		embed.set_author(name="#837 Jormungandr  (dark)")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758071281219272775/772032350568579082/Jormunganddark.png")
		embed.add_field(name="★★★★★", value="**Type**: Attaquant\n**Lead**: Résistance -20/25%\n**Passif**: Frappe courageuse\n(Dmg: +20%)\n**Actif**: Défense réduite 80% 3 tours\n(Dmg: +20%, effet: +10%)\n**PV**: 27901\n**Attaque**: 3739\n**Défense**: 2547\n**Récupération**:2377", inline=False)

		await message.channel.send(embed=embed)




@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
