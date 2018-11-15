import json

with open("edvardas_inventorius.json") as f:
    data = json.load(f)

prekes = set([preke for parduotuve in data.values() for preke in parduotuve])
bendras = {"visų_parduotuvių_inventorius":{preke:0 for preke in prekes}}

for parduotuve in data.values():
    for preke, info in parduotuve.items():
        bendras["visų_parduotuvių_inventorius"][preke]+= info['kiekis']

with open("rezultatai.json",'w') as fout:
    fout.write(json.dumps(bendras,indent=2, ensure_ascii=False))
