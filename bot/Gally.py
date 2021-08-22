import discord
from discord.ext import commands, tasks
import os
import json
import psycopg2
import asyncio

TOKEN = os.getenv("DiscordBotToken")

HOST = os.getenv("HostSqlHeroku")
USER = os.getenv("UserSqlHeroku")
PASSWORD = os.getenv("MdpSqlHeroku")
DATABASE = os.getenv("DataSqlHeroku")

bot = commands.Bot(command_prefix='', description="Ceci est un Bot Discord pour le jeu Monster Super League")

class FonctionSql:
	def __init__(self, Pseudo, Commande, CombienDeFois, Channel, Serveur):
		self.nom = Pseudo
		self.com = Commande
		self.time = CombienDeFois
		self.chan = Channel
		self.guild = Serveur

	def Connexion():
		conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

	def selection():
		try:
			with Connexion():
				sql = "SELECT \"Id\", \"Nom\" FROM \"Astromons\".\"AstromonsNom\""
				conn.cursor().execute(sql)
				vue = str(conn.cursor().fetchall())
				print(vue)
				await message.channel.send(vue)

'''
@bot.event
async def on_raw_reaction_add(payload):
	print(payload)
	UserId = payload.user_id
	Emoji = payload.emoji.name
	Canal = payload.channel_id
	membre = await bot.get_guild(payload.guild_id).fetch_member(payload.UserId)
	print(UserId)
	print(Emoji)
	print(Canal)
	if Canal == "784691401094594571":
	
	await bot.send("je crois que ce chat rigole")
'''

@bot.command(help="ping pong")
async def ping(ctx: commands.Context):
	print("ping")
	#if ctx.channel.name != CHANNEL_WORK:
		#return
	await ctx.send('pong')

@bot.command(help="Calculer l'epv d'un Pkmn")
async def Epv(ctx: commands.Context, pv: int, defense: int):
	epv = round(pv/(1-(defense/(defense+1500))))
	embed = discord.Embed(title="Epv", color=0xffffff)
	embed.set_thumbnail(url="https://img.pngio.com/bar-development-game-health-video-game-icon-video-game-health-png-512_204.png")
	embed.add_field(name="Calculs effectués avec:", value="\nPV : " + str(pv) + "\nDéfense : " + str(defense) + "\n\n**Epv : " + str(epv) + "**", inline=False)
	await ctx.send(embed=embed)

@Epv.error
async def Epv_Error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send ("Erreur, Ecrivez Epv suivi des PV et de la Def. (ex : Epv 20000 2000)")

@bot.command(help="Calculer la config la plus tanky et l'epv d'un Pkmn")
async def EpvGem(ctx: commands.Context, pv: int, defense: int):
	DblPv = int(pv * 2.36)
	DblDef = int(defense * 2.36)
	SmplPv = int(pv * 1.68)
	SmplDef = int(defense * 1.68)
	Epv1 = round((DblPv) / (1 - ((SmplDef) / ((SmplDef) + 1500))))
	Epv2 = round((SmplPv) / (1 - ((DblDef) / ((DblDef) + 1500))))
	embed=discord.Embed(title="Choisir entre 2 choix de gemmes :", description="- 2 gemmes Pv + 1 gemme Def \n- 2 gemmes Def + 1 gemme Pv", color=0xffffff)
	embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
	embed.add_field(name="Calculs effectués avec:", value="\nPV de base : " + str(pv) + "\nDéfense de base : " + str(defense), inline=False)
	embed.add_field(name="2Pv, 1Def", value="\n\n**Epv : " + str(Epv1) + "**\nPV : " + str(DblPv) + "\nDef : " + str(SmplDef), inline=True)
	embed.add_field(name="1Pv, 2Def", value="\n\n**Epv : " + str(Epv2) + "**\nPV : " + str(SmplPv) + "\nDef : " + str(DblDef), inline=True)
	await ctx.channel.send(embed=embed)
	
@EpvGem.error
async def EpvGem_Error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base. (ex : Epv 20000 2000)")

