from urllib2 import urlopen
from json import load
import json
import re

ingredients = raw_input("What ingredients do you want?")
url = "http://food2fork.com/api/search?key="
key = "7ca33bbd3af2eaa85e40644cb479036f"
url += key
url += "&q="
url += ingredients
url += "&sort=r"

print url

response = urlopen(url)
json_obj = load(response)

for i in json_obj['recipes']:
	print i['title'] + ' - ' + i['recipe_id']

rID = raw_input("Enter the ID number for the recipe you want.")

get_url = "http://food2fork.com/api/get?key="
get_url += key
get_url += "&rId="
get_url += rID

get_response = urlopen(get_url)
get_final = load(get_response)

calorie_api = "a70UXYhUSUx0bO3XF7SBAThe4gBAnbWLBfj3QWRR"
calorie_url = " http://api.nal.usda.gov/ndb/search/?format=json&q="

for ingredient in get_final['recipe']['ingredients']:
	comma_replace = ingredient.replace(",","")
	space_replace = comma_replace.replace(" ", "+")
	calorie_url += space_replace
	calorie_url += "&sort=n&max=25&offset=0&api_key="
	calorie_url += calorie_api
	print calorie_url
	calorie_response = urlopen(calorie_url)
	calorie_json_obj = load(calorie_response)

	for result in calorie_json_obj['list']['item']:
		print result['name'] + ' -- ' + result['ndbno']

#first_ingredient = "6 skinless, boneless chicken breast halves"
#first_ingredient_second = first_ingredient.replace(",", "")
#first_ingredient_third = first_ingredient_second.replace(" ", "+")
#print first_ingredient_third

#calorie_url += first_ingredient_third
#calorie_url += "&sort=n&max=25&offset=0&api_key="
#calorie_url += calorie_api
#print calorie_url
#calorie_response = urlopen(calorie_url)
#calorie_json_obj = load(calorie_response)
#for result in calorie_json_obj['list']['item']:
	#print result['name'] + ' -- ' + result['ndbno']
