import json
from collections import namedtuple

List = namedtuple("List",["parduotuve","preke","kiekis","kaina"])

with open("laurynas_pirkėjai.json", 'r',encoding='utf-8') as jsonas:
    prikejai = json.load(jsonas)

with open("laurynas_inventorius.json", 'r',encoding='utf-8') as jsonas:
    inventorius = json.load(jsonas)


lst = []
for parduotuve, pard_duom in inventorius.items():
    for preke, prekes_info in pard_duom.items():
        lst.append(List(parduotuve,preke,prekes_info['kiekis'],prekes_info['kaina']))

prekes = set([s.preke for s in lst])

db={}
for preke in prekes:
    db[preke] =sorted([s for s in lst if s.preke==preke],key=lambda x:x.kaina)

for pirkejas,np in prikejai.items():
	print( pirkejas + ":" )
	for norima_preke,norimas_kiekis in np.items():
		for pd in db[norima_preke]:
			kiekis = pd.kiekis
			kaina = pd.kaina
			parduotuve = pd.parduotuve
			if kiekis == 0:
				continue

			if kiekis >= norimas_kiekis:
				print(f"nusipirko {norimas_kiekis} {norima_preke} po {kaina} iš {parduotuve}")
				pd._replace(kiekis=kiekis-norimas_kiekis)
				norimas_kiekis = 0
			else:
				print(f"nusipirko {norimas_kiekis} {norima_preke} po {kaina} iš {parduotuve}")
				pd._replace(kiekis=0)
				norimas_kiekis -= kiekis
			if norimas_kiekis == 0:
				break
	print()


if __name__=='__main__':
    pass