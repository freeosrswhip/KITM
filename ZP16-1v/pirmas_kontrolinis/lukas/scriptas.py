import json

with open("Lukas_inventorius.json", 'r', encoding='utf-8') as file:
    inventorius = json.load(file)

x = []
prekes = []

for parduotuve in inventorius.values():
    for preke, info in parduotuve.items():
        prekes.append(preke)
        x.append([preke, info["kiekis"]])

unikalus = prekes
rezultatas = {"visu_parduotuviu_inventorius":{preke:0 for preke in unikalus}}

for info in x:
    preke = info[0]
    kiekis = info[1]
    rezultatas["visu_parduotuviu_inventorius"][preke] += kiekis

with open('rezultatai.json', 'w') as outfile:
    json.dump(rezultatas, outfile)

if __name__ == '__main__':
    pass