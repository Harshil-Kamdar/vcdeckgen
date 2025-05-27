import openai
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use env variable for deployment

def generate_images(slides):
    image_paths = []
    for i, slide in enumerate(slides):
        if slide['title'] in ["Problem", "Solution", "Product/Tech", "Team"]:
            prompt = f"An illustration for a business slide about: {slide['title']} - {slide['content'][:100]}"
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            image_data = requests.get(image_url).content
            image_path = f"output/{slide['title'].replace(' ', '_')}_image.png"
            with open(image_path, "wb") as img_file:
                img_file.write(image_data)
            image_paths.append(image_path)
        else:
            image_paths.append(None)
    return image_paths
