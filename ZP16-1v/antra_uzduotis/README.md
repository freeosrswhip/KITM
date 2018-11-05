aleiskite inventory_generator.py scriptą, kad sugeneruotų 10 parduotuvių inventorių ir prekių kainas.

    >python inventory_generator.py -f vardas_pavarde
    
Bus sukurti du failai, vardas_pavarde_inventorius.json ir vardas_pavarde_pirkėjai.json

Užduotis:

1) Nuskaityti JSON failus ir pasiversti jį į python dictionary naudojant json.loads(str)
2) Pradedant nuo pirmo pirkėjo, rasti kurias parduotuves jam reikėtų aplankyti, kad supirkit norimus produktus
mažiausia kaina. Jeigu tos prekės nėra, nieko nerašoma. Jeigu tik trūksta kiekio, rašoma kiek nusipirko.

        >python vardas_pavarde.py
        pirkėjas_1:
        parduotuvė_1 nusipirko 3 pomidorus po 1.45
        parduotuvė_3 nusipirko 4 apelsinus po 2.15
        parduotuvė_8 nusipirko 6 bulves po 2.50
        pirkėjas_2:
        ....
        pirkėjas_3:
        ....
        
3) Išsprendus užduotį, padaryti pull request pridedant abu JSON failus, bei .py scriptą.


#### Viską įvykdžius:

Pirmas pull requestas pilnai ir tiksliai atlikęs užduotį gaus 10 už užduoties įvykdymą.

Kiti po 25 taškus. Surinkus 100 taškų, gausite 10.