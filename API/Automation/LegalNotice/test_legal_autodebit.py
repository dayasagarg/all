import requests
import pytest
from datetime import datetime, timedelta

# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")

pre_15 = currentFullTime - timedelta(days=15)
pre_15_DateStr = datetime.strftime(pre_15, "%Y-%m-%d")

pre_5 = currentFullTime - timedelta(days=5) # 4-5
pre_5_DateStr = datetime.strftime(pre_5, "%Y-%m-%d")

pre_10 = pre_5 - timedelta(days=10)
pre_10_DateStr = datetime.strftime(pre_10, "%Y-%m-%d")




# note: execute at 12 am every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit,caseAssigned,summons, summons_data, summons_data_count, warrent, legalAutoDebit, autoDebitFailedAPI, legalNotice, autoDebitFailedAPI_current
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{pre_5_DateStr}T10:00:00.000Z",
                                                 "endDate": f"{pre_5_DateStr}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})

        autoDebitFailedAPI = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",
            params={"start_date": f"{pre_5_DateStr}T10:00:00.000Z", "end_date": f"{pre_5_DateStr}T10:00:00.000Z", "status": 4,
                    "page": 1, "skipPageLimit": "true"})

        autoDebitFailedAPI_current = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",
            params={"start_date": f"{curr_str}T10:00:00.000Z", "end_date": f"{curr_str}T10:00:00.000Z",
                    "status": 4,
                    "page": 1, "skipPageLimit": "true"})


        legalAutoDebit = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/autoDebitList", params={"page":1,"startDate":f"{curr_str}T10:00:00.000Z","endDate":f"{curr_str}T10:00:00.000Z","download":"true"})

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{pre_15_DateStr}T10:00:00.000Z",
                                           "endDate": f"{curr_str}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date


    def test_autodebit_failed(self, url):
        print("curr_str::", curr_str)
        print("pre_15_DateStr::", pre_15_DateStr)

        print("pre_5_DateStr::", pre_5_DateStr)
        print("pre_10_DateStr::", pre_10_DateStr)

        global af_lid_5, af_lid_curr
        afd_5 = autoDebitFailedAPI.json()["data"]["finalData"]
        afd_curr = autoDebitFailedAPI_current.json()["data"]["finalData"]
        # print("afd::",afd)
        # print("endDateStr::",endDateStr)

        af_lid_5 = []
        for a in afd_5:
            if a["Today's EMI status"] == "FAILED":
                af_lid_5.append(a["Loan ID"])

        af_lid_curr = []
        for a in afd_curr:
            if a["Today's EMI status"] == "FAILED":
                af_lid_curr.append(a["Loan ID"])




    # @pytest.mark.skip
    def test_legal_autodebit(self, url):
        global lId_autodebit, trans_fullpay_failed_lid, emiAPI_d, lId_notice_sent
        countOfAutoDebit = legalAutoDebit.json()["data"]["count"]
        print("countOfLegalAutodebit::", countOfAutoDebit)
        # print("end_date_2::",end_date_2)

        noticeAllData = legalAutoDebit.json()["data"]["rows"]

        lId_autodebit = []

        for ns in noticeAllData:
            if ns["Loan id"]:
                lId_autodebit.append(ns["Loan id"])

        print("legal_autodebit_lid::", lId_autodebit)
        print("af_lid::",af_lid_5)


        trans_full_lid_5 = []
        for n, j in enumerate(af_lid_5):
            # if n == 5:
            #     break

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": j},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            transData = response.json()["data"]


            for t in transData:

                if t["Pay type"] == "FULLPAY":
                    trans_full_lid_5.append(j)


        trans_fullpay_failed_lid =  set(trans_full_lid_5)

        # print("trans_fullpay_failed_lid::", trans_fullpay_failed_lid)

        noticeAllData = legalNotice.json()["data"]["rows"]

        lId_notice_sent = []

        for ns in noticeAllData:
            if ns["Loan ID"]:
                lId_notice_sent.append(ns["Loan ID"])


        miss_of_fullpay_in_notice_sent_u_p = trans_fullpay_failed_lid - set(lId_notice_sent)
        print("miss_of_fullpay_in_notice_sent_u_p::",miss_of_fullpay_in_notice_sent_u_p)

        miss_of_fullpay_in_notice_sent_u = []

        for m in miss_of_fullpay_in_notice_sent_u_p:

            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                              params={"loanId": m}, verify=False)

            emiAPI_d = emiAPI.json()["data"]["EMIData"]

            for n,e in enumerate(emiAPI_d):

                if e["status"] != "PAID":
                    miss_of_fullpay_in_notice_sent_u.append(m)
                # print("e::",e)

        print("miss_of_fullpay_in_notice_sent_u::", miss_of_fullpay_in_notice_sent_u)

        if len(miss_of_fullpay_in_notice_sent_u) > 0:
            print("Error :: miss_of_fullpay_in_notice_sent_u::",miss_of_fullpay_in_notice_sent_u)
            assert False
        else:
            print("*** No_miss_of_fullpay_in_notice_sent_u ***")


    # @pytest.mark.skip
    def test_legalDemandLetter(self, url):

        # global loanID, uniqLIdListDemand
        countOfLegalDemandLetter = legalDemandLetter.json()["data"]["count"]
        print("countOfLegalDemandLetter::", countOfLegalDemandLetter)

        demandAllData = legalDemandLetter.json()["data"]["rows"]
        # print(demandAllData)

        loanID_leg_demand = []

        for ld in demandAllData:
            if (ld["Emi 4 status"] == "UNPAID"):
                if ld["Loan ID"]:
                    loanID_leg_demand.append(ld["Loan ID"])

            if (ld["Emi 3 status"] == "UNPAID") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID_leg_demand.append(ld["Loan ID"])

            if (ld["Emi 2 status"] == "UNPAID") and (ld["Emi 3 status"] == "-") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID_leg_demand.append(ld["Loan ID"])

        print("legal demand loan ids::", loanID_leg_demand)

        # miss_last_emi_failed_demand_trans_full = set(loanID_leg_demand) - set(trans_fullpay_failed_lid)
        # print("miss_last_emi_failed_demand_fullpay::",miss_last_emi_failed_demand_trans_full)



        trans_full_lid_curr = []
        for n, j in enumerate(af_lid_curr):
            # if n == 5:
            #     break

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": j},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())

            transData_curr = response.json()["data"]

            for c in transData_curr:

                if c["Pay type"] == "FULLPAY":
                    trans_full_lid_curr.append(j)

        trans_fullpay_failed_lid_curr = set(trans_full_lid_curr)

        # print("trans_fullpay_failed_lid_curr::", trans_fullpay_failed_lid_curr)

        miss_last_emi_failed_demand_trans_full = set(loanID_leg_demand) - set(trans_fullpay_failed_lid_curr)
        print("miss_last_emi_failed_demand_fullpay::", miss_last_emi_failed_demand_trans_full)

        miss_last_emi_failed_demand_trans_full_miss_with_notice = miss_last_emi_failed_demand_trans_full - set(lId_notice_sent)
        print("miss_last_emi_failed_demand_trans_full_miss_with_notice::",miss_last_emi_failed_demand_trans_full_miss_with_notice)


        if len(miss_last_emi_failed_demand_trans_full_miss_with_notice) > 0:
            print("Error::last EMI failed miss found from fullpay atdbt &/ notice sent::",miss_last_emi_failed_demand_trans_full_miss_with_notice)
            assert False
        else:
            print("*** No last EMI failed miss found from fullpay atdbt &/ notice sent ***")




