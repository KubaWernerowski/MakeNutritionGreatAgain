from API_INFO import API_KEY, APP_ID
from typing import List, Union, Dict
import requests

API_POST = "https://trackapi.nutritionix.com/v2/natural/nutrients"


class APICall:

    def send_post(self, foods: str):
        """Returns a list of dictionaries of each food passed
        as a request."""
        query = self.make_query(foods)
        headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
        # Send POST to Nutritionix API for nutrition.
        r = requests.post(API_POST, data=query, headers=headers)
        all_foods = r.json()
        # Check case where no food was found.
        if 'message' in all_foods:
            return "Sorry, we couldn't find the food you requested."

        return all_foods['foods']

    def make_query(self, ingredients: str) -> Dict:
        """
        Create the query we send to the API.
        """
        json_post = {"query": ingredients}
        return json_post
