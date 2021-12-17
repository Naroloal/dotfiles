#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:49:37 2021

@author: thungur
"""

import configparser
import sys
import requests
from decimal import Decimal
from os.path import expanduser

config = configparser.ConfigParser()

# File must be opened with utf-8 explicitly
with open(expanduser('~/.config/polybar/crypto-config'), 'r', encoding='utf-8') as f:
	config.read_file(f)

# Everything except the general section
currencies = [x for x in config.sections() if x != 'general']
base_currency = config['general']['base_currency']
params = {'convert': base_currency}


with open("crypto.csv","w") as f:
    for currency in currencies:
        icon = config[currency]['icon']
        json = requests.get(f'https://api.coingecko.com/api/v3/coins/{currency}',
    					 	).json()["market_data"]
        price = round(Decimal(json["current_price"][f'{base_currency.lower()}']), 2)
        change_24 = round(float(json['price_change_percentage_24h']),2)
    
        f.write("{},{},{:,.2f}\n".format(config[currency]['name'],price,change_24))