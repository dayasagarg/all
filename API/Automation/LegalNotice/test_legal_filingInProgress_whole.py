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

    #


    # @pytest.mark.skip
    def test_case_assign_to_collection_1(self,url):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid
        case_data = caseAssigned.json()["data"]["rows"]

        # print("case_data::",case_data)

        case_lid = []


        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])
            # print(c)


    def test_filingInProgress_2emi_2unpaid(self, url):
        global paidBeforeLetter, paidAfterLetter, total_emi_amt, emi3_amount, paidBeforeLetter_3, paidAfterLetter_3, total_emi_amt_3, fillingInProgress_lid

        # print("summons_data::",summons_data)

        pp_gt_70_2emi_lid_f = []

        fillingInProgress_lid = []

        # print("case_lid::",case_lid)

        for s in fillingInProgress_data:
            if s['Loan ID']:
                fillingInProgress_lid.append(s['Loan ID'])

            if s["Emi 1 status"] == "UNPAID" and s["Emi 2 status"] == "UNPAID" and s["Emi 3 amount"] == "-" and s["Emi 4 amount"] == "-":


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

        pp_2emi_miss_in_ca_lid_f_2_unpaid = []
        for l in pp_gt_70_2emi_lid_f:
            if l not in case_lid:
                pp_2emi_miss_in_ca_lid_f_2_unpaid.append(l)



        if len(pp_2emi_miss_in_ca_lid_f_2_unpaid) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 2 emi, 2 unpaid in fillingInProgress ::{pp_2emi_miss_in_ca_lid_f_2_unpaid}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 2 emi, 2 unpaid in fillingInProgress ***")

    #


    def test_filingInProgress_2emi_1unpaid(self, url):
        global paidBeforeLetter_1_u, paidAfterLetter_1_u



        pp_gt_70_2emi_lid_f_1_u = []





        for o in fillingInProgress_data:


            if o["Emi 1 status"] == "PAID" and o["Emi 2 status"] == "UNPAID" and o["Emi 3 amount"] == "-" and o["Emi 4 amount"] == "-":



                emi2_amount_2emi_1u = int(o["Emi 2 amount"].replace(",", ""))



                # print("total_emi_amt::",total_emi_amt)

                # print("loan_id::",s["Loan ID"])

                if o["Amount paid (before letter)"]:
                    paidBeforeLetter_1_u = int(o["Amount paid (before letter)"].replace(",", ""))

                if o["Amount paid (after letter)"]:
                    paidAfterLetter_1_u = int(o["Amount paid (after letter)"].replace(",", ""))

                totalPaid_1_u = paidBeforeLetter_1_u + paidAfterLetter_1_u
                # print("totalPaid::",totalPaid)

                pp_emi_2_1_u = round((totalPaid_1_u / emi2_amount_2emi_1u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_2_1_u > 70.0:
                    pp_gt_70_2emi_lid_f_1_u.append(o['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)

        pp_2emi_miss_in_ca_lid_f_1_unpaid = []
        for m in pp_gt_70_2emi_lid_f_1_u:
            if m not in case_lid:
                pp_2emi_miss_in_ca_lid_f_1_unpaid.append(m)



        if len(pp_2emi_miss_in_ca_lid_f_1_unpaid) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 2 emi, 1 unpaid in fillingInProgress :: {pp_2emi_miss_in_ca_lid_f_1_unpaid}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 2 emi, 1 unpaid in fillingInProgress ***")



    def test_filingInProgress_3emi_1paid_2unpaid(self, url):
        global paidBeforeLetter, paidAfterLetter, total_emi_amt_1p_2u, emi3_amount, paidBeforeLetter_1p_2u, paidAfterLetter_1p_2u, total_emi_amt_3, fillingInProgress_lid, pp_gt_70_3emi_lid_f_1p_2u

        # print("summons_data::",summons_data)

        pp_gt_70_3emi_lid_f_1p_2u = []



        # print("case_lid::",case_lid)

        for t in fillingInProgress_data:


            if t["Emi 1 status"] == "PAID" and t["Emi 2 status"] == "UNPAID" and t["Emi 3 amount"] == "UNPAID" and t["Emi 4 amount"] == "-":



                emi2_amount_1p_2u = int(t["Emi 2 amount"].replace(",", ""))
                emi3_amount_1p_2u = int(t["Emi 3 amount"].replace(",", ""))

                total_emi_amt_1p_2u = emi2_amount_1p_2u + emi3_amount_1p_2u

                # print("total_emi_amt::",total_emi_amt)

                # print("loan_id::",s["Loan ID"])

                if t["Amount paid (before letter)"]:
                    paidBeforeLetter_1p_2u = int(t["Amount paid (before letter)"].replace(",", ""))

                if t["Amount paid (after letter)"]:
                    paidAfterLetter_1p_2u = int(t["Amount paid (after letter)"].replace(",", ""))

                total_paid_1p_2u = paidBeforeLetter + paidAfterLetter
                # print("totalPaid::",totalPaid)

                pp_emi_3_1p_2u = round((total_paid_1p_2u / total_emi_amt_1p_2u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_3_1p_2u > 70.0:
                    pp_gt_70_3emi_lid_f_1p_2u.append(t['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)


        pp_3emi_miss_in_ca_lid_f_1p_2u = []
        for n in pp_gt_70_3emi_lid_f_1p_2u:
            if n not in case_lid:
                pp_3emi_miss_in_ca_lid_f_1p_2u.append(n)


        if len(pp_3emi_miss_in_ca_lid_f_1p_2u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 1 paid, 2 unpaid in fillingInProgress ::{pp_3emi_miss_in_ca_lid_f_1p_2u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 1 paid, 2 unpaid in fillingInProgress ***")

    #
    def test_filingInProgress_3emi_2paid_1unpaid(self, url):
        global paidBeforeLetter_2p_1u, paidAfterLetter_2p_1u

        # print("summons_data::",summons_data)

        pp_gt_70_3emi_lid_f_2p_1u = []

        fillingInProgress_lid = []

        # print("case_lid::",case_lid)

        for u in fillingInProgress_data:
            if u['Loan ID']:
                fillingInProgress_lid.append(u['Loan ID'])

            if u["Emi 1 status"] == "PAID" and u["Emi 2 status"] == "PAID" and u["Emi 3 amount"] == "UNPAID" and u["Emi 4 amount"] == "-":

                emi3_amount_2p_1u = int(u["Emi 3 amount"].replace(",", ""))

                # print("total_emi_amt::",total_emi_amt)

                # print("loan_id::",u["Loan ID"])

                if u["Amount paid (before letter)"]:
                    paidBeforeLetter_2p_1u = int(u["Amount paid (before letter)"].replace(",", ""))

                if u["Amount paid (after letter)"]:
                    paidAfterLetter_2p_1u = int(u["Amount paid (after letter)"].replace(",", ""))

                total_paid_2p_1u = paidBeforeLetter_2p_1u + paidAfterLetter_2p_1u
                # print("totalPaid::",totalPaid)

                pp_emi_3_2p_1u = round((total_paid_2p_1u / emi3_amount_2p_1u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_3_2p_1u > 70.0:
                    pp_gt_70_3emi_lid_f_2p_1u.append(u['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)


        pp_3emi_miss_in_ca_lid_f_2p_1u = []
        for p in pp_gt_70_3emi_lid_f_2p_1u:
            if p not in case_lid:
                pp_3emi_miss_in_ca_lid_f_2p_1u.append(p)


        if len(pp_3emi_miss_in_ca_lid_f_2p_1u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 2 paid, 1 unpaid in fillingInProgress ::{pp_3emi_miss_in_ca_lid_f_2p_1u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 2 paid, 1 unpaid in fillingInProgress ***")
    #
    def test_filingInProgress_3emi_3unpaid(self, url):
        global paidBeforeLetter_3emi_3u, paidAfterLetter_3emi_3u

        # print("summons_data::",summons_data)

        pp_gt_70_3emi_lid_f_3u = []


        for q in fillingInProgress_data:

            if q["Emi 1 status"] == "UNPAID" and q["Emi 2 status"] == "UNPAID" and q["Emi 3 amount"] == "UNPAID" and q[
                "Emi 4 amount"] == "-":

                emi1_amount_3emi_3u = int(q["Emi 1 amount"].replace(",", ""))
                emi2_amount_3emi_3u = int(q["Emi 2 amount"].replace(",", ""))
                emi3_amount_3emi_3u = int(q["Emi 3 amount"].replace(",", ""))

                total_emi_amt_3u = emi1_amount_3emi_3u + emi2_amount_3emi_3u + emi3_amount_3emi_3u

                # print("total_emi_amt::",total_emi_amt)

                # print("loan_id::",q["Loan ID"])

                if q["Amount paid (before letter)"]:
                    paidBeforeLetter_3emi_3u = int(q["Amount paid (before letter)"].replace(",", ""))

                if q["Amount paid (after letter)"]:
                    paidAfterLetter_3emi_3u = int(q["Amount paid (after letter)"].replace(",", ""))

                total_paid_3emi_3u = paidBeforeLetter_3emi_3u + paidAfterLetter_3emi_3u
                # print("totalPaid::",totalPaid)

                pp_emi_3_3u = round((total_paid_3emi_3u / total_emi_amt_3u) * 100, 0)


                if pp_emi_3_3u > 70.0:
                    pp_gt_70_3emi_lid_f_3u.append(q['Loan ID'])


        pp_3emi_miss_in_ca_lid_f_3u = []
        for r in pp_gt_70_3emi_lid_f_3u:
            if r not in case_lid:
                pp_3emi_miss_in_ca_lid_f_3u.append(r)

        if len(pp_3emi_miss_in_ca_lid_f_3u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 3 unpaid in fillingInProgress ::{pp_3emi_miss_in_ca_lid_f_3u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 3 unpaid in fillingInProgress ***")


    def test_filingInProgress_4emi_1paid_3unpaid(self, url):
        global paidBeforeLetter_4emi_1p_3u, paidAfterLetter_4emi_1p_3u


        pp_gt_70_4emi_lid_f_1p_3u = []

        for v in fillingInProgress_data:

            if v["Emi 1 status"] == "PAID" and v["Emi 2 status"] == "UNPAID" and v["Emi 3 amount"] == "UNPAID" and v[
                "Emi 4 amount"] == "UNPAID":

                emi2_amount_1p_3u = int(v["Emi 2 amount"].replace(",", ""))
                emi3_amount_1p_3u = int(v["Emi 3 amount"].replace(",", ""))
                emi4_amount_1p_3u = int(v["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_1p_3u = emi2_amount_1p_3u + emi3_amount_1p_3u + emi4_amount_1p_3u


                if v["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_1p_3u = int(v["Amount paid (before letter)"].replace(",", ""))

                if v["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_1p_3u = int(v["Amount paid (after letter)"].replace(",", ""))


                total_paid_4emi_1p_3u = paidBeforeLetter_4emi_1p_3u + paidAfterLetter_4emi_1p_3u
                # print("totalPaid::",totalPaid)

                pp_emi_4_1p_3u = round((total_paid_4emi_1p_3u / total_emi_amt_4emi_1p_3u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_4_1p_3u > 70.0:
                    pp_gt_70_4emi_lid_f_1p_3u.append(v['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)

        pp_4emi_miss_in_ca_lid_f_1p_3u = []
        for w in pp_gt_70_4emi_lid_f_1p_3u:
            if w not in case_lid:
                pp_4emi_miss_in_ca_lid_f_1p_3u.append(w)

        if len(pp_4emi_miss_in_ca_lid_f_1p_3u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 1 paid, 3 unpaid in fillingInProgress ::{pp_4emi_miss_in_ca_lid_f_1p_3u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 1 paid, 3 unpaid in fillingInProgress ***")


    def test_filingInProgress_4emi_2paid_2unpaid(self, url):
        global paidBeforeLetter_4emi_2p_2u, paidAfterLetter_4emi_2p_2u

        pp_gt_70_4emi_lid_f_2p_2u = []

        # print("case_lid::",case_lid)

        for x in fillingInProgress_data:

            if x["Emi 1 status"] == "PAID" and x["Emi 2 status"] == "PAID" and x["Emi 3 amount"] == "UNPAID" and x[
                "Emi 4 amount"] == "UNPAID":


                emi3_amount_4emi_2p_2u = int(x["Emi 3 amount"].replace(",", ""))
                emi4_amount_4emi_2p_2u = int(x["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_2p_2u = emi3_amount_4emi_2p_2u + emi4_amount_4emi_2p_2u


                if x["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_2p_2u = int(x["Amount paid (before letter)"].replace(",", ""))

                if x["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_2p_2u = int(x["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_2p_2u = paidBeforeLetter_4emi_2p_2u + paidAfterLetter_4emi_2p_2u
                # print("totalPaid::",totalPaid)

                pp_emi_4_2p_2u = round((total_paid_4emi_2p_2u / total_emi_amt_4emi_2p_2u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_4_2p_2u > 70.0:
                    pp_gt_70_4emi_lid_f_2p_2u.append(x['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)

        pp_4emi_miss_in_ca_lid_f_2p_2u = []
        for y in pp_gt_70_4emi_lid_f_2p_2u:
            if y not in case_lid:
                pp_4emi_miss_in_ca_lid_f_2p_2u.append(y)

        if len(pp_4emi_miss_in_ca_lid_f_2p_2u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 2 paid, 2 unpaid in fillingInProgress ::{pp_4emi_miss_in_ca_lid_f_2p_2u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 2 paid, 2 unpaid in fillingInProgress ***")


    def test_filingInProgress_4emi_3paid_1unpaid(self, url):
        global paidBeforeLetter_4emi_3p_1u, paidAfterLetter_4emi_3p_1u

        pp_gt_70_4emi_lid_f_3p_1u = []



        for x in fillingInProgress_data:

            if x["Emi 1 status"] == "PAID" and x["Emi 2 status"] == "PAID" and x["Emi 3 amount"] == "PAID" and x[
                "Emi 4 amount"] == "UNPAID":


                emi4_amount_4emi_3p_1u = int(x["Emi 4 amount"].replace(",", ""))



                if x["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_3p_1u = int(x["Amount paid (before letter)"].replace(",", ""))

                if x["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_3p_1u = int(x["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_3p_1u = paidBeforeLetter_4emi_3p_1u + paidAfterLetter_4emi_3p_1u


                pp_emi_4_3p_1u = round((total_paid_4emi_3p_1u / emi4_amount_4emi_3p_1u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_4_3p_1u > 70.0:
                    pp_gt_70_4emi_lid_f_3p_1u.append(x['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_3p_1u = []
        for y in pp_gt_70_4emi_lid_f_3p_1u:
            if y not in case_lid:
                pp_4emi_miss_in_ca_lid_f_3p_1u.append(y)

        if len(pp_4emi_miss_in_ca_lid_f_3p_1u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 3 paid, 1 unpaid in fillingInProgress ::{pp_4emi_miss_in_ca_lid_f_3p_1u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 3 paid, 1 unpaid in fillingInProgress ***")


    def test_filingInProgress_4emi_4unpaid(self, url):
        global paidBeforeLetter_4emi_4u, paidAfterLetter_4emi_4u

        pp_gt_70_4emi_lid_f_4u = []

        for x in fillingInProgress_data:

            if x["Emi 1 status"] == "UNPAID" and x["Emi 2 status"] == "UNPAID" and x["Emi 3 amount"] == "UNPAID" and x[
                "Emi 4 amount"] == "UNPAID":

                emi1_amount_4emi_4u = int(x["Emi 1 amount"].replace(",", ""))
                emi2_amount_4emi_4u = int(x["Emi 2 amount"].replace(",", ""))
                emi3_amount_4emi_4u = int(x["Emi 3 amount"].replace(",", ""))
                emi4_amount_4emi_4u = int(x["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_4u = emi1_amount_4emi_4u + emi2_amount_4emi_4u + emi3_amount_4emi_4u + emi4_amount_4emi_4u


                if x["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_4u = int(x["Amount paid (before letter)"].replace(",", ""))

                if x["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_4u = int(x["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_4u = paidBeforeLetter_4emi_4u + paidAfterLetter_4emi_4u


                pp_emi4_4u = round((total_paid_4emi_4u / total_emi_amt_4emi_4u) * 100, 0)


                if pp_emi4_4u > 70.0:
                    pp_gt_70_4emi_lid_f_4u.append(x['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_4u = []
        for y in pp_gt_70_4emi_lid_f_4u:
            if y not in case_lid:
                pp_4emi_miss_in_ca_lid_f_4u.append(y)

        if len(pp_4emi_miss_in_ca_lid_f_4u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 4 unpaid in fillingInProgress ::{pp_4emi_miss_in_ca_lid_f_4u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 4 unpaid in fillingInProgress ***")

