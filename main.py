import discord
import random
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
  print(f'Message from {message.author}: {message.content}')

  if message.author == client.user:
    return

  msg = message.content

  def get_meme():
    res = requests.get("https://meme-api.com/gimme")
    data = json.loads(res.text)
    # print('data', data)
    return data

  if msg.startswith('$hi'):
    print('received message')
    await message.channel.send("I'm Diablo 4 World Boss Bot beep boop")
  elif msg.startswith('$pet'):
    PETS = ['Dindin', 'Milo', 'Ahri', 'Benji', 'Eddie']
    SOUNDS = ['BORK', 'MEOW', 'ARF', 'HISS', "I'M FUCKIN\' JUICED", "I'm gonna start selling my items cuz I'm poor", "I'M AN OG", 'AVENGERS ASSEMBLE', 'KAGE BUNSHIN NO JUTSU']
    name = PETS[random.randint(0, len(PETS) - 1)]
    sound = SOUNDS[random.randint(0, len(SOUNDS) - 1)]
    await message.channel.send(f'{name} says "{sound}"!')
  elif msg.startswith('$meme'):
    meme = get_meme()
    await message.channel.send(meme['url'])

client.run(os.getenv('TOKEN'))
