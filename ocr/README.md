 # Optical Character Reader for Invoices
    #### Video Demo:  https://www.youtube.com/watch?v=9MpPo9W1fG0
    #### Description:
    This project is designed to extract text from PDFs and image files, making it convenient for users to access and copy text without having to manually transcribe it.

    For example, if you need to find a bank account number on a phone invoice, this tool will scan the document, extract all the text, and allow you to easily copy and paste the needed information. It's important to remember that the success of text extraction depends on the quality of the images used.

    Optical Character Recognition for Invoices is a system designed to process documents and images, extract text from them, and convert this text into a PDF format. This system is particularly useful for digitizing printed documents or converting image-based text into an editable and searchable format. The project is implemented in Python, utilizing libraries such as pytesseract, pdfplumber, PIL (Python Imaging Library), and FPDF.

    The core functionality of the project revolves around the main() function. This function orchestrates the OCR process by first extracting text from a specified input file, which can be either an image or a PDF, and then converting this extracted text into a PDF document. The system is designed to handle both image files (like PNG, JPG, JPEG) and PDFs, making it versatile in its application.

    The OCR process begins with the extract_text() function, which determines the type of the input file. If the file is an image, it calls extract_text_from_image(), where the image undergoes preprocessing to enhance its quality for better text extraction. This preprocessing includes converting the image to grayscale, binarizing it for better contrast, and enhancing its contrast. The preprocessed image is then fed into the Tesseract OCR engine (through pytesseract), configured to recognize Romanian language text (as indicated by the 'ron' language code).

    In the case of PDF files, the extract_text() function utilizes pdfplumber to open the PDF and iterate through its pages. For each page, it extracts textual content directly and also looks for embedded images. These images are then processed in a similar way to standalone image files, using Tesseract to extract text from them.

    After extracting the text, whether from an image or a PDF, the program proceeds to create a PDF document from this text using the FPDF library. The create_pdf_from_text() function adds a page to the PDF, sets the font, and writes the extracted text onto the page, handling character encoding issues gracefully.

    Throughout the process, the system provides feedback to the user via print statements, indicating the progress of the OCR process. There's also a use of sleep() to simulate processing time, which can be helpful in providing a more user-friendly experience, especially when dealing with larger files.

    The script includes utility functions like is_image_file() to check if a file is an image, and extract_image_from_page() to extract an image from a PDF page. These functions add to the robustness of the system, ensuring that various file types and formats can be handled efficiently.

    In summary, the project is a comprehensive OCR system capable of handling both images and PDFs, extracting text from them, and converting this text into a PDF format. It's a versatile tool that can be used in various scenarios, such as digitizing paperwork, archiving documents, or processing forms and invoices. The use of Python and its libraries makes the system portable and easy to integrate into other software solutions or workflows.
