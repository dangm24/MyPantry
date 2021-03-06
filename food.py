from urllib2 import urlopen
from json import load
import json
import re

#User is prompted to enter ingredients for recipes. ie: Chicken, rice, beans
ingredients = raw_input("What ingredients do you want?\n")
ingredients = ingredients.replace(",","")
ingredients = ingredients.replace(" ", "+")
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

#User selects the choosen recipe based on ID number of recipe. ie: 15300
#A list of the ingredients is printed out.
rID = raw_input("\nEnter the ID number for the recipe you want.\n")

get_url = "http://food2fork.com/api/get?key="
get_url += key
get_url += "&rId="
get_url += rID

print get_url

get_response = urlopen(get_url)
get_final = load(get_response)



for ingredient in get_final['recipe']['ingredients']:
	print ingredient

total_calories = 0

ingredient_calories = []

while True:
	calorie_api = "a70UXYhUSUx0bO3XF7SBAThe4gBAnbWLBfj3QWRR"
	calorie_url = " http://api.nal.usda.gov/ndb/search/?format=json&q="

	nutrient_url =  " http://api.nal.usda.gov/ndb/nutrients/?format=json&api_key="
	nutrient_url += calorie_api
	nutrient_url += "&nutrients=208&ndbno="

	#From list of ingredients, user types the ingredient name to get its calories.
	#Example: "2 cups of milk". Input: "milk"
	calorie_search = raw_input("\nWhat ingredient do you want the calories for? Or type exit to see your total calories.\n")
	calorie_search = calorie_search.replace(",", "")
	calorie_search = calorie_search.replace(" ", "+")
	if calorie_search == "exit":
		print "\n"
		for ingredient,calories in ingredient_calories:
			print ingredient + " Calories: " + calories
		print "Your total calories are %d" % total_calories
		break 
	calorie_url += calorie_search
	calorie_url += "&sort=n&max=25&offset=0&api_key="
	calorie_url += calorie_api
	calorie_response = urlopen(calorie_url)
	calorie_json_obj = load(calorie_response)
	for result in calorie_json_obj['list']['item']:
		print result['name'] + ' -- ' + result['ndbno']
	calorie_search = raw_input("\nEnter the ID for your ingredient\n")
	nutrient_url += calorie_search
	nutrient_response = urlopen(nutrient_url)
	nutrient_json_obj = load(nutrient_response)
	ingredient_calories.append((nutrient_json_obj['report']['foods'][0]['name'],nutrient_json_obj['report']['foods'][0]['nutrients'][0]["value"]))
	print nutrient_json_obj['report']['foods'][0]['name'] + " Calories: " + nutrient_json_obj['report']['foods'][0]['nutrients'][0]["value"]
	total_calories += int(nutrient_json_obj['report']['foods'][0]['nutrients'][0]["value"])
