# Crypto Price

## Dependencies
- curl
- python3
- jq

## Installation 
### Linux Ubuntu/Debian
```
git clone https://github.com/AgungMoekti/crypto-price.git
sudo cp price /usr/local/bin/price
sudo chmod +x /usr/local/bin/price
```
### Android/Termux
- first install all dependencies (skip this if you already installing)
```
pkg update
pkg install python3
pkg install jq
pkg install git
pkg install curl
```
- setup
```
git clone https://github.com/AgungMoekti/crypto-price.git
cd crypto-price
cp $PREFIX/usr/bin/price
chmod +x $PREFIX/usr/bin/price
```

### Windows
- idk lol

## Usage
```
price btc
```