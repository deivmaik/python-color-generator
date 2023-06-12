import numpy as np
from PIL import Image, ImageDraw, ImageFont
import colorsys
import os
import json

# Number of colors to generate
num_colors = 5555

# Generate a linearly spaced array of hue values
hue_values = np.linspace(0, 1, num_colors)

# Initialize lists to store colors
rgb_colors = []
hex_colors = []

# Generate colors
for hue in hue_values:
    # We use a saturation and lightness value of 0.5 for a nice bright color
    r, g, b = colorsys.hsv_to_rgb(hue, 0.5, 0.5)
    
    # Convert RGB values from range [0, 1] to [0, 255]
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    # Store RGB and hex colors
    rgb_colors.append((r, g, b))
    hex_colors.append(f"#{r:02X}{g:02X}{b:02X}")  # Capital letters for hex

# Convert list to JSON
json_colors = json.dumps(hex_colors)

# Save to a file
with open('colors.json', 'w') as f:
    f.write(json_colors)

# Create a new directory for the images
if not os.path.exists('images'):
    os.makedirs('images')

# Load the font (make sure the Inter font file is in your script's directory or provide full path)
font = ImageFont.truetype('Inter-Black.ttf', 100)

# Create an image for each color
for i, hex_color in enumerate(hex_colors):
    img = Image.new('RGB', (1000, 1000), hex_color)
    draw = ImageDraw.Draw(img)

    # Calculate the width and height of the text to center it
    text_width, text_height = draw.textsize(hex_color, font)
    position = ((1000 - text_width) / 2, (1000 - text_height) / 2)

    # Adjust the lightness based on its current value to ensure contrast
    hue, saturation, lightness = colorsys.rgb_to_hsv(*rgb_colors[i])
    lightness = lightness - 0.2 if lightness > 0.5 else lightness + 0.2

    # Convert the adjusted color to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, lightness)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Draw the text with the adjusted color
    draw.text(position, hex_color, fill=(r, g, b), font=font)

    img.save(f'images/{hex_color}.png')
    # Close the image file
    img.close()
