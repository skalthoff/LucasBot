import discord

intents = discord.Intents.default()
intents.guilds = True # Enable the channels intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(menu())

@client.event
async def on_message(message):
    if message.author == client.user:  # Skip messages from the bot itself
        return
    print(f'Channel: {message.channel.name}, Author: {message.author.name}, Message: {message.content}')


def serverSelect():
    print('Available servers:')
    for position, server in enumerate(client.guilds):
        print(f'{position}, {server.id}: {server.name}')
    return client.guilds[int(input('Enter the number of the server you want to connect to: '))].id



async def channelSelect(serverId):
    guild = client.get_guild(serverId)
    text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]
    for channelNum, channel in enumerate(text_channels):
        print(f'Channel {channelNum}: {channel.id}: {channel.name}')
        
    return text_channels[int(input('Enter the number of the channel you want to connect to: '))]

async def sendMessage(serverId, channelId, messageContent):
    await client.get_guild(serverId).get_channel(channelId).send(str(messageContent))


async def menu():
    server_id = 0
    channel_id = 0
    menu_options = {
        '1': 'serverSelect',
        '2': 'channelSelect',
        '3': 'sendMessage',
        '4': 'exit'
    }
    while True:
        for option, description in menu_options.items():
            print(f'{option}: {description}')
        
        choice = input('Enter your choice (1-4): ')
        if choice not in menu_options:
            print('Invalid choice. Please try again.')
            continue
        
        if choice == '1':
            server_id =  serverSelect()
        elif choice == '2':
            channel_id = await channelSelect(server_id)
        elif choice == '3':
            await sendMessage(server_id, channel_id, "Hello World!")
        elif choice == '4':
            exit()





client.run('MTE2NDI5NjQwMDM5NDI2ODc3Mg.GevRTg.ik33vG6VTvBXLRFXsv8-FAwPvp4sXU6uHa-GFU')
