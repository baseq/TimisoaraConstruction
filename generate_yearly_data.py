import gzip
import json

with gzip.open("data/primariaTM_cleaned_geocoded.json.gz", "rb") as f:
    all_records = json.loads(f.read().decode("ascii"))

records_by_year = {}

for record in all_records:
    year = record['Data'][record['Data'].rfind('.') + 1:]
    if not year in records_by_year.keys():
        records_by_year[year] = []
    if len(record['geocode']['results']) > 0:
        records_by_year[year].append(record['geocode']['results'][0]['geometry']['location'])

for year in records_by_year.keys():
    with open('site/yearly_data/' + year + '.json', 'w') as outfile:
        json.dump(records_by_year[year], outfile)
