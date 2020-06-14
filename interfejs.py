from tkinter import *

class BladDanychException(Exception):
    """Zwraca tekst do message boxa przy blednych danych wejsciowych.
    
    Klasy pochodne przygotowuja odpowiedni tekst do wyswietlenia w zaleznosci od
    podanych w inputach parametrow.
    Lista klas pochodnych:
    BladSzerokosciException
    BladWysokosciException
    BladBombException"""
    def __init__(self, ktorepole, wartosc):
        self._pole = ktorepole
        self._trescbledu = wartosc
        
    def wypisz1(self):
        return "Blad w inpucie {}".format(self._pole)
    def wypisz2(self):
        return "O co chodzi? {}".format(self._trescbledu)
        
class BladSzerokosciException(BladDanychException):
    def __init__(self, wartosc):
        if wartosc < 2:
            super().__init__("Szerokosc planszy","Za mala szerokosc. Musi sie zawierac pomiedzy 2 a 15!")
        else:
            super().__init__("Szerokosc planszy","Za duza szerokosc. Musi sie zawierac pomiedzy 2 a 15!")
            
class BladWysokosciException(BladDanychException):
    def __init__(self, wartosc):
        if wartosc < 2:
            super().__init__("Wysokosc planszy","Za mala wysokosc. Musi sie zawierac pomiedzy 2 a 15!")
        else:
            super().__init__("Wysokosc planszy","Za duza wysokosc. Musi sie zawierac pomiedzy 2 a 15!")
            
class BladBombException(BladDanychException):
    def __init__(self, wysokosc, szerokosc, bomby):
        if wysokosc * szerokosc < bomby:
            super().__init__("Ilosc bomb",
                  "Za duzo bomb, nie zmieszcza sie na planszy! Wpisz pomiedzy 1 a {}!".
                  format(wysokosc*szerokosc-1))
        elif wysokosc * szerokosc == bomby:
            super().__init__("Ilosc bomb",
                  "Co ty, chcesz grac bez wolnych pol? Wpisz pomiedzy 1 a {}!".
                  format(wysokosc*szerokosc-1))
        elif bomby < 0:
            super().__init__("Ilosc bomb",
                  "Wpisz dodatnia ilosc bomb!")
        else:
            super().__init__("Ilosc bomb",
                  "Co ty, chcesz grac bez bomb? Wpisz dodatnia ilosc bomb!")
        

