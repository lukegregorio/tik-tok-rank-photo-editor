from PIL import Image
import os


def main(width=1000, height=1000):
    # open image files in images folder and save them in a list
    images = []

    for filename in os.listdir('images'):
        # ignore non-image files
        if not filename.endswith('.jpg') and not filename.endswith('.jpeg') and not filename.endswith('.png'):
            continue
        img = Image.open(f'images/{filename}')
        images.append(img)

    # amend all the images to have the same size 1000x1000
    for i in range(len(images)):
        images[i] = images[i].resize((width, height))

    # convert all the images to png format
    for i in range(len(images)):
        images[i].save(f'output/{i+1}.png')

if __name__ == '__main__':
    main()