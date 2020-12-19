# discordbot.py

import discord
import random


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(0000001010101010101010110)   # Add your channel # id to this section from discord
    await channel.send('The bot is now online')



@client.event
async def on_message(message):
    if message.author == client.user:

        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        
# This enables anybody that says the trigger word 'arty' in chat, to get an insult sent to chat based on the below code
# the if arty in message.content.lower() makes it so the data is translated as lowercase, thus removing capitalization from triggers

    if ('arty') in message.content.lower(): 
        arty_bot = random.choice([
            "Arty the Farty, had a party and all the fucking farts were there." ,
            "Arty...If laughter is the best medicine, your face must be curing the world." ,
            "Arty...You're so ugly, you scared the crap out of the toilet." ,
            "Arty...Your family tree must be a cactus because everybody on it is a prick." ,
            "Arty...No I'm not insulting you, I'm describing you." ,
            "Arty...It's better to let someone think you are an Idiot than to open your mouth and prove it." ,
            "Arty...If I had a face like yours, I'd sue my parents." ,
            "Arty...Your birth certificate is an apology letter from the condom factory." ,
            "Arty...I guess you prove that even god makes mistakes sometimes." ,
            "Arty...The only way you'll ever get laid is if you crawl up a chicken's ass and wait." ,
            "Arty...You're so fake, Barbie is jealous." ,
            "Arty...I’m jealous of people that don’t know you!" ,
            "Arty...My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too." ,
            "Arty...You're so ugly, when your mom dropped you off at school she got a fine for littering." ,
            "Arty...If I wanted to kill myself I'd climb your ego and jump to your IQ." ,
            "Arty...You must have been born on a highway because that's where most accidents happen." ,
            "Arty...Brains aren't everything. In your case they're nothing." ,
            "Arty...I don't know what makes you so stupid, but it really works." ,
            "Arty...I can explain it to you, but I can’t understand it for you." ,
            "Arty...Roses are red violets are blue, God made me pretty, what happened to you?" ,
            "Arty...Behind every fat woman there is a beautiful woman. No seriously, your in the way."])
        await message.channel.send(str(arty_bot))

    if message.content.startswith(('good bot' , 'bad bot' , 'shit bot')):
        good_bot = random.choice([":smile:" , 
                                  ":eyes:" , 
                                  ":grin:" , 
                                  ":heart_eyes:" , 
                                  ":kissing_heart:"])
        await message.channel.send(str(good_bot))






TOKEN = open("token.txt" , "r").readline()

client.run(TOKEN)

