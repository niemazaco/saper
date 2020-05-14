'''
#list comprehension 3 przyklady
1 - plansza 2d - tworzenie macierzy pol
    2 - przyciski 2d - tworzenie macierzy przyciskow pol
    
# 3x lambda

# klasy - 4 wlasne klasy, w tym dwie dziedziczace po innych moich

#klasy - podzial

#podzial na pliki

#walidacja wyjatkow - 
'''
import interfejs as gui

class logika():
    def __init__(self):
        self._aktualizacja = False
        #tworzenie interfejsu bez planszy
        self._i = gui.interfejs(self)
        #listener na przyc start (funkcje wczytywanie)
        pass
    
    def utworzplansze(self,w,k):
        self._plansza = plansza(self,w,k)
        pass
    
    
    
    def xyzzy(self):
        #wybierz pionki z bombami + ich stan
        #wyslij do interfejsu
        pass
    
program = logika()
'''
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

class plansza():
    def __init__(self,wier,kol,bomb):
        self._w = wier
        self._k = kol
        self._ilebomb = bomb
        self._wolnepola = wier * kol - bomb
        self._ileflag = 0
        self._flagzbomb = 0
        self._pytajniki = 0
        #utworz pionki
        self._lista = [[pole(i,j) for j in kol] for i in wier]
        
        
class pole():
    def __init__(self,wier,kol):
        self.w = wier
        self.k = kol
        pass'''