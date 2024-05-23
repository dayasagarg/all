import pytest
import requests
from datetime import datetime,timedelta


class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global autoDebitFailedAPI, emiRepaymentStatus, curr_str,curr_str_emi,pre_str_emi,pre_str_emi_2,pre_str_emi_3, disb_date_n

        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        curr_str_emi = datetime.strftime(curr, "%d/%m/%Y")

        prev_1 = curr - timedelta(days=1)
        prev_2 = curr - timedelta(days=2)
        prev_3 = curr - timedelta(days=3)

        pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
        pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")
        pre_str_3 = datetime.strftime(prev_3, "%Y-%m-%d")


        pre_str_emi = datetime.strftime(prev_1, "%d/%m/%Y")
        pre_str_emi_2 = datetime.strftime(prev_2, "%d/%m/%Y")
        pre_str_emi_3 = datetime.strftime(prev_3, "%d/%m/%Y")

        disb_date = "07-04-2024"
        disb_date_n = datetime.strptime(disb_date, "%d-%m-%Y")


        autoDebitFailedAPI = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{pre_str_3}T10:00:00.000Z","end_date":f"{curr_str}T10:00:00.000Z","status":4,"page":1,"skipPageLimit":"true"})

        # autoDebitFailedAPI = requests.get(
        #     "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=4&page=1") # 10 data / page

        # autoDebitFailedAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2024-02-03T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&status=9&page=4")

        emiRepaymentStatus = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",params={"fromDate":f"{prev_1}T10:00:00.000Z","endDate":f"{pre_str_1}T10:00:00.000Z","type":"TOTAL","page":1,"download":"true"})


    def test_bounce_charg_autodebit_unpaid_current_date(self, bcURL):
        global autoDebitData

        autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]
        # print(autoDebitData)
        bounceChMissed_LId = []
        autdebit_failed_loan_ids = []


        for ad in autoDebitData:

            if (datetime.strptime(ad["Disbursement date"], "%d-%m-%Y")) < disb_date_n:

                if ad["Today's EMI status"] == "FAILED":
                    if ad["Loan ID"]:
                        autdebit_failed_loan_ids.append(ad["Loan ID"])


        print("auto-debit_failed_loan_ids_count::",len(autdebit_failed_loan_ids))
        print("auto-debit_failed_loan_ids::", autdebit_failed_loan_ids)

        for e in autdebit_failed_loan_ids:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)
            # print(emiAPI.json())
            emiAPI_data = emiAPI.json()["data"]["EMIData"]


            for ed in emiAPI_data:
                if ed["emiDate"] == curr_str_emi:

                    if ed["totalBounceCharge"] == 0:
                        bounceChMissed_LId.append(e)

        bounceChMissed_LId_unique = []

        [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]


        if len(bounceChMissed_LId_unique) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_unique_unpaid_autodebit_current_date::{bounceChMissed_LId_unique}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_unique_unpaid_autodebit_current_date ***")


    def test_bounce_charg_autodebit_unpaid_yestarday_date(self, bcURL):
        global autoDebitData

        autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]
        # print(autoDebitData)
        bounceChMissed_LId = []
        autdebit_failed_loan_ids = []


        for ad in autoDebitData:

            if (datetime.strptime(ad["Disbursement date"], "%d-%m-%Y")) < disb_date_n:

                if ad["Today's EMI status"] == "FAILED":
                    if ad["Loan ID"]:
                        autdebit_failed_loan_ids.append(ad["Loan ID"])


        for e in autdebit_failed_loan_ids:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)
            # print(emiAPI.json())
            emiAPI_data = emiAPI.json()["data"]["EMIData"]


            for ed in emiAPI_data:
                if ed["emiDate"] == pre_str_emi:

                    if ed["totalBounceCharge"] == 0:
                        bounceChMissed_LId.append(e)

        bounceChMissed_LId_unique = []

        [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]



        if len(bounceChMissed_LId_unique) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_unique_unpaid_autodebit_yestarday_date::{bounceChMissed_LId_unique}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_unique_unpaid_autodebit_yestarday_date ***")

    def test_bounce_charg_autodebit_total(self, bcURL):
        global autoDebitData

        autoDebitData_2 = autoDebitFailedAPI.json()["data"]["finalData"]
        # print(autoDebitData)
        bounceChMissed_LId_2 = []
        aut_failed_loan_ids_2 = []


        for ad in autoDebitData_2:
            if (datetime.strptime(ad["Disbursement date"], "%d-%m-%Y")) < disb_date_n:

                if ad["Today's EMI status"] == "FAILED":
                    if ad["Loan ID"]:
                        aut_failed_loan_ids_2.append(ad["Loan ID"])


        for f in aut_failed_loan_ids_2:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": f}, verify=False)
            # print(emiAPI.json())
            emiAPI_data_2 = emiAPI.json()["data"]["EMIData"]

            for ed in emiAPI_data_2:
                if ed["penaltyDays"] > 0:

                    if ed["totalBounceCharge"] == 0:
                        bounceChMissed_LId_2.append(f)

        bounceChMissed_LId_unique_2 = []

        [bounceChMissed_LId_unique_2.append(ul) for ul in bounceChMissed_LId_2 if ul not in bounceChMissed_LId_unique_2]

        # print("bounceChMissed_LId::",bounceChMissed_LId)
        # print("bounceChMissed_LId_unique::", bounceChMissed_LId_unique)


        if len(bounceChMissed_LId_unique_2) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_unique_total_autodebit::{bounceChMissed_LId_unique_2}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_unique_total_autodebit ***")

    def test_no_need_bounce_charg_autodebit_total(self, bcURL):
        global emiRepaymentStatus_data_500

        emiRepaymentStatus_data_500 = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_500 = []

        for rs in emiRepaymentStatus_data_500:

            if (datetime.strptime(rs["Disbursement date"], "%d-%m-%Y")) < disb_date_n:

                if rs["Loan ID"]:
                    emiRepaymentStatus_data_lid_500.append(rs["Loan ID"])

        # print("emiRepaymentStatus_data_lid_2_count::", len(emiRepaymentStatus_data_lid_2))
        # print("emiRepaymentStatus_data_lid_2::",emiRepaymentStatus_data_lid_2)
        #
        bounceChMissed_LId_500 = []
        for r in emiRepaymentStatus_data_lid_500:
            emiAPI_500 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": r}, verify=False)
            # print(emiAPI.json())
            emiAPI_data500 = emiAPI_500.json()["data"]["EMIData"]

            # print(emiAPI_data2)
            #
            for ed2 in emiAPI_data500:
                if ed2["penaltyDays"] == 0:
                    if ed2["status"] == "PAID":

                        if ed2["totalBounceCharge"] > 0:
                            bounceChMissed_LId_500.append(r)


        if len(bounceChMissed_LId_500) > 0:
            print(
                f"Error::bounce charge found ::{bounceChMissed_LId_500}")
            assert False, "bounce charge found"
        else:
            print("*** No bounce charge for ontime users ***")



    @pytest.mark.skip
    def test_bounceCharge_repayStatus_unpaid(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2 = []

        for rs in emiRepaymentStatus_data:
            if rs["Loan ID"]:
                emiRepaymentStatus_data_lid_2.append(rs["Loan ID"])


        bounceChMissed_LId_2 = []
        for r in emiRepaymentStatus_data_lid_2:
            emiAPI_2 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": r}, verify=False)

            emiAPI_data2 = emiAPI_2.json()["data"]["EMIData"]

        #
            for ed2 in emiAPI_data2:
                if ed2["penaltyDays"] > 0:
                    if ed2["status"] == "PAID":

                        if ed2["totalBounceCharge"] == 0:
                            bounceChMissed_LId_2.append(r)



        if len(bounceChMissed_LId_2) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay::{bounceChMissed_LId_2}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay ***")


    @pytest.mark.skip
    def test_bounceCharge_repayStatus_total(self, bcURL):
        global emiRepaymentStatus_data_2

        emiRepaymentStatus_data_2 = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_3 = []

        for rs in emiRepaymentStatus_data_2:

            if rs["Loan ID"]:
                emiRepaymentStatus_data_lid_3.append(rs["Loan ID"])


        bounceChMissed_LId_3 = []
        for s in emiRepaymentStatus_data_lid_3:
            emiAPI_3 = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": s}, verify=False)
            # print(emiAPI.json())
            emiAPI_data3 = emiAPI_3.json()["data"]["EMIData"]

            # print(emiAPI_data2)
        #
            for ed3 in emiAPI_data3:
                if ed3["penaltyDays"] > 0:

                    if ed3["totalBounceCharge"] == 0:
                        bounceChMissed_LId_3.append(s)


        if len(bounceChMissed_LId_3) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_3_total_emi_repay::{bounceChMissed_LId_3}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_3_total_emi_repay ***")
