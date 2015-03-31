from dollar import Dollar
from servicesCaller import ServicesCaller

dollar = Dollar
print ("dolar:")
print (Dollar.askDollar())

appid = "fff7fd42955962a13b2f8c56d7e5f583"
sc = ServicesCaller
weather = sc.callJsonService("http://api.openweathermap.org/data/2.5/weather", {'q':"Capital ,ar", 'APPID':appid})
print (weather)