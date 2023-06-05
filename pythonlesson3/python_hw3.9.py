"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""

#propozitia = I have started learning Python, 1 week ago.!?

propozitia = input("introduce propozitia: ")
no_punctuation = propozitia.replace(',', '')\
    .replace('.', '')\
    .replace('!', '')\
    .replace('?', '')



print(no_punctuation)








