class Food:

    def __init__(self, myDict):
        self.name = myDict['food_name']
        self.quantity = myDict['serving_qty']

        self.weight = myDict['serving_weight_grams']

        self.calories = myDict['nf_calories']
        self.fat = myDict['nf_total_fat']
        self.saturatedfat = myDict['nf_saturated_fat']
        self.cholesterol = myDict['nf_cholesterol']
        self.sodium = myDict['nf_sodium']
        self.carbs = myDict['nf_total_carbohydrate']
        self.fiber = myDict['nf_dietary_fiber']
        self.sugar = myDict['nf_sugars']
        self.protein = myDict['nf_protein']

        # initialize the dictionary representation of the above information.
        self.nutrients = {}
        self.initDict()

    def initDict(self) -> None:
        """ initializes the nutrients dictionary with correct info."""
        self.nutrients["calories"] = self.calories
        self.nutrients["fat"] = self.fat
        self.nutrients["saturatedfat"] = self.saturatedfat
        self.nutrients["cholestrol"] = self.cholesterol
        self.nutrients["sodium"] = self.sodium
        self.nutrients["carbs"] = self.carbs
        self.nutrients["carbohydrate"] = self.carbs
        self.nutrients["fiber"] = self.fiber
        self.nutrients["sugar"] = self.sugar
        self.nutrients["protein"] = self.protein

    def __str__(self):
        output = self.name + "\n"
        for k,v in self.nutrients.items():
            output += k + ": " + str(v) + "\n"
        return output
