# -*- coding: utf-8 -*-
import urllib.request as request
import calendar as cal
from matplotlib import pyplot as plt
import csv
import sys
import time
import random

with open('BTC-Daily.csv','rt') as file:
    reader = csv.reader(file)
    rows = [r for r in reader]
    rows = rows[::-1]

z = 0
for line in rows:
    try:
        date = str(rows[z][0][0:10])
        dayopen = float(rows[z][2][0:8])
        
        tmrwdate = str(rows[z+1][0][0:10])
        tmrwclose = float(rows[z+1][5][0:8])
        tmrwopen = float(rows[z+1][2][0:8])
        
        URL = 'https://bitcoincharts.com/charts/chart.png?width=940&m=bitstampUSD&SubmitButton=Draw&r=1&i=2-hour&c=1&s=' + date + '&e=' + date + '&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=0&cv=0&ps=0&l=0&p=0&'
        
        if (tmrwclose - tmrwopen) > 0:
            print('GREEN', str(tmrwopen), str(tmrwclose))
            filename = 'Green\\' + date + ".png"
            request.urlretrieve(URL, filename)
        else:
            print("RED", str(tmrwopen), str(tmrwclose))
            filename = 'Red\\' + date + ".png"
            request.urlretrieve(URL, filename)
        z += 1
        time.sleep(random.randint(0, 2))
    
    except ValueError:
        print('Finished!')
        sys.exit()