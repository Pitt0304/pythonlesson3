"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""

propozitia = input('Intorduce textul tau: ')
print(propozitia.lower())
# vocale = '"a", "e", "i", "o", "u"'
# consoane = '"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"'
print('numar total de caractere: ' +  str(len(propozitia)))
print('numarul total de vocale "a" este: ' + str(propozitia.count("a")))
print('numarul total de vocale "e" este: ' + str(propozitia.count("e")))
print('numarul total de vocale "i" este: ' + str(propozitia.count("i")))
print('numarul total de vocale "o" este: ' + str(propozitia.count("o")))
print('numarul total de vocale "u" este: ' + str(propozitia.count("u")))


#doar asa mam discurcat, cu consoane o sa fie mai lung tar principiul acelasi