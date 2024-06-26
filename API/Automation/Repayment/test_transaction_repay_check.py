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

        # print("lIDs::",lIDs)


    def test_transa(self):
        currentFullTime_2 = datetime.now()  # whole date
        currentDateStr_2 = datetime.strftime(currentFullTime, "%d/%m/%Y")
        pre_time_1 = currentFullTime_2 - timedelta(days=1)
        pre_time_2 = currentFullTime_2 - timedelta(days=2)


        pre_time_1_str = datetime.strftime(pre_time_1,"%d/%m/%Y")
        pre_time_2_str = datetime.strftime(pre_time_2, "%d/%m/%Y")

        last_2_day_with_current = [currentDateStr_2,pre_time_2]
        # print("currentDateStr_2::",currentDateStr_2)

        global trans_amt, trans_prin, trans_int, trans_deffered, trans_penal, trans_fcc, trans_lc, trans_ecs
        totalTransAmt_n = []

        missMatchTransAmt = []
        transact_mismatch_lid = []
        diff_tran_3 = []

        for n,j in enumerate(lIDs):

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": j},
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
                    if t["Repaid date"] in last_2_day_with_current:

                        # if t["Repay Amount"]:
                        trans_amt = t["Repay amount"]
                            # trans_amt.append(t["Repay Amount"])

                        # if t["Principal"]:
                        trans_prin = t["Principal"]
    #                         trans_prin.append(t["Principal"])

                        # if t["Interest"]:
                        trans_int = t["Interest"]
    #                         trans_int.append(t["Interest"])


                        trans_deffered = t["Deferred interest"]
                        trans_penal = t["Penal charge"]
                        trans_fcc = t["For closure charge"]
                        trans_lc = t["Legal charge"]
                        trans_ecs = t["ECS charge"]

                        trans_amt_pert_f = trans_prin + trans_int + trans_deffered + trans_penal + trans_fcc + trans_lc + trans_ecs

                        diff_tran = trans_amt_pert_f - trans_amt
                        # print("diff_tran",diff_tran)
                        if diff_tran > 3 or diff_tran < -3:
                            diff_tran_3.append(j)

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
                            transact_mismatch_lid.append(j)



                            # assert False

                        else:
                            print(f"*** trans_amt is correct :: LID :: {j} ***")

                            # missMatchTransAmt.append(j)

        # print("transact_mismatch_lid::",transact_mismatch_lid)
        print("diff_tran_3::",diff_tran_3)

        if len(transact_mismatch_lid) > 0:
            print(f"Error:: transaction amount is not as per principal, interest and penalty::{set(transact_mismatch_lid)}")
            assert False
        else:
            print("*** transaction amount is as per principal, interest and penalty ***")


