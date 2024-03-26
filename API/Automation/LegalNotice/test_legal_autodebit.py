import requests
import pytest
from datetime import datetime, timedelta


# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")

end_2 = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
end_2_F = datetime.strptime(end_2, "%Y-%m-%d")  # string to date format

start_2 = end_2_F - timedelta(days=15)
start_2_DateStr = datetime.strftime(start_2, "%Y-%m-%d")

start_3 = end_2_F - timedelta(days=13)
start_3_DateStr = datetime.strftime(start_3, "%Y-%m-%d")

end = end_2_F - timedelta(days=5)
endDateStr = datetime.strftime(end, "%Y-%m-%d")

start = end - timedelta(days=5)
startDateStr = datetime.strftime(start, "%Y-%m-%d")

start_date = start.strftime("%Y-%m-%d")
end_date = end.strftime("%Y-%m-%d")

start_date_2 = start_2.strftime("%Y-%m-%d")
end_date_2 = end_2_F.strftime("%Y-%m-%d")

print("start_date::", start_date)
print("end_date::", end_date)

print("start_date_2::", start_date_2)
print("end_date_2::", end_date_2)


# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit,caseAssigned,summons, summons_data, summons_data_count, warrent, legalAutoDebit
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent



        legalAutoDebit = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/autoDebitList",params={"page":1,"startDate":f"{end_date_2}T10:00:00.000Z","endDate":f"{end_date_2}T10:00:00.000Z","download":"true"})



        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 11, "adminId": 153,
                                           "download": "true"})

        summons = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                               params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                       "endDate": f"{curr_str}T10:00:00.000Z", "type": 6, "adminId": 70,
                                       "download": "true"})


        summons_data = summons.json()["data"]["rows"]
        summons_data_count = summons.json()["data"]["count"]

        warrent = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
            params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                    "endDate": f"{curr_str}T10:00:00.000Z", "type": 7, "adminId": 70,
                    "download": "true"}
        )



    # @pytest.mark.skip
    def test_DemandLetter(self, url):
        print("start_date::", start_date)
        print("end_date::", end_date)

        print("start_date_2::", start_date_2)
        print("end_date_2::", end_date_2)

        # global loanID, uniqLIdListDemand
        countOfLegalDemandLetter = legalDemandLetter.json()["data"]["count"]
        print("countOfLegalDemandLetter::", countOfLegalDemandLetter)

        demandAllData = legalDemandLetter.json()["data"]["rows"]
        # print(demandAllData)

        loanID = []


        for ld in demandAllData:
            if (ld["Emi 4 status"] == "UNPAID"):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])


            if (ld["Emi 3 status"] == "UNPAID") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])


            if (ld["Emi 2 status"] == "UNPAID") and (ld["Emi 3 status"] == "-") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])


        print("count of demand loan ids::", len(loanID))


        uLIdSet = set(loanID)
        global uniqLIdListDemand
        uniqLIdListDemand = list(uLIdSet)
        print("count of demand unique loan ids list ::", len(uniqLIdListDemand))
        print("demand loan ids full::", loanID)
        print("demand uniqLIdList::", uniqLIdListDemand)


    # @pytest.mark.skip
    def test_legal_autodebit(self, url):
        global lId_autodebit
        countOfAutoDebit = legalAutoDebit.json()["data"]["count"]
        print("countOfAutodebit::", countOfAutoDebit)

        noticeAllData = legalAutoDebit.json()["data"]["rows"]


        lId_autodebit = []

        for ns in noticeAllData:
            if ns["Loan ID"]:
                lId_autodebit.append(ns["Loan ID"])

        print("lId_autodebit::", lId_autodebit)



        matchedDemandWithAutodebit = []
        missedDemandWithAutodebit = []

        global uniqLIdListDemand

        for unl in uniqLIdListDemand:
            if unl in lId_autodebit:
                matchedDemandWithAutodebit.append(unl)
                # print("loanID in lIdNS::", unl)

            if unl not in lId_autodebit:
                missedDemandWithAutodebit.append(unl)



        if len(missedDemandWithAutodebit) == 0:
            print("*** All Autodebit placed ***")
        else:
            print(f"Error:: Autodebit not placed cases found::{missedDemandWithAutodebit}")

        assert len(missedDemandWithAutodebit) == 0


        