import requests
import pytest


class TestPost:

    @pytest.fixture
    def url(self):
        global url_uat, url_prod
        url_uat = "http://144.24.112.239/bankingpro/statement/extractData"              # API URL
        url_prod = "http://lendittfinserve.com/bankingpro/statement/extractData"

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
    def test_post_R_standard_charterd_3(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\AutomationL\BankStatement\bank_statements\Standard Chartered.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "STANDARD_CHARTERED"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    #
    #
    def test_post_R_HDFC_4(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\hdfc.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "HDFC"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True
    #
    #

    def test_post_R_SBI_5(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\sbi.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "SBI"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True
    #
    #
    def test_postFedcS6(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\AutomationL\BankStatement\bank_statements\LaterAdded\federal bank\federal bank\CustomAccountStatementTpr05-01-2024 (2).pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "FEDERAL"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True
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
    def test_post_R_IDFC_8(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\idfc.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "IDFC"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True


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
    # def test_postIDFCES10(self,url):
    #
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

    def test_post_R_canara_11(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\canara.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "CANARA"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    def test_post_R_IDBI_12(self, url):
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\idbi.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "IDBI"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

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



    # def test_postUnion_c_16(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\23-02-2024\bank\union bank.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "UNION_BANK"}
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
    def test_postKotak_c_17(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\kotak.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "KOTAK"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True


    def test_postPNB_c_18(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\statements_tanish\pnb.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "PNB"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    def test_post_BOB_c_18(self,url):

        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\AutomationL\BankStatement\bank_statements\LaterAdded\bob\OpTransactionHistoryLstNTxnUX503-01-2024 (2).pdf"
        files = {"pdfFile": open(pdfFile, "rb")}

        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "BANK_OF_BARODA"}

        response = requests.post(url_prod, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True

    #
    # def test_postICICI_c_19(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\27-02-2024\ICICI_Bank.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "ICICI"}
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
    # def test_postIndusind_c_20(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\27-02-2024\IndusInd_bank.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "INDUSIND"}
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
    # def test_postHSBC_c_21(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\HSBC.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "HSBC"}
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
    # def test_post_DBS_c_22(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\2023\bank_statements\dbs.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "DBS"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True









