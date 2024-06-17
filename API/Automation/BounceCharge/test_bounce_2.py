import requests
from datetime import datetime,timedelta


# emiTranAPI = requests.post("https://chinmayfinserve.com/admin-prod/admin/qa/bulkEMIDetails")


class TestBounce:
    def test_bounce_charg(self):
        currentFullTime = datetime.now()  # whole date
        currentDateStr = datetime.strftime(currentFullTime, "%d-%m-%Y")  # date to string format
        currentDateF = datetime.strptime(currentDateStr, "%d-%m-%Y")  # string to date format

        previousDate1 = currentDateF - timedelta(days=15)
        previousDateStr1 = datetime.strftime(previousDate1, "%d-%m-%Y")

        print(previousDateStr1)
        print(currentDateStr)

        allRepaidAPI = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2024-02-05T10:00:00.000Z&end_date=2024-02-06T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")   # end date < current date
        # print(allRepaidAPI.json())

        allRepaidData = allRepaidAPI.json()["data"]["rows"]
        # print(allRepaidData)
        bounceChMissed_LId = []
        allRepaid_loan_ids = []

        # "05-02-2024"
        for ar in allRepaidData:
            if ar["Delay days (as on today)"] > 0:
                allRepaid_loan_ids.append(ar["Loan id"])


                # print(ad)

        # print("allRepaid_loan_ids::",allRepaid_loan_ids)


        for e in allRepaid_loan_ids:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": e},verify=False)
            # print(emiAPI.json())
            emiAPI_data = emiAPI.json()["data"]["EMIData"]


            for ed in emiAPI_data:
                if ed["bounceCharge"] == 0:
                    bounceChMissed_LId.append(e)

        # bounceChMissed_LId_unique = []
        #
        # [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]

        print("bounceChMissed_LId::",bounceChMissed_LId)
        # print("bounceChMissed_LId_unique::", bounceChMissed_LId_unique)

