# Import additional libraries to handle images
from PIL import Image
import requests
from io import BytesIO

# Load an image
img_url = "https://example.com/image.jpg"
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Use the gemini-pro-vision model
model = genai.GenerativeModel('gemini-pro-vision')

# Pass the image and text
response = model.generate_content(["Write a short and engaging blog post based on this image. It should include a description of the meal in the photo and talk about my meal prep journey.", img])

# Print the response text
print(response.text)
