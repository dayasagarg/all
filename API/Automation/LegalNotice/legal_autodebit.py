import requests
import pytest
from datetime import datetime, timedelta


# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")


start_2 = currentFullTime - timedelta(days=15)
start_2_DateStr = datetime.strftime(start_2, "%Y-%m-%d")

start_3 = currentFullTime - timedelta(days=13)
start_3_DateStr = datetime.strftime(start_3, "%Y-%m-%d")

end = currentFullTime - timedelta(days=5)
endDateStr = datetime.strftime(end, "%Y-%m-%d")

start = end - timedelta(days=5)
startDateStr = datetime.strftime(start, "%Y-%m-%d")

start_date = start.strftime("%Y-%m-%d")
end_date = end.strftime("%Y-%m-%d")

start_date_2 = start_2.strftime("%Y-%m-%d")
end_date_2 = currentFullTime.strftime("%Y-%m-%d")

print("start_date::", start_date)
print("end_date::", end_date)

print("start_date_2::", start_date_2)
print("end_date_2::", end_date_2)


# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit,caseAssigned,summons, summons_data, summons_data_count, warrent, legalAutoDebit, autoDebitFailedAPI, legalNotice
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        autoDebitFailedAPI = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",
            params={"start_date": f"{endDateStr}T10:00:00.000Z", "end_date": f"{endDateStr}T10:00:00.000Z", "status": 4,
                    "page": 1, "skipPageLimit": "true"})



        legalAutoDebit = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/autoDebitList",params={"page":1,"startDate":f"{end_date_2}T10:00:00.000Z","endDate":f"{end_date_2}T10:00:00.000Z","download":"true"})

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date







    def test_autodebit_failed(self, url):
        global af_lid
        afd = autoDebitFailedAPI.json()["data"]["finalData"]
        # print("afd::",afd)
        # print("endDateStr::",endDateStr)

        af_lid = []
        for a in afd:
            if a["Today's EMI status"] == "FAILED":
                af_lid.append(a["Loan ID"])



    # @pytest.mark.skip
    def test_legal_autodebit(self, url):
        global lId_autodebit
        countOfAutoDebit = legalAutoDebit.json()["data"]["count"]
        print("countOfLegalAutodebit::", countOfAutoDebit)
        # print("end_date_2::",end_date_2)

        noticeAllData = legalAutoDebit.json()["data"]["rows"]

        lId_autodebit = []

        for ns in noticeAllData:
            if ns["Loan id"]:
                lId_autodebit.append(ns["Loan id"])

        print("legal_autodebit_lid::", lId_autodebit)
        print("af_lid::",af_lid)


        trans_full_lid = []
        for n, j in enumerate(af_lid):
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
                    trans_full_lid.append(j)



        trans_fullpay_failed_lid =  set(trans_full_lid)

        print("trans_fullpay_failed_lid::", trans_fullpay_failed_lid)

        noticeAllData = legalNotice.json()["data"]["rows"]

        lId_notice_sent = []

        for ns in noticeAllData:
            if ns["Loan ID"]:
                lId_notice_sent.append(ns["Loan ID"])



        miss_of_fullpay_in_notice_sent = trans_fullpay_failed_lid - set(lId_notice_sent)
        print("miss_of_fullpay_in_notice_sent::",miss_of_fullpay_in_notice_sent)

    def test_legalDemandLetter(self, url):
        # print("start_date_2::", start_date_2)
        # print("end_date_2::", end_date_2)

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


