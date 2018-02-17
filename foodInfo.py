from Food import *
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from botTest import *
from Parser import *
from var_holder import *
from API_CALL import *
from NutritionGraphics import *
client = Bot(description="Basic Bot by Saamoz", command_prefix="!", pm_help = False)
state = var_holder()
food_api = APICall()
parser = Parser()

def getNurtritionalInfo(user_input: str, food_items: list):
    food_items = food_factory(food_items)  # make list of dict of foods into list of Food objects
    nutritionalKeywords = parser.getNutrientKeyWords(user_input)
    actionKeywords = parser.getActionKeyWords(user_input)
    text = []
    filenames = []
    for item in food_items:
        text.append(naturalResponse(item, nutritionalKeywords))

    if len(actionKeywords) > 0:
        if actionKeywords[0] == "pic":
            filenames = generatePic(food_items)
        if actionKeywords[0] == "compare":
            if (len(food_items) > 1):
                text.append(generateComparison(food_items[0], food_items[1], nutritionalKeywords))
            else:
                text.append("You need more 2 foods for a valid comparison.")
        if actionKeywords[0] == "sum":
            text.append(generateTotal(nutritionalKeywords, food_items))

    return {"text": text, "visual": filenames}


def generatePic(food_items: list):
    filenames = []
    for item in food_items:
        curr = NutritionGraphics(item)
        curr.create_nutrition_pie_chart()
        filenames.append(curr.pie_graph)
    return filenames

def generateTotal(keywords: list, food_items: list):
    if len(keywords) == 0:
        keys = food_items[0].nutrients.keys()
    else:
        keys = keywords
    output = "Total \n"
    for key in keys:
        sum = 0
        for food in food_items:
            if food.nutrients[key] is not None:
                sum += food.nutrients[key]
        output += f"{key}: {sum} \n"


    output+= "-------------------------------------------------------------"
    return output





def generateComparison(food1: "Food", food2: "Food", keyWords: list):
    if len(keyWords) == 0:
        keys = food1.nutrients.keys()
    else:
        keys = keyWords
    output = ""
    for key in keys:
        difference = food1.nutrients[key] - food2.nutrients[key]
        if difference > 0:
            output += f"{food1.name} has {abs(difference)} more {key} than {food2.name} \n"
        elif difference < 0:
            output += f"{food2.name} has {abs(difference)} more {key} than {food1.name} \n "
        else:
            output += f"Both, {food1.name} and {food2.name}, has the same amount of {key} (food1.nutrients[key]) \n"
    output+= "-------------------------------------------------------------"
    return output


def naturalResponse(food: 'Food', nutritionalKeyWords: list):
    numOfKeywords = len(nutritionalKeyWords)
    output = ""
    if numOfKeywords == 0:
        return str(food) + "\n" +  "-------------------------------------------------------------"
    if numOfKeywords > 0:
        output+= food.name + " \n"
        for word in nutritionalKeyWords:
            value = food.nutrients[word]
            output += f"The amount of {word} is {value}  \n "
    output+=  "-------------------------------------------------------------"
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
