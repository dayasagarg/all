import requests
from datetime import datetime,timedelta

import json
import math

lIDs = []
f_lid = []


currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d")
print("currentDateStr::",currentDateStr)



previousDate = currentDateF - timedelta(days=4)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")


class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans", params={"start_date":f"{previousDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","page":1,"pagesize":10,"getTotal":"true","download":"true",
            "verify":"False"})  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)
        match = []
        missMatch = []
        for lid in loanIDs:

            if lid["Loan id"] not in lIDs:

                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])

            else:
                pass

        # print("unique lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        unpaid = []
        withoutUnpaid = []
        # Upcoming EMI
        for i in lIDs:

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())
            sData = response.json()
            # jdata = json.dumps(sData,indent=2)
            # print(jdata)

            # print(response.headers)
            # print(response.content)

            '''getting EMIData data of Repayment '''
            emiData = response.json()["data"]["EMIData"]
            print(emiData)

            # EMI Data
            paymentType = []
            status = []

            for eD in emiData:
                # if "Payment type" in eD:
                #     paymentType.append(eD['Payment type'])
                #     # print(i['EMI date'])
                #
                # if "Paid" in eD:
                #     status.append(eD['Paid'])

                if ((eD["paymentType"] == "FULLPAY") and (eD["status"] == "UNPAID")) or ((eD["paymentType"] == "EMIPAY") and (eD["status"] == "UNPAID")):
                    unpaid.append(i)

                else:
                    withoutUnpaid.append(i)



            '''getting transactionData of Repayment'''
            # tranData = response.json()["data"]["transactionData"]
            # print(tranData)

            # Transaction data
            # tPaidAmount = []
            # tPrincipalAmount = []
            # tPrincipalDifference = []
            # tInterestAmount = []
            # tInterestDifference = []
            # tPenaltyAmount = []
            #
            # tPenaltyDifference = []


            # for td in tranData:
            #     if (td["status"] == "COMPLETED") and (td["type"] == "FULLPAY") or ((td["status"] == "INITIALIZED") and (td["type"] == "EMIPAY")):
            #         match.append(i)
            #
            #     else:
            #         missMatch.append(i)

        # print("match::", match)
        # print("missMatch::", missMatch)

        print("unpaid::", unpaid)
        print("withoutUnpaid::", withoutUnpaid)

        if len(unpaid) == 0:
            print("No unpaid found")
        else:
            print("unpaid found")

        assert len(unpaid) == 0


