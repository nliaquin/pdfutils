#!/bin/python

import argparse
import sys
from pypdf import PdfReader, PdfWriter

def parse_arguments():
    parser = argparse.ArgumentParser(description="PFD Manipulation Utilities")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    remove_parser = subparsers.add_parser("remove", help="Remove pages from a PDF")
    remove_parser.add_argument("input_pdf", type=str, help="Path to the input PDF file")
    remove_parser.add_argument("output_pdf", type=str, help="Path to the output PDF file")
    remove_parser.add_argument("pages", type=int, nargs="+", help="Page numbers to remove (0-indexed)")

    insert_parser = subparsers.add_parser("insert", help="Inserts all pages from one PDF to another")
    insert_parser.add_argument("source_pdf", type=str, help="Path to the source PDF file")
    insert_parser.add_argument("target_pdf", type=str, help="Path to the target PDF file")
    insert_parser.add_argument("output_pdf", type=str, help="Path to the output PDF file")
    insert_parser.add_argument("page_index", type=int, help="Index at which to insert the pages in the target pdf (0-indexed)")

    return parser.parse_args()

def remove_pages(input_pdf, output_pdf, pages):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        if i not in pages:
            writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as f:
        writer.write(f)

def insert_pages(source_pdf, target_pdf, output_pdf, page_index):
    source_reader = PdfReader(source_pdf)
    target_reader = PdfReader(target_pdf)
    writer = PdfWriter()

    for i in range(page_index):
        writer.add_page(target_reader.pages[i])

    for page in source_reader.pages:
        writer.add_page(page)

    for i in range(page_index, len(target_reader.pages)):
        writer.add_page(target_reader.pages[i])

    with open(output_pdf, "wb") as f:
        writer.write(f)


def main():
    args = parse_arguments()

    if args.command == "remove":
        remove_pages(args.input_pdf, args.output_pdf, args.pages)
    elif args.command == "insert":
        insert_pages(args.source_pdf, args.target_pdf, args.output_pdf, args.page_index)


if __name__ == "__main__":
    main()
