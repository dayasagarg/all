import requests
import json
import math
from datetime import datetime
# sample LIDs:430144,572277,532329


# f_lid = []
lIDs = []

currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
# print("currentDateStr::",currentDateStr)

class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans", params={"start_date":f"{currentDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","page":1,"pagesize":10,"getTotal":"true","download":"true",
            "verify":"False"})  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)

        for lid in loanIDs:

            if lid["Loan id"] not in lIDs:

                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])

            else:
                pass



        # print("unique lids::", lIDs)
        # print('count of unique lids::', len(lIDs))

        missMatchOfPaid = []
        total_Receivable = []
        # Upcoming EMI
        for i in lIDs:

            response = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i,"verify":"False"})  # current date
            # print(response.json())
        #
            # print('status code of get Repayment::', response.status_code)

        #     sData = response.json()
        #     # jdata = json.dumps(sData,indent=2)
        #     # print(jdata)
        #     # print(response.headers)
        #     # print(response.content)
        #
            # '''getting EMIData data of Repayment '''
            emiData = response.json()["data"]["EMIData"]
            # print(emiData)



            # # EMI Data

            #
            #
            for eD in emiData:
                if "totalReceivable" in eD:
                    total_Receivable.append(eD['totalReceivable'])
                    # print(eD['totalReceivable'])
            #
            #     if "EMI amount" in eD:
            #         emiAmountE.append(eD['EMI amount'])
            #

                else:
                    print("error")
            #
            print("total_Receivable::",total_Receivable)

            #
            # '''getting transactionData data of Repayment'''
            # trans_response = requests.get("https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": i,"verify":"False"})
            # tranData = trans_response.json()["data"]
            # # print(tranData)
            #
            # # Transaction data
            repay_Amount = []


            #
            # for td in tranData:
            #     if td["Status"] == "COMPLETED":
            #
            #         if "Repay Amount" in td:
            #             repay_Amount.append(td['Repay Amount'])


            # diff_totalReceivable_repay_Amount = totalReceivable - repay_Amount

            # print("repay_Amount::",repay_Amount)
            # # print("diff_totalReceivable_repay_Amount::",diff_totalReceivable_repay_Amount)
            #
            # if total_Receivable == sum(repay_Amount):
            #     print(f"Total amount paid in EMI data is as per formula::Loan ID::{i}")
            # else:
            #     missMatchOfPaid.append(i)
            #     print(f"Error::Total amount paid in EMI data is not as per formula::Loan ID::{i}")



        #     print("***************************************************************************")
        #
        # print("missMatchOfPaid::", missMatchOfPaid)
        # print("missMatchOfUnpaid::", missMatchOfUnpaid)
        #
        #
