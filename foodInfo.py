from Food import *
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from botTest import *
from Parser import *
from foodInfo import *
from var_holder import *
from API_CALL import *
client = Bot(description="Basic Bot by Saamoz", command_prefix="!", pm_help = False)
state = var_holder()
food_api = APICall()
parser = Parser()

def getNurtritionalInfo(user_input: list, food_items: list):
    food_items = food_factory(food_items)  # make list of dict of foods into list of Food objects
    keywords = parser.nutrientKeyWords()

    return naturalResponse(food_items, keywords)

def naturalResponse(food_items: list, nutritionalKeyWords: list):
    output = ""
    numOfKeywords = len(nutritionalKeyWords)
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

    dict_of_food = food_api.send_post(message.content)
    if type(dict_of_food) == str:
        return "Sorry we could not find the requested food item"
    else:
        return getNurtritionalInfo(message.content, dict_of_food)
