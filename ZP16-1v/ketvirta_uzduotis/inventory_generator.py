import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="Inventoriaus failo pavadinimas", required=True)
args = parser.parse_args("-f edvardas".split())

prekės = ['obuoliai', 'kriaušės', 'bulvės', 'pomidorai', "mandarinai", "vyšnios", 'apelsinai']
inventoriai = {}
pirkėjai = {}
koord = set()


def get_coord():
    k = (random.randint(0, 1000), random.randint(0, 1000))
    if k in koord:
        while k in koord:
            k = (random.randint(0, 1000), random.randint(0, 1000))
    else:
        koord.add(k)
    return k

def generuoti_norimas_prekes():
    return {
        prekė: kiekis
        for prekė, kiekis in
        zip(sugeneruoti_reikiamo_ilgio_atsitiktinį_sąrašą(prekės, 3), [random.randint(1, 10) for _ in range(3)])
    }

def zero_padding(s):
    return s if s > 9 else f'0{s}'


def sugeneruoti_reikiamo_ilgio_atsitiktinį_sąrašą(sąrašas, n):
    t = sąrašas.copy()
    unq = []
    for i in range(n):
        unq.append(random.choice(t))
        t = [e for e in t if e not in unq]
    return unq


for i in range(1, 11):
    parduotuvės_pavadinimas = f"parduotuvė_{i}"
    inventoriai[parduotuvės_pavadinimas] = {
        "dirba": {"nuo": f"{zero_padding(random.randint(7,12))}:00",
                  "iki": f"{zero_padding(random.randint(13,24))}:00"},
        "inventorius": {},
        "koordinates": get_coord()
    }

    atsitiktinės_prekės = sugeneruoti_reikiamo_ilgio_atsitiktinį_sąrašą(prekės, 4)
    for prekė in atsitiktinės_prekės:
        inventoriai[parduotuvės_pavadinimas]["inventorius"][prekė] = {"kiekis": random.randint(3, 5),
                                                                      "kaina": random.randint(100, 300) / 100.0}

with open(f"{args.f}_inventorius.json", 'w', encoding='utf-8') as fout:
    fout.write(json.dumps(inventoriai, indent=2, ensure_ascii=False))

for i in range(1, 4):
    pirkėjai[f"pirkėjas_{i}"] = {
        "norimos_prekes": generuoti_norimas_prekes(),
        "namai": get_coord(),
        "max_keliones_atstumas":random.randint(400,1200)
    }
    r_val = random.randint(7, 23)
    r_min = random.randint(1, 59)
    pirkėjai[f"pirkėjas_{i}"]["laikas"] = f"{zero_padding(r_val)}:{zero_padding(r_min)}"

with open(f"{args.f}_pirkėjai.json", 'w', encoding='utf-8') as fout:
    fout.write(json.dumps(pirkėjai, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    pass
