# -*- coding: utf-8 -*-
import urllib.request as request
import calendar as cal
from matplotlib import pyplot as plt
import csv

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

z = 0
for line in rows:
    print(rows[z][0][0:10])
    z += 1
    if z >= 7:
        break