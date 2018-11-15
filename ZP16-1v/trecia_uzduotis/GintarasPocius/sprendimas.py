import json
from collections import namedtuple

Sarasas = namedtuple("Sarasas", ["parduotuve", "preke", "kiekis", "kaina","nuo","iki"])


def versti(pavadinimas):
    galunes = ["ai", "ios", "ės"]
    galuniu_vertimai = ["us", "ias", "es"]
    for g, v in zip(galunes, galuniu_vertimai):
        if pavadinimas.endswith(g):
            return pavadinimas[:-len(g)] + v
    return pavadinimas

def laikas_to_int(laikas):
    return int(laikas.replace(":",""))

with open("gintaras_inventorius.json", 'r', encoding='utf-8') as failas:
    inventorius = json.load(failas)

with open("gintaras_pirkėjai.json", 'r', encoding='utf-8') as failas:
    pirkėjai = json.load(failas)

sarasas = []
for parduotuve, pard_duom in inventorius.items():
    for preke, prekes_info in pard_duom.items():
        sarasas.append(Sarasas(parduotuve, preke, prekes_info['kiekis'], prekes_info['kaina'], laikas_to_int(prekes_info['darba']['nuo']),laikas_to_int(prekes_info['darba']['iki'])))

prekes = set([s.preke for s in sarasas])

db = {}
for preke in prekes:
    db[preke] = sorted([s for s in sarasas if s.preke == preke], key=lambda x: x.kaina)

for pirkėjas, norimos_prekės in pirkėjai.items():
    print(f"{pirkėjas}:")
    pirkimo_laikas = laikas_to_int(norimos_prekės['laikas'])
    for norima_preke, norimas_kiekis in norimos_prekės.items():
        for prekės_duomenys in db.get(norima_preke,[]):
            kiekis = prekės_duomenys.kiekis
            kaina = prekės_duomenys.kaina
            parduotuve = prekės_duomenys.parduotuve
            if not (prekės_duomenys.nuo < pirkimo_laikas < prekės_duomenys.iki):
                continue
            if kiekis == 0:
                continue

            if kiekis >= norimas_kiekis:
                print(f"{parduotuve} (dirba nuo 09:00 iki 17:00) nusipirko {versti(norima_preke)} {norimas_kiekis} po {kaina}")
                prekės_duomenys._replace(kiekis=kiekis - norimas_kiekis)
                norimas_kiekis = 0
            else:
                print(f"{parduotuve} (dirba nuo 09:00 iki 17:00) nusipirko {versti(norima_preke)} {kiekis} po {kaina}")
                prekės_duomenys._replace(kiekis=0)
                norimas_kiekis -= kiekis

            if norimas_kiekis == 0:
                break

if __name__ == '__main__':
    pass
