import requests
import random

api_key = ''
headers = { 'x-api-key': api_key }

url = 'https://api.sygictravelapi.com/1.1/en'

places_endpoint = '/places/list'
place_detail_endpoint = '/places/{id}'
collections_endpoint = '/collections'

def get_random_place_of_interest(query):
    # query for place
    params = { 'query': query }
    r = requests.get(url + places_endpoint, params=params, headers=headers)
    
    places = r.json().get('data', {}).get('places', [])
    if places:
        place_id = places[0]['id']
        
        # query for places of interest
        params = { 'parent_place_id': place_id }
        r = requests.get(url + collections_endpoint, params=params, headers=headers)
        
        pois = set([poi for d in r.json()['data']['collections'] for poi in d['place_ids']
                    if poi.startswith('poi')])
        poi = random.choice(list(pois))
        
        # get place details
        r = requests.get(url + place_detail_endpoint.format(id=poi), headers=headers)
        name = r.json().get('data', {}).get('place', {}).get('name', None)
        
        return name
    
    return []