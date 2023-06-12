import os
import numpy as np
from PIL import Image
import colorsys

# Size of the banner
width, height = 1512, 322

# Number of colors to generate
num_colors = 10000

# Calculate the size of each square
square_size = int((width * height / num_colors) ** 0.5)

# Calculate the number of squares along width and height
num_squares_width = width // square_size
num_squares_height = height // square_size

# Generate a linearly spaced array of hue values
hue_values = np.linspace(0, 1, num_squares_width * num_squares_height)

# Initialize list to store colors
colors = []

# Generate colors
for hue in hue_values:
    # We use a saturation and lightness value of 0.5 for a nice bright color
    r, g, b = colorsys.hsv_to_rgb(hue, 0.5, 0.5)
    
    # Convert RGB values from range [0, 1] to [0, 255]
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    # Store RGB color
    colors.append((r, g, b))

# Create a new image for the banner
banner = Image.new('RGB', (width, height))

# Fill the banner with color squares
for i in range(num_squares_height):
    for j in range(num_squares_width):
        color = colors[i * num_squares_width + j]
        for y in range(i * square_size, (i+1) * square_size):
            for x in range(j * square_size, (j+1) * square_size):
                banner.putpixel((x, y), color)

# Save the banner
banner.save('banner.png')
