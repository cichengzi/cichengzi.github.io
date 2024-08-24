from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = 'featured.pdf'

# Convert PDF to a list of PIL images
images = convert_from_path(pdf_path)

# Save each page as a PNG file
for i, image in enumerate(images):
    image.save(f'page_{i + 1}.png', 'PNG')

