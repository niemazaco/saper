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
import interfejs as gui
import random


class pole():
    def __init__(self,wier,kol):
        self.w = wier
        self.k = kol
        self._stan = 0 #(0- puste, 1- flaga, 2 - pytajnik, 3 - klikniete)
        self._bomba = False
        pass
    
    def bomba(self):
        return self._bomba
    
    def ustaw_bombe(self):
        self._bomba = True
        
        

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
        #utworz pionki
        self._lista = [[pole(i,j) for j in range(kol)] for i in range(wier)]
        self.losujbomby()
        #interfejs - utworz przyciski i zwroc klikacze
   
    def losujbomby(self):
        licznik = self._ilebomb
        while 1:
            x = random.randint(0, self._w-1)
            y = random.randint(0, self._k-1)
            if self._lista[x][y].bomba() == False:
                self._lista[x][y].ustaw_bombe()
                licznik -= 1
                if licznik == 0:
                    break    
       
    #sprawdza pole po kliknieciu
    def sprawdz(self,w,k):
        
        #uzupelnic
        
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
        self.sprawdz(w,k)        
        self._aktualizacja = False
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