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

class Parser:
    """This represents a parser class."""
    def __init__(self):
        self.nutrientKeyWords = ["calories", "fat", "saturated", "cholesterol", "sodium", "carb", "fiber", "sugar",
                                 "protein", "potassium"]
        self.actionKeyWords = ["pic", "compare", "sum"]

    def isNutrient(self, s: str):
        s = self.stripString(s)
        if s in self.nutrientKeyWords:
            return True
        return False

    def stripString(self, s: str):
        """ Just makes inputed string lowercase and removes all spaces."""
        return s.lower().replace(",", " ").strip(" ")

    def getNutrientKeyWords(self, s: str):
        keyWords = []
        for item in self.nutrientKeyWords:

            if item in s.lower():
                keyWords.append(item)
        return keyWords

    def getActionKeyWords(self, s: str):
        keyWords = []
        for item in self.actionKeyWords:
            if item in s.lower():
                keyWords.append(item)
        return keyWords
