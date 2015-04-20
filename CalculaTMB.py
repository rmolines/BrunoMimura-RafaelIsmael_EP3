# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:30:36 2015

@author: Rafael
"""

def CalculaTMB (peso, altura, idade, atividade, sexo):
    
    grau = {'MINIMO': 1.2, 'BAIXO': 1.375, 'MEDIO': 1.55, 'ALTO': 1.725, 'MUITO ALTO': 1.9}
    
    TMB = (88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade))*grau[atividade]

    TMBM = (447.6+(9.2*peso)+(3.1*altura*100)-(4.3*idade))*grau[atividade]
    
    if sexo == 'M':
        return TMB
    else:
        return TMBM