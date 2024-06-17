import requests
import json
import math

# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []


class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-12-06T10:00:00.000Z&end_date=2023-12-06T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment '''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)
        match = []
        missMatch = []
        for lid in loanIDs:

            if "Loan id":
                if lid["Loan id"] not in lIDs:

                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass

        # print("unique lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        match = []
        missMatch = []
        # Upcoming EMI
        for i in lIDs:

            response = requests.get(
                "https://lendittfinserve.com/prod/admin/loan/getEMIRepaymentDetails", params={"loanId": i},
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
            # print(emiData)

            # EMI Data
            paymentType = []
            status = []

            # for eD in emiData:
            #     if "Payment type" in eD:
            #         paymentType.append(eD['Payment type'])
            #         # print(i['EMI date'])
            #
            #     if "Paid" in eD:
            #         status.append(eD['Paid'])
            #
            #     if (eD["Payment type"] == "FULLPAY") and (eD["Status"] == "Paid"):
            #         match.append(i)
            #
            #     else:
            #         missMatch.append(i)





            # print('EMI DATA:>','emiDate::',emiDateE,'emiAmount::',emiAmountE,'principalAmount::',principalAmountE,'interestAmount::',interestAmountE,'penaltyDays::',penaltyDaysE,'penaltyAmount::',penaltyAmountE,'totalPaidAmount::',totalPaidAmountE,'paidPenaltyAmount::',paidPenaltyAmountE,'totalUnpaidAmount::',totalUnpaidAmountE,'UnpaidEMIAmount::',UnpaidEMIAmountE,'UnpaidPenaltyAmount::',UnpaidPenaltyAmountE)

            # print("totalPaidAmountE::",sum(totalPaidAmountE))
            # print("emiAmountE::", sum(emiAmountE))
            # print("totalUnpaidAmountE::", sum(totalUnpaidAmountE))

            '''getting transactionData data of Repayment'''
            tranData = response.json()["data"]["transactionData"]
            # print(tranData)

            # Transaction data
            tPaidAmount = []
            tPrincipalAmount = []
            tPrincipalDifference = []
            tInterestAmount = []
            tInterestDifference = []
            tPenaltyAmount = []

            tPenaltyDifference = []

            for td in tranData:
                if (td["status"] == "COMPLETED") and (td["type"] == "FULLPAY"):
                    match.append(i)

                else:
                    missMatch.append(i)

        print("match::", match)
        print("missMatch::", missMatch)
