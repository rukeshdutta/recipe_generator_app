import openai

def generate_image_prompt(recipe_content):
    prompt = f"Generate a brief image prompt for a food photograph based on this recipe: {recipe_content[:500]}..."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates image prompts for recipes which focuses on aesthetics."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']