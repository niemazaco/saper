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
        #(0- puste, 1- flaga, 2 - pytajnik, 3 - bomba) - po xyzzy stan+=7
        #(4 - klikniete, 5 - zla flaga, 6 - wybuch) - tylko bez xyzzy
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
        
    #sprawdza pole po kliknieciu LPM
    def poleLPM(self,w,k,nieklikajflagi=False):
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                if self._pola[w][k][1] == True: #bomba
                    print('przegrana')
                else: 
                    self._pola[w][k][0] = 4 #ustawianie stanu
                    ile = str(self.przegladnijsasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                    
                    if ile == '':
                        self.przeklikajsasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    if self._wolnepola == 0 == self._pytajniki:
                        print('wygrana')

          
        #pole z flaga
        elif self._pola[w][k][0] % 7 == 1:
            #przyc lewy zablokowany
            pass
           
                
        #pole z pytajnikiem
        elif self._pola[w][k][0] % 7 == 2:
            #przy automatycznym odkrywaniu nie sprawdza flagi
            if nieklikajflagi == False: 
                self._pytajniki -= 1
                if self._pola[w][k][1] == True: #bomba
                    print('przegrana')
                else:
                    self._pola[w][k][0] = 4
                    ile = str(self.przegladnijsasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                    if ile == '':
                        self.przeklikajsasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    if self._wolnepola == 0 == self._pytajniki:
                        print('wygrana')


    #sprawdza pole po kliknieciu PPM
    def polePPM(self,w,k):
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                self._pola[w][k][0] = 1 + 7*self._uzytykod #ustaw stan
                self._ileflag += 1
                if self._pola[w][k][1] == True:
                    self._flagzbomb += 1
                self._gui.ustawpole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                if self._ilebomb == self._flagzbomb == self._ileflag and 0 == self._pytajniki:
                    print('wygrana')

          
        #pole z flaga
        elif self._pola[w][k][0] % 7 == 1:
                self._pola[w][k][0] = 2 + 7*self._uzytykod
                self._pytajniki += 1
                self._ileflag -= 1
                if self._pola[w][k][1] == True:
                    self._flagzbomb -= 1
                self._gui.ustawpole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                
                
        #pole z pytajnikiem
        elif self._pola[w][k][0] % 7 == 2:
                self._pytajniki -= 1
                self._pola[w][k][0] = 0+ 7*self._uzytykod
                self._gui.ustawpole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                
                #wszystkie bomby wczesniej poprawnie oflagowane, brak zbednych flag, znika ostatni pytajnik
                if self._ilebomb == self._flagzbomb == self._ileflag and 0 == self._pytajniki:
                    print('wygrana')
                    
                #wszystkie bez min byly klikniete LPM, ale byly rowniez pytajniki
                if self._wolnepola == 0 == self._pytajniki:
                    print('wygrana')




    def przegladnijsasiadow(self,m,n): # zlicza ile bomb wkolo
        licznik = 0
        if m>0:
            if n>0:
                if self._pola[m-1][n-1][1] == True:
                    licznik += 1
            if self._pola[m-1][n][1] == True:
                licznik += 1
            if n<self._k-1:
                if self._pola[m-1][n+1][1] == True:
                    licznik += 1
            
        if n>0:
            if self._pola[m][n-1][1] == True:
                    licznik += 1
        if n<self._k-1:
            if self._pola[m][n+1][1] == True:
                    licznik += 1
    
        if m<self._w-1:
            if n>0:
                if self._pola[m+1][n-1][1] == True:
                    licznik += 1
            if self._pola[m+1][n][1] == True:
                licznik += 1
            if n<self._k-1:
                if self._pola[m+1][n+1][1] == True:
                    licznik += 1
        return licznik

    def przeklikajsasiadow(self,m,n):  #LPM na pole 0 bomb - przeklikaj wszystkie wkolo
        if m>0:
            if n>0:
                self.poleLPM(m-1,n-1,nieklikajflagi=True)
            self.poleLPM(m-1,n,nieklikajflagi=True)
            if n<self._k-1:
                self.poleLPM(m-1,n+1,nieklikajflagi=True)
            
        if n>0:
            self.poleLPM(m,n-1,nieklikajflagi=True)
        if n<self._k-1:
            self.poleLPM(m,n+1,nieklikajflagi=True)
    
        if m<self._w-1:
            if n>0:
                self.poleLPM(m+1,n-1,nieklikajflagi=True)
            self.poleLPM(m+1,n,nieklikajflagi=True)
            if n<self._k-1:
                self.poleLPM(m+1,n+1,nieklikajflagi=True)




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
        if PPM == False:
            self._plansza.poleLPM(w,k)
        else:
            self._plansza.polePPM(w,k)
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
        if self._aktualizacja == True:
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


# eeee
