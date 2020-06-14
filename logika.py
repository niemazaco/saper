import interfejs as gui
import random
import time


class Plansza():
    """Przechowuje wszystkie info o planszy i wykonuje na niej dzialania.
    
    Jest to podklasa klasy Logika, wydzielenie jej umozliwia szybkie i bezbledne
    usuwanie starego obiektu i zastapienie go nowym przy restarcie gry.
    """
    def __init__(self,wier,kol,bomb,logika,gui):
        """Tworzy macierz reprezentujaca plansze.
        
        Przyjmuje wymiary planszy, ilosc bomb oraz referencje do klas Logika 
        i Interfejs."""
        #referencje
        self._logika = logika
        self._gui = gui
        #rozmiar planszy
        self._w = wier #numeracja 1-15
        self._k = kol
        
        #ilosc bomb
        self._ilebomb = bomb
        # liczniki
        self._wolnepola = wier * kol - bomb
        self._ileflag = 0
        self._flagzbomb = 0
        self._pytajniki = 0
        #czy zostal uzyty kod - potrzebne przy aktualizacji statusow pol
        self._uzytykod = False
          
        '''Tworzenie macierzy pol [wiersz][kolumna][nr stanu, czy jest bomba].
        Lista stanow pol:
        0- puste, 1- flaga, 2 - pytajnik, 3 - bomba   // po xyzzy stan+=7
        4 - klikniete bez bomby                       // tylko bez xyzzy
        5 - zle postawiona flaga, 6 - wybuch          // tylko bez xyzzy
        w sumie 7 + 4 = 11 stanow
        '''
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

    def wygrana(self):
        """Autoodkrywanie niewcisnietych pol + zwraca nr statusu 'wygrana'."""        
        #odkrywanie pozostałych pól       
        for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] %7 in [0]:  
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] = 3 + self._uzytykod * 7
                        ile = ''
                    else:
                        self._pola[w][k][0] = 4 #ustawianie stanu
                        ile = str(self.przegladnij_sasiadow(w,k))
                        #uaktualnianie przycisku
                        if ile == '0':
                            ile = ''
                    self._gui.ustaw_pole(w, k, ile, self._pola[w][k][0],0,0,0)
            
        return 1 #status wygranej
    
    def przegrana(self):
        """Sprawdzanie pol + zwraca nr statusu 'przegrana'."""
        for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] %7 in [0]:
                    #nieklikniete pole z bomba
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] = 3 + self._uzytykod * 7 #ustawianie stanu
                        self._gui.ustaw_pole(w, k, '', self._pola[w][k][0],
                                        self._ilebomb - self._flagzbomb, self._pytajniki,
                                        self._wolnepola)
                elif self._pola[w][k][0] %7 in [1]:
                    #flaga postawiona w zlym miejscu
                    if self._pola[w][k][1] == False: #bomba
                        self._gui.ustaw_pole(w, k, '', 5,
                                        self._ilebomb - self._flagzbomb, self._pytajniki,
                                        self._wolnepola)
                elif self._pola[w][k][0] %7 in [2]:
                    #odkrywanie pytajnika jezeli jest pod nim bomba
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] = 3 + self._uzytykod * 7 #ustawianie stanu
                        self._gui.ustaw_pole(w, k, '', self._pola[w][k][0],
                                        self._ilebomb - self._flagzbomb, self._pytajniki,
                                        self._wolnepola)             
        return 2 #status przegranej
       
    #sprawdza pole po kliknieciu LPM
    def poleLPM(self,w,k,nie_klikaj_pytajnika=False):
        """Obsluga algorytmu przy wcisnieciu przycisku LPM na polu o wspolrzednych [w,k].
        
        Zmienna nie_klikaj_pytajnika uchrania przed autoodkrywaniem pol oznaczonych
        pytajnikiem, umozliwiajac jego normalne klikniecie LPM w celu odkrycia pola."""
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                if self._pola[w][k][1] == True: #bomba
                    self._pola[w][k][0] = 6
                    self._gui.ustaw_pole(w, k, '', self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    return self.przegrana()
                else: 
                    self._pola[w][k][0] = 4 #ustawianie stanu
                    ile = str(self.przegladnij_sasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                        self.przeklikaj_sasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustaw_pole(w, k, ile, self._pola[w][k][0],
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
            if nie_klikaj_pytajnika == False: 
                self._pytajniki -= 1
                if self._pola[w][k][1] == True: #bomba
                    self._pytajniki -= 1
                    self._pola[w][k][0] = 6
                    self._gui.ustaw_pole(w, k, '', self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    return self.przegrana()
                    
            #klik PPM - z autoodkrywaniem
                else:
                    self._pola[w][k][0] = 4
                    ile = str(self.przegladnij_sasiadow(w,k))
                    #uaktualnianie przycisku
                    if ile == '0':
                        ile = ''
                        self.przeklikaj_sasiadow(w,k)
                    self._wolnepola -= 1
                    self._gui.ustaw_pole(w, k, ile, self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                    if self._wolnepola == 0 == self._pytajniki:
                        return self.wygrana()      
        return 0 #status "gramy dalej"

    #sprawdza pole po kliknieciu PPM
    def polePPM(self,w,k):
        """Obsluga algorytmu przy wcisnieciu przycisku PPM na polu o wspolrzednych [w,k]."""
        #pole w pozycji startowej
        if self._pola[w][k][0] % 7 == 0:
                #ustaw stan z uwzglednieniem kodu xyzzy jesli to jest pole z bomba
                self._pola[w][k][0] = 1 + 7*self._uzytykod*self._pola[w][k][1]
                #aktualizacja zliczaczy
                self._ileflag += 1
                if self._pola[w][k][1] == True:
                    self._flagzbomb += 1
                #ustawianie pola w interfejsie
                self._gui.ustaw_pole(w, k, "", self._pola[w][k][0],
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
                self._gui.ustaw_pole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                
                
        #pole z pytajnikiem
        elif self._pola[w][k][0] % 7 == 2:
                self._pytajniki -= 1
                self._pola[w][k][0] = 0+ 7*self._uzytykod*self._pola[w][k][1]
                self._gui.ustaw_pole(w, k, "", self._pola[w][k][0],
                                    self._ilebomb - self._ileflag, self._pytajniki,
                                    self._wolnepola)
                
                #wszystkie bomby wczesniej poprawnie oflagowane, brak zbednych flag, znika ostatni pytajnik
                if self._ilebomb == self._flagzbomb == self._ileflag and 0 == self._pytajniki:
                    return self.wygrana()
                    
                #wszystkie bez min byly klikniete LPM, ale byly rowniez pytajniki
                if self._wolnepola == 0 == self._pytajniki:
                    return self.wygrana()
                    
        return 0 #status "gramy dalej"



    def przegladnij_sasiadow(self,m,n):
        """Oblicza, z iloma minami sasiaduje pole o wspolrzednych [m,n]."""
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

    def przeklikaj_sasiadow(self,m,n):
        """Autoodkrywanie sasiednich pol."""
        if m>0:
            if n>0:
                self.poleLPM(m-1,n-1,nie_klikaj_pytajnika=True)
            self.poleLPM(m-1,n,nie_klikaj_pytajnika=True)
            if n<self._k-1:
                self.poleLPM(m-1,n+1,nie_klikaj_pytajnika=True)
            
        if n>0:
            self.poleLPM(m,n-1,nie_klikaj_pytajnika=True)
        if n<self._k-1:
            self.poleLPM(m,n+1,nie_klikaj_pytajnika=True)
    
        if m<self._w-1:
            if n>0:
                self.poleLPM(m+1,n-1,nie_klikaj_pytajnika=True)
            self.poleLPM(m+1,n,nie_klikaj_pytajnika=True)
            if n<self._k-1:
                self.poleLPM(m+1,n+1,nie_klikaj_pytajnika=True)

    def xyzzy(self):
        """Aktualizuje stan pol z bombami na stan po uzyciu kodu."""
        self._uzytykod = True
        for w in range(self._w):
            for k in range(self._k):
                if self._pola[w][k][0] in [0,1,2,3]:
                    if self._pola[w][k][1] == True: #bomba
                        self._pola[w][k][0] += 7
                        self._gui.ustaw_pole(w, k, '', self._pola[w][k][0],
                                        self._ilebomb - self._ileflag, self._pytajniki,
                                        self._wolnepola)


class Logika():
    """Klasa odpowiadajaca za logike gry.
    
    Jej czesc zostala wydzielona do klasy Plansza, aby ja latwo usuwac i tworzyc na nowo."""
    def __init__(self):
        '''Definiuje potrzebne zmienne i uruchamia interfejs, ktory przejmuje dzialanie programu.'''
        #blokuje wykonywanie wrazliwych fkcji (kilk buttona) az nie zakonczy sie poprzednie wywolanie
        self._aktualizacja = False   
        #blokada przyciskow po wygranej lub przegranej partii
        self._grazakonczona = False 
        #tworzenie interfejsu bez planszy
        self._gui = gui.Interfejs(self)
        #wyswietlanie i dzialanie okienka
        self._gui.start()
        

 
    def utworz_plansze(self,w,k,b):
        """Usuwa obiekt planszy z poprzedniej partii i wywoluje tworzenie nowego."""
        if self._aktualizacja == True:
            return False
        self._aktualizacja = True
        self._grazakonczona = False
        if hasattr(self, '_plansza') == True:
            del self._plansza
        self._plansza = Plansza(w,k,b,self,self._gui) #tworzenie planszy
        self._aktualizacja = False
        return True
    
    def klik(self,w,k,PPM):
        """Sprawdza pole po jego kliknieciu i podaje do interfejsu info o koncu gry."""
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
        self._aktualizacja = False
        pass
    
    def prosba_o_kod(self):
        '''Metoda wywolywana po wcisnieciu sekwencji xyzzy.'''
        while self._aktualizacja == True:
            time.sleep(0.05)
        #sekcja krytyczna
        self._aktualizacja = True
        self._plansza.xyzzy()
        self._aktualizacja = False
    
#uruchamianie programu
if __name__ == "__main__":
    start = Logika()
