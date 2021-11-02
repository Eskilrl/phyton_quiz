#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:59:43 2021

@author: eskilruud-larsen
"""


di = {1:0,2:0}

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

if __name__ == "__main__":
        
        S = Read_file()
        t1 = 0
        t2 = 0
        for l in S:
            print(l)
            
            in1 = int(input("spiller 1:"))
            print(" ")
            in2 = int(input("spiller 2:"))
            print(" ")
            if l.sjekk_svar(in1):
                t1+=1
                print("spiller 1 riktig")
            else: 
                print("spiller 1 feil")
            print(" ")
                
            if l.sjekk_svar(in2):
                t2+=1
                print("spiller 2 riktig")
            else: 
                print("spiller 2 feil")
            print(" ")
                
            print(l.korrekt_svar())
            print("---------------- ")
            print(" ")
        
        print("spiller 1 har",t1,"poeng")
        print(" ")
        print("spiller 2 har",t2,"poeng")






   
         