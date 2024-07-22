from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    pdf_list = ['file1.pdf', 'file2.pdf']
    output_path = 'merged_output.pdf'
    merge_pdfs(pdf_list, output_path)
    print("PDFs merged successfully.")

if __name__ == "__main__":
    main()
