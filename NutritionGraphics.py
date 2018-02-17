import matplotlib.pyplot as plt
from matplotlib import cm
import os
import numpy as np


class NutritionGraphics:

    def __init__(self, food) -> None:
        """
        Initialize a NutrionGraphics object for a single food object.
        """
        self.food = food
        # Gets unique nutrients that are measured in grams.
        # Works roughly for liquids since 1 mL of liquids ~ 1 g
        self.relevant_nutrients = [nutrient for nutrient in food.nutrients
                                   if nutrient not in ("calories", "cholestrol",
                                                  "sodium", "carbohydrate", "fat")]
        self.relevant_nutrients.append("unsaturated fat")

        self.pie_graph = ""
        self.bar_graph = ""

    def create_nutrition_pie_chart(self):
        """
        Saves a pie chart of nutrition for a single food object.
        """
        labels = self.relevant_nutrients
        sizes = [(self.food.nutrients[key] / self.food.weight) * 100 for
                 key in labels if key != "unsaturated fat"]
        # Find unsaturated fat amount. Total fat - saturated fat.
        sizes.append(self.food.nutrients["fat"] - self.food.nutrients["saturatedfat"])
        # Replace saturatedfat with saturated fat.
        labels[labels.index("saturatedfat")] = "saturated fat"

        explode = [0.05]*len(labels)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.title(f"{self.food.name} nutrition breakdown (grams)")
        plt.savefig(self.food.name)
        self.pie_graph = "./" + self.food.name + ".png"

    def create_bar_graph_comparison(self, other_food, comparison_nutrient):
        """
        Creates a bar graph comparing two distinct foods' nutrients.
        """
        food_one_nutrient = self.food.nutrients[comparison_nutrient]
        other_food_nutrient = other_food.nutrients[comparison_nutrient]

        food_one = [0, food_one_nutrient / 3, (2 * food_one_nutrient) / 3, food_one_nutrient]
        food_two = [0, other_food_nutrient / 3, (2 * other_food_nutrient) / 3, other_food_nutrient]

        fig, ax = plt.subplots()

        index = np.arrange(2)
        width = 1.0

        opacity = 0.5

        rect1 = plt.bar(index, food_one, color='b', label=self.food.name)
        rect2 = plt.bar(index, food_two, color='r', label=other_food.food.name)

        plt.xlabel('Food')
        plt.ylabel('Amount of nutrient')
        plt.title(f'Comparison of {comparison_nutrient} between {self.food.name} and {other_food.food.name}')
        plt.legend()

        plt.tight_layout()
        plt.savefig(f"{self.food.name}_{other_food.food.name}_bargraph")

        self.bar_graph = f"./{self.food.name}_{other_food.food.name}_bargraph.png"



    def delete_image_files(self):
        """Deletes images created once no longer needed."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        get_dir = os.listdir(dir_path)

        for item in get_dir:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_path, item))
