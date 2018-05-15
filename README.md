# crypto-fetcher
A simple tool designed to retrive prices and volumes of the most popular cryptocurrencies

## Description
Thanks to [CryptoCompare APIs](https://min-api.cryptocompare.com/) this tool simply let's you download the latest prices of the most popular cryptocurrencies at different time intervals and (eventually) visualize them on a candelstick graph.
Once that the program is started it will fetch the prices and the volumes of the currency you asked for, and put the data into a .json file

For a list of all the avaiable currencies, please check the [coin list](https://www.cryptocompare.com/api/data/coinlist/)

## Installation
A packed version of this program can be found in the [release section](https://github.com/Bleznudd/crypto-fetcher/releases/tag/v0.1),  download the `.tar.gz` file and install it using pip
```
sudo python pip install crypto-fetcher-0.1.tar.gz
```
Otherwise you can just clone this repository with
```
git clone https://github.com/Bleznudd/crypto-fetcher.git
```
navigate through the folders and once you've found `crypto-fetcher.py` start it with
```
python ./crypto-fetcher.py -h
```

## C++ version

An old and incomplete C++ version of this program can be found in the `old` directory

## Manteinance
This is a program made for personal purposes only, so it will not be manteined if I'm not interested in it anymore.
Don't expect update and/or bugfix.
