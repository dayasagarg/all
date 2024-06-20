import pytest
import requests
from datetime import datetime,timedelta


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

        autoDebitFailedAPI_daily_emi = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{pre_str_2}T10:00:00.000Z","end_date":f"{curr_s}T10:00:00.000Z","status":9,"page":4})

        emiRepaymentStatus = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",params={"fromDate":f"{pre_str_2}T10:00:00.000Z","endDate":f"{curr_s}T10:00:00.000Z","type":"TOTAL","page":1,"download":"true"})

    # @pytest.mark.skip
    def test_bounceCharge_repayStatus_unpaid_failed_emi_current_date(self, bcURL):
        global emiRepaymentStatus_data

        emiRepaymentStatus_data_f = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_f = []

        for f in emiRepaymentStatus_data_f:
            if (datetime.strptime(f["Disbursement date"], "%d-%m-%Y")) > datetime.strptime("07-04-2024", "%d-%m-%Y"):

                if (f["Emi paid date"] == f"{curr_str}") or (f["Emi date"] == f"{curr_str}"):
                    if f["Today's EMI status"] == "FAILED":
                        if f["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_f.append(f["Loan ID"])


        bounceChMissed_LId_2_f = []
        for rf in emiRepaymentStatus_data_lid_2_f:
            emiAPI_2_f = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                    params={"loanId": rf}, verify=False)

            emiAPI_data2_f = emiAPI_2_f.json()["data"]["EMIData"]

            for edf in emiAPI_data2_f:
                if (edf["repaymentDate"] == curr_str_emi) or (edf["emiDate"] == curr_str_emi):

                    if edf["totalBounceCharge"] == 0:
                        bounceChMissed_LId_2_f.append(rf)

        print("bounceChMissed_LId_2_f_without_ad_not_placed::",bounceChMissed_LId_2_f)

        ad_not_placed_f_lid = []
        for n, u in enumerate(bounceChMissed_LId_2_f):
            response_tran_dpd = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": u},
                verify=False)  # current date
            response_tran_d = response_tran_dpd.json()["data"]

            [ad_not_placed_f_lid.append(u) for a in response_tran_d if a["Sub status"] == "AD_NOT_PLACED"]

        print("ad_not_placed_f_lid::",ad_not_placed_f_lid)

        bounceChMissed_LId_f_anp = set(bounceChMissed_LId_2_f) - set(ad_not_placed_f_lid)


        if len(bounceChMissed_LId_f_anp) > 0:
            print(f"Error::bounce charge missing found for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_currenr_date::{bounceChMissed_LId_f_anp}")
            assert False, "bounce charge missing found"
        else:
            print("*** No bounce charge missed for bounceChMissed_LId_2_unpaid_emi_repay_failed_emi_current_date ***")

    # @pytest.mark.skip
    def test_bounceCharge_GST(self, bcURL):
        global emiRepaymentStatus_data_g

        emiRepaymentStatus_data_g = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_g = []

        for g in emiRepaymentStatus_data_g:
            if (datetime.strptime(g["Disbursement date"], "%d-%m-%Y")) > datetime.strptime("07-04-2024", "%d-%m-%Y"):

                if (g["Emi paid date"] == f"{curr_str}") or (g["Emi date"] == f"{curr_str}"):
                    if g["Today's EMI status"] == "FAILED":
                        if g["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_g.append(g["Loan ID"])


        bounceChMissed_LId_2_gst = []
        for rg in emiRepaymentStatus_data_lid_2_g:
            emiAPI_2_g = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                      params={"loanId": rg}, verify=False)

            emiAPI_data2_g = emiAPI_2_g.json()["data"]["EMIData"]

            for edg in emiAPI_data2_g:
                if (edg["repaymentDate"] == curr_str_emi) or (edg["emiDate"] == curr_str_emi):

                    if edg["totalBounceCharge"] != 590:
                        bounceChMissed_LId_2_gst.append(rg)

        print("bounceChMissed_LId_2_gst_without_ad_not_placed::",bounceChMissed_LId_2_gst)

        ad_not_placed_2g_lid = []
        for n, w in enumerate(bounceChMissed_LId_2_gst):
            response_tran_dpd = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": w},
                verify=False)  # current date
            response_tran_d = response_tran_dpd.json()["data"]

            [ad_not_placed_2g_lid.append(w) for a in response_tran_d if a["Sub status"] == "AD_NOT_PLACED"]

        print("ad_not_placed_2g_lid::",ad_not_placed_2g_lid)

        bounceChMissed_LId_2_gst_anp = set(bounceChMissed_LId_2_gst).difference(set(ad_not_placed_2g_lid))

        if len(bounceChMissed_LId_2_gst_anp) > 0:
            print(
                f"Error::bounce charge not equal to 590::{bounceChMissed_LId_2_gst_anp}")
            assert False, "bounce charge missing found"
        else:
            print("*** bounce charge equal to 590 for ad placed cases as per 7th April bifurcation ***")


    def test_bounceCharge_GST_2(self, bcURL):

        emiRepaymentStatus_data_g_n = emiRepaymentStatus.json()["data"]["rows"]

        emiRepaymentStatus_data_lid_2_g_n = []

        for gg in emiRepaymentStatus_data_g_n:
            if (datetime.strptime(gg["Disbursement date"], "%d-%m-%Y")) > datetime.strptime("07-04-2024",
                                                                                           "%d-%m-%Y"):

                if (gg["Emi paid date"] == f"{curr_str}") or (gg["Emi date"] == f"{curr_str}"):
                    # print(g)
                    if gg["Today's EMI status"] == "FAILED":
                        if gg["Loan ID"]:
                            emiRepaymentStatus_data_lid_2_g_n.append(gg["Loan ID"])


        bounceChMissed_LId_2_gst_n = []
        for r in emiRepaymentStatus_data_lid_2_g_n:
            emiAPI_2_g_n = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                      params={"loanId": r}, verify=False)

            emiAPI_data2_g_n = emiAPI_2_g_n.json()["data"]["EMIData"]

            #
            for n in emiAPI_data2_g_n:
                if (n["repaymentDate"] == curr_str_emi) or (n["emiDate"] == curr_str_emi):

                    if n["totalBounceCharge"] != 590:
                        bounceChMissed_LId_2_gst_n.append(r)

        print("bounceChMissed_LId_2_gst_n_without_ad_not_placed::", bounceChMissed_LId_2_gst_n)

        ad_not_placed_lid = []
        for n, s in enumerate(bounceChMissed_LId_2_gst_n):

            response_tran_dpd = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": s},
                verify=False)  # current date
            response_tran_d = response_tran_dpd.json()["data"]

            [ad_not_placed_lid.append(s) for t in response_tran_d if t["Sub status"] == "AD_NOT_PLACED"]

        print("ad_not_placed_lid::",ad_not_placed_lid)

        bounceChMissed_LId_2_gst_n_anp = set(bounceChMissed_LId_2_gst_n) - set(ad_not_placed_lid)

        if len(bounceChMissed_LId_2_gst_n_anp) > 0:
            print(
                f"Error::bounce charge not equal to 590::{bounceChMissed_LId_2_gst_n_anp}")
            assert False, "bounce charge missing found"
        else:
            print("*** bounce charge equal to 590 for ad placed cases ***")  # 7th April