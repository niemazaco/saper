'''
#list comprehension 3 przyklady
1 - plansza 2d - tworzenie macierzy pol
    2 - przyciski 2d - tworzenie macierzy przyciskow pol
    
# 3x lambda
1 - przycisk start
2 - przycisk pola


# klasy - 4 wlasne klasy, w tym dwie dziedziczace po innych moich

#klasy - podzial

JEST - podzial na pliki


#walidacja wyjatkow - 


1/5 (wynagane 4)
'''

'''
do zrobienia na pewno:
    klik - sprawdzanie i wszystko dalej
    aktualizacja pola
    xyzzy
    tworzenie tablicy przy wyg/przeg
    obslugiwanie wyg/przeg
'''
import interfejs as gui
import random


class plansza():
    def __init__(self,logika,wier,kol,bomb):
        self._logika = logika 
        self._w = wier
        self._k = kol
        self._ilebomb = bomb
        self._wolnepola = wier * kol - bomb
        self._ileflag = 0
        self._flagzbomb = 0
        self._pytajniki = 0
            #self._uzytykod = False
          
        #utworz pionki [wiersz][kolumna][nr stanu,czy jest bomba]
        #(0- puste, 1- flaga, 2 - pytajnik, 3 - klikniete)
        #(4 - bomba, 5 - zla flaga, xyzzy = stan+6)
        self._pola = [[[0,False] for j in range(kol)] for i in range(wier)]
        
        #losowanie pol
        licznik = self._ilebomb
        while 1:
            x = random.randint(0, self._w-1)
            y = random.randint(0, self._k-1)
            if self._pola[x][y][1] == False:
                self._pola[x][y][1] = True
                licznik -= 1
                if licznik == 0:
                    break    
    
    def wyslijplansze(self):
        pass
        
    #sprawdza pole po kliknieciu
    def sprawdz(self,w,k,zwroc=False):
        
        #uzupelnic
        print(w,k)
        pass



class logika():
    def __init__(self): 
        #blokuje wykonywanie wrazliwych fkcji (kilk buttona) az nie zakonczy sie poprzednie wywolanie
        self._aktualizacja = False   
        #tworzenie interfejsu bez planszy
        self._i = gui.interfejs(self)
        #wyswietlanie i dzialanie okienka
        self._i.start()
        
        #listener na przyc start (funkcje wczytywanie)

 
    def utworzplansze(self,w,k,b):
        if self._aktualizacja == True:
            return
        self._aktualizacja = True
        if hasattr(self, '_plansza') == True:
            del self._plansza
        self._plansza = plansza(self,w,k,b) #logika planszy
        self._i.ustawplansze(w, k, b) #przyciski w GUI
        self._aktualizacja = False
        pass
    
    #sprawdza pole po kliknieciu
    def klik(self,w,k):       
        if self._aktualizacja == True:
            return
        self._aktualizacja = True
        self._plansza.sprawdz(w,k, zwroc=True)
        #wygrana
        #zmienic przycisku stan 0 lub 0+xyzzy na odpowiadajace im pola(zwykle lub xyzzy)
        
        #przegrana
        #wyswietlic zawartosc wszystkich pol(przegrana + pokazac stan 2 + xyzzy
        #+ zle postawione flagi + klikniete pole z bomba)
        self._aktualizacja = False
        pass
    
    #kazdy pojedyncze pole do pokazania - wywolac gui i aktualizacja obrazka przycisku
    
    #pokazywanie wszystkich pol na koniec
    def wygrana(self):
        pass
    
    def przegrana(self):
        pass
    
if __name__ == "__main__":
    start = logika()

'''    
    
    
    def xyzzy(self):
        if self._aktualizacja == False:
            return False
        self._aktualizacja = True
        #wybierz pionki z bombami + ich stan
        #wyslij do interfejsu
        self._aktualizacja = False
        pass


def wczytywanie():
    if but_ile_bomb <= 0:
        print('wpisz prawidlowa ilosc bomb')
    if input_m>1 and input_mn>1 and input_mm<16 and input_mn<16:
        if m*n >= ile_bomb:
            #skasuj plansze (za 1 razem nie ma)
            #zeruj timer
            # utworz plansze
            pass
        else:
            print('za duzo bomb')
    else: print('zle wymiary pola')



        
        


'''