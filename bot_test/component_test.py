import discord
from discord.http import Route

app = discord.Client(intents=discord.Intents.all())
http = app.http

button_clicked = {}
        
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
                'embed': embed.to_dict(),
                'components': buttons
        }
        response = await http.request(r, json=payload)
        
        button_clicked[response.get('id')] = {
            'button_1': 0, 'button_2': 0, 'button_3': 0, 'button_4': 0
        }
        return

@app.event
async def on_socket_response(msg: dict):
    d = msg.get('d', {})
    t = msg.get('t');
    if t == 'INTERACTION_CREATE' and d.get('type') == 3:
        message = d.get('message', {})
        custom_id = d.get('data', {}).get('custom_id')
        
        button_clicked[message.get('id', 0)][custom_id] += 1
        
        embed = discord.Embed(
                title='Buttons',
                description='''Button 1 : {} clicked
                            Button 2 : {} clicked
                            Button 3 : {} clicked
                            Button 4 : {} clicked'''.format(
                                button_clicked[message.get('id', 0)]['button_1'], 
                                button_clicked[message.get('id', 0)]['button_2'], 
                                button_clicked[message.get('id', 0)]['button_3'], 
                                button_clicked[message.get('id', 0)]['button_4']),
                colour=0x0080ff
        )
        
        r = Route('PATCH', '/channels/{channel_id}/messages/{message_id}', channel_id=msg.message.get('channel_id').id, message_id=message.get('id'))
        payload = {
            'embed': embed.to_dict(),
            'components': buttons
        }
        await http.request(r, json=payload)
        
        interaction_id = d.get("id")
        interaction_token = d.get("token")

        await app.http.request(
            Route("POST", f"/interactions/{interaction_id}/{interaction_token}/callback"),
            json={"type": 4, "data": {
                "content": "당신은 {}를 고르셨군요!".format(custom_id),
                "flags": 64
            }},
        )
        
    return

app.run('my tokken')