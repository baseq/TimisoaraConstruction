import csv
import json

all_records = []
with open('data/primariaTM.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        record = {'Adresa': row['Adresa'], 'Beneficiar': row['Beneficiar'], 'Data': row['Data'],
                  'Descriere': row['Descriere'], 'Numar': row['Numar']}
        all_records.append(record)

with open('data/primariaTM_cleaned.json', 'w') as jsonfile:
    json.dump(all_records, jsonfile, sort_keys=True, indent=4)
