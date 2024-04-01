import requests
import json
import math
from datetime import datetime

# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []

currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format


# print("currentDateStr::",currentDateStr)
#
class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm, fullPay_unpaid_misssMatch
        responseAllLoanID = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{currentDateStr}T10:00:00.000Z", "end_date": f"{currentDateStr}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)

        for lid in loanIDs:

            if "Loan id":
                if lid["Loan id"] not in lIDs:

                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass
#
#

    def test_using_per_loan_id(self):

        global emiDataTotalReceived, totalTransAmt, j

        emiDataTotalReceived = []
        ontime_emi_lid = []

        for n,i in enumerate(lIDs):
            # if n == 15:
            #     break

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            data = response.json()["data"]
            # print(emiData)

            if data['loanStatus'] == 'OnTime':
                ontime_emi_lid.append(i)
                emiData = data["EMIData"]

                if data["totalReceived"]:
                    emiDataTotalReceived.append(data["totalReceived"])




        totalTransAmt_n = []
        for n,j in enumerate(ontime_emi_lid):
            # if n == 15:
            #     break

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": j},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            transData = response.json()["data"]

            trans_amt = []
            for t in transData:
                if t["Status"] == "COMPLETED":

                    if t["Repay Amount"]:
                        trans_amt.append(t["Repay Amount"])


            # print("totalTransAmt::",sum(trans_amt))
            # print("loanID_trans::",j)

            totalTransAmt = sum(trans_amt)

            if totalTransAmt:
                totalTransAmt_n.append(totalTransAmt)



        # print("totalTransAmt::",totalTransAmt)
        print("totalTransAmt_n::", totalTransAmt_n)


        print("emiDataTotalReceived::", emiDataTotalReceived)
        print("ontime_emi_lid::",ontime_emi_lid)

        if len(emiDataTotalReceived) == len(totalTransAmt_n):
            differences = []  # Initialize an empty list to store the differences

            # Iterate through the lists and calculate the differences
            for i in range(len(emiDataTotalReceived)):
                diff = emiDataTotalReceived[i] - totalTransAmt_n[i]
                differences.append(diff)

                if diff > 0:
                    print(f"difference more than 0 found in between EMI and Transaction::",diff)
                    assert False, "difference more than 0 found in between EMI and Transaction"
                else:
                    print("*** No difference in EMI and transaction amount ***")


            # Print or use the list of differences as needed
            print(f"Differences between corresponding elements between total receivable in EMI and Paid amount in transaction:",differences)

        else:
            print("Error: Lists have different lengths.")

