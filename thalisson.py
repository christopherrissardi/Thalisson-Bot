from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='thalinho ', intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name='Minecraft', type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("Conectado")

@client.command()
async def limpar(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        if amount <= 0 or amount > 100:
            embed = discord.Embed(title='Não foi possível excluir as mensagens!', description='Por favor, forneça um número entre 1 e 100 para limpar mensagens.')
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title='Limpeza de Mensagens feita!', description=f'{amount} mensagens foram excluídas. Thalinho Fazolo que manda!')
            await ctx.send(embed=embed, delete_after=5)
    else:
        embed = discord.Embed(description='Você não tem permissão para limpar as mensagens.')
        await ctx.send(embed=embed)

@client.command()
async def expulsar(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f'Usuário Expulso: {member.name}', description=f'O usuário {member.mention} foi expulso do servidor por ser pnc.')
    await ctx.send(embed=embed)

@client.command()
async def banir(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f'Usuário Banido: {member.name}', description=f'O usuário {member.mention} foi banido do servidor por ser cuzudinho.')
    await ctx.send(embed=embed)

@client.command()
async def desbanir(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Desbanido {user.mention}')
            return

@client.command()
async def mutar(ctx, member: discord.Member):
    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f'{member.mention} foi mutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para mutar membros.')

@client.command()
async def desmutar(ctx, member: discord.Member):
    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if mute_role:
            await member.remove_roles(mute_role)
            await ctx.send(f'{member.mention} foi desmutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para desmutar membros.')

@client.event
async def on_member_join(member):
    welcome = member.guild.get_channel(892840937749872750)
    user_id = member.id

    if welcome:
        embed = discord.Embed(title=f"Tudo pela firma, nada contra a firma - Termo de adesão de {member}", description=f'Então, agora mais do nunca, oficialmente, você <@{user_id}>, seja bem vindo, a ordem, a firma, a irmandade.')
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="Segue os documentos para terminarmos a sua inclusão na firma:", value="", inline=False)
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="", value=f"- 1 (uma) Foto ¾", inline=False)
        embed.add_field(name="", value=f"- 2 (duas) Cópias do RG com validação em cartório", inline=False)
        embed.add_field(name="", value=f"- 1 (uma) Cópia da conta de luz", inline=False)
        embed.add_field(name="", value=f"- 1 (uma) Cópia do título de eleitor que você ainda não tirou", inline=False)
        embed.add_field(name="", value=f"- 2 (duas) Cópias do comprovante de alistamento militar", inline=False)
        embed.add_field(name="", value=f"- 1 (uma) cópia da Carteira Nacional de Habilitação nas categorias A e B", inline=False)
        embed.add_field(name="", value=f"- 25 (vinte e cinco) Cópias do comprovante de residência banhadas a ouro", inline=False)
        embed.add_field(name="", value=f"- 40 (cópias) De renda familiar validada em cartório com assinatura do Padre Local", inline=False)
        embed.add_field(name="", value=f"- 500ml (mililitros) Do sangue de uma virgem oferecidos para o Deus Pato", inline=False)
        embed.add_field(name="", value=f"- 1 (um) Tubo de cola Art Attack", inline=False)
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="", value="**Para semana que vem**", inline=False)
        embed.set_image(url='https://i.imgur.com/MhawMCl.png')
        embed.set_footer(text='Thalinho Fazolo Brabão do server', icon_url='')
        role = member.guild.get_role(892848160370741358)
        if role:
            await member.add_roles(role)
        await welcome.send(embed=embed)

