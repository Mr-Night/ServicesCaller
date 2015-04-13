from dollar import Dollar
from weather import Weather
#The next line must be in each ServiceCaller, finished the class it must be deleted from here
from servicesCaller import ServicesCaller

dollar = Dollar
print ("dolar:")
print (Dollar.askDollar())

weather = Weather
print ("Clima actual:")
print (weather.askCurrentWeather())