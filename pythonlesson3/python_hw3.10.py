"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""

# text = I have started learning Python
text = input('introduce textul: ')
caractere_tinta = " ,1 week ago."
print(text + caractere_tinta)
caractere_inlocuire = input('introduce caractere de ilnocuire: ')
inlocuirea = (f'{text} {caractere_inlocuire} ')
print(inlocuirea)