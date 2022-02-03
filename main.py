import requests
import json
import sys, os

APP_VERSION = "1.0.0"
AUTHOR = "Agung Moekti Wibowo"
REPO = "https://github.com/AgungMoekti/crypto-price.git"

cyan="\033[1;36m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"

try:
    coin = sys.argv[1]
except:
    print(f"{red}Error. Mising 1 argument")
    exit()

api_indodax = requests.get('https://indodax.com/api/tickers')
raw = api_indodax.json()
if(coin == "-v"):
    print(f"{cyan}App Version",APP_VERSION)
    print(f"{cyan}Creator",AUTHOR)
    print(f"{cyan}Github Repository",REPO)
    
else:
    try:
        if(sys.argv[2] == "-u"):
            try:
                harga = raw['tickers'][sys.argv[1]+'_usdt']['buy']
                vol = raw['tickers'][sys.argv[1]+'_usdt']['vol_usdt']
                print(f'{yellow}\r{chr(62)} Current Price {sys.argv[1]} : {green}${int(harga):,}')
                print(f'{yellow}\r{chr(62)} Current Volume : {green}${float(vol):,}')
            except Exception as e:
                print(f"{red}\r{chr(62)} Error. No such coin name or pair {e}")
                
        else:
            print(f"{red}Invalid argument value")


    except:
        try:
                harga = raw['tickers'][sys.argv[1]+'_idr']['buy']
                vol = raw['tickers'][sys.argv[1]+'_idr']['vol_idr']
                print(f'{yellow}\r{chr(62)} Current Price {sys.argv[1]} : {green}Rp{int(harga):,}')
                print(f'{yellow}\r{chr(62)} Current Volume : {green}Rp{int(vol):,}')
        except Exception as e:
                print(f"{red}\r{chr(62)} Error. No such coin name or pair {e}")