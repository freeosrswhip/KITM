import json
from collections import namedtuple

List = namedtuple("List",["parduotuve","preke","kiekis","kaina"])

with open("Karolis_inventorius.json", 'r',encoding='utf-8') as jsonas:
    inventorius = json.load(jsonas)

x=[]
prekes = []

for parduotuve in inventorius.values():
    for preke,info in parduotuve.items():
        prekes.append(preke)
        x.append([preke,info["kiekis"]])

unikalus = set(prekes)
rezultatas = {"visų_parduotuvių_inventorius":{preke:0 for preke in unikalus}}

for info in x:
    preke = info[0]
    kiekis = info[1]
    rezultatas["visų_parduotuvių_inventorius"][preke]+=kiekis

if __name__ == '__main__':
    pass
