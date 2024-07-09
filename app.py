from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import anthropic
from recipe_formatter import format_recipe_html
from recipe_generator import generate_recipe  # Import the new function
import openai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('CLAUDE_API_KEY')
client = anthropic.Anthropic(api_key=api_key)

openai_api_key = os.getenv('OPENAI_API_KEY')

def generate_image_prompt(recipe_content):
    prompt = f"Generate a brief image prompt for a food photograph based on this recipe: {recipe_content[:500]}..."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates image prompts for recipes."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        dietary = request.form['dietary']
        temperature = int(request.form['temperature'])
        recipe_content = generate_recipe(client, ingredients, dietary, temperature)
        formatted_recipe = format_recipe_html(recipe_content)
        
        # Generate image prompt and image
        image_prompt = generate_image_prompt(recipe_content)
        image_url = generate_image(image_prompt)
        
        return render_template('index.html', recipe=formatted_recipe, image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)