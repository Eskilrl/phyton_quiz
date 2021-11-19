#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:59:43 2021

@author: eskilruud-larsen
"""


class Fler:

    
    def __init__(self, SS, SA, RS):
        self.SS = SS
        self.SA = SA
        self.RS = RS
        
        
    def __str__(self):
        return f"{self.SS}\n{self.SA}\n" 
        
        
    def svar(self): 
        return "\n".join([f"{value} {index}" for value,index in enumerate(self.SA, 1)])

        

     
    def sjekk_svar(self, brukerinput):
        if brukerinput == self.RS:
            return True
        else:
            return False
        
        
    def korrekt_svar(self):
        return f"korrekt svar: {self.SA[self.RS]}"
     
    
def Read_file():
    
    Spørsmål_liste = []
    with open('sporsmaalsfil.txt','r') as f:
   
        for line in f:
            linje = line.split(":", 3)
            ST = int(linje[1])
            TL = linje[2].replace('[',' ').replace(']',' ').replace(',',' ').split()
            Spørsmål_liste.append(Fler(linje[0],TL,ST))
        return Spørsmål_liste 

class Player:
    
    def __init__(self,navn,poengsum = 0):
        self.navn = navn
        self.poengsum = poengsum
    
def spillere(antall):
    SP = []
    for i in range(antall):
        
        SP.append(Player(str(input("hva er spillerens navn?"))))
    return SP

if __name__ == "__main__":
        LSP = spillere(int(input("hvor mange spillere er det:")))
    
        S = Read_file()
        
        for l in S:
            print(l)
            print(" ")
            L = []
            for P in LSP:
                ti = int(input(f"velg et svar til spiller {P.navn}"))
                if l.sjekk_svar(ti):
                    P.poengsum +=1
            print(" ")
            print(l.korrekt_svar())
            print(" ")
        score = []
        for spiller in LSP:
            print(f"spiller {spiller.navn} har {spiller.poengsum} poeng")
            print(" ")
            score.append(spiller.poengsum)
        print(f"vinneren er {LSP[score.index(max(score))].navn}")
        
                
      
            




   
         