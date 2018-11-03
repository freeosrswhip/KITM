import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="Inventoriaus failo pavadinimas", required=True)
args = parser.parse_args()

prekes = ['obuoliai', 'kriauses', 'bulves', 'pomidorai', "mandarinai", "vysnios", 'apelsinai']
inventoriai = {}
pirkejai = {}

def zero_padding(s):
	return str(s) if s > 9 else '0' + str(s)

def sugeneruoti_reikiamo_ilgio_atsitiktini_sarasa(sarasas, n):
	t = sarasas
	unq = []
	for i in range(n):
		unq.append(random.choice(t))
		t = [e for e in t if e not in unq]
	return unq

for i in range(1, 11):
	parduotuves_pavadinimas = "parduotuve_" + str(i)
	inventoriai[parduotuves_pavadinimas] = {}

	atsitiktines_prekes = sugeneruoti_reikiamo_ilgio_atsitiktini_sarasa(prekes, 4)
	for preke in atsitiktines_prekes:
		inventoriai[parduotuves_pavadinimas][preke] = {"kiekis": random.randint(3, 5),
													   "kaina": random.randint(100, 300) / 100.0,
														"darba":{"nuo":zero_padding(random.randint(7,12))+":00","iki":zero_padding(random.randint(13,24))+":00"}}
with open(args.f + "_inventorius.json", 'w') as fout:
	fout.write(json.dumps(inventoriai, indent=2, ensure_ascii=False))
	fout.close()

for i in range(1, 4):
	pirkejai["pirkejas_" + str(i)] = {
		preke: kiekis
		for preke, kiekis in zip(sugeneruoti_reikiamo_ilgio_atsitiktini_sarasa(prekes, 3), [random.randint(1, 10) for _ in range(3)])
	}
	r_val = random.randint(7,23)
	r_min = random.randint(1,59)
	pirkejai["pirkejas_"+str(i)]["laikas"] = zero_padding(r_val) + ":" + zero_padding(r_min)

with open(args.f+"_pirkejai.json", 'w') as fout:
	fout.write(json.dumps(pirkejai, indent=2, ensure_ascii=False))
	fout.close()

