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




@client.event
async def on_ready():
	print(client.user.name)
	print( "[ON]")
	print('- - - - - - - -')


client.run(TOKEN)
