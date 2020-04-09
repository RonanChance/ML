# -*- coding: utf-8 -*-
import urllib.request as request
import calendar as cal
from matplotlib import pyplot as plt
import csv
import sys

# =============================================================================
# URL = 'https://bitcoincharts.com/charts/chart.png?width=940&m=bitstampUSD&SubmitButton=Draw&r=1&i=2-hour&c=1&s=2020-04-08&e=2020-04-09&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=0&cv=0&ps=0&l=0&p=0&'
# 
# request.urlretrieve(URL, "Green\local-filename.png")
# 
# 
# =============================================================================


with open('BTC-Daily.csv','rt') as file:
    reader = csv.reader(file)
    rows = [r for r in reader]
    rows = rows[::-1]

z = 0
for line in rows:
    try:
        day = rows[z][0][8:10]
        year = rows[z][0][0:10]
        month = rows[z][0][5:7]
        
        dayopen = float(rows[z][2][0:8])
        tmrwclose = float(rows[z+1][5][0:8])
        
        if (tmrwclose - dayopen) > 0:
            print('GREEN', str(dayopen), str(tmrwclose))
        else:
            print("RED", str(dayopen), str(tmrwclose))
        z += 1
    
    except ValueError:
        print('Finished!')
        sys.exit()