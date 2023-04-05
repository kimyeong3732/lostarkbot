import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='/',intents=discord.Intents.all())
 
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')

app.run('MTA5MTY1NjAzNTkzODM1MzE4Mw.GzLOz2.LBFi_Uuf9nlHqc4Fz0cgQQCSHLH_AC4pBMt2WI')