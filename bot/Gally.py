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
			embed.set_thumbnail(url="https://img.pngio.com/bar-development-game-health-video-game-icon-video-game-health-png-512_204.png")
			embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(a) + "\nDéfense : " + str(b) + "\n\n**Epv : " + str(c) + "**", inline=False)
			await message.channel.send(embed=embed)
 
		else:
			await message.channel.send ("Erreur, Ecrivez Epv suivi des PV et de la Def. (ex : Epv 20000 2000)")

	if ListElementInMessage[0] == "EpvGem":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round((a * 2.36) / (1 - ((b * 1.68) / ((b * 1.68) + 1200))))
			d = round((a * 1.68) / (1 - ((b * 2.36) / ((b * 2.36) + 1200))))
			e = int(a * 2.36)
			f = int(b * 1.68)
			g = int(a * 1.68)
			h = int(b * 2.36)
			embed=discord.Embed(title="Choisir entre 2 choix de gemmes :", description="- 2 gemmes Pv + 1 gemme Def \n- 2 gemmes Def + 1 gemme Pv", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base : " + str(a) + "\nDéfense de base : " + str(b), inline=False)
			embed.add_field(name="2Pv, 1Def", value="\n\n**Epv : " + str(c) + "**\nPV : " + str(e) + "\nDef : " + str(f), inline=True)
			embed.add_field(name="1Pv, 2Def", value="\n\n**Epv : " + str(d) + "**\nPV : " + str(e) + "\nDef : " + str(f), inline=True)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")
			
	if ListElementInMessage[0] == "EpvGemTr":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(((a * 2.36)+10000) / (1 - (((b * 1.68)+1000) / (((b * 1.68)+1000) + 1200))))
			d = round(((a * 1.68)+10000) / (1 - (((b * 2.36)+1000) / (((b * 2.36)+1000) + 1200))))
			e = int(a * 2.36)
			f = int(b * 1.68)
			g = int(a * 1.68)
			h = int(b * 2.36)
			embed=discord.Embed(title="Choisir entre 2 choix de gemmes :", description="- 2 gemmes Pv + 1 gemme Def \n- 2 gemmes Def + 1 gemme Pv", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base : " + str(a) + " __(+ 10k via les attirails)__\nDéfense de base : " + str(b) + " __(+ 1k via les attirails)__", inline=False)
			embed.add_field(name="2Pv, 1Def", value="\n\n**Epv : " + str(c) + "**\nPV : " + str(e) + "\nDef : " + str(f), inline=True)
			embed.add_field(name="1Pv, 2Def", value="\n\n**Epv : " + str(d) + "**\nPV : " + str(e) + "\nDef : " + str(f), inline=True)
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
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(d) + " (dont 10k via les attirails)\nDéfense : " + str(b) + " (dont 1k via les attirails)\n\nEpv avec 3 Gemmes Pv : " + str(c), inline=False)
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
			embed.set_thumbnail(url = "https://www.flaticon.com/svg/static/icons/svg/1496/1496059.svg")
			embed.add_field(name="Calculs effectués avec : ", value="atk : "+ str(a) +"\nTc : "+ str(b) +"\nDc : "+ str(c) +"\n\nDégats sans crit : "+ str(d) +"\nDégats moyens : "+str(e)+"\nDégats crit : "+str(f),inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez D suivi de l'attaque, du taux critique et des dégats critique")
	
	if ListElementInMessage[0] == "ListeC":
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
	
	if ListElementInMessage[0] == "Tit":
		if len(ListElementInMessage) == 2 and ListElementInMessage[1].isnumeric():
			a = int(ListElementInMessage[1])
			b = a
			c = [" :dark:", " :eau:", " :bois:", " :light:", " :feu:"]
			d = int(0)
			e = ["3","3.25","3.5","3.75","4","5.5","7","8.5","10","12.5","15","17.5","20","27.5","35","42.5","50","62.5","75","87.5","100","125","150","175","200","225","250","275","300","325","350","375","400","425","450","475","500","525","550","575","600"]
			mess = ""
			for i in range(0,10):
				b = (a%5)-1
				d = int((a-1)/5)
				mess += ("Titan " + str(a) + str(c[b]) + " (" + str(e[d]) + "m) : ")
				if i<9:
					mess += "\n"
				a += 1
			await message.channel.send (mess)
		else:
			await message.channel.send ("Erreur, Ecrivez Titan suivi du chiffre qui vous intéresse")
	
@client.event
async def on_ready():
    print(client.user.name)
    print( "[ON]")
    print('- - - - - - - -')

client.run(TOKEN)
