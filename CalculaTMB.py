# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:30:36 2015

@author: Rafael
"""

import doctest

def CalculaTMB (peso, altura, idade, atividade, sexo):
    
    """
    Calcular a qtd de calorias diarias
    >>> CalculaTMB(77, 1.82, 17, 'MINIMO', 'M')
    2276.2319999999995
    """
    
    grau = {'MÍNIMO': 1.2, 'BAIXO': 1.375, 'MÉDIO': 1.55, 'ALTO': 1.725, 'MUITO ATIVO': 1.9}
    
    TMB = (88.36+(13.4*peso)+(4.8*altura*100)-(5.7*idade))*grau[atividade]

    TMBM = (447.6+(9.2*peso)+(3.1*altura*100)-(4.3*idade))*grau[atividade]
    
    if sexo == 'M':
        return TMB
    else:
        return TMBM
        
if __name__=="__main__":
    doctest.testmod(verbose="True")
