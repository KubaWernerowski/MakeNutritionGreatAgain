import matplotlib.pyplot as plt
import os


class NutritionGraphics:

    def __init__(self, food):
        """
        Initialize a NutrionGraphics object for a single food object.
        """
        self.food = food

    def create_nutrition_pie_chart(self):
        """
        Returns a pie chart of nutrition for a single food object.
        """
        labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
        sizes = [15, 30, 45, 10]

        explode = (0.05, 0.05, 0.05, 0.05)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.savefig("food_name")

    def delete_image_files(self):
        """Deletes images created once no longer needed."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir = os.listdir(dir_path)

        for item in dir:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_path, item))





a = NutritionGraphics("hello")
a.delete_image_files()
