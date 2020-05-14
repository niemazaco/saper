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
        
        #tla przyciskow
        self._i0 = PhotoImage(file="pusty.png")
        self._i1 = PhotoImage(file="flaga.png")
        self._i2 = PhotoImage(file="pytajnik.png")
        self._ibomb = PhotoImage(file="bomba.png")
        self._iwybuch = PhotoImage(file="wybuch.png")
        self._xyzzy0 = PhotoImage(file="xyzzy0.png")
        self._xyzzy1 = PhotoImage(file="xyzzy1.png")
        self._xyzzy2 = PhotoImage(file="xyzzy2.png")
        self._xyzzybomba = PhotoImage(file="xyzzybomba.png")
                
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
                            self.ustawplansze(int(float(self._inszer.get())),
                                              int(float(self._inwys.get()))))
        # print(pb.pole_klik(w,k)
        self._lczas = Label(self._panellewy, text='czas [s]: ')
        # ukladanie elementow w lewym panelu
        #model_label.grid(row=0, columnspan=3)
        self._lszer.grid(row=0, padx=3, pady=3)
        self._inszer.grid(row=1, padx=3, pady=3)
        self._lwys.grid(row=2, padx=3, pady=3)
        self._inwys.grid(row=3, padx=3, pady=3)
        self._lbomb.grid(row=4, padx=3, pady=3)
        self._inbomb.grid(row=5, padx=3, pady=3)
        self._bstart.grid(row=6, padx=3, pady=3)
        self._lczas.grid(row=7, padx=3, pady=3)
        #panel prawy
        '''for x in range(15): 
            self._panelprawy.columnconfigure(x, weight=1)
            self._panelprawy.rowconfigure(x, weight=1)'''
        
        self._window.mainloop()
        
    def ustawplansze(self,w,k):
        #czysci plansze
        self._xyzzy = False
        for widget in self._panelprawy.winfo_children():
            widget.destroy()
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
                                  command=lambda i=i,j=j: print(i,j),
                                  borderwidth=1, width=26, height=26)
                          for j in range(k)] for i in range(w)]
        #metoda Button.grid zwraca none (dokumentacja) - musialem rozdzielic
        for i in range(w):
            for j in range(k):
                #self._plansza[i][j].grid(row=i,column=j, sticky='news')
                self._plansza[i][j].place(x=26*i, y=26*j)
        #print(self._plansza)
    # print(pb.pole_klik(i,j))
    
    def sprawdz(self,w,k):
        self._plansza[w][k].invoke()
        
    #lambda z wciskaniem przyciskow dla logiki?
    
    #przyjmuje gotowa liste pktow do wyszarzenia
    def xyzzy(self,lista):
        self._xyzzy = False
        for i in lista:
            #odswiez tlo
            pass
        
    