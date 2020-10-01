"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://make-school-courses.github.io/BEW-2.3-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""

""" Notes:
Steganography is the practice of hiding a file, message, image or video within another file, message, image or video. The word steganography is derived from the Greek words steganos (meaning hidden or covered) and graphe (meaning writing).

An image consists of several pixels, each pixel contains three values (which are Red, Green, Blue), these values range from 0 to 255, in other words, they are 8-bit values. For example, a value of 225 is 11100001 in binary and so on.

"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image, ImageDraw, ImageChops


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    # red_channel = encoded_image.split()[0]    # isolates the red from the RGB image

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = encoded_image.copy()
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    # print(red_channel)  # Start coding here!
    for i in range(x_size):      # iterate through the x_size
        for j in range(y_size):     # and iterate through the y_size 
            if pixels[i,j][0] % 2:    # returns odd numbers
                pixels[i,j] = (255, 255, 255)   # change to white
            else:
                pixels[i,j] = (0, 0, 0)      # change to black


    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png, text_to_write):
    """
    write_text() will take a string and convert it to a black and white image of the string. You may use it as a helper function in completing your implementation of encode_image(). https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html?highlight=multiline_text#PIL.ImageDraw.ImageDraw.multiline_text

    PIL.Image.new(mode, size, color=0) --> color for image is black by default 
    Creates a new image with the given mode (mode we are using is RGB) and size. https://pillow.readthedocs.io/en/stable/reference/Image.html

    The ImageDraw module provides simple 2D graphics for Image objects. You can use this module to create new images, annotate or retouch existing images, and to generate graphics on the fly for web use. https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    """

    '''
    open image, create new image, draw on the image to write the text, *very important: change image color to black (see nested for loop), combine the images, then save
    '''
    # Open the image::
    image = Image.open(path_to_png).convert('RGB')   # convert opened image to RGB first
    image_with_msg = Image.new('RGB', image.size, color=0) # creates a new image in the color black
    draw = ImageDraw.Draw(image_with_msg)      

    # draw multiline text
    draw.multiline_text((10,10), "Can you read this message?\nIf so, good job!", fill=(1, 0, 0))
    # image_with_msg.save('test.png')

    pixels = image.load()
    x_size, y_size = image.size

    for i in range(x_size):      # iterate through the x_size
        for j in range(y_size):     # and iterate through the y_size 
            if pixels[i,j][0] % 2:    # returns odd numbers
                pixel = pixels[i,j]
                pixels[i,j] = (pixel[0] - 1, pixel[1], pixel[2]) 
                            

    encoded_img = ImageChops.add(image, image_with_msg)
    encoded_img.save('encoded_img.png')

