from tkinter import*
import os
import time

from numpy import insert
class gracz():
    def __init__(self) -> None:
        super().__init__()
        self.hp =5
        self.coins = 5
        self.equipment = []
        self.int=0
        self.sila=0
        self.pp=0
        self.suma=5
        self.punk=0

    def stat(self):
        print('*'*200 )
        print( f'\ncoins = {self.coins}\nhp = {self.hp}\nint = {self.int}\nping pong = {self.pp}\nsila = {self.sila}\n')

    def inv(self):
        print('*'*200 )
        print(f'\ninventory = {self.equipment}\n')

    def punkty(self):
        print('*'*200 )
        print( "Rozdziel swoje punkty\ndysponujesz 5 punktami\nINT\tPING PONG\tSIŁA\nPodaj punkty do inteligencji" )
        x=int(input())
        self.suma-=x
        if self.suma>=0:
            self.int+=x
        elif self.suma<0:
                print("ZŁA ILOŚĆ\nDODANO MOŻLIWĄ ILOŚĆ")
                self.int+=(self.suma*-1)
        else:
            self.int+=x
        if self.suma>=0:
            print( "Podaj punkty do PING PONG" )
            x=int(input())
            if self.suma<0:
                    print("ZŁA ILOŚĆ\nDODANO MOŻLIWĄ ILOŚĆ")
                    self.pp+=(self.suma*-1)
            else:
                self.pp+=x
            self.suma-=x
            if self.suma>=0:
                print("Podaj punkty do SIŁY" )
                x=int(input())
                if self.suma<0:
                    print("ZŁA ILOŚĆ\nDODANO MOŻLIWĄ ILOŚĆ")
                    self.sila+=(self.suma*-1)
                else:
                    self.sila+=self.suma
    
            


        



   