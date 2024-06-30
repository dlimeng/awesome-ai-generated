import os
from PIL import Image

# Define the paths
input_folder = r'D:\images'
output_folder = os.path.join(input_folder, 'Posters')
info_layer_path = os.path.join(input_folder, 'info.png')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the composite layer
info_layer = Image.open(info_layer_path).convert("RGBA")

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')) and filename != 'info.png':
        # Open the original image
        original_image_path = os.path.join(input_folder, filename)
        original_image = Image.open(original_image_path).convert("RGBA")

        # Combine the original image with the info layer
        combined_image = Image.alpha_composite(original_image, info_layer)

        # Save the processed image to the output folder with '_poster' appended to the name
        base_name, ext = os.path.splitext(filename)
        output_image_path = os.path.join(output_folder, f"{base_name}_poster.png")
        combined_image.save(output_image_path)

print("Batch image processing completed successfully.")
