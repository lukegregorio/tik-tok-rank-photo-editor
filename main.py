from PIL import Image, ImageDraw, ImageFont
import os


def add_text_to_image(image, text, text_size=40, text_color='white', outline_width=2, outline_color='red', font_path='my_font.ttf'):

    # create a drawing object
    draw = ImageDraw.Draw(image)

    # create a font object
    font = ImageFont.truetype(font_path, text_size)

    # get the width and height of the text
    text_width = draw.textlength(text, font)
    
    # set position of the text at the centre and bottom of the image
    x = (image.width - text_width) / 2
    y = image.height - text_size -  5

    # Draw the outline
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    
    # Draw the text
    draw.text((x, y), text, font=font, fill=text_color)

    return image


def main(image_width=300, image_height=300, add_name=False, text_size=40, text_color='white', outline_width=2, outline_color='red', font_path='my_font.ttf'):

    # empty the output folder except for the .gitkeep file
    for filename in os.listdir('output'):
        if filename != '.gitkeep':
            os.remove(f'output/{filename}')

    for filename in os.listdir('images'):

        # ignore non-image files
        if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png'):
            continue

        image = Image.open(f'images/{filename}')
        name = filename.split('\\')[-1].split('.')[0]

        # amend all the images to have the same size
        image = image.resize((image_width, image_height))

        # add name to the images
        if add_name:
            image = add_text_to_image(image, name, text_size, text_color, outline_width, outline_color, font_path)

        # convert the image to jpg format
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(f'output/{name}.jpg')

if __name__ == '__main__':
    main(add_name=True)