# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:37 2015

@author: Rafael
"""

""
alimentos = open ("alimentos.csv", encoding = "latin1")

tabela = alimentos.readlines()


usuario = open ("usuario.csv", encoding = "utf-8")

u = usuario.readlines ()

info = u [1].split (",")

nome = info [0]
idade = info [1]
peso = info [2]
sexo = info [3]
altura = info [4]
metabolismo = info [5]

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
        
        
        

print (dias)