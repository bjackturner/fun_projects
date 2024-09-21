import json
import os
from PIL import Image

# Creates object for each block in texture pack
class Block:
    def __init__(self, name, path, res, rgb, uni, top, bot) -> None:
        self.name = name    # Block name (string)
        self.path = path    # Block file path (string)
        self.res = res      # Block resolution pixels (int, int)
        self.rbg = rgb      # Block RBG vlaues (int, int, int)
        self.uni = uni      # Are all sides of block the same? (bool)
        self.top = top      # Is top of block? (bool) [ignored if uni = True]
        self.bot = bot      # Is bottom of block? (bool) [ignored if uni = True]

# Find the height and width of an image in pixels
def image_size(img_string) -> tuple:

    # Open inserted image and find pixel height and width
    with Image.open(img_string) as image:
        return image.size 

# Find the average color of an imported image (image path, image resolution)
def avg_RGB(img_string, res) -> tuple:

    return 0

# Generate a list of Block objects for every block in texture pack
def build_block_array(external_path=None) -> list:

    # Empty list that will contain all block objects [first element dictionary containing names]
    blocks = [None]

    # Determine current directory of this file
    current_dir = os.path.dirname(__file__)
    block_dir = os.path.join(current_dir, "default_textures") if external_path is None else external_path

    # Locate json file and create array of desired textures
    with open(os.path.join(current_dir, "_textures.json")) as f:
        texture_data = json.load(f)

    # Seperatre data
    desired_textures = texture_data["textures"]

    # Loop through each file in the texture pack and return its name
    for file in os.listdir(os.path.join(current_dir, "default_textures")):
        
        # Check if block is a desired block, if yes return index and name
        for i, texture in enumerate(desired_textures):
            if texture in file:

                # Determine elements of object
                name = texture.replace("_", " ") # Name of block with spaces (for display)
                path = os.path.join(block_dir, file) # Path of iamge 
                res = image_size(path) # Image size Width x Height (pixels)
                rgb = avg_RGB(path, res)
                uni = False
                top = False
                bot = False

                # Create object with data above
                block = Block(name, path, res, rgb, uni, top, bot)

                # Append object to list
                blocks.append(block)

                # Remove block from the desired textures array
                del desired_textures[i]

                # Quit the inner loop 
                break

    for row in desired_textures:
        print(row)

    return blocks

blocks = build_block_array()

# for block in blocks[1:]:
#     print(block.res)