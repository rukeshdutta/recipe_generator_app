from flask import Flask, render_template, request, session, redirect, url_for
from dotenv import load_dotenv
import os
import anthropic
from recipe_formatter import format_recipe_html
from recipe_generator import generate_recipe  # Import the new function
from image_generator import generate_image_prompt, generate_image


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

api_key = os.getenv('CLAUDE_API_KEY')
client = anthropic.Anthropic(api_key=api_key)

openai_api_key = os.getenv('OPENAI_API_KEY')

# def generate_image_prompt(recipe_content):
#     prompt = f"Generate a brief image prompt for a food photograph based on: {recipe_content[:500]}..."
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that creates image prompts for recipes which focuses on aesthetics."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message['content']

# def generate_image(prompt):
#     response = openai.Image.create(
#         prompt=prompt,
#         n=1,
#         size="1024x1024"
#     )
#     return response['data'][0]['url']

@app.route('/result')
def result():
    recipe = session.get('recipe')
    image_url = session.get('image_url')
    return render_template('result.html', recipe=recipe, image_url=image_url)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        dietary = request.form['dietary']
        cuisine = request.form.get('cuisine','')
        temperature = int(request.form['temperature'])
        recipe_content = generate_recipe(client, ingredients, dietary, temperature,cuisine)
        formatted_recipe = format_recipe_html(recipe_content)
        
        # Generate image prompt and image
        image_prompt = generate_image_prompt(recipe_content)
        image_url = generate_image(image_prompt)
        session['recipe'] = formatted_recipe
        session['image_url'] = image_url
        return redirect(url_for('result'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)