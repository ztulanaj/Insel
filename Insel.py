# -*- coding: utf-8 -*-

#Dieses Programm von Jana Lutz und Aaltje Mazur beschreibt das SIR-Modell auf unserer Insel mit 400 Einwohnerinnen
#S=susceptible=gesunde
#I=infectious=kranke
#R=resistant=resistente

#berechnet S'
def gesundenänderung(b,gesunde[i],kranke[i]):
    differenzgesunde = -b*gesunde*kranke
    return differenzgesunde

#berechnet R'
def resistentenänderung(g,kranke):
    differenzresistente = g*kranke
    return differenzresistente

#berechnet I'
def krankenänderung(differenzgesunde,differenzresistente):
    differenzkranke = -differenzgesunde-differenzresistente
    return differenzkranke

#Zahlen aus der Beispielaufgabe, Anfangswerte
#S(0) = gesunde
population = 400
gesunde=[]
kranke=[]
resistente=[]
#kranke[0]=anfangskranke
kranke[0] = 1
gesunde[0] = population - kranke[0]
resistente[0] = 0

#Woche 1
kranke[1] = 3
gesunde[1] = population - kranke[1]

#Woche 2
kranke[2] = 10
gesunde[2] = population - kranke[2]

#Woche 3
kranke[3] = 30
gesunde[3] = population - kranke[3]

#Woche 4
kranke[4] = 65
gesunde[4] = population - kranke[4]

#Woche 5
kranke[5] = 93
gesunde[5] = population - kranke[5]