# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:38:11 2020

@author: Kuba
"""



from tkinter import *



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
        self._panellewy = Frame(self._window, bg='red', width=160, height=400, padx=3, pady=3)
        self._panelprawy = Frame(self._window, bg='blue', width=400, height=400, padx=3, pady=3)
        
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
        
            #self._lczas = Label(self._panellewy, text='czas [s]: ')
        self._lflag = Label(self._panellewy, text='pozostalo bomb:')
        self._lpyt = Label(self._panellewy, text='ilosc pytajnikow:')
        self._lwolne = Label(self._panellewy, text='wolne pola:')
        
        
        # ukladanie elementow w lewym panelu
        #model_label.grid(row=0, columnspan=3)
        self._lszer.grid(row=0, padx=3, pady=3)
        self._inszer.grid(row=1, padx=3, pady=3)
        self._lwys.grid(row=2, padx=3, pady=3)
        self._inwys.grid(row=3, padx=3, pady=3)
        self._lbomb.grid(row=4, padx=3, pady=3)
        self._inbomb.grid(row=5, padx=3, pady=3)
        self._bstart.grid(row=6, padx=3, pady=3, rowspan=2)
            #self._lczas.grid(row=8, padx=3, pady=3)
        self._lflag.grid(row=9, padx=3, pady=3)
        self._lpyt.grid(row=10, padx=3, pady=3)
        self._lwolne.grid(row=11, padx=3, pady=3)
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
        
        #zrobic wyjatki
        w = int(float(w))
        k = int(float(k))
        b = int(float(b))
        #sprawdzac dane wejsciowe
        #wyjatki
        #jesli zle - wyswietlic okienko dialogowe / wyjatki
        #a jesli dobrze to wykonac self._logika.utworzplansze
        if int(float(self._inszer.get())) == 0:
            return
        
        self._logika.utworzplansze(w,k,b)
        #self.ustawplansze(w, k, b)
        
        
    
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
        #print(self._plansza)
    # print(pb.pole_klik(i,j))
    
    
    
    def ustawpole(self,w,k,cyfra,stan,ileflag,pyt,ilewolnych):
        #if stan<4 and self._xyzzy:
        #    l = stan + 7
        #else: l = stan
        self.ustawinfo(ileflag,pyt,ilewolnych)
        if stan==4:
            self._plansza[w][k].configure(text=cyfra, state=DISABLED, width=23, height=23)
            self._plansza[w][k].unbind('<Button-3>')
        self._plansza[w][k].configure(image=self._listatel[stan], width=23, height=23)
'''        
    def xyzzy(self,klawisz):
        if klawisz == "xyzzy"[self._kodwpisany]:
            self._kodwpisany += 1
            if self._kodwpisany == 5:
                #self._xyzzy = True
                if self._logika.prosbaOKod():
                    self._xyzzy = True
                #wywolac prosbe o pozycje pol z minami do przyciemnienia
        
'''   
'''
    def sprawdz(self,w,k):
        self._plansza[w][k].invoke()
        
    
    def wygrana(self,plansza):
        pass
    
    def przegrana(self,plansza):
        pass
    
    #przyjmuje gotowa liste pktow do wyszarzenia
    def xyzzy(self,lista):
        self._xyzzy = False
        for i in lista:
            #odswiez tlo
            pass
    '''   
if __name__ == "__main__":
    from logika import *
    start = logika()
    