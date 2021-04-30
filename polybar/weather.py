#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:25:30 2020

@author: lorenzo
"""


import requests
import urllib
import time
from bs4 import BeautifulSoup

time.sleep(5)

WARNING = '\033[93m'

url = "https://www.meteored.com.ar/tiempo-en_La+Plata-America+Sur-Argentina-Provincia+de+Buenos+Aires-SADL-1-16930.html"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
try:
    a=urllib.request.Request(url,headers = hdr)
    response = urllib.request.urlopen(a).read()
    
    soup = BeautifulSoup(response,"lxml")
    
    data =  soup.find_all(class_ = "dato-temperatura changeUnitT")
    temperature = data[0].text
    
    situation = soup.find_all("span","estado","strong")[0].contents[3].text
    
    
    if situation=="Despejado":icon="🌞"
    elif situation=="Intervalos nubosos":icon="🌥"
    elif (situation=="Cielos nubosos" or "Cielos Nubosos"):icon="🌥"
    elif situation=="Tormentas": icon = "⛈"
    elif (situation=="Lluvia moderada" or situation == "Lluvia débil"): icon ="🌧"
    elif situation=="Cielos Cubiertos": icon = "☁"
    else: icon = "NO ICON, FIX"
    
    
    if icon != "NO ICON, FIX":
        max_temp = soup.find_all(class_ = "maxima changeUnitT")[0].text
        min_temp = soup.find_all(class_ = "minima changeUnitT")[0].text
        print("🥶"+min_temp+" 🥵" + max_temp + "(" + icon + temperature+")")
    else: print(icon)
except:
    print("🥶 Nan "+" 🥵 Nan " + "( Nan )")
