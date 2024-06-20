import requests
import pytest
from datetime import datetime, timedelta


currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")

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
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3,caseAssigned,fillingInProgress, fillingInProgress_data, case_data
        legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
                                                 "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date

        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                           "endDate": f"{end_date_2}T10:00:00.000Z", "type": 11, "adminId": 153,
                                           "download": "true"})

        case_data = caseAssigned.json()["data"]["rows"]

        fillingInProgress = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                               params={"page": 1, "startDate": f"{start_3_DateStr}T10:00:00.000Z",
                                       "endDate": f"{curr_str}T10:00:00.000Z", "type": 4, "adminId": 70,
                                       "download": "true"})


        fillingInProgress_data = fillingInProgress.json()["data"]["rows"]



    # @pytest.mark.skip
    def test_case_assign_to_collection_1(self,url):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid

        # print("case_data::",case_data)

        case_lid = []

        perc_loanId = []

        cal_less_than_70 = []
        # paidPrincipleInterest = []
        # principleInterest = []
        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])
            # print(c)


    # @pytest.mark.skip
    def test_filingInProgress_2emi(self,url):
        global paidBeforeLetter, paidAfterLetter, total_emi_amt, emi3_amount, paidBeforeLetter_3, paidAfterLetter_3,total_emi_amt_3, fillingInProgress_lid

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

                    pp_emi_2 = round((totalPaid/total_emi_amt) * 100, 0)
                    # print("pp_emi_2::",pp_emi_2)

                    if pp_emi_2 > 70.0:
                        pp_gt_70_2emi_lid_f.append(s['Loan ID'])
                        # print("pp_emi_2::",pp_emi_2)

        pp_2emi_miss_in_ca_lid_f = []
        for l in pp_gt_70_2emi_lid_f:
            if l not in case_lid:
                pp_2emi_miss_in_ca_lid_f.append(l)


        if len(pp_2emi_miss_in_ca_lid_f) > 0:
            print(f"Error:: paid percentage more than 70 found for 2 emi in fillingInProgress ::{pp_2emi_miss_in_ca_lid_f}")
            assert False
        else:
            print("*** paid percentage less than 70 for 2 emi in fillingInProgress ***")
    #
    #


    @pytest.mark.skip
    def test_filingInProgress_3emi(self, url):

        global paidBeforeLetter_3, paidAfterLetter_3, pp_emi_3

        pp_gt_70_3emi_lid_f = []
        for f in fillingInProgress_data:

            if f["Emi 3 amount"]== "UNPAID":
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

                    pp_emi_3 = round((totalPaid_3/total_emi_amt_3) * 100,2)
                    # print("pp_emi_3::",pp_emi_3)

                    if pp_emi_3 > 70.0:
                        pp_gt_70_3emi_lid_f.append(f['Loan ID'])

        pp_3emi_miss_in_ca_lid = []
        for ll in pp_gt_70_3emi_lid_f:
            if ll not in case_lid:
                pp_3emi_miss_in_ca_lid.append(ll)


        if len(pp_3emi_miss_in_ca_lid) > 0:
            print(f"Error:: paid percentage more than 70 found for 3 emi in fillingInProgress::{pp_3emi_miss_in_ca_lid}")
            assert False
        else:
            print("*** paid percentage less than 70 for 3 emi in fillingInProgress ***")


    # @pytest.mark.skip
    def test_filingInprogress_per_emi_70(self, url):

        global paidEMIAmt, emiAmt

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

        print("pp_more_than_70_filingInProgres_lid::", pp_more_than_70_filingInProgres_lid)

        pp_more_than_70_filingInProgres_lid_missed_collection = []
        for m in pp_more_than_70_filingInProgres_lid:
            if m not in case_lid:
                pp_more_than_70_filingInProgres_lid_missed_collection.append(m)


        if len(pp_more_than_70_filingInProgres_lid_missed_collection) > 0:
            print(
                f"Error:: missing of pp_more_than_70_filingInProgres per emi found with collection::{pp_more_than_70_filingInProgres_lid_missed_collection}")
            assert False
        else:
            print("*** paid percentage inside filing in progress for per emi is below 70 % ***")


