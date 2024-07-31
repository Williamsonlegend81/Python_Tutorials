from pypdf import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
files.sort()

for pdf in files:
    merger.append(pdf)

merger.write("final.pdf")
merger.close()