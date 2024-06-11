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
        global all_emi_details_report, all_emi_details_report_data, repay_status_loans_data, all_repaid_loans, all_repaid_loans_data

        # repay_status = requests.get(
        #     "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",
        #     params={"fromDate": f"{currentDateStr}T10:00:00.000Z", "endDate": f"{currentDateStr}T10:00:00.000Z",
        #             "type": "TOTAL",
        #             "page": 1, "download": "true",
        #             "verify": False})  # current date
        # repay_status_loans_data = repay_status.json()


        all_repaid_loans = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{currentDateStr}T10:00:00.000Z", "end_date": f"{currentDateStr}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date

        all_repaid_loans_data = all_repaid_loans.json()["data"]["rows"]


        pay_l_emi = {"emiStatus": "0",
                    "endDate": "2024-06-11T10:00:00.000Z",
                    "isCountOnly": False,
                    "page": 1,
                    "pagesize": 10,
                    "needAllData":"true",
                    "download":"true",
                    "report": "All EMI Details",
                    "startDate": "2024-06-11T10:00:00.000Z"}

        all_emi_details_report = requests.post("https://chinmayfinserve.com/admin-prod/admin/report/getTodayEmiData",json=pay_l_emi)
        all_emi_details_report_data = all_emi_details_report.json()["data"]["rows"]


    def test_all_emi_details(self,url):
        # repay_status_loans_data_count = repay_status_loans_data["data"]["count"]
        # print("repay_status_loans_data_count::",repay_status_loans_data_count)

        all_repaid_users = all_repaid_loans.json()["data"]["count"]
        print("all_repaid_users_count::", all_repaid_users)


        all_emi_details_report_users = all_emi_details_report.json()["data"]["count"]
        print("all_emi_details_report_users_count::",all_emi_details_report_users)


        # repay_status_loans_all_data = repay_status_loans_data["data"]["rows"]
        # print("repay_status_loans_all_data::",repay_status_loans_all_data)
        # print("all_emi_details_report_data::", all_emi_details_report_data)

        emi_amt_repaid_status = []
        placed_princ_repaid_status = []
        all_repaid_lid = []

        for r in all_repaid_loans_data:
            if r["Loan id"]:
                all_repaid_lid.append(r["Loan id"])



        print("emi_amt_repaid_status::",emi_amt_repaid_status)
        print("placed_princ_repaid_status::",placed_princ_repaid_status)
        # print("all_repaid_lid::",all_repaid_lid)



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

        # print(len(all_repaid_lid))
        # print(len(all_emi_d_report_lid))

        repaid_lid_not_in_report = set(all_repaid_lid) - set(all_emi_d_report_lid)
        print("repaid_lid_not_in_report::",repaid_lid_not_in_report)
        print("repaid_lid_not_in_report_count::", len(repaid_lid_not_in_report))

        report_lid_not_in_repaid__unpaid = set(all_emi_d_report_lid) - set(all_repaid_lid)
        print("report_lid_not_in_repaid__unpaid::", report_lid_not_in_repaid__unpaid)
        print("report_lid_not_in_repaid__unpaid_count::", len(report_lid_not_in_repaid__unpaid))



        refund_compl = [904294, 870029, 903247, 931767, 919116, 949002, 866732, 876070, 915747, 818249, 821385, 873617, 885270, 903178, 906692, 896021, 813861, 871195, 894691, 908947, 912308, 922158, 848968, 868131, 910273, 930989, 849287, 911470, 886604, 786478, 922049, 913704, 914331, 917137, 919581, 931015, 931736, 926649, 937907, 890835, 906586, 934055, 863430, 938089, 944003, 638151, 803973, 945815, 885178, 905518, 933365, 936608, 917182, 794601, 913506, 810781, 905416, 784456, 913840, 950457]
        refund_pend_data = [821619, 854222, 864748, 878053, 878224, 890605, 901872, 909984, 915802]
        all_refund = refund_compl + refund_pend_data
        print("all_refund_count::",len(all_refund))




        miss = []
        match = []

        # for d in all_emi_d_report_lid:
        #     if d not in all_repaid_lid:
        #         miss.append(d)
        #     else:
        #         match.append(d)
        #
        # print("miss::",len(miss))
        # print("match::", len(match))


        for d in all_repaid_lid:
            if d not in all_emi_d_report_lid:
                miss.append(d)
            else:
                match.append(d)

        print("miss::",len(miss))
        print("match::", len(match))


        match_rm_refund = set(match) - set(all_refund)
        refund_rm_match = set(all_refund) - set(match)
        print("match_rm_refund::",len(match_rm_refund))
        print("refund_rm_match::", len(refund_rm_match))