@client.command()
async def oracao(ctx):

    embed = discord.Embed(title="Oração da Firma", description="Tudo pela firma, nada contra a firma")

    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="Lema", value="", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="", value="No dia mais claro\nNa noite mais densa\nO mal sucumbirá ante vossa presença\nTodo aquele que venera a Sony há de penar\nQuando o poder do Deus Pato enfrentar!", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="Oração", value="", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="", value="Deus Pato que jaz no HD velho do Lucas\nEternizado seja vosso nome,\nVenha a nós GPUs melhores,\nSeja feita vossa vontade, assim na call, quanto na Lan Party\nO sea nosso de cada dia nos dai hoje,\nPerdoai os cheats do Thalisson, assim como perdoamos a chatice do Leo.\nE não nos deixes cair em baixos custo-benefícios, mas livrai-nos da EA games, amém.", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="Credo", value="", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="", value="A criancice de nossos berros é revelada por meio dessas palavras:\nManter sua lâmina longe das e-grilos\nZuar a mãe de todos a todo momento\nTudo pela firma, nada contra a firma.", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="Jura", value="", inline=False)
    embed.add_field(name="\n\n", value="\n\n", inline=False)
    embed.add_field(name="", value="Juras manter os princípios da firma e tudo o que zoamos?\nNunca compartilhar a senha do Gamepass nem as frases excluídas?\nJuras fazê-lo deste momento até o Daniel arranjar uma namorada/o (vai demorar pra caralho), custe o que custar?\nEntão, primeiramente, desejamos que vá tomar bem no olho do cu, irmão.\nEntão, agora mais do nunca, oficialmente, você 'fulano de tal', seja bem vindo, a ordem, a firma, a irmandade,\nAgora você é um de nós, arauto da zoeira\nVocê é parte do Let's Dale\nE que o grandioso Deus Pato nos Guie.", inline=False)
    embed.set_image(url='')
    embed.set_footer(text='Thalinho Fazolo Brabão do server', icon_url='')

    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if client.user in message.mentions:
        response = random.choice(responses)
        await message.channel.send(response)
    await client.process_commands(message)

responses = [
    "Agora Fodeu",
    "Fala ae piazote",
    "Bao nego?",
    "O Cristopher é lindo fds",
    "GTAzinho hoje?",
    "Bagual dms nego",
    "Pior que sim pia",
    "Daora dms mano",
    "Pia do djanho",
    "Que b.o",
    "B.o dms",
    "Quero mais que se lasque kkkkk",
    "Meeeeeeeeeee",
    "Claro fi",
    "Claro fi, vamobora",
    "Massa dms",
    "Uma merda do krl mano",
    "Krllllll",
    "Brabo",
    "Tesão Pia",
    "Puta merda pia",
    "Que cagada isso ai kkkkkkkkkk",
    "Fica susse pia",
    "Fechou pia veio",
    "O negao",
    "Fala baitola",
    "Massa pra caraio pia",
    "Alguém: a\nThalisson: vou xitar até o talo",
    "Vc disse que entrava hj em seu fdp",
    "Mas é um corno mesmo",
    "Entre Home ( ͡° ͜ʖ ͡°)",
    "Parala que vou mijar rapidao",
    "Gayzinho mesmo"
]

@client.command()
async def letsdale(ctx):
    await ctx.send("https://discord.gg/j5Cs5UZbvk")

@client.command()
async def lindo(ctx):
    await ctx.send("Ain eu sou lindo mesmo")

@client.command()
async def delicia(ctx):
    await ctx.send("Para que assim fico com vergonha")

@client.command()
async def dlc(ctx):
    await ctx.send("Sou com muito orgulho 😘")

@client.command()
async def gay(ctx):
    await ctx.send("Nem tanto bb")

@client.command()
async def pnc(ctx):
    await ctx.send("Pau no cu é uns ai slk")

@client.command()
async def oi(ctx):
    await ctx.send("Fala nego veio")

@client.command()
async def tchau(ctx):
    await ctx.send("Conversamo piazote")

@client.command()
async def fodeu(ctx):
    await ctx.send("Fodeu pa caraio mesmo")

@client.command()
async def cheat(ctx):
    await ctx.send("Nem uso essas coisas não mano kkkkkkkkkkkkkkkkk")

@client.command()
async def minecraft(ctx):
    await ctx.send("To jogando agora kkkkkkkkk da uma olhada\nhttps://i.imgur.com/PETtNpB.jpeg")

@client.command()
async def freefire(ctx):
    await ctx.send("Olha meu Booyah da Ranqueada\nhttps://i.imgur.com/v0F9S5a.png")



client.run('')
