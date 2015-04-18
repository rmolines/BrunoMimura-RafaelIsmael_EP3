# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:37 2015

@author: Rafael
"""

""
from datetime import *
d3 = datetime.strptime('13/02/2015', '%d/%m/%Y')

alimentos = open ("alimentos.csv", encoding = "latin-1")

tabela = {}


for i in alimentos.readlines():
    x = i.strip ().split (",")
    tabela [x[0]] = x[1:]    

usuario = open ("usuario.csv", encoding = "latin-1")

u = usuario.readlines ()

info = u [1].split (",")

nome = info [0]
idade = info [1]
peso = info [2]
sexo = info [3]
altura = info [4]
atividade = info [5]

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

calorias = []

for i in dias:
    calorias.append  (datetime.strptime(i, "%d/%m/%y"))
    

print (sorted (calorias))
