# importing all the required modules
import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader(r"C:\Users\lendi\OneDrive\Desktop\1688312573612.pdf")

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())

first_page = reader.pages[0].extract_text()

assert first_page['Loan Amount'] in 41,500.00