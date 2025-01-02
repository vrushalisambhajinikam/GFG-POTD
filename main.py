import fitz  # PyMuPDF

# Input and output file paths
input_pdf_path = "C:/Users/Vrushali/Downloads/250+DSA QUESTIONS FOR PLACEMENTS.pdf"
output_pdf_path = "C:/Users/Vrushali/Desktop/NewQnumberAdded.pdf"

# Initialization
question_number = 1

# Function to add numbers to questions
def add_question_numbers(text, question_number):
    lines = text.split("\n")
    numbered_lines = []

    for line in lines:
        # Identify lines that are likely questions
        if "- Link" in line or line.strip().startswith(".") or line.strip().startswith("Q."):
            numbered_lines.append(f"{question_number}. {line.strip()}")
            question_number += 1
        else:
            numbered_lines.append(line)

    return "\n".join(numbered_lines), question_number

# Open the input PDF
pdf_document = fitz.open(input_pdf_path)
new_pdf = fitz.open()  # Create a new PDF

# Process each page and add question numbers
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    text = page.get_text("text")  # Extract text from the page
    updated_text, question_number = add_question_numbers(text, question_number)

    # Create a new page in the output PDF
    new_page = new_pdf.new_page(width=page.rect.width, height=page.rect.height)
    new_page.insert_text(
        (72, 72),  # Start position (1 inch margin)
        updated_text,
        fontsize=10,
        color=(0, 0, 0),  # Black text
    )

# Save the updated PDF
new_pdf.save(output_pdf_path)
new_pdf.close()

print(f"Updated PDF saved to: {output_pdf_path}")
