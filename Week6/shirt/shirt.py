import sys
from pathlib import Path
from PIL import Image, ImageOps


def main():

    if len(sys.argv) == 3:
        inp = Path(sys.argv[1])
        output = Path(sys.argv[2])

        if inp.suffix != output.suffix:
            sys.exit('Input and output have different extensions')
        if inp.suffix not in ['.jpg', '.jpeg', '.png']:
            sys.exit('Invalid extension')

        shirtify(inp, output)

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')


def shirtify(inp, output):

    try:
        shirt = Image.open('shirt.png')

        with Image.open(inp) as im:
            fitted_img = ImageOps.fit(im, shirt.size)
            fitted_img.paste(shirt, shirt)
            fitted_img.save(output)

    except FileNotFoundError:
        sys.exit('Image does not exist')


if __name__ == "__main__":
    main()
