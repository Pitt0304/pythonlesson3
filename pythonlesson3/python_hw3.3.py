"""Declaraţi o variabilă price, de tip int, care va reţine preţul unui produs citit de la tastatură.

* Calculaţi cât va reprezenta 30% din preţul iniţial şi salvaţi valoarea în variabila reducere
*	Scădeţi din preţul iniţial valoarea reducerii, calculate la pasul precedent. Salvaţi valoarea în variabila preţ_final
* Creaţi o variabilă nouă pret_100_lei, şi salvaţi în această variabilă cât va fi preţul iniţial minus 100 lei
* Afişaţi la final ambele preturi.

"""

pret_initial = input("Intoduceti pretul: ")
pret_initial = int(pret_initial)

reducere = (30 / 100) * pret_initial
print("reducerea de la pret initial = " + str(reducere) + " " + "lei")

pret_final = pret_initial - reducere
print("pretul final va fi: " + str(pret_final) + " " + "lei")

pret_100_lei = int(pret_initial - 100)
print(f'Pretul initial - 100 lei va fi: {pret_100_lei}')



print(f"pretul pana la reducere: {pret_initial}")
print(f"pretul dupa reducere : {pret_initial} - {reducere} = {pret_final} lei ")