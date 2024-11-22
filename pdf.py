from PyPDF2 import PdfReader
from PIL import Image, ImageDraw, ImageFont

pdf_path = "/mnt/data/978-3-658-06363-4.pdf"
reader = PdfReader(pdf_path)

page_number = 307  # Page 308 in document, index 307 in Python

page_text = reader.pages[page_number].extract_text()
quote = "In großen Einheiten lassen sich repräsentative Demokratien effizienter organisieren, da komplexe Entscheidungen delegiert werden können."

if quote in page_text:
    # Define the screenshot page location
    screenshot_path = "/mnt/data/Screenshot_Page_308.png"

    image = Image.new("RGB", (800, 1000), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
  # Write the text line by line
    y = 20
    for line in page_text.split("\n"):
        if quote in line:
            # Highlight the line containing the quote
            draw.rectangle([(10, y - 2), (780, y + 12)], fill="yellow")
        draw.text((10, y), line, fill="black", font=font)
        y += 15

    # Save the image with the highlighted quote
    image.save(screenshot_path)
    screenshot_path
else:
    print ("The quote was not found on the specified page.")
