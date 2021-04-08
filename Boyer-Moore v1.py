
"""
WYTYCZNE:

Algorytm Boyer-Moore

Program powinien wczytać z pliku przeszukiwany tekst oraz wzorzec (wzorce) do wyszukiwania
zapisać indeksy do odrębnego pliku z wynikami.

Co ma sie znalezc w pdliku wyjsciowym?:

ile razy wzorzec pojawił się w tekście;
indeksy początków wzorców w tekście.

"""

# Pobranie danych od użytkownika i wczytanie pliku wejściowego

sciezka = input('Podaj ścieżkę plliku:  ')
plik = open(sciezka, 'r', encoding='UTF-8')
tekst = plik.read()

# # Pętla na dodawanie wzorców
#
# wzorce = []
# powtorz = 'T'
# while powtorz == 'T':
#     wzorzec = input('Podaj wzorzec, który chcesz wyszukać w pliku:  ')
#     wzorce.append(wzorzec)
#     odp = input('Wzorzec dodany, czy chcesz dodać kolejny [T/N]?:  ').upper()
#     if odp == 'T':
#         powtorz = odp
#     elif odp == 'N':
#         powtorz = odp
#     else:
#         odp = input('Zła odpowiedź, czy chcesz dodać kolejny [T/N]?:  ').upper()
#
#
# # Czyści plik wyjściowy przed kolejnym użyciem programu (kolejne wyszukiwania, są dodawane na zasadzie append, stąd taka potrzeba
#
# with open('plik_wyjsciowy.txt', 'w', encoding='utf-8') as f:
#     f.write('')

# Algorytm Boyer-Moore


wzorzec = input('Podaj szukany wzorzec: ')

i = 0
j = len(wzorzec) - 1

wartosci = {x: max(1, len(wzorzec) - i - 1) for (x, i) in zip(wzorzec, range(len(wzorzec)))} # o ile algorytm ma się przesuwać
indeksy = []
wystapienia = 0

while i+len(wzorzec) <= len(tekst) - 1:
    zakres = tekst[i:i+len(wzorzec)]
    while j >= 0:
        if wzorzec[j] == zakres[j]:
            if j == 0:
                indeksy.append(i)
                wystapienia += 1
                przesun = len(wzorzec)
                i += przesun
                break
            j -= 1
        else:
            if zakres[j] in wartosci:
                przesun = wartosci[zakres[j]]
                i += przesun
                break
            else:
                przesun = len(wzorzec)
                i += przesun
                break
    j = len(wzorzec) - 1

wynik = '\nIlośc wystąpień \"{}\" : {}\nIndeksy pierwszych znaków : {}\n\n'.format(wzorzec, wystapienia, indeksy)
print(wynik)

# Generowanie pliku wyjściowego
#
# with open('plik_wyjsciowy.txt', 'a', encoding='utf-8') as f:
#     f.write('Ilośc wystąpień \"{}\" : {}\nIndeksy pierwszych znaków : {}\n\n'.format(wzorzec, wystapienia, indeksy))
#
# plik.close()
# print('Zakończono przeszukiwanie')










