import pytest
import requests
from datetime import datetime,timedelta

class TestLoanStatus:
    @pytest.fixture
    def url(self):
        global allRepay

        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")
        preTime = currTime - timedelta(days=2)
        preTimeStr = datetime.strftime(preTime, "%Y-%m-%d")
        # print(currTimeStr)
        # print(preTimeStr)

        # emiRepaymentStatus = requests.get(
        #     "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus?fromDate=2024-02-18T10:00:00.000Z&endDate=2024-02-23T10:00:00.000Z&type=TOTAL&page=1&download=true")

        allRepay = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{preTimeStr}T10:00:00.000Z", "end_date": f"{currTimeStr}T10:00:00.000Z", "page": 1,
                    "pagesize": 10, "getTotal": "true", "download": "true"})



    def test_loan_status(self,url):
        global principal, interest, totalPaid
        allRepay_data = allRepay.json()["data"]["rows"]

        repay_loan_id = []
        less_total_paid = []
        for al in allRepay_data:
            if al["Loan id"]:
                repay_loan_id.append(al["Loan id"])

            if al["Repaid flag"] == "Delayed":
                if al["Principal"]:
                    principal = al["Principal"]
                if al["Interest"]:
                    interest = al["Interest"]
                if al["Total paid Amt"]:
                    totalPaid = al["Total paid Amt"]

                pi = principal + interest
                if totalPaid < pi:
                    less_total_paid.append(al["userId"])

                # print("pi::",pi)
                # print("totalPaid::",totalPaid)
        # print("less_total_paid::", less_total_paid)


        # Complete, Active
        loanStatus_wrong = []
        for l in less_total_paid:
            loanStatus = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getLoanHistory", params={"userId":l})
            loanStatusData = loanStatus.json()["data"]["loanData"]

            # loanStatus_wrong = []
            for l in loanStatusData:
                if l["loanStatus"]:
                    if l["loanStatus"] == "Complete":
                        loan_St_id = l["id"]
                        # loanStatus_wrong_d += loan_St_id
                        loanStatus_wrong.append(loan_St_id)
                        # print("loan_St_id::",loan_St_id)
                        # print(l["id"])

                    break

        # print("loanStatus_wrong::",loanStatus_wrong)


        if len(loanStatus_wrong) > 0:
            print(f"Error::paid amount is less than emi amount found in loan complete/close::{loanStatus_wrong}")
            assert False, "paid amount is less than emi amount found"

        else:
            print("*** loan status is active ***")

