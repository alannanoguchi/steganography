from PIL import Image

encoded_image = Image.open("encoded_sample.png")

# Create a new PIL image with the same size as the encoded image:
decoded_image = Image.new("RGB", encoded_image.size)
pixels = encoded_image.load()
x_size, y_size = encoded_image.size

