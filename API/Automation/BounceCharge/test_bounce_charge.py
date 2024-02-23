import pytest
import requests
from datetime import datetime,timedelta


# emiTranAPI = requests.post("https://lendittfinserve.com/admin-prod/admin/qa/bulkEMIDetails")


class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global autoDebitFailedAPI, emiRepaymentStatus

        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")

        prev_1 = curr - timedelta(days=1)
        prev_2 = curr - timedelta(days=2)

        pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
        pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")



        # emi date < current date

        autoDebitFailedAPI = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{pre_str_2}T10:00:00.000Z","end_date":f"{pre_str_1}T10:00:00.000Z","status":4,"page":1,"skipPageLimit":"true"})

        # autoDebitFailedAPI = requests.get(
        #     "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=4&page=1") # 10 data / page

        # autoDebitFailedAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-03T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=9&page=4")

        emiRepaymentStatus = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus",params={"fromDate":f"{pre_str_2}T10:00:00.000Z","endDate":f"{pre_str_1}T10:00:00.000Z","type":"TOTAL","page":1,"download":"true"})


    def test_bounce_charg_autodebit(self, bcURL):
        global autoDebitData

        autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]
        # print(autoDebitData)
        bounceChMissed_LId = []
        aut_failed_loan_ids = []


        for ad in autoDebitData:

            # if ad["AD Response date"] == "05-02-2024":

            if ad["Today's EMI status"] == "FAILED":
                if ad["Loan ID"]:
                    aut_failed_loan_ids.append(ad["Loan ID"])
                # print(ad)

            # print("aut_failed_loan_ids::",aut_failed_loan_ids)

        for e in aut_failed_loan_ids:
            emiAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)
            # print(emiAPI.json())
            emiAPI_data = emiAPI.json()["data"]["EMIData"]

            for ed in emiAPI_data:
                if ed["penaltyDays"] > 0:
                    if ed["status"] == "UNPAID":
                        # if ed["emiDate"] == "08/02/2024":

                        if ed["bounceCharge"] == 0:
                            bounceChMissed_LId.append(e)

        bounceChMissed_LId_unique = []

        [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]

        # print("bounceChMissed_LId::",bounceChMissed_LId)
        # print("bounceChMissed_LId_unique::", bounceChMissed_LId_unique)

        if len(bounceChMissed_LId_unique) > 0:
            print(f"bounce charge missing found::{bounceChMissed_LId_unique}")
            assert False, "bounce charge missing found"
        else:
            print("No bounce charge missed")

    #@pytest.mark.skip
    def test_bounceCharge_repayStatus(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:

            # emi date < current date
            # if rs["Emi date"] == "09-02-2024":

            if rs["Today's EMI status"] == "FAILED":
                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_2.append(rs["Loan ID"])

        # print(emiRepaymentStatus_data_lid_2)
        #
        bounceChMissed_LId_2 = []
        for r in emiRepaymentStatus_data_lid_2:
            emiAPI_2 = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": r}, verify=False)
            # print(emiAPI.json())
            emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

            # print(emiAPI_data2)
        #
            for ed2 in emiAPI_data2:
                if ed2["penaltyDays"] > 0:
                    if ed2["status"] == "UNPAID":

                        if ed2["bounceCharge"] == 0:
                            bounceChMissed_LId_2.append(r)


        print("bounceChMissed_LId_2::",bounceChMissed_LId_2)
        # print("bounceChMissed_LId_unique_2::", bounceChMissed_LId_unique_2)

        # print(emiRepaymentStatus_data_lid)
        
        if len(bounceChMissed_LId_2) > 0:
            print(f"bounce charge missing found::{bounceChMissed_LId_2}")
            assert False, "bounce charge missing found"
        else:
            print("No bounce charge missed")


    def test_status_failed_val(self,bcURL):
        # autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]
        # emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emi_aut_status = []

        for aut in autoDebitData:
            if aut["Today's EMI status"] != "FAILED":
                emi_aut_status.append(aut["Loan ID"])

        print("emi_aut_status::",emi_aut_status)

    @pytest.mark.skip
    def test_date_val(self, bcURL):

        emi_aut_status = []
        emi_ers_status = []

        for aut in autoDebitData:
            if aut["Today's EMI status"] != "FAILED":
                emi_aut_status.append(aut["Loan ID"])

        for ers in emiRepaymentStatus_data:
            if ers["Loan ID"]:
                emi_ers_status.append(ers["Loan ID"])

        emiDate = []
        for o in emi_ers_status:

            emi = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
                               params={"loanId": o, "encoding": 'utf-8', "errors": 'ignore'})

            emiD = emi.json()["data"]["EMIData"]

            for e in emiD:
                if e["emiDate"] == e["repaymentDate"]:
                    if e["penaltyDays"] != 0:
                        emiDate.append(o)

        print("emiDate::", emiDate)



            # emi_ers_status.append(ers["Loan ID"])

                # # if ers["Payment type"] == "AUTODEBIT":
                # if aut["EMI date"] != ers["Emi date"]:
                #     emi_date_miss_match_aut_ers.append(ers["Loan ID"])

        # print("emi_ers_status::",emi_ers_status)
        # print("emi_aut_status::",emi_aut_status)
