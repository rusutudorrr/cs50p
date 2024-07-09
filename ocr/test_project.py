import os
import pytest
from PIL import Image
from unittest.mock import patch
from project import is_image_file, preprocess_image, extract_text


@pytest.mark.parametrize("filename, expected", [
    ("test.jpg", True),
    ("test.jpeg", True),
    ("test.png", True),
    ("test.pdf", False),
    ("test.docx", False),
    ("test.JPG", True),  # test case insensitivity
    ("test.JPEG", True),
    ("test.PNG", True),
    ("test.PDF", False),
    ("test.DOCX", False),
    ("", False),  # test an empty string
    ("test", False),  # test no extension
    ("test.txt", False)  # testing an unsupported but common file type
])
def test_is_image_file(filename, expected):
    assert is_image_file(filename) == expected


# fixture to create and delete test images
@pytest.fixture(params=[("test_image.jpg", (100, 100), "RGB"),
                        ("test_image_grayscale.jpg", (50, 50), "L"),
                        ("test_image_small.jpg", (25, 25), "RGB")])
def test_image(request):
    # create working images
    filename, size, mode = request.param
    test_image = Image.new(mode, size, "white")
    test_image.save(filename)

    yield filename, test_image

    # delete image after usage for testing purposes
    os.remove(filename)
    test_image.close()


def test_preprocess_image(test_image):
    image_path, _ = test_image
    processed_image = preprocess_image(image_path)

    assert isinstance(processed_image, Image.Image)
    assert processed_image.mode == 'L' # check if img is grayscale



@pytest.mark.parametrize("file_name, expected_output", [
    ("test.jpg", "Extracted Image Text"),
    ("test.png", "Different Extracted Text"),
])
@patch('project.extract_text_from_image')
def test_extract_text_from_image_file(mock_extract_text_from_image, file_name, expected_output):
    mock_extract_text_from_image.return_value = expected_output

    assert extract_text(file_name) == expected_output
