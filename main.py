
from gracz import gracz
from tkinter import *
from lore import lore
from kopalnia import kopalnia

kopalnia=kopalnia()
gracz = gracz()
lore = lore()

first=True
zero=False
onne=False



if first:
    gracz.punkty()
    gracz.stat()
    first=False
    zero=True
if zero:
    lore.zero()
    zero=False
    onne=True
if onne:
    lore.one(gracz)
    onne=False
if lore.drugi_akt:
    onne=False
    lore.game=False
    lore.two(gracz)
while lore.trzeci_atk:
    lore.drugi_akt=False
    lore.three(gracz)
    if lore.kop:
        kopalnia.loop(gracz)
        lore.kop=False
while lore.fina:
    lore.final(gracz)    
    if lore.pong_L:
        import pongD
        pongD()
        lore.ff=False
    if lore.pong_W:
        import pong
        pong()
        lore.ff=False