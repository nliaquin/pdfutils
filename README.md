# pdfutils
I got tired of premium programs to perform basic edits to PDF files, so I decided to make my own for free.

# Features added so far:
- insert pages from one PDF to another
- remove pages from a PDF

# Manual
PFD Manipulation Utilities

### positional arguments
  {remove,insert}  Commands
    remove         Remove pages from a PDF
    insert         Inserts all pages from one PDF to another

### remove
usage: python pdfutils.py remove [-h] input_pdf output_pdf pages [pages ...]

positional arguments:
  input_pdf   Path to the input PDF file (which file we are removing pages from)
  output_pdf  Path to the output PDF file (where to output the final results, as we do not directly edit source files as to prevent data loss)
  pages       Page numbers to remove (0-indexed)

### insert
usage: python pdfutils.py insert [-h] source_pdf target_pdf output_pdf page_index

positional arguments:
  source_pdf  Path to the source PDF file (where to copy all pages from)
  target_pdf  Path to the target PDF file (where to add pages from source)
  output_pdf  Path to the output PDF file (where to output the final results, as we do not edit any existing files directly for data loss prevention)
  page_index  Index at which to insert the pages in the target pdf (0-indexed)