@bot.command(help="Calculer la meilleure config pour l'epv d'un Healeur")
async def GemHeal(ctx: commands.Context, pv: int, defense: int, recup: int):
	SmplPv = int(pv*1.68)
	DblPv = int(pv*2.36)
	SmplDef = int(defense*1.68)
	DblDef = int(defense*2.36)
	SmplRec = int(recup*1.68)
	DblRec = int(recup*2.36)
	TrplRec = int(recup*3.04)
	Epv1 = round(SmplPv / (1 - (SmplDef / (SmplDef + 1500))))
	Epv2 = round(SmplPv / (1 - (defense / (defense + 1500))))
	Epv3 = round(pv / (1 - (SmplDef / (SmplDef + 1500))))
	Epv4 = round(DblPv / (1 - (SmplDef / (SmplDef + 1500))))
	Epv5 = round(SmplPv / (1 - (DblDef / (DblDef + 1500))))
	Epv6 = round(pv / (1 - (defense / (defense + 1500))))

	embed=discord.Embed(title="Choix de Gemmes pour un healer", description="Quelles gemmes choisir ? voici la réponse")
	embed.set_thumbnail(url="https://wiki.dungeondefenders2.com/images/6/6e/Heal.png")
	embed.add_field(name="1 Pv, 1 Def, 1 Recup", value="**Epv : "+str(Epv1)+"**"+"\nPv : "+str(SmplPv)+"\nDef : "+str(SmplDef)+"\nRecup : " +str(SmplRec), inline=True)
	embed.add_field(name="1 Pv, 2 Recup", value="**Epv : "+str(Epv2)+"**"+"\nPv : "+str(SmplPv)+"\nDef : "+str(defense)+"\nRecup : " +str(DblRec), inline=True)
	embed.add_field(name="1 Def, 2 Recup", value="**Epv : "+str(Epv3)+"**"+"\nPv : "+str(pv)+"\nDef : "+str(SmplDef)+"\nRecup : " +str(DblRec), inline=True)
	embed.add_field(name="2 Pv, 1 Def", value="**Epv : "+str(Epv4)+"**"+"\nPv : "+str(DblPv)+"\nDef : "+str(SmplDef)+"\nRecup : " +str(recup), inline=True)
	embed.add_field(name="1 Pv, 2 Def", value="**Epv : "+str(Epv5)+"**"+"\nPv : "+str(SmplPv)+"\nDef : "+str(DblDef)+"\nRecup : " +str(recup), inline=True)
	embed.add_field(name="3 Rec", value="**Epv : "+str(Epv6)+"**"+"\nPv : "+str(pv)+"\nDef : "+str(defense)+"\nRecup : " +str(TrplRec), inline=True)
	embed.add_field(name="Attention", value="\n\n__les sub, attirails, amélio, etc. ne sont pas pris en compte__ ;)", inline=False)
	await ctx.channel.send(embed=embed)

@GemHeal.error
async def GemHeal_Error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.channel.send ("Erreur, Ecrivez GemHeal suivi des PV de base, de la Def de base et de la récup de base")
	
@bot.command(help="Calculer les degats du pkmn")
async def D(ctx: commands.Context, Atk: int, Tc: int, Dc: int):
	AtkSmpl = round(Atk*5.5)
	AtkNorm = round(Atk*5.5*(1+(Tc/100)*(Dc/100)))
	FullAtk = round(Atk*5.5*(1+(Dc/100)))
	embed = discord.Embed(title="", color=0xffffff)
	embed.set_thumbnail(url = "https://img2.pngio.com/markeus-b-ui-buttons-opengameartorg-attack-png-187_207.png")
	embed.add_field(name="Calculs effectués avec : ", value="\nAttaque : " + str(Atk) + "\nTaux critique : " + str(Tc) + "\nDommages critiques : " + str(Dc) +
		"\n\n__**Dégâts moyens__ : "+ str(AtkNorm)+ "**" + " (75k recomandé)" +
		"\n\n__Dégâts min :__ " + str(AtkSmpl)+ " (no crit)" +
		"\n__Dégâts crit :__ "+ str(FullAtk)+ " (crit)",inline=False)
	await ctx.channel.send(embed=embed)

@D.error
async def D_Error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.channel.send ("Erreur, Ecrivez D suivi de l'attaque, du taux critique et des dégats critique")

@bot.command(help= "Savoir quoi choisir entre une gemme Atk ou Dc")
async def AtkDc(ctx: commands.Context, Atk: int, Dc: int):
	FullAtk1 = round((Atk*1.68)*5.5*(1+(Dc/100)))
	FullAtk2 = round(Atk*5.5*(1+((Dc*1.7)/100)))
	embed = discord.Embed(title="", color=0xffffff)
	embed.set_thumbnail(url = "https://img2.pngio.com/markeus-b-ui-buttons-opengameartorg-attack-png-187_207.png")
	embed.add_field(name="Avec une gemme Atk :", value="Les degats crit seront de : " +str(FullAtk1), inline=True)
	embed.add_field(name="Avec une gemme Dc :", value="Les degats crit seront de : " +str(FullAtk2), inline=True)
	if FullAtk1 > FullAtk2:
		embed.add_field(name="Résultat :", value="La gemme Atk serait un meilleur choix.", inline=False)
	elif FullAtk2 > FullAtk1:
		embed.add_field(name="Résultat :", value="La gemme Dc serait un meilleur choix.", inline=False)
	else:
		embed.add_field(name="Résultat :", value="Il n'y a pas de meilleur choix.", inline=False)
	embed.add_field(name="Attention", value="\n\n__les sub, attirails, amélio, etc. ne sont pas pris en compte__ ;)", inline=False)
	await ctx.channel.send(embed=embed)

