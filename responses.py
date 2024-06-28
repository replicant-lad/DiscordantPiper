from requests import get
import re
from json import loads

async def scryfall_query(message):

    card_images : list = []

    card_queries = re.findall(r'\[\[([A-Za-z0-9_ ,-:/]+)\]\]', message.content)

    if len(card_queries) >= 10:
        await message.channel.send(f'This bot only allows for up to nine queries to keep response time high and to respect Scryfall API standards. Try again.')

    else:
        for card in card_queries:
            print(card)
            card_get = loads(get(f"https://api.scryfall.com/cards/search?q={card}").text)
            try:
                card_images.append(card_get['data'][0]['image_uris']['png'])
            except Exception as e:
                print("Attempted to query a card that has no results, ignoring...")

        cards = ('\n').join(card_images)

        if len(card_queries) == len(card_images):
            mismatch = ''
        else:
            mismatch = f'Detected {len(card_queries)} card queries, but Scryfall only returned {len(card_images)}: \n'
            
        
        await message.channel.send(f'{mismatch} {cards}')