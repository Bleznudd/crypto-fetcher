import os
import requests as rq
import pandas as pd
import json
from sys import argv
from bokeh.plotting import figure, show, output_file

#----------------------------------------------------------- NOTA: CRYPTOCOMPARE APIs -----------------------------------------------------------
# tryConversion	If set to false, it will try to get only direct trading values
# fsym 			REQUIRED The cryptocurrency symbol of interest [Max character length: 10]
# tsym 			REQUIRED The currency symbol to convert into [Max character length: 10]
# e 				The exchange to obtain data from (our aggregated average - CCCAGG - by default) [Max character length: 30]
# aggregate 		Time period to aggregate the data over (for daily it's days, for hourly it's hours and for minute histo it's minutes)
# limit 			The number of data points to return
# allData 		Returns all data (only available on histo day)
# toTs 			Last unix timestamp to return data for
# extraParams 		The name of your application (we recommend you send it) [Max character length: 50]
# sign 			If set to true, the server will sign the requests (be default we don't sign them), this is useful for usage in smart contracts
#
# for more infos: https://min-api.cryptocompare.com/ 
#-------------------------------------------------------------------------------------------------------------------------------------------------

try:
	if len(argv) != 6:
		if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help'):
		    print("This programs aims to retrive prices and volumes of the most popular\n"+
				  "cryptocurrencies, this is done by using https://www.cryptocompare.com/\n"+
				  "APIs and saving the data on a json file. To achive this, you must call\n"+
			      "the program, and passing it the crypto you want the data of, the time\n"+
				  "interval you're interested in (m for minutes, h for hours, d for days),\n"+
		          "the aggragation period, and the number of points\n"+
				  "(use 'all' instead of a number, if you want all the avaiable data)\n \n" +
		          "example --> python ./crypto-fetcher.py BTC EUR m 10 100\n \n" +
		          "This way you will obtain a list of the lasts 100 bitcoin/euros prices\n"+
				  "updated every 10 minute. To get the full coin list, please visit:\n"+
				  "https://www.cryptocompare.com/api/data/coinlist/ \n" +
		          "Remember that cryptocompare lets you fetch the prices up to 'only'\n"+
				  "6000 times per hour \n \n" +
		          "This tool is released under GNU GPL Version 3")
		    exit()
		else:
			raise Exception()

	filename = argv[1]+'_'+argv[2]+'_'+argv[3]+'_'+argv[4]+'_'+argv[5]+'.json'
	url = '?fsym='+argv[1]+'&tsym='+argv[2]+'&aggregate='+argv[4]+'&e=CCCAGG'

	if argv[5] == 'all':
		url = url + '&allData=true'
	elif isinstance(int(argv[5]), int):
		url = url + '&limit=' + argv[5]
	else :
		raise Exception()

	if argv[3] == 'm' or argv[3] == 'h' or argv[3] == 'd':
		if argv[3] == 'm':
		    url = 'https://min-api.cryptocompare.com/data/histominute' + url
		elif argv[3] == 'h':
		    url = 'https://min-api.cryptocompare.com/data/histohour' + url
		elif argv[3] == 'd':
		    url = 'https://min-api.cryptocompare.com/data/histoday' + url
	else:
		raise Exception()

		
	if not (os.path.exists(filename)):
		print("Downloading...")
		data = rq.get(url)
		file = open(filename, "w")
		file.write(data.text)
		file.close()
		data = data.json()

	else:
		file = open(filename, "r")
		data = json.load(file)
		file.close()

	data = pd.DataFrame(data["Data"])

	#-----------CONVERTING TIMESTAMPS TO DATE------------
	data["time"] = pd.to_datetime(data["time"], unit='s')
	#----------------------------------------------------

	if data.empty:
		os.remove(filename)
		print("Inserted currencies has not been found")
		exit()

	else:
		print("Download completed \n"
		      "File saved as " + filename)

	choice = input("Do you want to visualize the data? (Y/n): ")
	if choice == 'Y' or choice == 'y':

	#----------------- TAKEN FROM: http://bokeh.pydata.org/en/latest/docs/gallery/candlestick.html -----------------------

		inc = data.close > data.open
		dec = data.open > data.close
		width = data.time[1]-data.time[0]
		width = width - width/4

		TOOLS = ['pan', 'wheel_zoom', 'box_zoom', 'reset', 'save']

		p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1200, title=argv[1]+'/'+argv[2]+' '+argv[3], toolbar_location='above')
		p.xaxis.major_label_orientation = 3.1415/4
		p.xaxis.axis_label = 'Time'
		p.yaxis.axis_label = argv[2]
		p.grid.grid_line_alpha=0.3

		p.segment(data.time, data.high, data.time, data.low, color="black")
		p.vbar(data.time[inc], width, data.open[inc], data.close[inc], fill_color="#00C241", line_color="black")
		p.vbar(data.time[dec], width, data.open[dec], data.close[dec], fill_color="#F2583E", line_color="black")

		output_file(argv[1]+argv[2]+argv[3]+".html", title=argv[1]+'/'+argv[2]+' '+argv[3])

		show(p)

	#----------------------------------------------------------------------------------------------------------------------

except Exception as e:
    print("Parameters are wrong, use -h for help")

finally:
	exit()








