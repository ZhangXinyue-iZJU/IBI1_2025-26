class food_item:
    """
    A class to represent a food item with nutritional information.
    
    Attributes:
        name (str): Name of the food item
        calories (float): Calories in the food item (kcal)
        protein (float): Protein content (grams)
        carbs (float): Carbohydrate content (grams)
        fat (float): Fat content (grams)
    """
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


def calculate_daily_nutrition(food_list):
    """
    Calculate total daily nutritional intake from a list of food_item objects.
    
    Args:
        food_list (list): A list of food_item objects consumed in 24 hours.
        
    Returns:
        dict: A dictionary containing total calories, protein, carbs, and fat.
    """
    # Initialize totals
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    
    # Iterate through each food item
    for food in food_list:
        if not isinstance(food, food_item):
            raise TypeError("All items must be instances of the food_item class.")
        
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat
    
    # Round values
    totals = {
        "calories": round(total_calories, 2),
        "protein": round(total_protein, 2),
        "carbs": round(total_carbs, 2),
        "fat": round(total_fat, 2)
    }
    
    # Print results
    print("\n===== Daily Nutritional Intake =====")
    print(f"Total Calories: {totals['calories']} kcal")
    print(f"Total Protein: {totals['protein']} g")
    print(f"Total Carbohydrates: {totals['carbs']} g")
    print(f"Total Fat: {totals['fat']} g")
    
    # Check for excessive intake
    if totals["calories"] > 2500:
        print("\n⚠️  WARNING: Daily calorie intake exceeds 2500 kcal!")
    if totals["fat"] > 90:
        print("⚠️  WARNING: Daily fat intake exceeds 90 g!")
    
    return totals


# Example usage
if __name__ == "__main__":
    # Create food items
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken = food_item("Chicken Breast", 165, 31, 0, 3.6)
    rice = food_item("White Rice", 206, 4.3, 45, 0.4)
    ice_cream = food_item("Vanilla Ice Cream", 270, 4, 31, 14)
    
    # Daily food list
    daily_food = [apple, chicken, rice, ice_cream]
    
    # Calculate totals
    daily_totals = calculate_daily_nutrition(daily_food)