import openai

def generate_image_prompt(recipe_content):
    try:
        prompt = f"Generate a brief image prompt for a food photograph based on this recipe: {recipe_content[:500]}..."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates image prompts for recipes which focuses on aesthetics."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        print(f"Error generating image prompt: {str(e)}")
        return None

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response['data'][0]['url']
    except openai.error.OpenAIError as e:
        print(f"Error generating image: {str(e)}")
        return None