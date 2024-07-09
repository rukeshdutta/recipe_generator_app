from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import anthropic
from recipe_formatter import format_recipe_html
from recipe_generator import generate_recipe  # Import the new function
from bs4 import BeautifulSoup

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('CLAUDE_API_KEY')
client = anthropic.Anthropic(api_key=api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        dietary = request.form['dietary']
        temperature = int(request.form['temperature'])
        recipe_content = generate_recipe(client, ingredients,dietary, temperature)  # Pass the client
        formatted_recipe = format_recipe_html(recipe_content)
        # soup = BeautifulSoup(formatted_recipe,'html.parser')
        # recipe_title = soup.find('h2').text
        # chatgpt_prompt_title = chatgpt_prompt_title(recipe_title)
        return render_template('index.html', recipe=formatted_recipe)
    return render_template('index.html')

def chatgpt_prompt_title(recipe_title):
    return f"Processed recipe: {recipe_title}"


if __name__ == '__main__':
    app.run(debug=True)