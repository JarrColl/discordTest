# bot.py
import os, discord, random
from dotenv import load_dotenv
from collections import defaultdict
from threading import Timer

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(f'{client.user} is connected to {guild.name}(id: {guild.id})')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, screw you')


sentMessages = defaultdict(lambda: [])
userStrikes = defaultdict(lambda: 0)

@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    
    lines = ['It wont hurt you! :raised_hands:<:9359_MCcoal:663920230057115649>:raised_hands:<:9359_MCcoal:663920230057115649>', 'How goods the cricket?', r"The suggestion that Australia, by having some trade-off where we could have higher emissions reduction targets, which would destroy jobs in regional communities, if we did that, then we wouldn't be having these fires. That is just not true.", "Well thankfully we’ve had no loss of life.\nTwo. Yes two, that’s quite right. I was thinking about firefighters firstly.", 'It wont hurt you! :raised_hands:<:9359_MCcoal:663920230057115649>:raised_hands:<:9359_MCcoal:663920230057115649>', "Have one of these bad boys :handshake::handshake::handshake::handshake:"]

    #Reply when fire is mentioned
    if 'fire' in message.content:
        response = random.choice(lines)
        await message.channel.send(response)

    #reply when GDP is mentioned
    if 'gdp' in message.content.lower():
        await message.channel.send("We are number 1 we are in a budget surplus in the black, no thanks to Labor the worst economic managers")
    
    if message.content.startswith('&&speech'):
         message.author.voice_channels[0].connect()
#        args = message.content.split(' ')
#        if len(args) == 2:
#            for chann in message.guild.voice_channels:
#                if args[1]==chann.name:
#                    await chann.connect()
        
@client.event
async def on_message_edit(before, after):
    print(f"Edit detected from {after.author}")

    if after.author != client.user:
        embedEdit = discord.Embed(title="Edit Detected", description=f"User: {after.author}", color=0xff1a1a)
        embedEdit.add_field(name="Before", value=before.content, inline=False)
        embedEdit.add_field(name="After", value=after.content, inline=False)
        await after.channel.send(embed=embedEdit)




client.run(token)