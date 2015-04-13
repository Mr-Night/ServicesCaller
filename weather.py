from servicesCaller import ServicesCaller

servicesCaller = ServicesCaller
appid = "fff7fd42955962a13b2f8c56d7e5f583"
defaultParametters = {'q':"Capital ,ar", 'APPID':"fff7fd42955962a13b2f8c56d7e5f583", 'units':"metric", 'lang':"es"}

class Weather():
	"""Weather"""
	def __init__(self):
		super(Weather, self).__init__()
		
	def askWeather():
		pyDictionary = servicesCaller.callJsonService("http://ws.geeklab.com.ar/dolar/get-dolar-json.php")
		print ("Precio del dolar oficial: $:" + pyDictionary['libre'] + "\nPrecio del dolar Blue: $" + pyDictionary['blue'])

	def askCurrentWeather():
		weather = servicesCaller.callJsonService("http://api.openweathermap.org/data/2.5/weather", defaultParametters)
		print (weather)
		for x in weather:
			print (x)
			print (weather[x])
			pass
		return "Clima actual de " + weather['name'] + ", " + weather['sys']['country'] + "\nTemperatura: " + weather['main']['temp'] + "°C \nHumedad:" + weather['main'] 

