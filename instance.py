# Imports class libraries needed to interact with discord,randomly generates something, importing token
import discord
import os
import random
from ec2_metadata import ec2_metadata

from dotenv import load_dotenv

print(ec2_metadata.region)
print(ec2_metadata.instance_id)
print(ec2_metadata.public_ipv4)

load_dotenv()

client = discord.Client()
token = str(os.getenv('TOKEN'))


@client.event #<--Fix
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    
    
    print(f'Message {user_message} by {username} on {channel}')

    
    if message.author == client.user:
        return 
    
    
    if channel == "random": 
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f"Hi There! {username} Your EC2 Data: {ec2_metadata.region}")
            return 
        
        elif user_message.lower() == "hello world":
            await message.channel.send(f"hello {username} Your EC2 Data: {ec2_metadata.region}")
            
        
        elif user_message.lower() == "tell me about my server!":
            await message.channel.send(f"Here is your IP Address: {ec2_metadata.public_ipv4}, Your EC2 Region: {ec2_metadata.region}, and Avaliability zone: {ec2_metadata.availability_zone}")
            return
        
        elif user_message.lower() == "bye":
            await message.channel.send(f"Bye {username} Your EC2 Data: {ec2_metadata.region}")


client.run(token)