#Lista: Zbior elementow roznych typow danych, ktore mozna zmienic w czasie wykonywania.
    
Lista = ['Przyklad1', 'Przyklad2', 'Przyklad3', 'Przyklad1', 'Przyklad2', 'Przyklad4', 'Przyklad5'] #przyklad inicjalizacji listy

print(Lista.count('Przyklad1')) #zliczanie elementow listy
print(Lista.index('Przyklad1')) #zwraca wartosc, na ktorym indeksie pierwszy raz trafi na Przyklad1
print(Lista.index('Przyklad5', 4)) #zwraca wartosc, na ktorym ideksie(zaczynając od indeksu nr 4) pierwszy raz trafi na Przyklad5
Lista.reverse() #odwraca kolejnosc elementow w liscie
print(Lista)
Lista.append('Przyklad6') #dodaje Przyklad6 na koncu listy
print(Lista)
Lista.sort() #sortuje liste alfabetycznie
print(Lista)
print(Lista.pop()) #zwraca co znajduje się na ostatnim elemencie listy