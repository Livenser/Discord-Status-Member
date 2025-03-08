# Library Import Yang Digunakan
import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv

# Sambungan Token dari file .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Integrasi dengan Discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Aktifkan {bot.user} ({bot.user.id})')
    await bot.tree.sync()
    update_status.start()
    print("Bot sudah siap digunakan dan dipakai.")

@tasks.loop(minutes=1)  # Update Real Time 1 Menit
async def update_status():
    total_members = sum(guild.member_count for guild in bot.guilds)
    activity = discord.Activity(type=discord.ActivityType.watching, name=f"{total_members} Member")
    await bot.change_presence(activity=activity)

# Codingan inti
@bot.hybrid_command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
