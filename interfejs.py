from tkinter import *

class BladDanychException(Exception):
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
        



class interfejs():
    def __init__(self,logika):
        self._logika = logika 
        self._window=Tk()
        self._window.title("Saper Jakub Medalion")
        self._window.geometry("570x400")
        
        #bindowanie klawiszy do kody xyzzy:
        self._window.bind("x", lambda e:self.xyzzy('x'))
        self._window.bind("y", lambda e:self.xyzzy('y'))
        self._window.bind("z", lambda e:self.xyzzy('z'))
        self._window.bind("X", lambda e:self.xyzzy('x'))
        self._window.bind("Y", lambda e:self.xyzzy('y'))
        self._window.bind("X", lambda e:self.xyzzy('z'))
        self._kodwpisany = 0
        
        #tla przyciskow
        #(0- puste, 1- flaga, 2 - pytajnik, 3 - klikniete)
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
        #xyzzy3 == _i3
        self._xyzzybomba = PhotoImage(file="xyzzybomba.png")
        #xyzzy wybuch - nie wystapi
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

        # print(pb.pole_klik(w,k)
        
        self._lflag = Label(self._panellewy, text='pozostalo bomb:')
        self._lpyt = Label(self._panellewy, text='ilosc pytajnikow:')
        self._lwolne = Label(self._panellewy, text='wolne pola:')
        self._lstatus = Label(self._panellewy, text='WPISUJ I ZACZYNAJ :-)')
        
        
        # ukladanie elementow w lewym panelu
        #model_label.grid(row=0, columnspan=3)
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
        #panel prawy
        '''for x in range(15): 
            self._panelprawy.columnconfigure(x, weight=1)
            self._panelprawy.rowconfigure(x, weight=1)'''
        
    def start(self):
        self._window.mainloop()
        
    #aktualizacja labeli na lewym panelu
    def ustawinfo(self,flagi,pyt,ilewolnych):
            #print(bomby,flagi,pyt,ilewolnych)
        self._lflag.configure(text='pozostalo bomb: {}'.format(flagi))
        self._lpyt.configure(text='ilosc pytajnikow: {}'.format(pyt))
        self._lwolne.configure(text='wolne pola: {}'.format(ilewolnych))
            #self._panellewy.update_idletasks()
        
    def wczytaj(self,w,k,b):
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
            self._logika.utworzplansze(w,k,b)
    
    def ustawplansze(self,w,k,b):
        #lewy panel
        self.ustawinfo(b-0, 0, w*k-b)
        #czysci plansze z poprzedniej gry
        self._xyzzy = False
        for widget in self._panelprawy.winfo_children():
            widget.destroy()
        
    
        #tworzy plansze
        '''if self._plansza:
            print(self._plansza[0][0])
            for i in range(self._pop_w):
                for j in range (self._pop_k):
                    self._plansza[i][j].destroy()
        self._pop_k = k
        self._pop_w = w    '''
        '''self._plansza = [[ Button(self._panelprawy,
                                  command=lambda i=i,j=j: print(i,j),borderwidth=1)
                          .grid(row=i,column=j, sticky='news') for j in range(k)] for i in range(w)]'''
    
        
        self._plansza = [[ Button(self._panelprawy, image=self._i0,
                                  command=lambda i=i,j=j: self._logika.klik(i,j,False),
                                  borderwidth=1, width=26, height=26, compound="center")
                          for j in range(k)] for i in range(w)]
        #metoda Button.grid zwraca none (dokumentacja) - musialem rozdzielic
        for i in range(w):
            for j in range(k):
                #self._plansza[i][j].grid(row=i,column=j, sticky='news')
                self._plansza[i][j].place(x=26*i, y=26*j)
                #self._plansza[i][j].geometry('26x26')
                #akcja na PPM
                self._plansza[i][j].bind('<Button-3>',lambda e,i=i,j=j: self._logika.klik(i,j,True))
        
        self._lstatus.configure(text='graj, graj')
        #print(self._plansza)
    # print(pb.pole_klik(i,j))
    
    
    
    def ustawpole(self,w,k,cyfra,stan,ileflag,pyt,ilewolnych):
        self.ustawinfo(ileflag,pyt,ilewolnych)
        if stan in [3,4,5,6,10]: #inne LPM - blokujace nastepne kliki
            self._plansza[w][k].configure(text=cyfra, state=DISABLED, width=23, height=23)
            self._plansza[w][k].unbind('<Button-3>')
        self._plansza[w][k].configure(image=self._listatel[stan], width=23, height=23)
        
    def xyzzy(self,klawisz):
        if self._xyzzy == False and klawisz == "xyzzy"[self._kodwpisany]:
            self._kodwpisany += 1
            if self._kodwpisany == 5:
                self._kodwpisany = 0
                self._logika.prosbaOKod()
                self._xyzzy = True
        
    def wygrana(self):
        self._lstatus.configure(text='WYGRANA :-)')
        messagebox.showinfo(title='WYGRANA', message='WYGRANA! :-) Dawaj jeszce raz')
        
    def przegrana(self):
        self._lstatus.configure(text='PRZEGRANA :-(')
        messagebox.showinfo(title='PRZEGRANA', message='PRZEGRANA :-( Dawaj jeszce raz')

    


if __name__ == "__main__":
    from logika import *
    start = Logika()
    