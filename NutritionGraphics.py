import matplotlib.pyplot as plt
import os
import Food


class NutritionGraphics:

    def __init__(self, food: Food) -> None:
        """
        Initialize a NutrionGraphics object for a single food object.
        """
        self.food = food
        # Gets unique nutrients that are measured in grams.
        # Works roughly for liquids since 1 mL of liquids ~ 1 g
        self.relevant_nutrients = [food.nutrients[key] for key in food.nutrients
                                   if key not in ("calories", "cholestrol",
                                                  "sodium", "carbohydrate")]

    def create_nutrition_pie_chart(self) -> None:
        """
        Saves a pie chart of nutrition for a single food object.
        """
        labels = self.relevant_nutrients
        sizes = [(self.food.nutrients[key] / self.food.weight) * 100 for
                 key in labels]
        explode = [0.05]*len(labels)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.title(f"{self.food.name} nutrition breakdown (grams)")
        plt.savefig(self.food.name)

    def delete_image_files(self):
        """Deletes images created once no longer needed."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir = os.listdir(dir_path)

        for item in dir:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_path, item))

