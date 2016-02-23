from servicesCaller import ServicesCaller
import math

servicesCaller = ServicesCaller
appid = "fff7fd42955962a13b2f8c56d7e5f583"
defaultParametters = {'q':"Capital ,ar", 'APPID':"fff7fd42955962a13b2f8c56d7e5f583", 'units':"metric", 'lang':"es"}

class Weather():
	"""Weather"""
	def __init__(self):
		super(Weather, self).__init__()

	def askWeather():
		weather = servicesCaller.callJsonService("http://ws.geeklab.com.ar/dolar/get-dolar-json.php")
		return weather

	def askCurrentWeather():
		weather = servicesCaller.callJsonService("http://api.openweathermap.org/data/2.5/weather", defaultParametters)
		print(weather)
        #city = weather['name']
        #country = weather['sys']['country']
        #temperature = weather['main']['temp']
        #humidity = weather['main']
        #feelsLike = calculateFeelsLike()
		#return "Clima actual de " + weather['name'] + ", " + weather['sys']['country'] + "\nTemperatura: " + weather['main']['temp'] + " grados celcius.\nHumedad: " + weather['main'] + "%\nSensacion Termica: "
        
	def calculateFeelsLike(temperature, windSpeed):
		feelsLike = 33 + (temperature- 33)*(0.474 + 0.454 * math.sqrt((windSpeed))-0.0454*windSpeed)
		return feelsLike
