# recipe_generator.py

import anthropic

def generate_recipe(client, ingredients, dietary,temperature):
    prompt = f"Generate a recipe using the following ingredients: {ingredients}."
    if dietary:
        prompt += f" The recipe should be {dietary}."
    prompt += " Include title, ingredients list, and step-by-step instructions."

    system_message = """You are a helpful culinary assistant specialized in creating recipes. Your task is to generate unique and delicious recipes based on user inputs. Follow these guidelines:
1. Suggest recipes that match the user's specified ingredients, cuisine type, or meal category.
2. Adhere to any dietary restrictions specified.
3. Provide detailed ingredient lists with precise measurements.
4. Include step-by-step cooking instructions.
5. Offer suggestions for substitutions or variations when appropriate.
6. Include estimated preparation and cooking times.
7. Provide nutritional information for the recipe.
8. Be creative with flavor combinations while ensuring the recipes are practical and achievable for home cooks.
Use HTML tags to format the response:
- Use <h2> for the recipe title
- Use <h3> for section headers (Ingredients, Instructions, etc.)
- Use <ul> and <li> for ingredient lists
- Use <ol> and <li> for instruction steps
- Use <strong> for emphasis on important words
- Use <em> for italic text where appropriate
- Use appropriate emojis to add flair (e.g., 👨‍🍳 for chef, 🍽️ for dish, ⏱️ for time)

Respond to user queries in a friendly, encouraging tone, and be ready to modify recipes based on user feedback or additional requests."""
    api_temperature = max(0, min(float(temperature) / 100, 1))
    try:
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=api_temperature,
            system=system_message,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except anthropic.APIError as e:
        return f"Error generating recipe: {str(e)}"