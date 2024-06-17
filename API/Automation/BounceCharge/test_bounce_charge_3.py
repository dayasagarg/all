import pytest
import requests
from datetime import datetime,timedelta


# emiTranAPI = requests.post("https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails")


class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global autoDebitFailedAPI, emiRepaymentStatus,pre_str_er,curr_str,curr_str_emi, disAPI, disAPI_d, disb_date_n

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%d-%m-%Y")
        curr_str_emi = datetime.strftime(curr, "%d/%m/%Y")

        curr_s = datetime.strftime(curr, "%Y-%m-%d")
        prev_1 = curr - timedelta(days=1)
        prev_2 = curr - timedelta(days=3)

        pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
        pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")

        pre_str_er = datetime.strftime(prev_1, "%d-%m-%Y")

        disb_date = "07-04-2024"
        disb_date_n = datetime.strptime(disb_date, "%d-%m-%Y")


        autoDebitFailedAPI = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{pre_str_2}T10:00:00.000Z","end_date":f"{curr_s}T10:00:00.000Z","status":4,"page":1,"skipPageLimit":"true"})

        # autoDebitFailedAPI = requests.get(
        #     "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=4&page=1") # 10 data / page

        # autoDebitFailedAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-03T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=9&page=4")

        emiRepaymentStatus = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",params={"fromDate":f"{pre_str_2}T10:00:00.000Z","endDate":f"{curr_s}T10:00:00.000Z","type":"TOTAL","page":1,"download":"true"})


    @pytest.mark.skip
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

        print("emiRepaymentStatus_data_lid_2_count::", len(emiRepaymentStatus_data_lid_2))
        print("emiRepaymentStatus_data_lid_2::",emiRepaymentStatus_data_lid_2)
        #
        bounceChMissed_LId_2 = []
        for r in emiRepaymentStatus_data_lid_2:
            emiAPI_2 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": r}, verify=False)
            # print(emiAPI.json())
            emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

            # print(emiAPI_data2)
        #
            for ed2 in emiAPI_data2:
                if ed2["penaltyDays"] > 0:
                    if ed2["status"] == "UNPAID":

                        if ed2["totalBounceCharge"] == 0:
                            bounceChMissed_LId_2.append(r)

        if len(bounceChMissed_LId_2) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay before 7th April 2024 cases::{bounceChMissed_LId_2}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay ***")

    def test_bounceCharge_repayStatus_unpaid_failed_emi_current_date(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data_f = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_f = []

        for f in emiRepaymentStatus_data_f:
            if (datetime.strptime(f["Disbursement date"], "%d-%m-%Y")) > datetime.strptime("07-04-2024", "%d-%m-%Y"):

                if f["Emi date"] == f"{curr_str}":
                    if f["Today's EMI status"] == "FAILED":
                        if f["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_f.append(f["Loan ID"])

        # print("emiRepaymentStatus_data_lid_2_count_f::", len(emiRepaymentStatus_data_lid_2_f))
        # print("emiRepaymentStatus_data_lid_2_f::",emiRepaymentStatus_data_lid_2_f)

        bounceChMissed_LId_2_f = []
        for rf in emiRepaymentStatus_data_lid_2_f:
            emiAPI_2_f = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": rf}, verify=False)
            # print(emiAPI.json())
            emiAPI_data2_f = emiAPI_2_f.json()["data"]["EMIData"]

        #
            for edf in emiAPI_data2_f:
                if edf["emiDate"] == curr_str_emi:

                    if edf["totalBounceCharge"] == 0:
                        bounceChMissed_LId_2_f.append(rf)


        if len(bounceChMissed_LId_2_f) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_currenr_date before 7th April 2024 cases::{bounceChMissed_LId_2_f}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_current_date ***")

    def test_bounceCharge_500(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data_g = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_g = []

        for g in emiRepaymentStatus_data_g:
            if (datetime.strptime(g["Disbursement date"], "%d-%m-%Y")) < datetime.strptime("07-04-2024", "%d-%m-%Y"):

                if g["Emi date"] == f"{curr_str}":
                    if g["Today's EMI status"] == "FAILED":
                        if g["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_g.append(g["Loan ID"])


        bounceChMissed_LId_2_gst = []
        for rg in emiRepaymentStatus_data_lid_2_g:
            emiAPI_2_g = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                      params={"loanId": rg}, verify=False)

            emiAPI_data2_g = emiAPI_2_g.json()["data"]["EMIData"]

            for edg in emiAPI_data2_g:
                if edg["emiDate"] == curr_str_emi:

                    if edg["totalBounceCharge"] != 500:
                        bounceChMissed_LId_2_gst.append(rg)


        if len(bounceChMissed_LId_2_gst) > 0:
            print(
                f"Error::bounce charge not equal to 500::{bounceChMissed_LId_2_gst}")
            assert False, "bounce charge missing found"
        else:
            print("*** bounce charge equal to 500 before 7th April 2024 cases***")