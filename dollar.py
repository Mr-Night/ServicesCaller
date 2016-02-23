from servicesCaller import ServicesCaller

servicesCaller = ServicesCaller

class Dollar():
	"""Dollar"""
	def __init__(self):
		super(Dollar, self).__init__()
		
	def askDollar(self):
		pyDictionary = servicesCaller.callJsonService("http://ws.geeklab.com.ar/dolar/get-dolar-json.php")
		return ("Precio del dolar oficial: $:" + pyDictionary['libre'] + "\nPrecio del dolar Blue: $" + pyDictionary['blue'])