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
        ORDERED_NUTRIENTS = [x for x in self.food.nutrients]

        food1data = [[self.food.name, nutrient,
                      self.food.nutrients[nutrient]] for nutrient in ORDERED_NUTRIENTS]
        food2data = [[other_food.food.name, nutrient,
                      other_food.food.nutrients[nutrient]] for nutrient in ORDERED_NUTRIENTS]

        dpoints = np.array(food1data, food2data)

        bar = plt.figure()
        ax = bar.add_subplot(111)

        space = 0.3

        conditions = np.unique(dpoints[:, 0])
        categories = np.unique(dpoints[:, 1])

        n = len(conditions)

        width = (1 - space) / len(conditions)

        print("width:", width)

        for i, cond in enumerate(conditions):
            vals = dpoints[dpoints[:, 0] == cond][:, 2].astype(np.float)
            pos = [j - (1 - space) / 2. + i * width for j in range(1, len(categories) + 1)]

            ax.bar(pos, vals, width=width)

            ax.set_xticks("indeces")
            ax.set_xticklabels(categories)
            plt.setp(plt.xticks()[1], rotation=90)

            ax.set_ylabel("Amount")
            ax.set_xlabel("Nutrient")

            ax.bar(pos, vals, width=width, label=cond, color=cm.Accent(float(i) / n))

            handles, labels = ax.get_legend_handles_labels()
            ax.legend(handles[::-1], labels[::-1])


            bar_graph = self.food.name + "_" + other_food.food.name + "_bar_graph"
            plt.savefig(bar_graph)

        self.bar_graph = "./" + self.food.name + "_" + other_food.food.name + "_bar_graph.png"



    def delete_image_files(self):
        """Deletes images created once no longer needed."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        get_dir = os.listdir(dir_path)

        for item in get_dir:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_path, item))
