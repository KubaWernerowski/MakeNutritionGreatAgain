from API_INFO import API_KEY, APP_ID

import requests as r
import json

API_POST = "https://trackapi.nutritionix.com/v2/natural/nutrients"

class APICall:
    """
    Return a single ingredient for now.
    """

    def __init__(self) -> None:
        """Initialize the APICall."""
        pass

    def send_post(self, ) -> json:
        """Placeholder."""
        pass

    def make_query(self, ingredients: str, servings: float = 1.0) -> str:
        """
        Create the query we send to the API.
        Default servings to 1.0
        """
        json_string = f'''
                        {
                          "query": "{ingredients}",
                          "num_servings": {servings},
                          "aggregate": "string",
                          "line_delimited": false,
                          "use_raw_foods": true,
                          "include_subrecipe": false,
                          "timezone": "US/Eastern",
                          "consumed_at": null,
                          "lat": null,
                          "lng": null,
                          "meal_type": 0,
                          "use_branded_foods": true
                        }
                        '''

        return json_string







