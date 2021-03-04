import sys
import os
from PIL import Image

working_path = './{folder}'.format(folder=sys.argv[1]) # Designates folder containing files to be converted.
new_folder = sys.argv[2] # Designates new folder where converted files will be stored. File name determined by second command line arg.

current_directory = './'
os.chdir(current_directory)
os.mkdir(new_folder)

os.chdir(working_path)

for f in os.listdir():
    img = Image.open('./{image}'.format(image = f))
    base = os.path.basename('./' + f)
    image_name = os.path.splitext(base)[0]
    os.chdir('../'+new_folder)
    img.save(image_name + '.png', 'png')
    os.chdir('../'+working_path)






# Grab first and second argument (Pokedex / New folder)
# Check if new exists, if not create

# Loop through Pokedex
# Convert image to png