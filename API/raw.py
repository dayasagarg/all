import requests
from datetime import datetime

# response = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
#                         params={"loanId": 735576, "verify": "False"})


# response = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": 735576,"verify":"False"})  # current date


# print(response.json())
currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d")

responseAllLoanID = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans", params={"start_date":f"{currentDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","page":1,"pagesize":10,"getTotal":"true","download":"true",
            "verify":"False"})  # current date

'''getting loan ids from Repayment'''
loanIDs = responseAllLoanID.json()["data"]["rows"]
# print(loanIDs)
lIDs = []
for lid in loanIDs:

    if lid["Loan id"] not in lIDs:

        lIDs.append(lid["Loan id"])
        # print(i["Loan id"])

    else:
        pass



# print("unique lids::", lIDs)
# print('count of unique lids::', len(lIDs))


# Upcoming EMI
for i in lIDs:

    response = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i,"verify":"False"})  # current date
    print(response.json())
#
