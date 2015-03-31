import json
import requests

class ServicesCaller():
	"""A object to calll WewServices"""
	def __init__(self):
		super(servicesCaller, self).__init__()
		
	def callJsonService(url, parametters={}):
		parameterizedUrl = url + "?"
		for key in parametters:
			if parameterizedUrl[-1] != '?':
				parameterizedUrl += '&'
			parameterizedUrl += key + "=" + parametters[key]
		print ("-parameterizedUrl-")
		print (parameterizedUrl)
		print ("-requests.get(url)-")
		print (requests.get(url))
		jsonResult = (requests.get(url)).text
		print ("-jsonResult-")
		print (jsonResult)
		pyDictionaryResult = json.loads(jsonResult)
		print ("-pyDictionaryResult-")
		print (pyDictionaryResult)
		return pyDictionaryResult
