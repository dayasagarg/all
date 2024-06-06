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
                    "endDate": "2024-06-04T10:00:00.000Z",
                    "isCountOnly": False,
                    "page": 1,
                    "pagesize": 10,
                    "report": "All EMI Details",
                    "startDate": "2024-06-04T10:00:00.000Z"}

        all_emi_details_report = requests.post("https://chinmayfinserve.com/admin-prod/admin/report/getTodayEmiData",json=pay_l_emi)
        all_emi_details_report_data = all_emi_details_report.json()["data"]["rows"]


    def test_all_emi_details(self,url):
        repay_status_loans_data_count = repay_status_loans_data["data"]["count"]
        print("repay_status_loans_data_count::",repay_status_loans_data_count)


        all_emi_details_report_users = all_emi_details_report.json()["data"]["count"]
        print("all_emi_details_report_users_count::",all_emi_details_report_users)


        print("all_emi_details_report_data::", all_emi_details_report_data)


        aed_lid = []
        for e in all_emi_details_report_data:
            if e["Loan ID"]:
                aed_lid.append(e["Loan ID"])

        print("aed_lid::",aed_lid)



        # print("repaid_loans_data::",repaid_loans_data)
