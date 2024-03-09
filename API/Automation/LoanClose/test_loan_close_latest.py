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



        for l in less_total_paid:
            loanStatus = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getLoanHistory", params={"userId":l})

            print("loanStatus::",loanStatus)




        # print(repay_loan_id)







































            # for l in repay_loan_id:
            #     emi = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",params={"loanId":l})
            #     emi_data = emi.json()["data"]["EMIData"]
            #     # print("emi_data::",emi_data)
            #     # print("emi_data::",emi_data)
            #
            #     for d in emi_data:
            #         if d["dueStatus"]=="DELAY":
            #             delay_lid.append(al)



        # print("delay_lid:",delay_lid)
                # if d["dueStatus"] == "DELAY":
                #     print(d["dueStatus"])




        # print("repay_loan_id_count::", len(repay_loan_id))
        # print("repay_loan_id::",repay_loan_id)

































































        # # Upcoming EMI
        #
        # # url = "https://lendittfinserve.com/prod/admin/loan/massEMIRepaymentDetails"
        # url = "https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails"
        # # print(lIDs)
        #
        # data = {"loanIds": repay_loan_id}
        #
        # headers = {"qa-test-key": "28947f203896ea859233415d1904c927098484d2"}
        #
        # response = requests.post(url, json=data, headers=headers,verify=False)  # current date
        # response_data = response.json()["data"]
        #
        # # print("response_data::",response_data)
        #
        #
        #
        # delay_lid = []
        # for md in response_data:
        #     loan_d = response_data[md]
        #     emi_details = loan_d["emiDetails"]
        #     print("emi_details::",emi_details)
        #
        #     # for d in emi_details:
        #     #     print(d)
        #     #     delay_lid.append(loan_d)
        #
        # # print("delay_lid::",delay_lid)







