from docx2pdf import convert

def word_to_pdf(input_path, output_path=None):
    """
    Converts a Word file to PDF.
    
    input_path: path to .docx file
    output_path: optional output PDF path or folder
    """
    convert(input_path, output_path)


# Convert single file
word_to_pdf("Panopticon.docx")



