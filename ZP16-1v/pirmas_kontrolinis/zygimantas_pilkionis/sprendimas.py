import json

with open("zygimantas_inventorius.json", 'r', encoding='utf-8') as failas:
    inventorius = json.load(failas)

prekes = set([preke for parduotuve in inventorius.values() for preke in parduotuve])

db = {}

for parduotuve, parduotuves_info in inventorius.items():
    for preke, prekes_info in parduotuves_info.items():
        db[preke] = db.get(preke, 0) + prekes_info['kiekis']

rezultatas = {"visų_parduotuvių_inventorius": db}

with open("rezultatai.json", 'w', encoding='utf-8') as failas:
    failas.write(json.dumps(rezultatas, indent=2, ensure_ascii=False))
if __name__ == '__main__':
    pass

