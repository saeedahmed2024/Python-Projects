from pypdf import PdfWriter

merger = PdfWriter()

pdfs = ["4 semester past.pdf", "4th semester papers 2021 batch.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("4th sem_past_papers_combined.pdf")
merger.close()
