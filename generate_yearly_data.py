import gzip
import json

with gzip.open("data/primariaTM_cleaned_geocoded.json.gz", "rb") as f:
    all_records = json.loads(f.read().decode("ascii"))

records_by_year = {}

for record in all_records:
    year = record['Data'][record['Data'].rfind('.') + 1:]
    if not year in records_by_year.keys():
        records_by_year[year] = {}
        records_by_year[year]['points'] = []
        records_by_year[year]['accurate'] = 0
        records_by_year[year]['ignored'] = 0
    if len(record['geocode']['results']) > 0:
        if record['geocode']['results'][0]['geometry']['location_type'] == 'ROOFTOP':
            new_item = record['geocode']['results'][0]['geometry']['location']
            new_item['data'] = record['Data']
            new_item['adresa'] = record['Adresa']
            new_item['beneficiar'] = record['Beneficiar']
            new_item['descriere'] = record['Descriere']
            records_by_year[year]['points'].append(record['geocode']['results'][0]['geometry']['location'])
            records_by_year[year]['accurate'] += 1
        else:
            records_by_year[year]['ignored'] += 1

for year in records_by_year.keys():
    with open('site/yearly_data/' + year + '.json', 'w') as outfile:
        json.dump(records_by_year[year], outfile)
