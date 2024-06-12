import pytest
import requests
import json
import math
from datetime import datetime


currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
currentDateStr_emi = datetime.strftime(currentFullTime, "%d/%m/%Y")  # date to string format


class TestRepayment:
    @pytest.fixture
    def url(self):
        global all_emi_details_report, all_emi_details_report_data, repay_status_loans_data, all_repaid_loans, all_repaid_loans_data

        repay_status = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",
            params={"fromDate": f"{currentDateStr}T10:00:00.000Z", "endDate": f"{currentDateStr}T10:00:00.000Z",
                    "type": "TOTAL",
                    "page": 1, "download": "true",
                    "verify": False})  # current date
        repay_status_loans_data = repay_status.json()


        pay_l_emi = {"emiStatus": "0",
                    "endDate": f"{currentDateStr}T10:00:00.000Z",
                    "isCountOnly": False,
                    "page": 1,
                    "pagesize": 10,
                    "needAllData":"true",
                    "download":"true",
                    "report": "All EMI Details",
                    "startDate": f"{currentDateStr}T10:00:00.000Z"}

        all_emi_details_report = requests.post("https://chinmayfinserve.com/admin-prod/admin/report/getTodayEmiData",json=pay_l_emi)
        all_emi_details_report_data = all_emi_details_report.json()["data"]["rows"]


    def test_all_emi_details(self,url):
        repay_status_loans_data_count = repay_status_loans_data["data"]["count"]
        print("repay_status_loans_data_count::",repay_status_loans_data_count)

        repay_status_loans_data_total = repay_status_loans_data["data"]["rows"]
        # print("repay_status_loans_data_total::",repay_status_loans_data_total)

        repay_status_lid = []
        for r in repay_status_loans_data_total:
            if r["Loan ID"]:
                repay_status_lid.append(r["Loan ID"])

        print("repay_status_lid::",repay_status_lid)


        all_emi_details_report_users = all_emi_details_report.json()["data"]["count"]
        print("all_emi_details_report_users_count::",all_emi_details_report_users)


        all_emi_d_report_lid = []
        emi_amt_report = []
        prin_amt_report = []

        for e in all_emi_details_report_data:
            if e["Loan ID"]:
                all_emi_d_report_lid.append(e["Loan ID"])

            if e["EMI Amount"]:
                emi_amt_report.append(int(e["EMI Amount"].replace(",","")))

            if e["Principal Amount"]:
                prin_amt_report.append(int(e["Principal Amount"].replace(",","")))


        # print("emi_amt_report::",emi_amt_report)
        # print("prin_amt_report::",prin_amt_report)
        print("all_emi_d_report_lid::",all_emi_d_report_lid)

        comm_repay_emi_report = set(repay_status_lid).intersection(set(all_emi_d_report_lid))
        print("comm_repay_emi_report::",comm_repay_emi_report)
        print("comm_repay_emi_report_count::", len(comm_repay_emi_report))
        assert len(comm_repay_emi_report) == repay_status_loans_data_count

        diff_repay_emi_report = set(repay_status_lid).difference(set(all_emi_d_report_lid))
        print("diff_repay_emi_report::", diff_repay_emi_report)
        print("diff_repay_emi_report::", len(diff_repay_emi_report))

        diff_emi_report_repay_prepaid = set(all_emi_d_report_lid).difference(set(repay_status_lid))
        print("diff_emi_report_repay_prepaid::", diff_emi_report_repay_prepaid)
        print("diff_emi_report_repay_prepaid_count::", len(diff_emi_report_repay_prepaid))


        diff_emi_report_repay_prepaid_notOntime = []
        diff_emi_report_repay_prepaid_receive_amt_issue = []
        diff_emi_report_repay_prepaid_unpaid = []

        for m,k in enumerate(diff_emi_report_repay_prepaid):

            response_emi = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": k},
                verify=False)  # current date

            # # print('status code of get Repayment::', response.status_code)
            ## print(response.json())
            ##
            ## data = response_emi.json()["data"]
            ## # print(emiData)
            ##
            ## if data['loanStatus'] != 'OnTime':
            ##     diff_emi_report_repay_prepaid_notOntime.append(k)
            ##
            ##     # emiData = data["EMIData"]
            ##
            ##     if data["totalReceived"] != data["totalReceivable"]:
            ##         diff_emi_report_repay_prepaid_receive_amt_issue.append(k)
            ##
            ## print("diff_emi_report_repay_prepaid_notOntime::",diff_emi_report_repay_prepaid_notOntime)
            ## print("diff_emi_report_repay_prepaid_receive_amt_issue::",diff_emi_report_repay_prepaid_receive_amt_issue)



            data_emi = response_emi.json()["data"]["EMIData"]

            for emi in data_emi:

                if emi["emiDate"] == currentDateStr_emi:
                    # print("emi::",emi)
                    if emi["status"] == "UNPAID":
                        diff_emi_report_repay_prepaid_unpaid.append(k)
        #
        #
        print("diff_emi_report_repay_prepaid_unpaid::",diff_emi_report_repay_prepaid_unpaid)


        if len(diff_emi_report_repay_prepaid_unpaid) > 0:
            print(f"Error :: All emi detail report data is not as per daily EMI (upcomming EMI) for prepaid ::,{diff_emi_report_repay_prepaid_unpaid}")
        else:
            print(" *** All emi detail report data is per as daily EMI (upcomming EMI) with prepaid users ***")


