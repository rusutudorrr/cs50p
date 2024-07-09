import pytesseract
import pdfplumber

from PIL import Image, ImageEnhance
from fpdf import FPDF
from time import sleep


def main():
    print("***OCR process has started***")
    sleep(0.3)
    # ideally this should look with iterdir() for all the files in the dir
    input_file = "/workspaces/93213219/ocr/images/invoice-ro.pdf"
    output_file = "/workspaces/93213219/ocr/output/output.pdf"

    try:
        text = extract_text(input_file)
        create_pdf_from_text(text, output_file)
        print(f"***OCR process completed. Text has been written to {output_file}***")
    except Exception as e:
        print(f"An error occurred: {e}")


def is_image_file(filename):
    # ideally we can extend this with a lot of file types
    return filename.lower().endswith(('.png', '.jpg', '.jpeg'))


def preprocess_image(image_path):
    print("***Processing image***")
    sleep(0.3)
    image = Image.open(image_path)
    # convert to grayscale for better contrast
    image = image.convert('L')
    # binarize image, < 200 is set to black, > 200 is set to white
    threshold = 200
    image = image.point(lambda p: p > threshold and 255)
    # enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    return image


def extract_text_from_image(image_path):
    print("***Extracting text***")
    sleep(0.3)
    processed_image = preprocess_image(image_path)
    # expect a single text block for psm 6
    return pytesseract.image_to_string(processed_image, lang='ron', config='--psm 6')


def extract_text(input_path):
    print("***Checking input file***")
    sleep(0.3)
    # it it's a jpeg/png etc
    if is_image_file(input_path):
        return extract_text_from_image(input_path)
    else:
        # if it's a pdf or non image
        text_parts = []
        with pdfplumber.open(input_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
                for image_detail in page.images:
                    image = extract_image_from_page(page, image_detail)
                    # auto text block detection for psm 3 and LTSM engine for oem1
                    text_parts.append(pytesseract.image_to_string(image,
                                                                  lang='ron',
                                                                  config='--psm 3 --oem 1'))
        return "\n".join(text_parts)


def extract_image_from_page(page, image_detail):
    # get the coordinates x0/x1 horizontal, bottom/top vertial, and crop bounding box
    # then return the original image cropped
    bbox = (image_detail["x0"], image_detail["top"], image_detail["x1"], image_detail["bottom"])
    return page.crop(bbox).to_image().original


def create_pdf_from_text(text, output_pdf_path):
    print("***Creating output file***")
    sleep(0.3)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    # 0 width of cell, 10 height of cell
    pdf.multi_cell(0, 10, text.encode('latin-1', 'replace').decode('latin-1'))
    # also could add a regex matcher to return exactly something that the user wants
    pdf.output(output_pdf_path)


if __name__ == "__main__":
    main()
