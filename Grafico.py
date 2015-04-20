# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:49:13 2015

@author: Rafael
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def Grafico (X,Y1,Y2,eixoX,eixoY1,eixoY2):
    
    fig, ax1 = plt.subplots()
    ax1.plot(X, Y1, 'b' + '-')
    ax1.set_xlabel(eixoX)
    ax1.set_ylabel(eixoY1, color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
        
    ax2 = ax1.twinx()
    ax2.plot(X, Y2, 'r' + '-')
    ax2.set_ylabel(eixoY2, color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    plt.show() 
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()
    
    return None
