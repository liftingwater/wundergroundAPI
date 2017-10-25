import requests
import json

def getWeather(key): 
	url = "http://api.wunderground.com/api/" + str(key) + "/conditions/q/PA/Philadelphia.json"
	data = requests.get(url).json()

	categories = ["weather", "temp_f", "relative_humidity", "wind_mph"]

	weather_info = {}
	for i in categories: 
		weather_info[i] = data['current_observation'][i]

	return weather_info

def printResults(api_key): 
	weather_results = getWeather(api_key)
	for i in weather_results: 
		print i + ": " + str(weather_results[i])


	