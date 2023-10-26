import discord
import asyncio
import random

client = discord.Client(intents=discord.Intents.default())

# List of quotes to reply with when !lucas is typed.
lucas_quotes = [
    "Quote 1",
    "Quote 2",
    "Quote 3",
    # ... add more quotes as desired
]



@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(send_message())  # Move the task creation here

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'{message.channel}: {message.author}: {message.content}')

        
@client.event
async def send_message():
    await client.wait_until_ready()

    # Get server and channel IDs from the user``
    try:
        server_id = 1084655016486387742
        channel_id = 1156074392535711744
        
    except ValueError:
        server_id = int(input("Enter the server ID: "))
        channel_id = int(input("Enter the channel ID: "))
        print("Invalid input. Please enter numeric IDs.")
        return

    server = client.get_guild(server_id)
    if not server:
        print(f"Could not find server with ID: {server_id}")
        return

    channel = server.get_channel(channel_id)
    if not channel:
        print(f"Could not find channel with ID: {channel_id}")
        return

    print(f"Connected to {channel.name} in {server.name}")

    while True:
        message = input("Enter your message: ")
        if message.lower() == 'exit':
            break
        await channel.send(message)


client.run('MTE2NDI5NjQwMDM5NDI2ODc3Mg.GevRTg.ik33vG6VTvBXLRFXsv8-FAwPvp4sXU6uHa-GFU')

