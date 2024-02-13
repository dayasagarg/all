import requests
import json
import math
from datetime import datetime
# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []

currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
print("currentDateStr::",currentDateStr)

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

            if "Loan id":
                if lid["Loan id"] not in lIDs:

                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass



        print("unique lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        missMatchOfPaid = []
        missMatchOfUnpaid = []
        # Upcoming EMI

        url = "https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails"
        data = lIDs


    response = requests.get("https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails",data=data,
        verify=False)  # current date

    print(response.status_code)



