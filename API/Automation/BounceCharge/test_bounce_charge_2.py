import pytest
import requests
from datetime import datetime,timedelta


# emiTranAPI = requests.post("https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails")


class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global autoDebitFailedAPI, emiRepaymentStatus,pre_str_er

        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")

        prev_1 = curr - timedelta(days=1)
        prev_2 = curr - timedelta(days=3)

        pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
        pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")

        pre_str_er = datetime.strftime(prev_1, "%d-%m-%Y")



        # emi date < current date

        autoDebitFailedAPI = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{pre_str_2}T10:00:00.000Z","end_date":f"{pre_str_1}T10:00:00.000Z","status":4,"page":1,"skipPageLimit":"true"})

        # autoDebitFailedAPI = requests.get(
        #     "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=4&page=1") # 10 data / page

        # autoDebitFailedAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-03T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=9&page=4")

        emiRepaymentStatus = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus",params={"fromDate":f"{pre_str_2}T10:00:00.000Z","endDate":f"{pre_str_1}T10:00:00.000Z","type":"TOTAL","page":1,"download":"true"})




    def test_bounceCharge_repayStatus_unpaid(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:

            # emi date < current date
            if rs["Emi date"] == f"{pre_str_er}":
            # if rs["Today's EMI status"] == "FAILED":

                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_2.append(rs["Loan ID"])

        print("emiRepaymentStatus_data_lid_count_unpaid::", len(emiRepaymentStatus_data_lid_2))
        print("emiRepaymentStatus_data_lid__unpaid::",emiRepaymentStatus_data_lid_2)
        #
        # bounceChMissed_LId_2 = []
        # for r in emiRepaymentStatus_data_lid_2:
        #     emiAPI_2 = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
        #                             params={"loanId": r}, verify=False)
        #     # print(emiAPI.json())
        #     emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

            # print(emiAPI_data2)
        #
            # for ed2 in emiAPI_data2:
            #     if ed2["penaltyDays"] > 0:
            #         if ed2["status"] == "UNPAID":
            #
            #             if ed2["bounceCharge"] == 0:
            #                 bounceChMissed_LId_2.append(r)


        # print("bounceChMissed_LId_2::",bounceChMissed_LId_2)
        # print("bounceChMissed_LId_unique_2::", bounceChMissed_LId_unique_2)

        # print(emiRepaymentStatus_data_lid)

        # if len(bounceChMissed_LId_2) > 0:
        #     print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay::{bounceChMissed_LId_2}")
        #     assert False, "bounce charge missing found"
        # else:
        #     print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay ***")

    def test_bounceCharge_repayStatus_paid(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:

            # emi date < current date
            if rs["Emi date"] == pre_str_er:
            # if rs["Today's EMI status"] == "FAILED":

                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_2.append(rs["Loan ID"])

        print("emiRepaymentStatus_data_lid_count_paid::", len(emiRepaymentStatus_data_lid_2))
        print("emiRepaymentStatus_data_lid_paid::",emiRepaymentStatus_data_lid_2)

        # bounceChMissed_LId_2 = []
        # for r in emiRepaymentStatus_data_lid_2:
        #     emiAPI_2 = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
        #                             params={"loanId": r}, verify=False)
        #     # print(emiAPI.json())
        #     emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

            # print(emiAPI_data2)
        #
            # for ed2 in emiAPI_data2:
            #     if ed2["penaltyDays"] > 0:
            #         if ed2["status"] == "PAID":
            #
            #             if ed2["bounceCharge"] == 0:
            #                 bounceChMissed_LId_2.append(r)


        # print("bounceChMissed_LId_2::",bounceChMissed_LId_2)
        # print("bounceChMissed_LId_unique_2::", bounceChMissed_LId_unique_2)

        # print(emiRepaymentStatus_data_lid)

        # if len(bounceChMissed_LId_2) > 0:
        #     print(f"Error::bounce charge missing found for bounceChMissed_LId_2_paid_emi_repay::{bounceChMissed_LId_2}")
        #     assert False, "bounce charge missing found"
        # else:
        #     print("*** No bounce charge missed for bounceChMissed_LId_2_paid_emi_repay ***")

