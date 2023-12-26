import requests
import json
import math

# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []


class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm, i, emiData
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-12-06T10:00:00.000Z&end_date=2023-12-08T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
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

        fullpay = []
        withoutFullpay = []
        match = []
        miss = []

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
                if (td["type"] == "FULLPAY") or (td["status"] == "COMPLETED"):
                    fullpay.append(i)
                # if (td["type"] == "FULLPAY") or (td["status"] == "COMPLETED"):
                #     fullpay.append(i)

                else:
                    withoutFullpay.append(i)




        # for full in fullpay:
        #     response2 = requests.get(
        #         "https://lendittfinserve.com/prod/admin/loan/getEMIRepaymentDetails", params={"loanId": full},
        #         verify=False)  # current date
        #
        #     emiData = response2.json()["data"]["EMIData"]
        #
        #     for td in emiData:
        #         if td["Status"] == "Unpaid":
        #             match.append(i)
        #
        #         else:
        #             miss.append(i)
        #         break
        #     break

        # print("match::", match)
        # print("miss::", miss)
        # print("fullpay",fullpay)


