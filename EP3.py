# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:37 2015

@author: Rafael
"""

from Grafico import Grafico
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

calorias = {}

for i in sorted(dias):
    calorias[i] = 0
    for a in dias[i]:
        calorias[i] += dias[i][a]*float(tabela[a][1])/float(tabela[a][0])

TMB = [CalculaTMB (peso, altura, idade, atividade, sexo)]*len(list(dias))

c = []

for i in calorias:
    c.append (calorias[i])
    
      

print (len (dias))       
