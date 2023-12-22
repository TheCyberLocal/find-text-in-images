"""
This script is a practical demonstration of OCR capabilities using easyocr.
It is designed to read and analyze text from images, which can be useful in various applications such as data entry automation, 
 digitizing documents, or image-based translation services.
The loop processes a series of images, showcasing the library's ability to handle multiple files efficiently.
"""

import easyocr  # Import the easyocr library for Optical Character Recognition (OCR).

# Initialize the OCR reader for English language.
reader = easyocr.Reader(['en'])  # 'en' specifies English; you can choose other languages like 'ch_sim', 'ch_tra', etc.

# Loop to process multiple images.
for i in range(0, 3):
    results = reader.readtext(f'images{i}.png')  # Read text from each image.

    # Initialize empty strings to store the results.
    position = ''
    text = ''
    probability = ''

    # Iterate through results and concatenate the position, text, and probability.
    for result in results:
        position += str(result[0]) + ' '  # Append the position of the text in the image.
        text += str(result[1]) + ' '  # Append the recognized text.
        probability += str(result[2]) + ' '  # Append the probability/confidence level of the recognition.

    # Print the results.
    print(position)  # Print positions of text.
    print(text)  # Print recognized texts.
    print(probability)  # Print probabilities for each recognized text.
