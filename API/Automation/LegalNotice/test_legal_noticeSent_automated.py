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

print("start_date::", start_date)
print("end_date::", end_date)

print("start_date_2::", start_date_2)
print("end_date_2::", end_date_2)


# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3, caseAssigned, fillingInProgress_data, paidCollection, todayEmiFailedData
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date

        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{end_date_2}T10:00:00.000Z",
                                            "endDate": f"{end_date_2}T10:00:00.000Z", "type": 11, "adminId": 153,
                                            "download": "true"})

        paidCollection = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{end_date_2}T10:00:00.000Z",
                                            "endDate": f"{end_date_2}T10:00:00.000Z", "type": 10, "adminId": 153,
                                            "download": "true"})



        todayEmiFailed = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",params={"start_date":f"{curr_str}T10:00:00.000Z","end_date":f"{curr_str}T10:00:00.000Z","status":9,"page":1})

        todayEmiFailedData = todayEmiFailed.json()["data"]["finalData"]

    #
    # @pytest.mark.skip
    def test_case_assign_to_collection_1(self,url):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid
        case_data = caseAssigned.json()["data"]["rows"]
        paid_legal = paidCollection.json()["data"]["rows"]

        # print("case_data::",case_data)


        case_lid = []
        paid_legal_lid = []

        perc_loanId = []

        cal_less_than_70 = []
        # paidPrincipleInterest = []
        # principleInterest = []

        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])

        print("case_lid::",case_lid)

        for p in paid_legal:

            if p["Loan ID"]:
                paid_legal_lid.append(p["Loan ID"])

        print("paid_legal_lid::",paid_legal_lid)



        collection_paid_cons = []
        collection_unpaid_cons = []

        for n,i in enumerate(case_lid):

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i},
                verify=False)  # current date


            '''getting EMIData data of Repayment'''
            emiData = response.json()["data"]["EMIData"]
            # print(emiData)

            for eD in emiData:

                if eD["status"] == "PAID":
                    collection_paid_cons.append(i)

                elif eD["status"] == "UNPAID":
                    collection_unpaid_cons.append(i)

        print("collection_paid_cons::",collection_paid_cons)
        print("collection_unpaid_cons::",collection_unpaid_cons)

        actual_paid = set(collection_paid_cons) - set(collection_unpaid_cons)
        print("actual_paid::",actual_paid)

        sub_actual_paid_and_paid_legal_lid = set(actual_paid) - set(paid_legal_lid)

        if len(sub_actual_paid_and_paid_legal_lid) > 0:
            print(f"Error:: Paid percentage 100% /all emi paid found in case assigned to collection and not assigned to paid section :: {sub_actual_paid_and_paid_legal_lid}")
            assert False
        else:
            print("*** Paid percentage is below 100% in case assigned to collection ***")



    def test_DemandLetter(self, url):
        global loanID_d_unique
        # print("start_date_2::", start_date_2)
        # print("end_date_2::", end_date_2)

        # global loanID, uniqLIdListDemand
        countOfLegalDemandLetter = legalDemandLetter.json()["data"]["count"]
        print("countOfLegalDemandLetter::", countOfLegalDemandLetter)

        demandAllData = legalDemandLetter.json()["data"]["rows"]
        # print(demandAllData)

        loanID_d = []

        for ld in demandAllData:
            if (ld["Emi 4 status"] == "UNPAID"):
                if ld["Loan ID"]:
                    loanID_d.append(ld["Loan ID"])

            if (ld["Emi 3 status"] == "UNPAID") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID_d.append(ld["Loan ID"])

            if (ld["Emi 2 status"] == "UNPAID") and (ld["Emi 3 status"] == "-") and (ld["Emi 4 status"] == "-"):
                if ld["Loan ID"]:
                    loanID_d.append(ld["Loan ID"])



        print("count of demand loan ids::", len(loanID_d))
        # print("unpaid loan ids::",loanID)
        # print(demandCreatedDate)
        # print(emiNo)
        # print(asOnDueAmt)
        # print(dueDate)

        loanID_d_unique = set(loanID_d)


        print("count of demand unique loan ids list ::", len(loanID_d_unique))
        print("demand loan ids::", loanID_d_unique)
        print("demand uniqLIdList::", loanID_d_unique)

    # @pytest.mark.skip
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
            print("*** No duplicate found in notice sent ***")
        else:
            print("Error::duplicate found in notice sent")

        assert len(duplNotice) == 0

        matchedDemandWithNotice = []
        missedDemandWithNotice = []
        global uniqLIdListDemand
        # checking demand against notice sent
        for unl in loanID_d_unique:
            if unl in lIdNS:
                matchedDemandWithNotice.append(unl)
                # print("loanID in lIdNS::", unl)

            if unl not in lIdNS:
                missedDemandWithNotice.append(unl)
                # print("loanID not in lIdNS::", unl)

        # print("matchedDemandWithNotice::", matchedDemandWithNotice)
        # print("missedDemandWithNotice::", missedDemandWithNotice)

        # print("case_lid_in_notice", case_lid)


        todays_failed_emi_lid = [f["Loan ID"] for f in todayEmiFailedData if f["Today's EMI status"] == "AD NOT PLACED"]
        print("todays_failed_emi_lid::", todays_failed_emi_lid)

        missedDemandWithNotice_subs_todays_failed_emi_lid = set(missedDemandWithNotice) - set(todays_failed_emi_lid)


        if len(missedDemandWithNotice_subs_todays_failed_emi_lid) == 0:
            print("*** Notice are sent ***")
        else:
            print(f"Error:: Notice not sent cases found with neglecting ad not placed ::{missedDemandWithNotice_subs_todays_failed_emi_lid}") ###
        assert len(missedDemandWithNotice_subs_todays_failed_emi_lid) == 0



    # @pytest.mark.skip
    def test_notice_not_sent(self):
        # noticeNotSent_sub_coll = set(noticeNotSent) - set(case_lid)
        # print("noticeNotSent_sub_coll::",noticeNotSent_sub_coll)

        if len(noticeNotSent) > 0:
            print(f"Notice not sent found ::{noticeNotSent}")
            assert False
        else:
            print("*** All notice sent ***")


    # @pytest.mark.skip
    def test_case_assign_to_collection_2(self):
        count_cal_less_than_70 = len(cal_less_than_70)
        print("count_cal_less_than_70 :: ", count_cal_less_than_70)
        #

        if count_cal_less_than_70 > 0:
            print(f"Error:: Paid percentage less than 70% found in case assigned to collection :: {cal_less_than_70}")
            assert False
        else:
            print("Paid percentage is above 70% in case assigned to collection")

    @pytest.mark.skip
    def test_filingInProgress_2emi(self, url):
        global paidBeforeLetter, paidAfterLetter, total_emi_amt, emi3_amount, paidBeforeLetter_3, paidAfterLetter_3, total_emi_amt_3, fillingInProgress_lid

        # print("summons_data::",summons_data)

        pp_gt_70_2emi_lid_f = []

        fillingInProgress_lid = []

        # print("case_lid::",case_lid)

        for s in fillingInProgress_data:
            if s['Loan ID']:
                fillingInProgress_lid.append(s['Loan ID'])

            if s["Emi 1 status"] == "UNPAID" and s["Emi 2 status"] == "UNPAID":
                if s["Emi 3 amount"] == "-" and s["Emi 4 amount"] == "-":

                    emi1_amount = int(s["Emi 1 amount"].replace(",", ""))
                    emi2_amount = int(s["Emi 2 amount"].replace(",", ""))

                    total_emi_amt = emi1_amount + emi2_amount

                    # print("total_emi_amt::",total_emi_amt)

                    # print("loan_id::",s["Loan ID"])

                    if s["Amount paid (before letter)"]:
                        paidBeforeLetter = int(s["Amount paid (before letter)"].replace(",", ""))

                    if s["Amount paid (after letter)"]:
                        paidAfterLetter = int(s["Amount paid (after letter)"].replace(",", ""))

                    totalPaid = paidBeforeLetter + paidAfterLetter
                    # print("totalPaid::",totalPaid)

                    pp_emi_2 = round((totalPaid / total_emi_amt) * 100, 0)
                    # print("pp_emi_2::",pp_emi_2)

                    if pp_emi_2 > 70.0:
                        pp_gt_70_2emi_lid_f.append(s['Loan ID'])
                        # print("pp_emi_2::",pp_emi_2)

        pp_2emi_miss_in_ca_lid_f = []
        for l in pp_gt_70_2emi_lid_f:
            if l not in case_lid:
                pp_2emi_miss_in_ca_lid_f.append(l)

        if len(pp_2emi_miss_in_ca_lid_f) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 2 emi in fillingInProgress ::{pp_2emi_miss_in_ca_lid_f}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 2 emi in fillingInProgress ***")

    #
    #

    @pytest.mark.skip
    def test_filingInProgress_3emi(self, url):

        global paidBeforeLetter_3, paidAfterLetter_3, pp_emi_3

        pp_gt_70_3emi_lid_f = []
        for f in fillingInProgress_data:

            if f["Emi 3 amount"] == "UNPAID":
                emi1_amount_e3 = int(f["Emi 1 amount"].replace(",", ""))
                emi2_amount_e3 = int(f["Emi 2 amount"].replace(",", ""))
                # print("emi1_amount::",emi1_amount)

                if f["Emi 3 amount"] != "-":

                    emi3_amount_e3 = int(f["Emi 3 amount"].replace(",", ""))
                    # print("emi3_amount_e3::",emi3_amount_e3)

                    total_emi_amt_3 = emi1_amount_e3 + emi2_amount_e3 + emi3_amount_e3
                    # print("total_emi_amt_3::",total_emi_amt_3)

                    if f["Amount paid (before letter)"]:
                        paidBeforeLetter_3 = int(f["Amount paid (before letter)"].replace(",", ""))

                    if f["Amount paid (after letter)"]:
                        paidAfterLetter_3 = int(f["Amount paid (after letter)"].replace(",", ""))

                    # print("loan_id::", s["Loan ID"])

                    totalPaid_3 = paidBeforeLetter_3 + paidAfterLetter_3
                    # print("totalPaid_3::",totalPaid_3)

                    pp_emi_3 = round((totalPaid_3 / total_emi_amt_3) * 100, 2)
                    # print("pp_emi_3::",pp_emi_3)

                    if pp_emi_3 > 70.0:
                        pp_gt_70_3emi_lid_f.append(f['Loan ID'])

        pp_3emi_miss_in_ca_lid = []
        for ll in pp_gt_70_3emi_lid_f:
            if ll not in case_lid:
                pp_3emi_miss_in_ca_lid.append(ll)

        if len(pp_3emi_miss_in_ca_lid) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi in fillingInProgress::{pp_3emi_miss_in_ca_lid}")
            assert False
        else:
            print("*** paid percentage less than 70 for 3 emi in fillingInProgress ***")

    @pytest.mark.skip
    def test_filingInprogress_emi_70(self, url):

        global paidEMIAmt, emiAmt
        s_e_lid = []
        pp_more_than_70_filingInProgres_lid = []

        for e in fillingInProgress_lid:
            emi = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                               params={"loanId": e}, verify=False)

            emi_data = emi.json()["data"]["EMIData"]
            # print("emi_data::",emi_data)

            for n, ed in enumerate(emi_data):
                # if n == 2:
                #     break

                if ed["status"] == "UNPAID":
                    # s_e_lid.append(e)
                    # if ed["paidEmiAmount"]:
                    paidEMIAmt = ed["paidEmiAmount"]
                    # print("paidEMIAmt::",paidEMIAmt)

                    # if ed["emiAmount"]:
                    emiAmt = ed["emiAmount"]
                    # print("emiAmt::",emiAmt)

                    pp_f = round((paidEMIAmt / emiAmt) * 100, 0)

                    if pp_f >= 70.0:
                        pp_more_than_70_filingInProgres_lid.append(e)

        print("pp_more_than_70_filingInProgres::", pp_more_than_70_filingInProgres_lid)

        pp_more_than_70_filingInProgres_lid_missed_collection = []
        for m in pp_more_than_70_filingInProgres_lid:
            if m not in case_lid:
                pp_more_than_70_filingInProgres_lid_missed_collection.append(m)

        if len(pp_more_than_70_filingInProgres_lid_missed_collection) > 0:
            print(
                f"Error:: missing of pp_more_than_70_filingInProgres found with collection::{pp_more_than_70_filingInProgres_lid_missed_collection}")
            assert False
        else:
            print("*** paid percentage inside filing in progress is below 70 % ***")

    # @pytest.mark.skip
    def test_notice_sent_unpaid_emi_total_70(self, url):

        global paidEMIAmt, emiAmt

        pp_more_than_70_notice_sent_lid = []

        for o,l in enumerate(lIdNS):
            # if o == 5:
            #     break
            emi = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                               params={"loanId": l}, verify=False)

            emi_data_2 = emi.json()["data"]["EMIData"]
            # print("emi_data::",emi_data)

            paid_emi = []
            emi_amt = []

            for n, ed in enumerate(emi_data_2):
                # if n == 5:
                #     break

                if ed["status"] == "UNPAID":
                    # s_e_lid.append(e)
                    # if ed["paidEmiAmount"]:
                    paidEMIAmt = ed["paidEmiAmount"]
                    paid_emi.append(paidEMIAmt)
                    # print("paidEMIAmt::",paidEMIAmt)

                    # if ed["emiAmount"]:
                    emiAmt = ed["emiAmount"]
                    emi_amt.append(emiAmt)
                    # print("emiAmt::",emiAmt)

                    # print("lid::",l)
                    # print("paid_emi::",paidEMIAmt)
                    # print("emiAmt::",emiAmt)
                    # print("ed::",ed)

            # print("paid_emi::",paid_emi)
            # print("emi_amt::",emi_amt)

            total_paid_emi = sum(paid_emi)
            total_emi = sum(emi_amt)

            # print("lid::",l)
            # print("total_paid_emi::",total_paid_emi)
            # print("total_emi::",total_emi)

            pp_f = round((total_paid_emi / total_emi) * 100, 0)

            if pp_f >= 70.0:
                pp_more_than_70_notice_sent_lid.append(l)

        # print("pp_more_than_70_notice_sent_lid::", pp_more_than_70_notice_sent_lid)

        pp_more_than_70_noticeSent_unpaid_total_lid_missed_collection = []
        for n in pp_more_than_70_notice_sent_lid:
            if n not in case_lid:
                pp_more_than_70_noticeSent_unpaid_total_lid_missed_collection.append(n)

        if len(pp_more_than_70_noticeSent_unpaid_total_lid_missed_collection) > 0:
            print(
                f"Error:: missing of pp_more_than_70_notice_sent found with collection::{pp_more_than_70_noticeSent_unpaid_total_lid_missed_collection}")
            assert False
        else:
            print("*** paid percentage inside notice sent is below 70 % for unpaid total ***")


    @pytest.mark.skip
    def test_notice_sent_paid_unpaid_as_per_emi_70(self, url):

        global paidEMIAmt, emiAmt

        pp_more_than_70_notice_sent_per_emi_lid = []

        for p, e in enumerate(lIdNS):
            # if o == 5:
            #     break
            emi = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                               params={"loanId": e}, verify=False)

            emi_data_2 = emi.json()["data"]["EMIData"]
            # print("emi_data::",emi_data)

            paid_emi_2 = []
            emi_amt_2 = []

            for n, ed in enumerate(emi_data_2):
                # if n == 5:
                #     break

                if ed["status"] == "UNPAID":
                    if ed["status"] == "PAID":
                        # s_e_lid.append(e)
                        # if ed["paidEmiAmount"]:
                        paidEMIAmt = ed["paidEmiAmount"]
                        paid_emi_2.append(paidEMIAmt)

                        # print("paidEMIAmt::",paidEMIAmt)

                        # if ed["emiAmount"]:
                        emiAmt = ed["emiAmount"]
                        emi_amt_2.append(emiAmt)

                        # print("emiAmt::",emiAmt)

                        # print("lid::",l)
                        # print("paid_emi::",paidEMIAmt)
                        # print("emiAmt::",emiAmt)

            total_paid_emi_2 = sum(paid_emi_2)
            total_emi_2 = sum(emi_amt_2)

            print("lid::",e)
            print("total_paid_emi_2::",total_paid_emi_2)
            print("total_emi_2::",total_emi_2)

            pp_f_2 = round((total_paid_emi_2 / total_emi_2) * 100, 0)

            if pp_f_2 >= 70.0:
                pp_more_than_70_notice_sent_per_emi_lid.append(e)

        # print("pp_more_than_70_notice_sent_lid::", pp_more_than_70_notice_sent_lid)

        pp_more_than_70_noticeSent_per_emi_lid_missed_collection = []
        for r in pp_more_than_70_notice_sent_per_emi_lid:
            if r not in case_lid:
                pp_more_than_70_noticeSent_per_emi_lid_missed_collection.append(r)


        if len(pp_more_than_70_noticeSent_per_emi_lid_missed_collection) > 0:
            print(
                f"Error:: missing of pp_more_than_70_notice_sent found with collection for paid-unpaid as per emi ::{pp_more_than_70_noticeSent_per_emi_lid_missed_collection}")
            assert False
        else:
            print("*** paid percentage inside notice sent is below 70 % for paid-unpaid as per emi ***")

