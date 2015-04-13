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
		jsonResult = (requests.get(parameterizedUrl)).text
		pyDictionaryResult = json.loads(jsonResult)
		return pyDictionaryResult
