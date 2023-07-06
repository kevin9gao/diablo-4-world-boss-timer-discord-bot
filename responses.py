import random
import requests
import json

def get_meme():
  res = requests.get("https://meme-api.com/gimme")
  data = json.loads(res.text)
  # print('data', data)
  return data

def get_response(message: str) -> str:
  p_message = message.lower()

  if message == 'hi':
    return "I'm Diablo 4 World Boss beep boop"
  elif message == 'pet':
    PETS = ['Dindin', 'Milo', 'Ahri', 'Benji', 'Eddie']
    SOUNDS = ['BORK', 'MEOW', 'ARF', 'HISS', "I'M FUCKIN\' JUICED", "I'm gonna start selling my items cuz I'm poor", "I'M AN OG", 'AVENGERS ASSEMBLE', 'KAGE BUNSHIN NO JUTSU']
    name = PETS[random.randint(0, len(PETS) - 1)]
    sound = SOUNDS[random.randint(0, len(SOUNDS) - 1)]
    return f'{name} says "{sound}"!'
  elif message == 'meme':
    meme = get_meme()
    return meme['url']
