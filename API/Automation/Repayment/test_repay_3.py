import pytest
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

    def test_using_per_loan_id_ontime_user(self):

        global emiDataTotalReceived, totalTransAmt, j

        emiDataTotalReceived = []
        ontime_emi_lid = []

        for n,i in enumerate(lIDs):
            # if n == 5:
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
            # if n == 5:
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


        if len(emiDataTotalReceived) == len(totalTransAmt_n):
            differences = []  # Initialize an empty list to store the differences

            # Iterate through the lists and calculate the differences
            for i in range(len(emiDataTotalReceived)):
                diff = emiDataTotalReceived[i] - totalTransAmt_n[i]
                differences.append(diff)

            print(
                f"Differences between corresponding elements between total receivable in EMI and Paid amount in transaction for ontime users:",
                differences)

            for o in differences:
                if o > 0:
                    print(f"difference more than 0 found in between EMI and Transaction for ontime users::",o)
                    assert False, "difference more than 0 found in between EMI and Transaction for ontime users"
                else:
                    print("*** No difference in EMI and transaction amount for ontime users ***")

        else:
            print("Error: Lists have different lengths for ontime users.")


        # print("totalTransAmt::",totalTransAmt)
        print("totalTransAmt_n::", totalTransAmt_n)

        print("emiDataTotalReceived::", emiDataTotalReceived)
        print("ontime_emi_lid::", ontime_emi_lid)



    def test_using_per_loan_id_except_ontime_user(self):

        global emiDataTotalReceived_eo, totalTransAmt_eo

        emiDataTotalReceived_eo = []
        emi_lid_eo = []

        for m,k in enumerate(lIDs):
            # if m == 5:
            #     break

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": k},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            data = response.json()["data"]
            # print(emiData)

            if data['loanStatus'] != 'OnTime':
                emi_lid_eo.append(k)

                emiData = data["EMIData"]

                if data["totalReceived"]:
                    emiDataTotalReceived_eo.append(data["totalReceived"])




        totalTransAmt_n_eo = []
        for n,l in enumerate(emi_lid_eo):
            # if n == 5:
            #     break

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": l},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            transData = response.json()["data"]

            trans_amt_eo = []
            for t in transData:
                if t["Status"] == "COMPLETED":

                    if t["Repay Amount"]:
                        trans_amt_eo.append(t["Repay Amount"])

            totalTransAmt_eo = sum(trans_amt_eo)

            if totalTransAmt_eo:
                totalTransAmt_n_eo.append(totalTransAmt_eo)



        # print("totalTransAmt_eo::",totalTransAmt_eo)
        print("totalTransAmt_n_eo::", totalTransAmt_n_eo)


        print("emiDataTotalReceived_eo::", emiDataTotalReceived_eo)
        print("emi_lid_eo::",emi_lid_eo)

        if len(emiDataTotalReceived_eo) == len(totalTransAmt_n_eo):
            differences_eo = []  # Initialize an empty list to store the differences

            # Iterate through the lists and calculate the differences
            for o in range(len(emiDataTotalReceived_eo)):
                diff_eo = emiDataTotalReceived_eo[o] - totalTransAmt_n_eo[o]
                differences_eo.append(diff_eo)

            print(
                f"Differences between corresponding elements between total receivable in EMI and Paid amount in transaction other than ontime users:",
                differences_eo)

            for d in differences_eo:
                if d > 0:
                    print(f"Error::difference more than 0 found in between EMI and Transaction on total amount except ontime users::",d)
                    assert False, "difference more than 0 found in between EMI and Transaction on total amount except ontime users"
                else:
                    print("*** No difference found for EMI and transaction on total amount except ontime users ***")

        else:
            print("Error: Lists have different lengths other than ontime users.")

