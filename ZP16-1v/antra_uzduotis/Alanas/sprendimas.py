import json
from collections import namedtuple

Sarasas = namedtuple("Sarasas", ["parduotuve", "preke", "kiekis", "kaina"])


def versti(pavadinimas):
    galunes = ["ai", "ios", "ės"]
    galuniu_vertimai = ["us", "ias", "es"]
    for g, v in zip(galunes, galuniu_vertimai):
        if pavadinimas.endswith(g):
            return pavadinimas[:-len(g)] + v
    return pavadinimas


with open("Alanas_inventorius.json", 'r', encoding='utf-8') as failas:
    inventorius = json.load(failas)

with open("Alanas_pirkėjai.json", 'r', encoding='utf-8') as failas:
    pirkėjai = json.load(failas)

sarasas = []
for parduotuve, pard_duom in inventorius.items():
    for preke, prekes_info in pard_duom.items():
        sarasas.append(Sarasas(parduotuve, preke, prekes_info['kiekis'], prekes_info['kaina']))

prekes = set([s.preke for s in sarasas])

db = {}
for preke in prekes:
    db[preke] = sorted([s for s in sarasas if s.preke == preke], key=lambda x: x.kaina)

for pirkėjas, norimos_prekės in pirkėjai.items():
    print(f"{pirkėjas}:")
    for norima_preke, norimas_kiekis in norimos_prekės.items():
        for prekės_duomenys in db[norima_preke]:
            kiekis = prekės_duomenys.kiekis
            kaina = prekės_duomenys.kaina
            parduotuve = prekės_duomenys.parduotuve
            if kiekis == 0:
                continue

            if kiekis >= norimas_kiekis:
                print(f"{parduotuve} nusipirko {versti(norima_preke)} {norimas_kiekis} po {kaina}")
                prekės_duomenys._replace(kiekis=kiekis - norimas_kiekis)
                norimas_kiekis = 0
            else:
                print(f"{parduotuve} nusipirko {versti(norima_preke)} {kiekis} po {kaina}")
                prekės_duomenys._replace(kiekis=0)
                norimas_kiekis -= kiekis

            if norimas_kiekis == 0:
                break

if __name__ == '__main__':
    pass
