import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import pypdf
from datetime import datetime
from datetime import timedelta
import json


file = open("inputData2.json")
info = json.load(file)
email = info["email"]
password = info["password"]
otp = info["otp"]
loanPdf = info["loanPdf"]

# print(email,password,otp,loanID,loanPdf)


# Folder Path
folder_path = r"C:\Users\lendi\OneDrive\Desktop\loan_pdf"

# List all files in the folder
files_in_folder = os.listdir(folder_path)
# print(files_in_folder)

# Filter for PDF files
pdf_files = [file for file in files_in_folder if file.endswith('.pdf')]
reader = pypdf.PdfReader(folder_path)

for i in reader:
    print(i)


# #001
# if pdf_files:
#     first_pdf_filename = pdf_files[0]
#     first_pdf_path = os.path.join(folder_path, first_pdf_filename)
#
#
#     # pdf reader
#     reader = pypdf.PdfReader(first_pdf_path)        # pdf file location
#     # reader = PyPDF2.PdfReader(loanPdf)               # pdf file location
#     firstPage = reader.pages[0].extract_text()
#     thirdPage = reader.pages[2].extract_text()
#     fourthPage = reader.pages[3].extract_text()
#     sixthPage = reader.pages[5].extract_text()
#     ninthPage = reader.pages[8].extract_text()
#
#     if 'Loan Id' in firstPage:
#         index1 = firstPage.index('Loan Id')
#         index2 = firstPage.index('LOAN DETAILS')
#         text = firstPage[index1 + 7:index2]
#         # print(f"loanID :: {text}")
#
#         loanID = "L-" + text
#
#
#
