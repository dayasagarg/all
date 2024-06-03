import pytest
import requests
from datetime import datetime,timedelta


class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global autoDebitFailedAPI, emiRepaymentStatus,pre_str_er,curr_str,curr_str_emi, disb_date_n

        from datetime import datetime, timedelta

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
    def test_bounceCharge_repayStatus_unpaid_prev(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:
            if (datetime.strptime(rs["Disbursement date"], "%d-%m-%Y")) > disb_date_n:

                if rs["Emi paid date"] == f"{pre_str_er}":

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

        #
            for ed2 in emiAPI_data2:
                if ed2["penaltyDays"] > 0:
                    if ed2["status"] == "UNPAID":

                        if ed2["totalBounceCharge"] == 0:
                            bounceChMissed_LId_2.append(r)


        if len(bounceChMissed_LId_2) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay::{bounceChMissed_LId_2}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay ***")


    def test_bounceCharge_repayStatus_unpaid_failed_emi_current_date(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data_f = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_f = []

        for f in emiRepaymentStatus_data_f:
            if (datetime.strptime(f["Disbursement date"], "%d-%m-%Y")) > disb_date_n:


                if f["Emi paid date"] == f"{curr_str}":
                    if f["Today's EMI status"] == "FAILED":
                        if f["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_f.append(f["Loan ID"])


        bounceChMissed_LId_2_f = []
        for rf in emiRepaymentStatus_data_lid_2_f:
            emiAPI_2_f = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": rf}, verify=False)

            emiAPI_data2_f = emiAPI_2_f.json()["data"]["EMIData"]
    #
            for edf in emiAPI_data2_f:

                if edf["totalBounceCharge"] == 0:
                    bounceChMissed_LId_2_f.append(rf)


        if len(bounceChMissed_LId_2_f) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_currenr_date::{bounceChMissed_LId_2_f}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_current_date ***")


    def test_bounceCharge_repayStatus_paid(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:
            if (datetime.strptime(rs["Disbursement date"], "%d-%m-%Y")) > disb_date_n:


                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_2.append(rs["Loan ID"])

        bounceChMissed_LId_2 = []
        for r in emiRepaymentStatus_data_lid_2:
            emiAPI_2 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": r}, verify=False)

            emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

            for ed2 in emiAPI_data2:
                if ed2["penaltyDays"] > 0:
                    if ed2["status"] == "PAID":

                        if ed2["totalBounceCharge"] == 0:
                            bounceChMissed_LId_2.append(r)


        if len(bounceChMissed_LId_2) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_paid_emi_repay::{bounceChMissed_LId_2}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_paid_emi_repay ***")


    def test_bounceCharge_repayStatus_total(self, bcURL):
        global emiRepaymentStatus_data_2

        emiRepaymentStatus_data_2 = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_3 = []

        for rs in emiRepaymentStatus_data_2:
            if (datetime.strptime(rs["Disbursement date"], "%d-%m-%Y")) > disb_date_n:


                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_3.append(rs["Loan ID"])

        bounceChMissed_LId_3 = []
        for s in emiRepaymentStatus_data_lid_3:
            emiAPI_3 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": s}, verify=False)

            emiAPI_data3 = emiAPI_3.json()["data"]["EMIData"]

            for ed3 in emiAPI_data3:
                if ed3["penaltyDays"] > 0:

                    if ed3["totalBounceCharge"] == 0:
                        bounceChMissed_LId_3.append(s)

        if len(bounceChMissed_LId_3) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_3_total_emi_repay::{bounceChMissed_LId_3}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_3_total_emi_repay ***")


    def test_bounceCharge_repayStatus_more(self, bcURL):
        global emiRepaymentStatus_data_n

        emiRepaymentStatus_data_n = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_n = []

        for rsn in emiRepaymentStatus_data_n:
            if (datetime.strptime(rsn["Disbursement date"], "%d-%m-%Y")) > disb_date_n:

                if rsn["Loan ID"]:
                    emiRepaymentStatus_data_lid_n.append(rsn["Loan ID"])

        bounceChMissed_LId_n = []
        for s in emiRepaymentStatus_data_lid_n:
            emiAPI_n = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": s}, verify=False)

            emiAPI_datan = emiAPI_n.json()["data"]["EMIData"]

            for edn in emiAPI_datan:
                if edn["penaltyDays"] > 0:

                    if edn["totalBounceCharge"] > 590:
                        bounceChMissed_LId_n.append(s)

        if len(bounceChMissed_LId_n) > 0:
            print(f"Error::bounce charge more ::{bounceChMissed_LId_n}")
            # assert False, "bounce charge more"
        else:
            print("*** No bounce charge more ***")

