import discord
from discord import app_commands
from discord.ext import commands

print("""
     _____                         _____            _                       
    |  __ \                       |  __ \          (_)                      
    | |__) |___   ___  _ __ ___   | |  | | ___  ___ _  __ _ _ __   ___ _ __ 
    |  _  // _ \ / _ \| '_ ` _ \  | |  | |/ _ \/ __| |/ _` | '_ \ / _ \ '__|
    | | \ \ (_) | (_) | | | | | | | |__| |  __/\__ \ | (_| | | | |  __/ |   
    |_|  \_\___/ \___/|_| |_| |_| |_____/ \___||___/_|\__, |_| |_|\___|_|   
                                                       __/ |                
                                                      |___/                 
     """)

# PARAMÉTRER LE BOT

intents = discord.Intents().all()

intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix = "§", intents = intents, description = "Room Designer")

tree = app_commands.CommandTree(discord.Client(intents = intents))

# MONTRER QUE LE BOT EST CONNECTÉ

@bot.event
async def on_ready():
    
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "Les Salons Créés"))

    print("\n---------------------- Le bot est en ligne ----------------------")
    
    try:
        synced = await bot.tree.sync()
        print(f"\n-------------- {len(synced)} commandes ont été synchronisées ! --------------\n")
        
    except Exception as e:
        print(e)

# CRÉER DES COMMANDES DE TESTS

@bot.tree.command(name = "test", description = "Tester les commandes.")
async def test(interaction : discord.Interaction):
    
    await interaction.response.send_message(f"Salut ! Tu viens d'utiliser une slash commande.", ephemeral = True)

# CRÉER DES SALONS

@bot.tree.command(name="creer_salon", description="Crée un salon textuel.")
@app_commands.describe(nom_salon = "Nom du salon à créer.")
async def creer_salon(interaction: discord.Interaction, nom_salon: str):
    
    guild = interaction.guild
    category = interaction.channel.category
    
    await guild.create_text_channel(nom_salon, category = category)
    await interaction.channel.send(f"Le salon `{nom_salon}` a été créé dans la catégorie `{category.name}`.")


bot.run('MTEyMTg0MDk3NzA3MDUzNDg0Ng.GnjDk3.q3b3Nkw7Km_bGbWXORs5ObQihmJ-FFXjHVT6zc')
