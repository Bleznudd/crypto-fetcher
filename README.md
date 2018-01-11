# crypto-fetcher
A simple tool designed to retrive prices and volumes of the most popular cryptocurrencies

## Description
This tool simply let's you download the latest prices of the most popular cryptocurrencyes at different time intervals.
Once that the program is started it will fetch the prices and the volumes of the currency you asked for, and put the data into a .json file

For a list of all the avaiable currencyes, please click [here](https://www.cryptocompare.com/api/data/coinlist/)

## Installation
Start by cloning this repository on your PC, open a terminal and
```
git clone https://github.com/Bleznudd/crypto-fetcher.git
```

Once that the download has finished cd into the directory
```
cd crypto-fetcher
```

And run the Makefile with the command
```
make
```

You will find and executable file in the directory, called **crypto-fetcher**, start the game with
```
./crypto-fetcher
```

### Note for Windows users
Due to the lack of support for makefiles in Windows, you will need [GnuWin](http://gnuwin32.sourceforge.net/) or [Cygwin](http://www.cygwin.com/) to properly run the `make` command.
Once that you have succefully generated the binaries, you may need to rename `crypto-fetcher` in `crypto-fecther.exe` before executing the program.
Anyway, I'm not interested in making this program compatible with Windows, if it doesn't work, is none of my business.

## Manteinance
This is a program made for personal purposes only, so it will not be manteined if I'm not interested in it anymore.
Don't expect update and/or bugfix.

