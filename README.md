# PDF Generator & Merger 📖🗞️

**Create beautiful PDFs and merge documents effortlessly!**

## 💻 Prerequisites

🧩 **Python 3.6+** - [Download Python](https://www.python.org/downloads/)
📦 **Required Packages** - Install using:
```bash
pip install -r requirements.txt
```

## 🛠️ wkhtmltopdf Installation (Windows)
1. 📥 Download installer from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
2. 📁 Run installer **using default settings**
3. 📍 Add to PATH:
   - Right-click Start > System > Advanced system settings
   - Environment Variables > Path > Edit > Add:
   ```
   C:\Program Files\wkhtmltopdf\bin
   ```
4. 🂯 Verify installation in Command Prompt:
```bash
wkhtmltopdf --version
```

## 🎨 Using the Tool

### 🌟 Generate Stylish PDF
```bash
python main.py
```
📝 Choose option 1 and follow prompts!
- Creates modern, formatted PDFs
- Automatic saving as `generated_pdf.pdf`

### 🔭 Merge PDF Files
```bash
python main.py
```
📝 Choose option 2 and:
1. Enter filenames separated by spaces
   ```
   file1.pdf file2.pdf document.docx
   ```
2. Find merged PDF as `super_merged.pdf`

## 🚨 Troubleshooting

🔴 **"Could not find wkhtmltopdf"**
- Verify PATH configuration
- Reinstall wkhtmltopdf if needed

🔴 **File Not Found Errors**
- Keep files in same directory
- Use exact filenames with extensions

🔴 **Formatting Issues**
- Avoid special characters in content
- Use simple text formatting

---
🎉 **Happy Document Creating!** Need help? [Email support](leviathan_rohit@proton.me)

## Rohit Sharma
leviathan_rohit@proton.me
<!-- Created By Rohit Sharma -->
