"""Eliminați spațiile
Scrieți un program care primește o propoziție ca intrare și elimină toate caracterele de spațiu din ea."""

#propozitia = I have started learning Python 1 week ago.
propozitia = input('please input your text: ')

print(propozitia.replace(' ', ''))
print(propozitia.replace('', ' '))
print(propozitia.replace('week', 'month'))