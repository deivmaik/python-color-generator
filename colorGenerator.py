import os
import numpy as np
from PIL import Image
import colorsys
import json

# Number of colors to generate
num_colors = 10000

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
    hex_colors.append(f"#{r:02x}{g:02x}{b:02x}")

# Convert list to JSON
json_colors = json.dumps(hex_colors)

# Save to a file
with open('colors.json', 'w') as f:
    f.write(json_colors)

# Create a new directory for the images
if not os.path.exists('images'):
    os.makedirs('images')

# Create an image for each color
for hex_color in hex_colors:
    img = Image.new('RGB', (100, 100), hex_color)
    img.save(f'images/{hex_color}.png')
