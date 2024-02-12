import requests
import json

# emiTranAPI = requests.post("https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails")

class TestBounce:


    def test_bounce_charg(self):

        allRepaidAPI = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2024-02-01T10:00:00.000Z&end_date=2024-02-02T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")
        # print(allRepaidAPI.json())

        allRepaidData = allRepaidAPI.json()["data"]["rows"]
        # print(allRepaidData)
        bounceChMissed_LId = []
        allRepaid_loan_ids = []

        for ar in allRepaidData:
            if ar["Delay days (as on today)"] > 0:

                if ar["Loan id"]:
                    allRepaid_loan_ids.append(ar["Loan id"])
                # print(ad)

        # print("allRepaid_loan_ids::",allRepaid_loan_ids)

        headers = {

            "qa-test-key": "28947f203896ea859233415d1904c927098484d2",
            "Content-Type": "application/json"
        }

        data = {"loanIds": allRepaid_loan_ids}
        url = "https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails"

        emiTranAPI = requests.post(url,headers=headers,data=json.dumps(data))
        emiTranAPIData = emiTranAPI.json()["data"]
        for i in emiTranAPIData:
            if i == 61646:

                print(i["emiDetails"])

        # for i in allRepaid_loan_ids:
        #     if i in emiTranAPI.json()["data"]:
        #         print(i)














        # for lid in allRepaid_loan_ids:
        #     if lid:
        #         ed = emiTranAPI.json()["data"]["lid"]["emiDetails"]["EMIData"]
        #         print(ed)










        # print("emiTranAPIData::",emiTranAPIData)

        # for id in emiTranAPIData:
        #     print(id)

        # print("emiTranAPIData::",emiTranAPIData)



























        #
        # for e in allRepaid_loan_ids:
        #     emiAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": e},verify=False)
        #     # print(emiAPI.json())
        #     emiAPI_data = emiAPI.json()["data"]["EMIData"]
        #
        #
        #     for ed in emiAPI_data:
        #         if ed["bounceCharge"] == 0:
        #             bounceChMissed_LId.append(e)
        #
        # bounceChMissed_LId_unique = []
        #
        # [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]
        #
        # # print("bounceChMissed_LId::",bounceChMissed_LId)
        # print("bounceChMissed_LId_unique::", bounceChMissed_LId_unique)
