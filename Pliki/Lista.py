#Lista: Zbior elementow roznych typow danych, ktore mozna zmienic w czasie wykonywania.

def funkcjaSortujaca(elementy):
  return len(str(elementy))

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
print(Lista.pop()) #zwraca co znajduje sie na ostatnim elemencie listy i usuwa go
Lista2 = list(range(5)) #tworzenie listy z wartosciami od 0 do 4
Lista.extend(Lista2) #dodaje Liste2 na koniec Listy
print(Lista)
Lista.insert(4, 2) #wstawia cyfre 2 jako 5(bo liczymy od 0) element w liscie
print(Lista)
Lista.remove(2) #usuwa pierwszy znaleziony element z listy rowny 2
print(Lista)
Lista.sort(reverse=False, key=funkcjaSortujaca) #sortuje liste według klucza podanego w funkcjiSortujaca
print(Lista)
Lista2=Lista.copy() #Tworzy kopię listy, w wypadku przypisania listy do listy2 metodą Lista2=Lista i wyczyszczeniu Lista Lista2 zostałaby również wyczyszczona
Lista.clear() #czysci liste
print(Lista2)
