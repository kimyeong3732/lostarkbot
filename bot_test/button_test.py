import discord
from discord.ext import commands
from discord_buttons_plugin import *
 
app = commands.Bot(command_prefix='/',intents=discord.Intents.all())
button = ButtonsClient(app)
 
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def make(ctx):
    await button.send(
        content = 'buttons are maked.', 
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    label='Button 1',
                    style=ButtonType().Primary, 
                    custom_id='button_one'
                ),
                Button(
                    label='Button 2',
                    style=ButtonType().Primary, 
                    custom_id='button_two'
                )
            ])
        ]
    )

@button.click #interaction error. must find different way
async def button_one(ctx):
    await ctx.reply('Button 1 is pressed!')

async def button_two(ctx):
    await ctx.reply('Button 2 is pressed?!')

app.run('my tokken')