@AtkDc.error
async def AtkDc_Error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.channel.send ("Erreur, Ecrivez AtkDc suivi de l'attaque et des dégats critique")

@bot.command(help= "Obtenir l'id de l'interlocuteur")
async def GetId(ctx: commands.Context):
	print(ctx.author)
	auteur = ctx.author
	await ctx.send('id obtenue')

@bot.command(help= "timer pour le World Boss")
async def WbTime(ctx: commands.Context):
	GetId(ctx)
	#print("Timer pour", auteur)
	await ctx.send("le Timer va être mis en place")
	await ctx.send("Dans combien de temps (en jours) le WorldBoss arrive-t-il ? ")
	
	
'''	if len(ListElementInMessage) == 2 and ListElementInMessage[1].isnumeric():
	temps = ListElementInMessage[1]

	reste = int(temps * 86400)
	counter1 = 0
	while counter1==0:
		counter2 = 0
		await message.channel.send("Prochain WorldBoss dans " + temps + " jours.")
		await asyncio.sleep(reste) # task runs every 10 seconds
		while counter2<3:
			counter2 += 1
			await message.channel.send("@here Amis humains, pensez à faire vos attaques World Boss.")
			await asyncio.sleep(86400) # task runs every 10 seconds
		temps = 12
'''
'''@bot.event
async def on_message(message):
	if message.author == bot.user:
		return  
	ListElementInMessage = message.content.split()
	
	if ListElementInMessage[0] == "ping":
		await message.channel.send ("ping")
	
	if ListElementInMessage[0] == "Hello":
		await message.channel.send ("salut ami humain")

	if ListElementInMessage[0] == "WBTime":
		if len(ListElementInMessage) == 2 and ListElementInMessage[1].isnumeric():
			temps = ListElementInMessage[1]
			
			reste = int(temps * 86400)
			counter1 = 0
			while counter1==0:
				counter2 = 0
				await message.channel.send("Prochain WorldBoss dans " + temps + " jours.")
				await asyncio.sleep(reste) # task runs every 10 seconds
				while counter2<3:
					counter2 += 1
					await message.channel.send("@here Amis humains, pensez à faire vos attaques World Boss.")
					await asyncio.sleep(86400) # task runs every 10 seconds
				temps = 12

	if ListElementInMessage[0] == "Epv":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(a/(1-(b/(b+1500))))
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
			embed.add_field(name="1Pv, 2Def", value="\n\n**Epv : " + str(d) + "**\nPV : " + str(g) + "\nDef : " + str(h), inline=True)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez EpvGem suivi des PV de base et de la Def de base")
			
	if ListElementInMessage[0] == "EpvGemTr":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = round(((a * 2.36)+10000) / (1 - (((b * 1.68)+1000) / (((b * 1.68)+1000) + 1200))))
			d = round(((a * 1.68)+10000) / (1 - (((b * 2.36)+1000) / (((b * 2.36)+1000) + 1200))))
			e = int((a * 2.36)+10000)
			f = int((b * 1.68)+1000)
			g = int((a * 1.68)+10000)
			h = int((b * 2.36)+1000)
			embed=discord.Embed(title="Choisir entre 2 choix de gemmes :", description="- 2 gemmes Pv + 1 gemme Def \n- 2 gemmes Def + 1 gemme Pv", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec:", value="\nPV de base : " + str(a) + " __(+ 10k via les attirails)__\nDéfense de base : " + str(b) + " __(+ 1k via les attirails)__", inline=False)
			embed.add_field(name="2Pv, 1Def", value="\n\n**Epv : " + str(c) + "**\nPV : " + str(e) + "\nDef : " + str(f), inline=True)
			embed.add_field(name="1Pv, 2Def", value="\n\n**Epv : " + str(d) + "**\nPV : " + str(g) + "\nDef : " + str(h), inline=True)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez EpvGemTr suivi des PV de base et de la Def de base")
			
	if ListElementInMessage[0] == "3GemPv":
		if len(ListElementInMessage) == 3 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])+1000
			c = round(((a * 3.04)+10000) / (1 - (b / (b + 1200))))
			d = int((a*3.04)+10000)
			embed = discord.Embed(title="Ce que donnent 3 gemmes PV", color=0xffffff)
			embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/mslgame/images/a/aa/Gem.png/revision/latest/top-crop/width/150/height/150?cb=20160922163030")
			embed.add_field(name="Calculs effectués avec :", value="\nPV : " + str(d) + " (dont 10k via les attirails)\nDéfense : " + str(b) + " (dont 1k via les attirails)\n\n**Epv : " + str(c) + "**", inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez 3GemPv suivi des PV de base et de la Def")
	
	if ListElementInMessage[0] == "GemHeal":
		if len(ListElementInMessage) == 4 and ListElementInMessage[1].isnumeric() and ListElementInMessage[2].isnumeric() and ListElementInMessage[3].isnumeric():
			a = int(ListElementInMessage[1])
			b = int(ListElementInMessage[2])
			c = int(ListElementInMessage[3])
			d = int((a*1.68)+10000)
			e = int((b*1.68)+1000)
			f = round(d / (1 - (e / (e + 1200))))
			g = round((a +10000) / (1 - (e / (e + 1200))))
			h = round(d / (1 - ((b +1000) / ((b +1000) + 1200))))
			i = int((c*2.36)+500)
			j = int((c*1.68)+500)
			k = int(a+10000)
			l = int(b+1000)
			embed=discord.Embed(title="Choix de Gemmes pour un healer", description="Les calculs sont effectués en prenant compte des attirails : \n +10k Pv, +1k Def, +500 Recup")
			embed.set_thumbnail(url="https://wiki.dungeondefenders2.com/images/6/6e/Heal.png")
			embed.add_field(name="1 Pv, 1 Def, 1 Recup", value="**Epv : "+str(f)+"**"+"\nPv : "+str(d)+"\nDef : "+str(e)+"\nRecup : " +str(j), inline=True)
			embed.add_field(name="1 Pv, 2 Recup", value="**Epv : "+str(h)+"**"+"\nPv : "+str(d)+"\nDef : "+str(l)+"\nRecup : " +str(i), inline=True)
			embed.add_field(name="1 Def, 2 Recup", value="**Epv : "+str(g)+"**"+"\nPv : "+str(k)+"\nDef : "+str(e)+"\nRecup : " +str(i), inline=True)
			embed.add_field(name="Attention", value="\n\n__les sub ne sont pas pris en compte__ ;)", inline=False)
			await message.channel.send(embed=embed)
		else:
			await message.channel.send ("Erreur, Ecrivez GemHeal suivi des PV de base, de la Def de base et de la récup de base")
	
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
	
	if ListElementInMessage[0] == "Code":
		if len(ListElementInMessage) == 1:
			CodeName = "Nom du mob + (élément)"
			CodeUn = "★"
			CodeDeux ="**Type**: ....\n**Lead**: ....\n**Passif**: ....\n(....)\n**Actif**: ....\n(....)\n**PV**: ....\n**Attaque**: ....\n**Défense**: ....\n**Récupération**: ...."
			CodeTexte = "Copiez/collez, donnez un nom et un élément, modifiez le nombre d'étoiles puis changez les '....' par les infos que vous avez trouvé.\n Un grand merci pour votre aide :blush: \n\nPour le test, pensez à mettre un espace là où j'ai fais un retour à la ligne svp. \nTest coming soon"
			await message.channel.send (CodeName +"\n"+ CodeUn +"\n"+ repr(CodeDeux)+"\n"+ CodeTexte)

	if ListElementInMessage[0] in ["Feu","Eau","Bois","Dark","Light"]:
		with open('fichiers/Astromons.json', 'r') as f:
			names = json.load(f)
			element = ListElementInMessage[0]
			nom = ListElementInMessage[1]
			if nom in names:
				embed = discord.Embed(title="", url="", color=0xffffff)
				embed.set_author(name=nom)
				embed.set_thumbnail(url=names[nom][element]['img'])
				embed.add_field(name=names[nom][element]['stars'], value="**Type**: "+names[nom][element]['type']+"\n**Lead**: "+names[nom][element]['lead']+"\n**Passif**: "+names[nom][element]['passif']+"\n("+names[nom][element]['passif_book']+")\n**Actif**: "+names[nom][element]['actif']+"\n("+names[nom][element]['actif_book']+")\n**PV**: "+names[nom][element]['pv']+"\n**Attaque**: "+names[nom][element]['atk']+"\n**Défense**: "+names[nom][element]['def']+"\n**Récupération**: "+names[nom][element]['rec'], inline=False)
				await message.channel.send(embed=embed)
			else:
				await message.channel.send("Erreur, Ecrivez l'élément suivi d'un espace puis le nom de l'astromon qui vous intéresse")

	if ListElementInMessage[0] == "TestCode":
		NomMob = ListElementInMessage[1] + ListElementInMessage[2]
		Star = ListElementInMessage[3]
		reste = ListElementInMessage[4:]
		for i, e in enumerate(reste):
			if e.endswith(':'):
				reste[i] = '\n' + e
		reste = ' '.join(reste)
		embed=discord.Embed(title="", url="", color=0xffffff)
		embed.set_author(name=NomMob)
		embed.set_thumbnail(url="")
		embed.add_field(name=Star, value=reste, inline=False)
		await message.channel.send(embed=embed)

#	if ListElementInMessage[0] == "ON":
#		# Open connection
#		conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
#		print("Connecxion ouverte.")
	if ListElementInMessage[0] == "DB":
		cur = conn.cursor()
#		Create, Read, Update, Delete
		if ListElementInMessage[1] == "SHOW":
			if ListElementInMessage[2] == "Nom":
				sql = "SELECT \"Id\", \"Nom\" FROM \"Astromons\".\"AstromonsNom\""
				cur.execute(sql)
				vue = str(cur.fetchall())
				print(vue)
				await message.channel.send(vue)
			elif ListElementInMessage[2] == "Table":
				sql = "SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = 'Astromons'"			
				cur.execute(sql)
				vue = ""
				for row in cur.fetchall():
					vue += str(row)
					vue += "\n"
				print(vue)
				await message.channel.send(vue)
#			if ListElementInMessage[2] == "DATA":
#				sql = "SELECT \"Nom\" FROM \"Astromons\".\"AstromonsNom\""
#				cur.execute(sql)
#				sql = str(cur.fetchall())
#				sql = "SELECT \"Nom\" FROM \"Astromons\".\"AstromonsNom\""
#				cur.execute(sql)
#				sql = "SELECT * FROM  \"Astromons\".\"Astroguide\""			
#				cur.execute(sql)
#				sql = str(cur.fetchall())
#				for row in sql:
#					Nom = str(row[1])
#					Element = "( "+row[2]+" )"
#					Star = row[3] * "★"
#					Type = row[4]
#					Lead = row[5]
#					
#				await message.channel.send(Nom+Element+"\n"+Star+"\n"+Type+"\n"+Lead)

		if ListElementInMessage[1] == "ADD":
			if ListElementInMessage[2] == "Nom":
				try:
					sql = "INSERT INTO \"Astromons\".\"AstromonsNom\" (\"Nom\") VALUES ('"+ListElementInMessage[3]+"')"
					cur.execute(sql)
					conn.commit()
					sql = "SELECT * FROM \"Astromons\".\"AstromonsNom\""
					cur.execute(sql)
					vue = str(cur.fetchall())
					await message.channel.send(vue)
				except Exception as e:
					print("Erreur Doublon")
					await message.channel.send("Cet Atromon est déjà enregistré, merci ^^")

#			elif ListElementInMessage[3] == "Rac":
#				NomId = "SELECT Id FROM Astromons.AstromonsNom WHERE Nom = ListElementInMessage[2]"
#				sql = "INSERT INTO Astromons.AstromonsRaccourcis (Nom_Id, Mot_Clef) VALUES (NomId,'ListElementInMessage[4]')"
#				cur.execute(sql)
#				sql = "SELECT Nom FROM Astromons.AstromonsNom"
#				sql += "SELECT Mot_Clef FROM Astromons.AstromonsRaccourcis"
#				cur.execute(sql)
#				await message.channel.send(cur.fetchall())				
#			elif ListElementInMessage[2] in ["Img","Star","Passif_Book","Actif_Book","Pv","Atk","Def","Rec"]
	if ListElementInMessage[0] == "OFF":
		conn.close()
		print(type(conn)+" fermée.")

	if ListElementInMessage[0] == "Gally":
		await message.channel.send("Oui ?")
'''		

@bot.event
async def on_ready():
    print(bot.user.name)
    print( "[ON]")
    print('- - - - - - - -')

bot.run(TOKEN)
