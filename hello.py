from docx import Document
from docx.shared import Inches
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image

def convert_docx_to_pdf(docx_path, pdf_path):
    # Read the docx file
    doc = Document(docx_path)
    
    # Create a BytesIO object to store the resulting PDF
    pdf_buffer = BytesIO()
    
    # Create a PDF document with reportlab
    pdf = SimpleDocTemplate(pdf_buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()

    flowables = []
    
    for element in doc.paragraphs:
        # Handle text paragraphs
        text = element.text
        p = Paragraph(text, styles["Normal"])
        flowables.append(p)
        
    # Images are handled differently, they are not directly in the document body
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            try:
                image_data = rel.target_part.blob
                image_path = "temp_image.png"
                with open(image_path, 'wb') as img:
                    img.write(image_data)
                img = Image(image_path)
                flowables.append(img)
            except ValueError:
                pass  # Skip images with external relationships
    
    pdf.build(flowables)
    
    # Save the PDF to the specified
    with open(pdf_path, "wb") as f:
        f.write(pdf_buffer.getvalue())

# Path to the input docx file
docx_file = "CERTIFICADO_DEUDA_AL_DIA_1.docx"

# Path to the output pdf file
pdf_file = "file.pdf"

# Convert the docx file to the pdf file
convert_docx_to_pdf(docx_file, pdf_file)
