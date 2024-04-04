import pytest
import requests
import json
import math
from datetime import datetime, timedelta

# sample LIDs:430144,572277,532329




currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format

pre_3 = currentFullTime - timedelta(days=3)
pre_3_str = datetime.strftime(pre_3,"%Y-%m-%d")


# print("currentDateStr::",currentDateStr)
#
class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm, fullPay_unpaid_misssMatch, princ, interest, penalty, repaid, repaid_emi_trans_amt_f,loan_id,lIDs

        repaid_emi_trans_amt_f = 0

        responseAllLoanID = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{pre_3_str}T10:00:00.000Z", "end_date": f"{currentDateStr}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)

        miss_match_repay_in_trans_pert_emi = []
        # princ = []
        # interest = []
        # penalty = []

        repay_amt = []
        lIDs = []

        for lid in loanIDs:

            if lid["Loan id"] :
                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])


    def test_transa(self):
        currentFullTime_2 = datetime.now()  # whole date
        currentDateStr_2 = datetime.strftime(currentFullTime, "%d/%m/%Y")
        pre_time_1 = currentFullTime_2 - timedelta(days=1)
        pre_time_2 = currentFullTime_2 - timedelta(days=2)


        pre_time_1_str = datetime.strftime(pre_time_1,"%d/%m/%Y")
        pre_time_2_str = datetime.strftime(pre_time_2, "%d/%m/%Y")

        last_2_day_with_current = [currentDateStr_2]
        # print("currentDateStr_2::",currentDateStr_2)

        global trans_amt, trans_prin, trans_int, trans_penalty
        totalTransAmt_n = []

        missMatchTransAmt = []
        for n,j in enumerate(lIDs):
            if n == 45:
                break

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": j},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            transData = response.json()["data"]

            # trans_amt = []
            # trans_prin = []
            # trans_int = []
            # trans_penalty = []




            for t in transData:

                if t["Status"] == "COMPLETED":
                    if t["Repaid Date"] in last_2_day_with_current:

                        # if t["Repay Amount"]:
                        trans_amt = t["Repay Amount"]
                            # trans_amt.append(t["Repay Amount"])

                        # if t["Principal"]:
                        trans_prin = t["Principal"]
    #                         trans_prin.append(t["Principal"])

                        # if t["Interest"]:
                        trans_int = t["Interest"]
    #                         trans_int.append(t["Interest"])

                        # if t["Penalty"]:
                        trans_penalty = t["Penalty"]
    #                         trans_penalty.append(t["Penalty"])

                        trans_amt_pert_f = trans_prin + trans_int + trans_penalty
                        # print("trans_amt_pert_f::",trans_amt_pert_f)
                        # print("trans_amt::",trans_amt)
                        # print("trans_amt::",trans_amt)
                        # print("trans_prin::",trans_prin)
                        # print("trans_int::",trans_int)
                        # print("trans_penalty::",trans_penalty)
                        # print("trans_lid::", j)

                        if trans_amt_pert_f != trans_amt:
                            print("Error::trans_amt_pert_f not match with trans_amt trans_lid::", j)
                            print("trans_amt_pert_f::", trans_amt_pert_f)
                            print("trans_amt::",trans_amt)
                            # assert False

                        else:
                            print("*** trans_amt is correct ***")

                            # missMatchTransAmt.append(j)



