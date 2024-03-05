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

class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm, fullPay_unpaid_misssMatch
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
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

        print("unique lids::", lIDs)
        # print('count of unique lids::', len(lIDs))

        missMatchOfPaid = []
        missMatchOfUnpaid = []

        # Upcoming EMI

        url = "https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails"
        # print(lIDs)

        data = {"loanIds": lIDs}

        headers = {"qa-test-key": "28947f203896ea859233415d1904c927098484d2"}

        response = requests.post(url, headers=headers, json=data, verify=False)  # current date
        response_data = response.json()["data"]


        totalPaidAmount_mismatch = []
        fullPay_unpaid_misssMatch = []

        for r in response_data:
            loanData = response_data[r]

            emiDetails = loanData['emiDetails']["EMIData"]
            tranDetails = loanData["transactions"]
            # print("emiDetails::",emiDetails)

            emiPaid = []
            emiPenalty = []
            emiBounce = []
            for emi in emiDetails:
                if emi["status"] == "PAID":
                    if "emiAmount" in emi:
                        emiPaid.append(emi["emiAmount"])

                    if emi["paidPenalty"]:
                        emiPenalty.append(emi["paidPenalty"])

                    if emi["bounceCharge"]:
                        emiPenalty.append(emi["bounceCharge"])

            # print("emiPaid::",emiPaid)
            # print("emiPenalty::", emiPenalty)

            totalPaidEMI = sum(emiPaid) + sum(emiPenalty) + sum(emiBounce)
            # print("totalPaidEMI::",totalPaidEMI)

            TransPaidAmt = []
            for tr in tranDetails:
                if tr["paidAmount"]:
                    TransPaidAmt.append(round(tr["paidAmount"], 0))

            totalTransAmt = sum(TransPaidAmt)
            # print("totalTransAmt::", totalTransAmt)

            if totalPaidEMI != totalTransAmt:
                totalPaidAmount_mismatch.append(r)

            diffPaidAmt = totalPaidEMI - totalTransAmt

            print(f"difference of PaidAmt in emi and paidAmt in trans::lid::{r}::",diffPaidAmt)
    #

        # print("totalPaidAmount_mismatch::", totalPaidAmount_mismatch)




        if len(totalPaidAmount_mismatch) > 0:
            print(f"totalPaidAmount_mismatch found in repayment::{totalPaidAmount_mismatch}")
            assert False
        else:
            print("No totalPaidAmount_mismatch found in repayment")

        assert len(totalPaidAmount_mismatch) > 0, "totalPaidAmount_mismatch found in repayment"


    #
    def test_fullpay_unpaid(self):

        if len(fullPay_unpaid_misssMatch) > 0:
            print(f"fullPay_unpaid_misssMatch found in repayment::{fullPay_unpaid_misssMatch}")
            assert False, "fullPay_unpaid_misssMatch found in repayment"
        else:
            print("No fullPay_unpaid_misssMatch found in repayment")


    # def test_using_per_loan_id(self):
    #     for i in lIDs:
    #         response = requests.get(
    #             "https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i},
    #             verify=False)  # current date
    #
    #         print('status code of get Repayment::', response.status_code)
            # print(response.json())
