import json
from collections import namedtuple

Sarasas = namedtuple("Sarasas",["parduotuve","preke","kiekis","kaina"])

with open("evaldas_inventorius.json",'r',encoding='utf-8') as failas:
    inventorius = json.load(failas)

with open("evaldas_pirkėjai.json",'r',encoding='utf-8') as failas:
    pirkėjai = json.load(failas)

sarasas = []
for parduotuve, pard_duom in inventorius.items():
    for preke, prekes_info in pard_duom.items():
        sarasas.append(Sarasas(parduotuve,preke,prekes_info['kiekis'],prekes_info['kaina']))
prekes = ([s.preke for s in sarasas])

db = {}
for preke in prekes:
    db[preke] = sorted([s for s in sarasas if s.preke == preke], key=lambda  x:x.kaina)

for pirkėjas .norimos_prekės in pirkėjai.items():
    print(f'(pirkėjas):')
    for norima_preke, norimas_kiekis in norimos_prekės


if __name__ == '__main__':
    pass
