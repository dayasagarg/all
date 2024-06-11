import pytest
import requests
import json
import math
from datetime import datetime


currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format


class TestRepayment:
    @pytest.fixture
    def url(self):
        global all_emi_details_report, all_emi_details_report_data, repay_status_loans_data

        repay_status = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",
            params={"fromDate": f"{currentDateStr}T10:00:00.000Z", "endDate": f"{currentDateStr}T10:00:00.000Z",
                    "type": "TOTAL",
                    "page": 1, "download": "true",
                    "verify": False})  # current date

        repay_status_loans_data = repay_status.json()

        pay_l_emi = {"emiStatus": "0",
                    "endDate": "2024-06-11T10:00:00.000Z",
                    "isCountOnly": False,
                    "page": 1,
                    "pagesize": 10,
                    "needAllData": "true",
                    "report": "All EMI Details",
                    "startDate": "2024-06-04T10:00:00.000Z"}

        all_emi_details_report = requests.post("https://chinmayfinserve.com/admin-prod/admin/report/getTodayEmiData",json=pay_l_emi)
        all_emi_details_report_data = all_emi_details_report.json()["data"]["rows"]


    def test_all_emi_details(self,url):
        repay_status_loans_data_count = repay_status_loans_data["data"]["count"]
        print("repay_status_loans_data_count::",repay_status_loans_data_count)


        all_emi_details_report_users = all_emi_details_report.json()["data"]["count"]
        print("all_emi_details_report_users_count::",all_emi_details_report_users)


        repay_status_loans_all_data = repay_status_loans_data["data"]["rows"]
        # print("repay_status_loans_all_data::",repay_status_loans_all_data)
        # print("all_emi_details_report_data::", all_emi_details_report_data)

        emi_amt_repay_status = []
        placed_princ_repay_status = []
        for r in repay_status_loans_all_data:
            if r["Emi amount"]:
                emi_amt_repay_status.append(r["Emi amount"])

            if r["Placed amount"]:
                placed_princ_repay_status.append(r["Placed amount"])

        print("emi_amt_repay_status::",emi_amt_repay_status)
        print("placed_princ_repay_status::",placed_princ_repay_status)



        aed_lid = []
        emi_amt_report = []
        prin_amt_report = []

        for e in all_emi_details_report_data:
            if e["Loan ID"]:
                aed_lid.append(e["Loan ID"])

            if e["EMI Amount"]:
                emi_amt_report.append(int(e["EMI Amount"].replace(",","")))

            if e["Principal Amount"]:
                prin_amt_report.append(int(e["Principal Amount"].replace(",","")))


        print("emi_amt_report::",emi_amt_report)
        print("prin_amt_report::",prin_amt_report)
        print("aed_lid::",aed_lid)



