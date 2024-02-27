import requests
import pytest


class TestPost:

    # def test_postWBcS1(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\netBanking_name change (1).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "STANDARD_CHARTERED"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('valid::',response.json()['valid'])
    #     print('message::', response.json()['message'])
    #     print('errorCode::', response.json()['errorCode'])
    #     # print('valid::', response.json())
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    #
    # def test_postWBcS2(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\netBanking_name change (1).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "SBI"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('valid::', response.json()['valid'])
    #     print('message::', response.json()['message'])
    #     print('errorCode::', response.json()['errorCode'])
    #     # print('valid::', response.json())
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    #
    # def test_postRBcS3(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\Standard Chartered.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "STANDARD_CHARTERED"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    #
    #
    # def test_postRBcS4(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\HDFC Statement.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "HDFC"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    #
    #
    # def test_postRBcS5(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\SBI Statement.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "SBI"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    #
    # def test_postFedcS6(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\federal bank\federal bank\CustomAccountStatementTpr05-01-2024 (2).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "FEDERAL"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    #
    # def test_postFedES7(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\federal bank\federal bank\EDITED 1.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "FEDERAL"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    # def test_postIDFCcS8(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\IDFC\IDFC\App.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "IDFC"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    # def test_postIDFCES9(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\IDFC\IDFC\edited 1.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "IDFC"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    # def test_postIDFCES10(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\RBL bank\RBL bank\AccountStatement02-01-2023 To 30-06-2023 (1).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "RBL"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    # def test_postIDFCES11(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\RBL bank\RBL bank\edit.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "RBL"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    #
    #
    #
    #
    # def test_postIDFCES12(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\yes bank\yes bank\Account_Statement_01_Apr_2023-04_Jan_2024.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "YES"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    # def test_postIDFCES13(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\yes bank\yes bank\Account_Statement_edit1.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "YES"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101
    #
    # def test_postIDFCES14(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\bob\OpTransactionHistoryLstNTxnUX503-01-2024 (2).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "BANK_OF_BARODA"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    # def test_postIDFCES15(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank statements\LaterAdded\EITED_City Union Bank 25kb (2).pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "CITY_UNION"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.json()['valid'] == False
    #     assert response.json()['message'] == 'Please download valid statement from the bank site'
    #     assert response.json()['errorCode'] == 101



    def test_postUnion_c_16(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\23-02-2024\bank\union bank.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "UNION_BANK"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True


    def test_postKotak_c_17(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\26-02-2024\kotak.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "KOTAK"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    def test_postPNB_c_18(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\26-02-2024\PNB.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "PNB"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    def test_postICICI_c_19(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\27-02-2024\ICICI_Bank.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "ICICI"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True


    def test_postIndusind_c_20(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\27-02-2024\IndusInd_bank.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "INDUSIND"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

