from rembg import remove
from PIL import Image

input_path = 'cl.jpg'
output_path = 'output.png'

img = Image.open(input_path)
output = remove(img)
output.save(output_path)
