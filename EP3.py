# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:37 2015

@author: Rafael
"""

from Grafico import Grafico, Grafico2
from CalculaTMB import CalculaTMB


alimentos = open ("alimentos.csv", encoding = "latin-1")

tabela = {}

for i in alimentos.readlines():
    x = i.strip ().split (",")
    tabela [x[0]] = x[1:]   

usuario = open ("usuario.csv", encoding = "latin-1")

u = usuario.readlines ()

info = u [1].split (",")

nome = info [0]
idade = int(info [1])
peso = float(info [2])
sexo = info [3]
altura = float(info [4])
atividade = info [5].upper ().strip ()

alimentacao = u [3:]

dias = {}

for i in alimentacao:
    
    dia = i.split (",")[0]
    comida = i.split (",")[1]
    qtd = int(i.split (",")[2])
    
    if dia not in dias:
        dias[dia] = {}
    else:
        if comida in dias[dia]:
            dias[dia][comida] += qtd
        else:
            dias [dia][comida] = qtd
            
           
def CalculaNutriente (nutriente, p):

    n = tabela['Alimento'].index (p)
    x = 0
    for i in sorted(dias):
        for a in dias[i]:
            nutriente[x] += (dias[i][a]*float(tabela[a][n])/float(tabela[a][0]))
        x += 1
    
    
calorias = [0]*len(list(dias))
CalculaNutriente (calorias, 'Calorias (kcal)') 

proteinas = [0]*len(list(dias))
CalculaNutriente (proteinas, 'Prote\x92nas (g)')

carbs = [0]*len(list(dias))
CalculaNutriente (carbs, 'Carboidratos (g)')

fat = [0]*len(list(dias))
CalculaNutriente (fat, 'Gorduras (g)')       
        

TMB = [CalculaTMB (peso, altura, idade, atividade, sexo)]*len(dias)

    
datas = [d for d in sorted(dias)]


IMC = 1.3*peso/altura**2.5

txt = open ('IMC.txt', 'w')
txt.write ('Seu Índice de Massa Corporal é %i.\n' %IMC)
if IMC < 17:
    d = 'muito abaixo do peso ideal.'
elif IMC < 18:
    d = 'abaixo do peso ideal'
elif IMC < 25:
    d = 'no peso ideal'
elif IMC < 30:
    d = 'acima do peso ideal'
elif IMC < 35:
    d = 'com obesidade I'
elif IMC < 40:
    d = 'com obesidade II (severa)'
else:
    d = 'com obesidade III  (mórbida)'
txt.write ('Você está ')
txt.write (d)
txt.write ('.\n')
z = 0

for i in sorted (dias):
    txt.write ('No dia ')
    txt.write (i)
    txt.write (' você comeu ')
    if calorias[z]-TMB[0] < 0:
        w = TMB[0]-calorias[z]
        txt.write ('%d a menos do que o ideal.\n' %w)
    else:
        w = calorias[z]-TMB[0]
        txt.write ('%d a mais do que o ideal.\n' %w)
    z+=1

txt.close ()


Grafico (calorias, TMB, 'Dias', 'Calorias Consumidas', 'Calorias Recomendadas', datas)

Grafico2 (proteinas, 'Dias', 'Proteinas Consumidas', datas, 'Proteinas', ' Diarias')

Grafico2 (carbs, 'Dias', 'Carboidratos Consumidos', datas, 'Carboidratos', ' Diarias')

Grafico2 (fat, 'Dias', 'Gorduras Consumidas', datas, 'Gorduras', ' Diarias')
