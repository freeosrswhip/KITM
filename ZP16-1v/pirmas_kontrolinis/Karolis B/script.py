import json
from collections import namedtuple

List = namedtuple("List",["parduotuve","preke","kiekis","kaina"])

with open("Karolis_inventorius.json", 'r',encoding='utf-8') as jsonas:
    inventorius = json.load(jsonas)

x=[]

for parduotuve in inventorius.values():
    for preke,info in parduotuve.items():
        x.append([preke,info["kiekis"]])


if __name__ == '__main__':
    pass