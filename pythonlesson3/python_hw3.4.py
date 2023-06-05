

"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

proba1 = int(input("proba1 = "))
proba2 = int(input("proba2 = "))
proba3 = int(input("proba3 = "))
media = int((proba1 + proba2 + proba3) / 3)

print(f'proba medie este egala cu = {media} secunde')