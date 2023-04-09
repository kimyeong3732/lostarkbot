import discord
from discord.http import Route

app = discord.Client(intents=discord.Intents.all())
http = app.http

        
buttons = [
    {
        'type': 1,
        'components': [
            {
                'type': 2,
                'label': 'Button 1',
                'style': 1,
                'custom_id': 'button_1'
            }, {
                'type': 2,
                'label': 'Button 2',
                'style': 2,
                'custom_id': 'button_2'
            }, {
                'type': 2,
                'label': 'Button 3',
                'style': 3,
                'custom_id': 'button_3'
            }, {
                'type': 2,
                'label': 'Button 4',
                'style': 4,
                'custom_id': 'button_4'
            }
        ]
    }
]

@app.event
async def on_message(msg: discord.Message):
    if msg.content == '/make':
        embed = discord.Embed(
                title='Buttons',
                description='''Button 1 : 0 clicked
                            Button 2 : 0 clicked
                            Button 3 : 0 clicked
                            Button 4 : 0 clicked''',
                colour=0x0080ff
        )
        
        r = Route('POST', '/channels/{channel_id}/messages', channel_id=msg.channel.id)
        payload = {
                'components': buttons
        }
        await msg.channel.send(embed=embed)
        await http.request(r, json=payload)
        return

app.run('my tokken')