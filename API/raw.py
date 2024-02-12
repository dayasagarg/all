import requests
from datetime import datetime

autoDebitFailedAPI = requests.get(
    "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-10T10:00:00.000Z&end_date=2024-02-11T10:00:00.000Z&status=4&page=1&skipPageLimit=true")

autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]

emiRepaymentStatus = requests.get(
    "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2024-02-10T10:00:00.000Z&endDate=2024-02-11T10:00:00.000Z&type=TOTAL&page=1&download=true")

emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]



emi_aut_status = []
emi_ers_status = []


emi_date_miss_match_aut_ers = []

for aut in autoDebitData:
    if aut["Today's EMI status"] != "FAILED":


        emi_aut_status.append(aut["Loan ID"])

for ers in emiRepaymentStatus_data:
    if ers["Loan ID"]:
        emi_ers_status.append(ers["Loan ID"])

emiDate = []

# https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails?loanId=685459
# for o in emi_ers_status:
#     emi = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
#                        params={"loanId": o, "encoding": 'utf-8', "errors": 'ignore'})
#     emiD = emi.json()["data"]["EMIData"]
#     print(emiD)

for o in emi_ers_status:
    emi = requests.get("https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails",
                       params={"loanId": o, "encoding": 'utf-8', "errors": 'ignore'})
    emiD = emi.json()["data"]
    print(emiD)