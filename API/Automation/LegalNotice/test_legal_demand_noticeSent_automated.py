import requests
import pytest
from datetime import datetime, timedelta

currentFullTime = datetime.now()  # whole date
end_2 = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
end_2_F = datetime.strptime(end_2,"%Y-%m-%d") # string to date format

start_2 = end_2_F - timedelta(days=15)
start_2_DateStr = datetime.strftime(start_2,"%Y-%m-%d")

end = end_2_F - timedelta(days=7)
endDateStr = datetime.strftime(end,"%Y-%m-%d")

start = end - timedelta(days=7)
startDateStr = datetime.strftime(start,"%Y-%m-%d")



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
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3
        legalDemandLetter = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        legalNotice = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date


    def test_DemandLetter(self, url):
        global loanID, uniqLIdListDemand
        countOfLegalDemandLetter = legalDemandLetter.json()["data"]["count"]
        print("countOfLegalDemandLetter::", countOfLegalDemandLetter)

        demandAllData = legalDemandLetter.json()["data"]["rows"]
        # print(demandAllData)

        loanID = []
        demandCreatedDate = []
        custName = []
        loanTenure = []
        disburseDate = []
        loanAmt = []
        emiNo = []
        asOnDueAmt = []
        dueDate = []
        totalPenaltyDays = []
        emi1Date = []
        emi1Amt = []
        emi1Penalty = []
        emi1Status = []

        emi2Date = []
        emi2Amt = []
        emi2Penalty = []
        emi2Status = []

        emi3Date = []
        emi3Amt = []
        emi3Penalty = []
        emi3Status = []

        receivedPartPayment = []
        adPlAmt = []
        adPlDate = []
        adSource = []
        amtPaidBeforeLetter = []
        amtPaidAfterLetter = []

        emailDate = []
        daysPostLetterSent = []

        for ld in demandAllData:
            if ld["Emi 3 status"] == "UNPAID":
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])



            if ld["Emi 2 status"] == "UNPAID" and (ld["Emi 3 status"] == "UNPAID" or ld["Emi 3 status"] == "-"):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])




            if (ld["Emi 1 status"] == "UNPAID" and (ld["Emi 2 status"] == "UNPAID" or ld["Emi 2 status"] == "-") and (
                    ld["Emi 3 status"] == "UNPAID" or ld["Emi 3 status"] == "-")):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])

        print("count of demand loan ids::", len(loanID))
        # print("unpaid loan ids::",loanID)
        # print(demandCreatedDate)
        # print(emiNo)
        # print(asOnDueAmt)
        # print(dueDate)

        uLIdSet = set(loanID)
        uniqLIdListDemand = list(uLIdSet)
        print("count of demand unique loan ids list ::", len(uniqLIdListDemand))
        print("demand loan ids::", loanID)
        print("demand uniqLIdList::", uniqLIdListDemand)

    def test_NoticeSent(self, url):
        global lIdNS, missedDemandWithNotice, matchedDemandWithNotice
        countOfNoticeSent = legalNotice.json()["data"]["count"]
        print("countOfNoticeSent::", countOfNoticeSent)

        noticeAllData = legalNotice.json()["data"]["rows"]
        # print(noticeAllData)

        lIdNS = []
        legalCrDateNS = []
        typeNS = []
        adPlDateNS = []
        daysPostLetterSentNS = []

        for ns in noticeAllData:
            if ns["Loan ID"]:
                lIdNS.append(ns["Loan ID"])

            if ns["Legal created date"]:
                legalCrDateNS.append(ns["Legal created date"])

            if ns["Type"]:
                typeNS.append(ns["Type"])

            if ns["AD placed date"]:
                adPlDateNS.append(ns["AD placed date"])

            if ns["Days post letter sent"]:
                daysPostLetterSentNS.append(ns["Days post letter sent"])

        print("lIdNS::", lIdNS)
        # print(legalCrDateNS)
        # print(typeNS)
        # print(adPlDateNS)
        # print(daysPostLetterSentNS)

        unNotice = []
        duplNotice = []

        for d in lIdNS:
            if d not in unNotice:
                unNotice.append(d)
            else:
                duplNotice.append(d)

        print("duplNotice::",duplNotice)
        print("count_of_duplNotice::",len(duplNotice))

        if len(duplNotice) == 0:
            print("No duplicate found in notice sent")
        else:
            print("Error::duplicate found in notice sent")

        assert len(duplNotice) == 0



        matchedDemandWithNotice = []
        missedDemandWithNotice = []

        # checking demand against notice sent
        for unl in uniqLIdListDemand:
            if unl in lIdNS:
                matchedDemandWithNotice.append(unl)
                # print("loanID in lIdNS::", unl)

            if unl not in lIdNS:
                missedDemandWithNotice.append(unl)
                # print("loanID not in lIdNS::", unl)

        print("matchedDemandWithNotice::",matchedDemandWithNotice)
        print("missedDemandWithNotice::",missedDemandWithNotice)



        if len(missedDemandWithNotice) == 0:
            print("demand letter matched with notice menu in legal section")
        else:
            print("Error:: demand letter not matched with notice menu in legal section")
        assert len(missedDemandWithNotice) == 0



