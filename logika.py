'''
#list comprehension 3 przyklady (byle pokazać, że się umie)
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

JEST

własne moduły - podział na dwa pliki
JEST

4/5 (wynagane 4)

'''

'''
do zrobienia na pewno:
    dokumentacja
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
        self._uzytykod = False #kod xyzzy
          
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
 

    def wygrana(self):        
        #odkrywanie pozostałych pól       
        for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] %7 in [0]:  
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] = 3 + self._uzytykod * 7
                        ile = ''
                    else:
                        self._pola[w][k][0] = 4 #ustawianie stanu
                        ile = str(self.przegladnijsasiadow(w,k))
                        #uaktualnianie przycisku
                        if ile == '0':
                            ile = ''
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                        self._ilebomb - self._ileflag, self._pytajniki,
                                        self._wolnepola)
            
        return 1 #status wygranej
    
    def przegrana(self):
        '''for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] %7 in [0,2]:  
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] = 3 + self._uzytykod * 7
                        ile = ''
                    else:
                        self._pola[w][k][0] = 4 #ustawianie stanu
                        ile = str(self.przegladnijsasiadow(w,k))
                        #uaktualnianie przycisku
                        if ile == '0':
                            ile = ''
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                        self._ilebomb - self._ileflag, self._pytajniki,
                                        self._wolnepola)
                    
        '''      
        return 2 #status przegranej
       
    #sprawdza pole po kliknieciu LPM
    def poleLPM(self,w,k,nieklikajflagi=False):
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                if self._pola[w][k][1] == True: #bomba
                    self._pola[w][k][0] = 6
                    return self.przegrana()
                else: 
                    self._pola[w][k][0] = 4 #ustawianie stanu
                    ile = str(self.przegladnijsasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                        self.przeklikajsasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    if self._wolnepola == 0 == self._pytajniki:
                        return self.wygrana()

          
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
                    self._pytajniki -= 1
                    self._pola[w][k][0] = 6
                    return self.przegrana()
                    
            #klik PPM - z autoodkrywaniem
                else:
                    self._pola[w][k][0] = 4
                    ile = str(self.przegladnijsasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                        self.przeklikajsasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustawpole(w, k, ile, self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    if self._wolnepola == 0 == self._pytajniki:
                        return self.wygrana()
        
        return 0 #status "gramy dalej"

    #sprawdza pole po kliknieciu PPM
    def polePPM(self,w,k):
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                #ustaw stan z uwzglednieniem kodu xyzzy jesli to jest pole z bomba
                self._pola[w][k][0] = 1 + 7*self._uzytykod*self._pola[w][k][1]
                #aktualizacja zliczaczy
                self._ileflag += 1
                if self._pola[w][k][1] == True:
                    self._flagzbomb += 1
                #ustawianie pola w interfejsie
                self._gui.ustawpole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                #sprawdzanie czy nastapila wygrana
                if self._ilebomb == self._flagzbomb == self._ileflag and 0 == self._pytajniki:
                    return self.wygrana()

          
        #pole z flaga
        elif self._pola[w][k][0] % 7 == 1:
                self._pola[w][k][0] = 2 + 7*self._uzytykod*self._pola[w][k][1]
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
                self._pola[w][k][0] = 0+ 7*self._uzytykod*self._pola[w][k][1]
                self._gui.ustawpole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                
                #wszystkie bomby wczesniej poprawnie oflagowane, brak zbednych flag, znika ostatni pytajnik
                if self._ilebomb == self._flagzbomb == self._ileflag and 0 == self._pytajniki:
                    return self.wygrana()
                    
                #wszystkie bez min byly klikniete LPM, ale byly rowniez pytajniki
                if self._wolnepola == 0 == self._pytajniki:
                    return self.wygrana()
                    
        return 0 #status "gramy dalej"



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

    def xyzzy(self):
        if self._uzytykod == True:
            return
        self._uzytykod = True
        for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] in [0,1,2,3]:
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] += 7
                        self._gui.ustawpole(w, k, '', self._pola[w][k][0],
                                        self._ilebomb - self._ileflag, self._pytajniki,
                                        self._wolnepola)







class Logika():
    def __init__(self): 
        #blokuje wykonywanie wrazliwych fkcji (kilk buttona) az nie zakonczy sie poprzednie wywolanie
        self._aktualizacja = False   
        #blokada przyciskow po wygranej lub przegranej partii
        self._grazakonczona = False 
        #tworzenie interfejsu bez planszy
        self._gui = gui.interfejs(self)
        #wyswietlanie i dzialanie okienka
        self._gui.start()
        

 
    def utworzplansze(self,w,k,b):
        if self._aktualizacja == True:
            return
        self._aktualizacja = True
        self._grazakonczona = False
        if hasattr(self, '_plansza') == True:
            del self._plansza
        self._plansza = plansza(w,k,b,self,self._gui) #logika planszy
        self._gui.ustawplansze(w, k, b) #przyciski w GUI
        self._aktualizacja = False
        pass
    
    #sprawdza pole po kliknieciu
    def klik(self,w,k,PPM):       
        if self._aktualizacja == True or self._grazakonczona == True:
            return
        self._aktualizacja = True
        if PPM == True:
            w = self._plansza.polePPM(w,k)      
        else:
            w = self._plansza.poleLPM(w,k)
        if w == 1: #wygrana
            self._grazakonczona = True
            self._gui.wygrana()
        elif w == 2: #przegrana
            self._grazakonczona = True
            self._gui.przegrana()
        
        #przegrana
        #wyswietlic zawartosc wszystkich pol(przegrana + pokazac stan 2 + xyzzy
        #+ zle postawione flagi + klikniete pole z bomba)
        self._aktualizacja = False
        pass
    
    def prosbaOKod(self):
        if self._aktualizacja == True:
            return False
        self._aktualizacja = True
        self._plansza.xyzzy()
        self._aktualizacja = False
        return True
    
if __name__ == "__main__":
    start = Logika()
