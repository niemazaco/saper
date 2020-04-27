import random

def wczytywanie():
    if ile_bomb <= 0:
        print('wpisz prawidlowa ilosc bomb')
    if m>1 and n>1 and m<16 and n<16:
        if m*n >= ile_bomb:
            pass
        else:
            print('za duzo bomb')
    else: print('zle wymiary pola')

def plansza():
    rozmiar int m, n
    ilosc bomb = ile_bomb
    ilosc flag = 0
    ilosc flagzbombami = 0
    ilosc pytajnikow = 0
    ilosc wolnych = m*n - ile_bomb
    m*n - ilosc bomb
    pass



def losujbomby():
    licznik = ile_bomb
    while true:
        x = random.randint(0, m-1)
        y = random.randint(0, n-1)
        if plansza[m][n].bomba == false:
            plansza[m][n].bomba = true
            licznik -= 1
            if licznik == 0:
                break

def pole():
    bool mina
    int stan (0- puste, 1- flaga, 2 - pytajnik, 3 - klikniete)
    
    pass

def pole_klik(self,przyc): #klik na pole lub autom.odkrycie (bo sa zera)
    if self.stan == 0:
        if przyc == lewy:
            if self.bomba == true:
                print('przegrana')
            else: 
                self.stan = 3
                ile = przegladnij sasiadow(m,n)
                _wyswietl ile jest
                if ile == 0:
                    przeklikaj sasiadow(m,n)
                plansza.ilosc wolnych -= 1
                if plansza.ilosc wolnych == 0 == ilosc pytajnikow:
                    print('wygrana')
        else:
            self.stan = 1
            plansza. ilosc flag += 1
            if self.bomba == true:
                plansza. ilosc flagzbombami += 1
            if plansza.ilosc bomb == ilosc flagzbombami == ilosc flag:
                print('wygrana')
            
    elif self.stan == 1: #flaga
        #przyc lewy zablokowany
        if przyc == prawy:
            self.stan = 2
            plansza. ilosc pytajnikow += 1
            plansza. ilosc flag -= 1
            if self.bomba == true:
                plansza. ilosc flagzbombami -= 1
            
            
            
    elif self.stan == 2: #pytajnik
        
        plansza. ilosc pytajnikow -= 1
        if przyc == lewy:
            if self.bomba == true:
                print('przegrana')
            else:
                self.stan = 3
                ile = przegladnij sasiadow(m,n)
                _wyswietl ile jest
                if ile == 0:
                    przeklikaj sasiadow(m,n)
                if plansza.ilosc wolnych == 0 == ilosc pytajnikow:
                    print('wygrana')
        else: #prawy
            self.stan = 0
            if plansza.ilosc bomb == ilosc flagzbombami == ilosc flag:
                print('wygrana')   
        
        
    elif self.stan == 3:
        pass
    
    
#test

def przegladnij sasiadow(m,n): # sprawdza ile bomb wkolo
    licznik = 0
    if m>0:
        if n>0:
            if [m-1][n-1].bomba == true:
                licznik += 1
        if [m-1][n].bomba == true:
            licznik += 1
        if n<plansza.n-1:
            if [m-1][n+1].bomba == true:
                licznik += 1
        
    if n>0:
        if [m][n-1].bomba == true:
                licznik += 1
    if n<plansza.n-1:
        if [m][n+1].bomba == true:
                licznik += 1

    if m<plansza.m-1:
        if n>0:
            if [m+1][n-1].bomba == true:
                licznik += 1
        if [m+1][n].bomba == true:
            licznik += 1
        if n<plansza.n-1:
            if [m+1][n+1].bomba == true:
                licznik += 1
    


def przeklikaj sasiadow(m,n):  #lmb na pole 0 bomb - przeklikaj wszystkie wkolo
    if m>0:
        if n>0:
            pole_klik([m-1][n-1])
        pole_klik [m-1][n]
        if n<plansza.n-1:
            pole_klik [m-1][n+1]
        
    if n>0:
        pole_klik [m][n-1]
    if n<plansza.n-1:
        pole_klik [m][n+1]

    if m<plansza.m-1:
        if n>0:
            pole_klik [m+1][n-1]
        pole_klik [m+1][n]
        if n<plansza.n-1:
            pole_klik [m+1][n+1]

        