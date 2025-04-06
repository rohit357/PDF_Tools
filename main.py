from pypdf import PdfWriter  
import pdfkit

# Create a PDF merger object
merger = PdfWriter()

# Path to wkhtmltopdf.exe (download and install if not already)
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


# PDF Generator---------------------------------------------------------------------------------------------------------
# Ask user for content
def gen_pdf():
    title = input("Enter a title for your PDF page: ")
    body_content = input("Paste your content here: ")

    # HTML Template (with styling like a modern webpage)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 40px;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                background: #fff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #007BFF;
                text-align: center;
            }}
            p {{
                font-size: 16px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            <p>{body_content}</p>
        </div>
    </body>
    </html>
    """

    # Generate PDF
    pdfkit.from_string(html, "generated_pdf.pdf", configuration=config)

    print("✅ Stylish PDF generated successfully: generated_pdf.pdf")
# ----------------------------------------------------------------------------------------


# PDF Merger-------------------------------------------------------------------------------------------------------------
def merge():
    ls = input("Enter names separated by spaces:\n").split()

    for pdf in ls:
        merger.append(pdf)

    # Merge pdf

    merger.write("super_merged.pdf")

    merger.close()

    print("✅ PDFs merged successfully: super_merged.pdf")

# ----------------------------------------------------------------------------------------------------------------------------
# run the program

def main():
    while True:
        print("1. Generate PDF")
        print("2. Merge PDFs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            gen_pdf()
        elif choice == '2':
            merge()
        elif choice == '3':
            break


if __name__ == "__main__":
    main()

# Created By Rohit Sharma
# -----------------------------------------------------------------------------------------------------------------------------
