#Najlepszym sposobem do testowania jednostkowego jest zastosowanie unittest w celu przetestowania jednostek lub klas.
import unittest

class TestStringMethods(unittest.TestCase): #Unittest dostarcza razem z klasa unittest.TestCase zbior metod z prefixem assert, ktore sluza do porownywania wynikow
    def BlednaNazwa(self): #nazwa musi rozpoczynac sie od slowa test
        self.assertEqual(3+6, 9) #sprawdza czy rownanie 3+6=9
    def test1Poprawny(self):
        self.assertEqual(3+6, 9) #sprawdza czy rownanie 3+6=9
    def test2Poprawny(self):
        self.assertTrue('TEKST'.isupper()) #test sprawdzajacy czy wartosc w nim jest prawdziwa
        self.assertFalse('Tekst2'.isupper()) #test sprawdzajacy czy wartosc w nim jest falszywa
    def test3Bledny(self):
        self.assertEqual("test"+"TEST", "test3") #sprawdza czy dzialanie napis będzie rowny "test3", ale widzimy z gory, ze test sie nie uda

if __name__ == '__main__':
    unittest.main()