class Interfejs():
    """Wydzielona czesc programu - odpowiada za tworzenie i aktualizacje interfejsu."""
    def __init__(self,logika):
        '''Tworzy interfejs umozliwiajacy rozpoczecie gry.
        
        Przyjmuje referencje do obiektu Logika, aby mogly zostac wykonane akcje
        przy wciskaniu przyciskow.'''
        self._logika = logika 
        self._window=Tk()
        self._window.title("Saper Jakub Medalion")
        self._window.geometry("570x400")
        
        #bindowanie klawiszy do kodu xyzzy:
        self._window.bind("x", lambda e:self.xyzzy('x'))
        self._window.bind("y", lambda e:self.xyzzy('y'))
        self._window.bind("z", lambda e:self.xyzzy('z'))
        self._window.bind("X", lambda e:self.xyzzy('x'))
        self._window.bind("Y", lambda e:self.xyzzy('y'))
        self._window.bind("X", lambda e:self.xyzzy('z'))
        #ilosc znakow z kodu juz wpisana
        self._kodwpisany = 0
        
        #tla przyciskow dla stanow 0-10 wypisanych w klasie Plansza
        self._i0 = PhotoImage(file="pusty.png")
        self._i1 = PhotoImage(file="flaga.png")
        self._i2 = PhotoImage(file="pytajnik.png")
        self._i3 = PhotoImage()
        self._ibomb = PhotoImage(file="bomba.png")
        self._iwybuch = PhotoImage(file="wybuch.png")
        self._flagazla = PhotoImage(file="flagazla.png")
        self._xyzzy0 = PhotoImage(file="xyzzy0.png")
        self._xyzzy1 = PhotoImage(file="xyzzy1.png")
        self._xyzzy2 = PhotoImage(file="xyzzy2.png")        
        self._xyzzybomba = PhotoImage(file="xyzzybomba.png")
        self._listatel = [self._i0,self._i1,self._i2,self._ibomb,
                          self._i3,self._flagazla,self._iwybuch,
                          self._xyzzy0,self._xyzzy1,self._xyzzy2,self._xyzzybomba]
        
        # utworzenie glownych kontenerow
        self._panellewy = Frame(self._window, bg='blue', width=160, height=400, padx=3, pady=3)
        self._panelprawy = Frame(self._window, bg='gold', width=400, height=400, padx=3, pady=3)
        
        # rozstawienie glownych kontenerow
        self._window.grid_rowconfigure(1, weight=1)
        self._window.grid_columnconfigure(0, weight=1)
        
        self._panellewy.grid(row=0, sticky="nsw")
        self._panelprawy.grid(row=0, sticky="nse")
        
        self._panellewy.grid_propagate(0)
        self._panelprawy.grid_propagate(0)
        
        #panel lewy
        self._lszer = Label(self._panellewy, text='szerokosc:')
        self._lwys = Label(self._panellewy, text='wysokosc:')
        self._lbomb = Label(self._panellewy, text='ilosc bomb:')
        
        self._inszer = Entry(self._panellewy, background="pink")
        self._inwys = Entry(self._panellewy, background="orange")
        self._inbomb = Entry(self._panellewy, background="orange")
        self._bstart = Button(self._panellewy, text="start", 
                        command=lambda: 
                            self.wczytaj(self._inwys.get(),
                                         self._inszer.get(),
                                         self._inbomb.get()))
        
        self._lflag = Label(self._panellewy, text='pozostalo bomb:')
        self._lpyt = Label(self._panellewy, text='ilosc pytajnikow:')
        self._lwolne = Label(self._panellewy, text='wolne pola:')
        self._lstatus = Label(self._panellewy, text='WPISUJ I ZACZYNAJ :-)')        
        
        # ukladanie elementow w lewym panelu
        self._lszer.grid(row=0, padx=3, pady=3)
        self._inszer.grid(row=1, padx=3, pady=3)
        self._lwys.grid(row=2, padx=3, pady=3)
        self._inwys.grid(row=3, padx=3, pady=3)
        self._lbomb.grid(row=4, padx=3, pady=3)
        self._inbomb.grid(row=5, padx=3, pady=3)
        self._bstart.grid(row=6, padx=3, pady=3, rowspan=2)
        self._lflag.grid(row=9, padx=3, pady=3)
        self._lpyt.grid(row=10, padx=3, pady=3)
        self._lwolne.grid(row=11, padx=3, pady=3)
        self._lstatus.grid(row=12, padx=3, pady=3)
        #panel prawy - tworzony w metodzie ustaw_plansze()
        
    def start(self):
        '''Uruchamia interfejs po zwroceniu referencji do obiektu z konstruktora do klasy Logika.'''
        self._window.mainloop()
        
    #aktualizacja labeli na lewym panelu
    def ustaw_info(self,flagi,pyt,ilewolnych):
        '''Metoda aktualizujaca labele na lewym panelu.'''
        self._lflag.configure(text='pozostalo bomb: {}'.format(flagi))
        self._lpyt.configure(text='ilosc pytajnikow: {}'.format(pyt))
        self._lwolne.configure(text='wolne pola: {}'.format(ilewolnych))
        
    def wczytaj(self,w,k,b):
        '''Metoda walidujaca dane wejsciowe przy rozpoczynaniu gry.'''
        try:
            w = int(float(w))
            k = int(float(k))
            b = int(float(b))
        except Exception:
            messagebox.showinfo(title='Blad!', message="zly format danych")
            return
        try:
            if w < 2:
                raise BladWysokosciException(w)  
            elif w > 15:
                raise BladWysokosciException(w)   
            elif k < 2:
                raise BladSzerokosciException(k)  
            elif k > 15:
                raise BladSzerokosciException(k)    
            elif b <= 0:
                raise BladBombException(w,k,b)  
            elif b >= w*k:
                raise BladBombException(w,k,b)  
        except BladDanychException as e:            
            messagebox.showinfo(title=e.wypisz1(), message=e.wypisz2())
            return
        else:
            if (self._logika.utworz_plansze(w,k,b)):
                self.ustaw_plansze(w,k,b)
    
    def ustaw_plansze(self,w,k,b):
        '''Tworzy siatke przyciskow z akcjami przy PPM i LPM.
        
        Przyjmuje ilosc wierszy, kolumn i bomb tworzonej planszy.'''
        
        #lewy panel
        self.ustaw_info(b-0, 0, w*k-b)
        #czyszczenie planszy z poprzedniej gry
        self._xyzzy = False
        self._kodwpisany = 0
        for widget in self._panelprawy.winfo_children():
            widget.destroy()
        #tworzenie planszy
        self._plansza = [[ Button(self._panelprawy, image=self._i0,
                                  command=lambda i=i,j=j: self._logika.klik(i,j,False),
                                  borderwidth=1, width=26, height=26, compound="center")
                          for j in range(k)] for i in range(w)]
        #metoda Button.grid zwraca none (dokumentacja) - musialem rozdzielic
        for i in range(w):
            for j in range(k):
                self._plansza[i][j].place(x=26*i, y=26*j) #rozmieszczenie
                #akcja na PPM
                self._plansza[i][j].bind('<Button-3>',lambda e,i=i,j=j: self._logika.klik(i,j,True))
        self._lstatus.configure(text='graj, graj')    
    
    def ustaw_pole(self,w,k,cyfra,stan,ileflag,pyt,ilewolnych):
        '''Aktualizuje lewy panel inform. oraz tlo i liczbe w przycisku.'''
        #lewy panel
        self.ustaw_info(ileflag,pyt,ilewolnych)
        #przy LPM - blokujace nastepne kliki
        if stan in [3,4,5,6,10]: 
            self._plansza[w][k].configure(text=cyfra, state=DISABLED, width=23, height=23)
            self._plansza[w][k].unbind('<Button-3>')
        #ustawia odpowiednie tlo przycisku
        self._plansza[w][k].configure(image=self._listatel[stan], width=23, height=23)
        
    def xyzzy(self,klawisz):
        '''Sprawdza, czy została wcisnieta sekwencja znaków do uruchomienia kodu'''
        if hasattr(self, '_xyzzy') == False: #gra jeszcze nierozpoczeta
            return
        if self._xyzzy == False and klawisz == "xyzzy"[self._kodwpisany]:
            self._kodwpisany += 1
            if self._kodwpisany == 5:
                self._logika.prosba_o_kod()
                #kod zostal wpisany, blokada wpisywania do rozpoczenia nastepnej partii
                self._xyzzy = True      
        else: #wcisnieto inny niz wymagany przycisk (z przyciskow bindowanych)
            self._kodwpisany = 0
        
    def wygrana(self):
        '''Wyswietla komunikat o wygranej partii.'''
        self._lstatus.configure(text='WYGRANA :-)')
        del self._xyzzy
        messagebox.showinfo(title='WYGRANA', message='WYGRANA! :-) Dawaj jeszce raz')
        
    def przegrana(self):
        '''Wyswietla komunikat o przegranej partii.'''
        self._lstatus.configure(text='PRZEGRANA :-(')
        del self._xyzzy
        messagebox.showinfo(title='PRZEGRANA', message='PRZEGRANA :-( Dawaj jeszce raz')

    
#uruchamianie programu
if __name__ == "__main__":
    from logika import *
    start = Logika()
    