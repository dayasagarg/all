import pytest
import requests
from datetime import datetime,timedelta

class TestLoanStatus:
    @pytest.fixture
    def url(self):
        global allRepay

        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")
        preTime = currTime - timedelta(days=1)
        preTimeStr = datetime.strftime(preTime, "%Y-%m-%d")
        # print(currTimeStr)
        # print(preTimeStr)

        # emiRepaymentStatus = requests.get(
        #     "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2024-02-18T10:00:00.000Z&endDate=2024-02-23T10:00:00.000Z&type=TOTAL&page=1&download=true")

        allRepay = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{preTimeStr}T10:00:00.000Z", "end_date": f"{currTimeStr}T10:00:00.000Z", "page": 1,
                    "pagesize": 10, "getTotal": "true", "download": "true"})

    def test_loan_status(self,url):
        allRepay_data = allRepay.json()["data"]["rows"]

        repay_user_id = []
        for al in allRepay_data:
            if al["userId"]:
                repay_user_id.append(al["userId"])


        # print("repay_loan_id::",repay_loan_id)

        l_h_compl = []
        for uid in repay_user_id:

            l_hist = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getLoanHistory",params={"userId":uid})
            l_hist_data = l_hist.json()["data"]["loanData"]
            # print("l_hist_data::",l_hist_data)


            for lh in l_hist_data:
                if lh["loanStatus"] == "Complete":
                    l_h_compl.append(lh["id"])



            # Upcoming EMI

            url = "https://lendittfinserve.com/prod/admin/loan/massEMIRepaymentDetails"
            # print(lIDs)

            data = {"loanIds": l_h_compl}

            # headers = {"qa-test-key": "28947f203896ea859233415d1904c927098484d2"}

            response = requests.post(url, json=data, verify=False)  # current date
            response_data = response.json()["data"]

            for md in response_data:
                loan_d = response_data[md]
                # print("loan_d::",loan_d)

        print("l_h_compl::", l_h_compl)
