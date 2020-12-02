import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DiscordBotToken")

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return  
	ListElementInMessage = message.content.split()
	
	if ListElementInMessage[0] == "Hello":
		await message.channel.send ("salut ami humain")

	if ListElementInMessage[0] == "Epv":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(a/(1-(b/(b+1200))))
			embed = discord.Embed(title="Epv", color=0xffffff)
			embed.set_thumbnail(url="")
			embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(a) + "\nDéfense : " + str(b) + "\n\nEpv : " + str(c), inline=False)
			await message.channel.send(embed=embed)
 
		else:
			await message.channel.send ("Erreur, Ecrivez Epv suivi des PV et de la Def. (ex : Epv 20000 2000)")

	if ListElementInMessage[0] == "EpvGem":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round((a * 2.36) / (1 - ((b * 1.68) / ((b * 1.68) + 1200))))
			d = round((a * 1.68) / (1 - ((b * 2.36) / ((b * 2.36) + 1200))))
			embed = discord.Embed(title="Choisir entre : \n- 2 gemmes pv + 1 gemme def\n- 2 gemmes def + 1 gemme pv", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base: " + str(a) + "\nDéfense de base: " + str(b) + "\n\nEpv avec 2Pv + 1Def: " + str(c) + "\nEpv avec 1Pv + 2Def: " + str(d), inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")
			
	if ListElementInMessage[0] == "EpvGemTr":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(((a * 2.36)+10000) / (1 - (((b * 1.68)+1000) / (((b * 1.68)+1000) + 1200))))
			d = round(((a * 1.68)+10000) / (1 - (((b * 2.36)+1000) / (((b * 2.36)+1000) + 1200))))
			embed = discord.Embed(title="Choisir entre : \n- 2 gemmes pv + 1 gemme def\n- 2 gemmes def + 1 gemme pv", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base : " + str(a) + "(+ 10 000 via les attirails)\nDéfense de base : " + str(b) + "(+ 1 000 via les attirails)\n\nEpv avec 2Pv + 1Def: " + str(c) + "\nEpv avec 1Pv + 2Def: " + str(d), inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez EpvGemTr suivi des PV de base et de la Def de base")
			
	if ListElementInMessage[0] == "3GemPv":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])+1000
			c = round(((a * 3.04)+10000) / (1 - (b / (b + 1200))))
			d = int((a*3.04)+10000)
			embed = discord.Embed(title="Ce que donne 3 gemmes PV", color=0xffffff)
			embed.set_thumbnail(url="")
			embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(d) + "(dont 10 000 via les attirails)\nDéfense : " + str(b) + "(dont 1 000 via les attirails)\n\nEpv avec 3 Gemmes Pv : " + str(c), inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez 3GemPv suivi des PV de base et de la Def")
	
	if ListElementInMessage[0] == "D":
		if len(ListElementInMessage) == 4 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric and ListElementInMessage[3].isnumeric:
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = int(ListElementInMessage[3])
			d = round(a*5.5)
			e = round(a*5.5*(1+(b/100)*(c/100)))
			f = round(a*5.5*(1+(c/100)))
			embed = discord.Embed(title="les Dmg de l'Astromon :", color=0xffffff)
			embed.set_thumbnail(url = "")
			embed.add_field(name="Calculs effectués avec : ", value="atk : "+ str(a) +"\nTc : "+ str(b) +"\nDc : "+ str(c) +"\n\nDégats sans crit : "+ str(d) +"\nDégats moyens : "+str(e)+"\nDégats crit : "+str(f),inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez D suivi de l'attaque, du taux critique et des dégats critique")
	
	if ListElementInMessage[0] == "Liste":
		embed = discord.Embed(title="Liste des commandes :", color=0xffffff)
		embed.set_thumbnail(url = "")
		embed.add_field(name="Menu :", value="Menu \nSommaire \nInfo \nHelp \npas fini",inline=False)
		embed.add_field(name="Lexique :", value="Lexique",inline=False)
		embed.add_field(name="Trinket :", value="Trink \nTrinkPv \nTrinkAtk \n TrinkDc",inline=False)
		embed.add_field(name="Gemmes :", value="On met quoi dans Gemmes ?",inline=False)
		embed.add_field(name="Améliorations :", value="Hp+ Hp% Def+ Atk+ Atk% Dc",inline=True)
		embed.add_field(name="Astromons :", value="DarkVadehors",inline=False)
		embed.add_field(name="Calculs :", value="Epv \nEpvGem \nDégats \nDmg Aggr PV \nDmg Aggr Def \nDmg Aggr Rec \nHeal",inline=False)
		embed.add_field(name="Titi :", value="Titi# (# étant un chiffre ou un nombre)",inline=False)
		embed.add_field(name="Lead :", value="Lead \nLdTcDown \nLdTcUp \nLdDefUp \nLdDefDown",inline=False)
		embed.add_field(name="Attaques :", value="Competences \nAdrenaline",inline=False)
		embed.add_field(name="Top Liste :", value="En image ce serai pas mal \nHeal \npvp \nTiti \nbois \nEtc",inline=False)
		embed.add_field(name="Boss :", value="Colosses \nTitans \nGolems \nDragon \n WB",inline=False)
		embed.add_field(name="Liste de Commandes :", value="Liste",inline=False)
		await message.channel.send(embed=embed)
	
	if ListElementInMessage[0] == "Titan":
		if len(ListElementInMessage) == 2 and ListElementInMessage[1].isnumeric():
			a = int(ListElementInMessage[1])
			b = a
			i = int(0)
			c = [":Dark:", ":Eau:", ":Bois:", ":Light:", ":Feu:"]
			d = int(0)
			e = ["3","3.25","3.5","3.75","4","5.5","7","8.5","10","12.5","15","17.5","20","27.5","35","42.5","50","62.5","75","87.5","100","125","150","175","200","225","250","275","300","325","350","375","400"]
			while i < 10:
				while b > 5:
				b -= 5
				d += 1
			print("Titan", a, c[b-1],"(",e[d],"m) : ")
			a += 1
			i += 1
			b += 1
	
@client.event
async def on_ready():
    print(client.user.name)
    print( "[ON]")
    print('- - - - - - - -')

client.run(TOKEN)