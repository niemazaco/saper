'''
#list comprehension 3 przyklady
1 - plansza 2d - tworzenie macierzy pol
2 - przyciski 2d - tworzenie macierzy przyciskow pol
    
# 3x lambda
JEST
1 - przycisk start LPM
2 - przycisk pola LPM
3 - bind PPM pola
4 - bind x,y,z


# klasy - 4 wlasne klasy, w tym dwie dziedziczace po innych moich

#klasy - podzial

JEST - podzial na pliki


#walidacja wyjatkow - 


2/5 (wynagane 4)
'''

'''
do zrobienia na pewno:
    klik - sprawdzanie i wszystko dalej
    xyzzy
    tworzenie tablicy przy wyg/przeg
    obslugiwanie wyg/przeg
'''
import interfejs as gui
import random


class plansza():
    def __init__(self,wier,kol,bomb,logika,gui):
        self._logika = logika
        self._gui = gui
        #rozmiar
        self._w = wier #numeracja 1-15
        self._k = kol
        
        self._ilebomb = bomb
        #dodatkowe info
        self._wolnepola = wier * kol - bomb
        self._ileflag = 0
        self._flagzbomb = 0
        self._pytajniki = 0
        self._uzytykod = False
          
        #utworz pionki [wiersz][kolumna][nr stanu,czy jest bomba]
        #(0- puste, 1- flaga, 2 - pytajnik, 3 - bomba) -
        #(4 - klikniete, 5 - zla flaga, 6 - wybuch, xyzzy = stan+7) - tylko bez xyzzy
        # w sumie 7+4 stanow
        #
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
        if self._uzytykod:
            [[ self._pola[i][j][0] for j in range(self._k) if self._pola[i][j][0] in [0,1,2,3,5,6] ]
             for i in range(self._w)]
        #zrobic list comprehension selekcja pol z kodami 0,1,2,3,5,6 + sprawdzic czy xyzzy
        pass
        
    #sprawdza pole po kliknieciu
    def pole_klik(self,w,k):
        
        if self._pola[w][k][0] != 4:            
            self._gui.ustawpole(w, k, str(1), 4)
            self._pola[w][k][0] = 4
            self.przeklikajsasiadow(w, k)
        #uzupelnic
        print(w,k)
        pass

    def przeklikajsasiadow(self,m,n):  #lmb na pole 0 bomb - przeklikaj wszystkie wkolo
        if m>0:
            if n>0:
                self.pole_klik(m-1,n-1)
            self.pole_klik(m-1,n)
            if n<self._k-1:
                self.pole_klik(m-1,n+1)
            
        if n>0:
            self.pole_klik(m,n-1)
        if n<self._k-1:
            self.pole_klik(m,n+1)
    
        if m<self._w-1:
            if n>0:
                self.pole_klik(m+1,n-1)
            self.pole_klik(m+1,n)
            if n<self._k-1:
                self.pole_klik(m+1,n+1)




class logika():
    def __init__(self): 
        #blokuje wykonywanie wrazliwych fkcji (kilk buttona) az nie zakonczy sie poprzednie wywolanie
        self._aktualizacja = False   
        #tworzenie interfejsu bez planszy
        self._i = gui.interfejs(self)
        #wyswietlanie i dzialanie okienka
        self._i.start()
        

 
    def utworzplansze(self,w,k,b):
        if self._aktualizacja == True:
            return
        self._aktualizacja = True
        if hasattr(self, '_plansza') == True:
            del self._plansza
        self._plansza = plansza(w,k,b,self,self._i) #logika planszy
        self._i.ustawplansze(w, k, b) #przyciski w GUI
        self._aktualizacja = False
        pass
    
    #sprawdza pole po kliknieciu
    def klik(self,w,k,PPM):       
        if self._aktualizacja == True:
            return
        self._aktualizacja = True
        self._plansza.pole_klik(w,k)
        #wygrana
        #zmienic przycisku stan 0 lub 0+xyzzy na odpowiadajace im pola(zwykle lub xyzzy)
        
        #przegrana
        #wyswietlic zawartosc wszystkich pol(przegrana + pokazac stan 2 + xyzzy
        #+ zle postawione flagi + klikniete pole z bomba)
        self._aktualizacja = False
        pass
    
    def prosbaOKod(self):
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