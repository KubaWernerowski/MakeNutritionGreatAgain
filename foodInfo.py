nutrients = {"calories":1, "totalfat": 2, "fat":34, "saturatedfat":456, "cholesterol":45, "sodium":223, "carbohydrate": 13, "dietaryfiber": 166, "sugars": 14, "protein":17, "potassium":109}
def isNutrient(s: str):
    s = stripString(s)
    if s in nutrients.keys():
        return True
    return False



def getNurtritionalInfo(user_input: list):
    output = ""
    for item in user_input:
        if isNutrient(item):
            item = stripString(item)
            output += (item + ": " + str(nutrients[item]) + "\n")
    return output


def stripString(s: str):
    """ Just makes inputed string lowercase and removes all spaces."""
    return s.lower().replace(",", " ").strip(" ")
