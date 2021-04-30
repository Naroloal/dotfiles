#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:02:57 2020

@author: lorenzo
"""


import sys
import requests
from bs4 import BeautifulSoup
import re
import urllib

try:
    json = requests.get("https://www.bullmarketbrokers.com/Information/StockPrice/GetIndexes?_ts=1607106749711").json()["merval"]
    price = json["stockState"]["price"]
    data = urllib.request.urlopen("https://www.dolarhoy.com/").read()
#data = requests.get("https://www.dolarhoy.com/")
    soup = BeautifulSoup(data,features="lxml")

    #a = soup.find_all("class":"pill pill-coti"})
    #ccl = float(a[3].find_all_="price")[1].text.split()[1].replace(",","."))

    aa = soup.find_all(attrs={"href":"/cotizaciondolarcontadoconliqui"})
    ccl = float(aa[1].findAll(class_="compra")[0].text)

    bb = soup.find_all(attrs= {"href":"/cotizaciondolarblue"})
    blue = float(bb[2].findAll(class_="compra")[0].text)

    with open("merval_ccl","w") as f:
        f.write(str(round(price/ccl,2)) + " " + str(round(ccl,2)) + " " + str(round(blue,2)))
        print("📈Merv:"+str(round(price/ccl,2)) + " " +"💵CCL:$"+ str(round(ccl,2))+ " Blue:"+str(blue))
        
except:
    with open("merval_ccl","r") as f:
        aux = f.readline()
        aux = aux.split()
        print("📈Merv:"+aux[0] + " " +"💵CCL:$"+aux[1]+ " Blue:"+str(aux[2]))


