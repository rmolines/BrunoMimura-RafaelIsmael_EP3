# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:49:13 2015

@author: Rafael
"""

import matplotlib.pyplot as plt
import numpy as np

def Grafico (Y1,Y2,eixoX,eixoY1,eixoY2, datas, x, y):
    index = np.arange(len(Y1))
    
    fig, ax1 = plt.subplots()
    
    plt.bar(index, Y1, 0.35, color='b', label=eixoY1)
    
    plt.bar(index + 0.35, Y2, 0.35, color='r', label=eixoY2)
    
    plt.xlabel(eixoX)
    plt.ylabel(x)
    plt.title(x+y)
    plt.xticks(index + 0.35, (datas))
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def Grafico2 (Y,eixoX, eixoY, datas, x, y):
    index = np.arange(len(Y))
    
    fig, ax1 = plt.subplots()
    
    plt.bar (index+0.35, Y, 0.35, color='b', label=eixoY)

    plt.xlabel(eixoX)
    plt.ylabel(x)
    plt.title(x+y)
    plt.xticks(index+0.53, (datas))
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return None
