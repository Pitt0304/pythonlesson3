"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""
#propozitia = <built-in method lower of str object at 0x000001C52E1F54D0>EEEEEEE
propozitie = input("introduceti propozitia: ")
print(len(propozitie))
print(propozitie.lower().count('e'))
