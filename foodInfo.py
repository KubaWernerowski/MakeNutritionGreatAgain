from Food import *
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from botTest import *
from foodInfo import *
from var_holder import *
from API_CALL import *
client = Bot(description="Basic Bot by Saamoz", command_prefix="!", pm_help = False)
state = var_holder()
food_api = APICall()
nutrients = {"calories": 1, "fat": 2, "saturatedfat": 456, "cholesterol": 45, "sodium": 223,
             "carbs": 13, "fiber": 166, "sugar": 14, "protein": 17, "potassium": 109}

def isNutrient(s: str):
    s = stripString(s)
    if s in nutrients.keys():
        return True
    return False


def getNurtritionalInfo(user_input: list, food_items: list):
    food_items = food_factory(food_items)  # make list of dict of foods into list of Food objects
    numOfKeywords = 0
    keywords = []
    for item in user_input:
        item = stripString(item)
        if isNutrient(item):
            numOfKeywords += 1
            keywords.append(item)
    return naturalResponse(numOfKeywords, keywords, food_items)


def stripString(s: str):
    """ Just makes inputed string lowercase and removes all spaces."""
    return s.lower().replace(",", " ").strip(" ")

def naturalResponse(numOfKeywords: int, keywords: list, food_items: list):
    output = ""
    if numOfKeywords == 0:
        for item in food_items:
            output += str(item)
    return output


def food_factory(food_items: list):
    output = []
    for item in food_items:
        output.append(Food(item))
    return output

def bot_response(message):
    food_input = message.content
    user_input = [stripString(item) for item in food_input.split()]
    dict_of_food = food_api.send_post(message.content)
    if type(dict_of_food) == str:
        return "Sorry we could not find the requested food item"
    else:
        return getNurtritionalInfo(user_input, dict_of_food)
