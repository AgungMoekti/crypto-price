import requests
import json
import sys, os

def price(coin):
    try:
            api_indodax = requests.get('https://indodax.com/api/tickers')
            raw = api_indodax.json()
            harga = raw['tickers'][coin+'_idr']['buy']
            vol = raw['tickers'][coin+'_idr']['vol_idr']      
            print(f'\r{chr(62)}Harga {coin} Saat Ini : Rp{int(harga):,}')
            print(f'\r{chr(62)}Volume Market : Rp{int(vol):,}')
    except:   
            print("No such coin name " + coin)
price(coin=str(input('Masukan Kode Coin : '))) 