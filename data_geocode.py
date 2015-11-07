import json
import requests

all_records = json.load(open('data/primariaTM_cleaned.json', 'r'))

for record in all_records:
    address = record['Adresa'] + ', Timisoara'
    record['geocode'] = requests.get('https://maps.googleapis.com/maps/api/geocode/json', address=address,
                                     key='SUPER_SECRET_KEY').json()

with open('data/primariaTM_cleaned_geocoded.json', 'w') as jsonfile:
    json.dump(all_records, jsonfile, sort_keys=True, indent=4)
