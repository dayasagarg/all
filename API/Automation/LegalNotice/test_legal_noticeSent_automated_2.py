import requests
import pytest
from datetime import datetime, timedelta

# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime, "%Y-%m-%d")

end_2 = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
end_2_F = datetime.strptime(end_2, "%Y-%m-%d")  # string to date format

start_2 = end_2_F - timedelta(days=15)
start_2_DateStr = datetime.strftime(start_2, "%Y-%m-%d")

start_3 = end_2_F - timedelta(days=30)
start_3_DateStr = datetime.strftime(start_3, "%Y-%m-%d")

end = end_2_F - timedelta(days=7)
endDateStr = datetime.strftime(end, "%Y-%m-%d")

start = end - timedelta(days=7)
startDateStr = datetime.strftime(start, "%Y-%m-%d")

start_date = start.strftime("%Y-%m-%d")
end_date = end.strftime("%Y-%m-%d")

start_date_2 = start_2.strftime("%Y-%m-%d")
end_date_2 = end_2_F.strftime("%Y-%m-%d")

# print("start_date::", start_date)
# print("end_date::", end_date)
#
# print("start_date_2::", start_date_2)
# print("end_date_2::", end_date_2)


# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3, caseAssigned, fillingInProgress_data
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date

        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                            "endDate": f"{end_date_2}T10:00:00.000Z", "type": 11, "adminId": 153,
                                            "download": "true"})

        fillingInProgress = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                                 "endDate": f"{curr_str}T10:00:00.000Z", "type": 4, "adminId": 70,
                                                 "download": "true"})

        fillingInProgress_data = fillingInProgress.json()["data"]["rows"]



    def test_NoticeSent(self, url):
        global lIdNS, missedDemandWithNotice, matchedDemandWithNotice, noticeNotSent
        countOfNoticeSent = legalNotice.json()["data"]["count"]
        print("countOfNoticeSent::", countOfNoticeSent)

        noticeAllData = legalNotice.json()["data"]["rows"]
        # print(noticeAllData)

        lIdNS = []
        legalCrDateNS = []
        typeNS = []
        adPlDateNS = []
        daysPostLetterSentNS = []

        noticeNotSent = []
        noticeOpenStatus = []
        for ns in noticeAllData:
            if ns["Loan ID"]:
                lIdNS.append(ns["Loan ID"])

            if ns["Sent on email"] == "Not sent":
                noticeNotSent.append(ns["Loan ID"])

            if ns["Sent on email"] == "Opened":
                noticeOpenStatus.append(ns["Loan ID"])

            if ns["Legal created date"]:
                legalCrDateNS.append(ns["Legal created date"])

            if ns["Type"]:
                typeNS.append(ns["Type"])

            if ns["AD placed date"]:
                adPlDateNS.append(ns["AD placed date"])

            if ns["Days post letter sent"]:
                daysPostLetterSentNS.append(ns["Days post letter sent"])

        print("lIdNS::", lIdNS)
        print("noticeNotSent::", noticeNotSent)
        print("noticeOpenStatus::", noticeOpenStatus)
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

        print("duplNotice::", duplNotice)
        print("count_of_duplNotice::", len(duplNotice))

        if len(duplNotice) == 0:
            print("No duplicate found in notice sent")
        else:
            print("Error::duplicate found in notice sent")

        assert len(duplNotice) == 0

        matchedDemandWithNotice = []
        missedDemandWithNotice = []
        global uniqLIdListDemand
        # checking demand against notice sent
        for unl in uniqLIdListDemand:
            if unl in lIdNS:
                matchedDemandWithNotice.append(unl)
                # print("loanID in lIdNS::", unl)

            if unl not in lIdNS:
                missedDemandWithNotice.append(unl)
                # print("loanID not in lIdNS::", unl)

        # print("matchedDemandWithNotice::", matchedDemandWithNotice)
        # print("missedDemandWithNotice::", missedDemandWithNotice)

        # print("case_lid_in_notice", case_lid)

        if len(missedDemandWithNotice) == 0:
            print("*** Notice sent ***")
        else:
            print(f"Error:: Notice not sent cases found::{missedDemandWithNotice}")
        assert len(missedDemandWithNotice) == 0




    def test_case_assign_to_collection_1(self):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid
        case_data = caseAssigned.json()["data"]["rows"]

        # print("case_data::",case_data)

        case_lid = []

        perc_loanId = []

        cal_less_than_70 = []
        # paidPrincipleInterest = []
        # principleInterest = []

        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])



    def test_notice_sent_emi_70_per_emi(self, url):

        global paidEMIAmt, emiAmt

        pp_more_than_70_notice_sent_per_emi_lid = []

        for m in lIdNS:
            emi = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                               params={"loanId": m}, verify=False)

            emi_data_2 = emi.json()["data"]["EMIData"]
            # print("emi_data::",emi_data)

            for o, p in enumerate(emi_data_2):
                # if n == 2:
                #     break

                if p["status"] == "UNPAID":
                    # s_e_lid.append(e)
                    # if ed["paidEmiAmount"]:
                    paidEMIAmt_e = p["paidEmiAmount"]
                    # print("paidEMIAmt::",paidEMIAmt)

                    # if ed["emiAmount"]:
                    emiAmt_e = p["emiAmount"]
                    # print("emiAmt::",emiAmt)

                    pp_f_e = round((paidEMIAmt_e / emiAmt_e) * 100, 0)

                    if pp_f_e >= 70.0:
                        pp_more_than_70_notice_sent_per_emi_lid.append(m)

        # print("pp_more_than_70_notice_sent_per_emi_lid::", pp_more_than_70_notice_sent_per_emi_lid)

        pp_more_than_70_noticeSent_per_emi_lid_missed_collection = []
        for q in pp_more_than_70_notice_sent_per_emi_lid:
            if q not in case_lid:
                pp_more_than_70_noticeSent_per_emi_lid_missed_collection.append(q)


        if len(pp_more_than_70_noticeSent_per_emi_lid_missed_collection) > 0:
            print(
                f"Error:: missing of pp_more_than_70_notice_sent per emi found with collection::{pp_more_than_70_noticeSent_per_emi_lid_missed_collection}")
            assert False
        else:
            print("*** paid percentage inside notice sent is below 70 % per emi ***")


