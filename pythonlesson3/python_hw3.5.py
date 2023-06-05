"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""

text = input("introduceti un cuvant: ")
sub_str = text[-6:]
print(sub_str)

str_inversat = text[::-1]
print(str_inversat)