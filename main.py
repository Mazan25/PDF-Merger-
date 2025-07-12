import PyPDF2 # type: ignore
import os

def merge_pdfs(pdf_list, output_name):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")
    
    merger.write(output_name)
    merger.close()
    print(f"PDFs merged into '{output_name}' successfully.")

if __name__ == "__main__":
    # List your PDFs here
    pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # Change to your actual file names
    output_file = 'merged_output.pdf'
    
    merge_pdfs(pdf_files, output_file)
