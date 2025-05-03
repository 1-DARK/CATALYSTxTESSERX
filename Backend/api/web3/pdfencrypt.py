from pypdf import PdfReader, PdfWriter
from pathlib import Path

current_dir = Path(__file__).resolve()
parent_dir = current_dir.parents[2]

class EncryptPdf:
    def encrypt(self, pdfname):
        reader = PdfReader(f"{parent_dir}/media/pdfs/{pdfname}")
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.encrypt("pass")

        encrypt_pdf_loc = f"{parent_dir}/media/pdfs/{pdfname}"
        with open(f"{parent_dir}/media/pdfs/{pdfname}", "wb") as f:
            writer.write(f) 
        
        return encrypt_pdf_loc
