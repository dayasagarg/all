import requests
import pytest
from datetime import datetime, timedelta

# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime, "%Y-%m-%d")

prev_30 = currentFullTime - timedelta(days=30)
prev_30Str = datetime.strftime(prev_30, "%Y-%m-%d")


class TestLegal:
    @pytest.fixture
    def url(self):
        global caseAssigned, legalNotice, legalNotice_data
        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{prev_30Str}T10:00:00.000Z",
                                            "endDate": f"{curr_str}T10:00:00.000Z", "type": 11, "adminId": 153,
                                            "download": "true"})

        legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{prev_30Str}T10:00:00.000Z",
                                           "endDate": f"{curr_str}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date

        legalNotice_data = legalNotice.json()["data"]["rows"]

    def test_case_assign_to_collection(self, url):
        global case_lid
        case_data = caseAssigned.json()["data"]["rows"]

        # print("case_data::",case_data)

        case_lid = []

        for c in case_data:
            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])

    def test_legal_notice_2emi_2unpaid(self, url):
        global paidBeforeLetter, paidAfterLetter

        pp_gt_70_2emi_lid_f = []

        for a in legalNotice_data:

            if a["Emi 1 status"] == "UNPAID" and a["Emi 2 status"] == "UNPAID" and a["Emi 3 amount"] == "-" and a[
                "Emi 4 amount"] == "-":

                emi1_amount = int(a["Emi 1 amount"].replace(",", ""))
                emi2_amount = int(a["Emi 2 amount"].replace(",", ""))

                total_emi_amt = emi1_amount + emi2_amount

                if a["Amount paid (before letter)"]:
                    paidBeforeLetter = int(a["Amount paid (before letter)"].replace(",", ""))

                if a["Amount paid (after letter)"]:
                    paidAfterLetter = int(a["Amount paid (after letter)"].replace(",", ""))

                totalPaid = paidBeforeLetter + paidAfterLetter

                pp_emi_2 = round((totalPaid / total_emi_amt) * 100, 0)

                if pp_emi_2 > 70.0:
                    pp_gt_70_2emi_lid_f.append(a['Loan ID'])

        pp_2emi_miss_in_ca_lid_f_2_unpaid = []
        for b in pp_gt_70_2emi_lid_f:
            if b not in case_lid:
                pp_2emi_miss_in_ca_lid_f_2_unpaid.append(b)

        if len(pp_2emi_miss_in_ca_lid_f_2_unpaid) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 2 emi, 2 unpaid in notice sent ::{pp_2emi_miss_in_ca_lid_f_2_unpaid}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 2 emi, 2 unpaid in notice sent ***")


    def test_notice_2emi_1unpaid(self, url):
        global paidBeforeLetter_1_u, paidAfterLetter_1_u

        pp_gt_70_2emi_lid_f_1_u = []

        for c in legalNotice_data:

            if c["Emi 1 status"] == "PAID" and c["Emi 2 status"] == "UNPAID" and c["Emi 3 amount"] == "-" and c["Emi 4 amount"] == "-":

                emi2_amount_2emi_1u = int(c["Emi 2 amount"].replace(",", ""))


                if c["Amount paid (before letter)"]:
                    paidBeforeLetter_1_u = int(c["Amount paid (before letter)"].replace(",", ""))

                if c["Amount paid (after letter)"]:
                    paidAfterLetter_1_u = int(c["Amount paid (after letter)"].replace(",", ""))

                totalPaid_1_u = paidBeforeLetter_1_u + paidAfterLetter_1_u


                pp_emi_2_1_u = round((totalPaid_1_u / emi2_amount_2emi_1u) * 100, 0)


                if pp_emi_2_1_u > 70.0:
                    pp_gt_70_2emi_lid_f_1_u.append(c['Loan ID'])


        pp_2emi_miss_in_ca_lid_f_1_unpaid = []
        for d in pp_gt_70_2emi_lid_f_1_u:
            if d not in case_lid:
                pp_2emi_miss_in_ca_lid_f_1_unpaid.append(d)



        if len(pp_2emi_miss_in_ca_lid_f_1_unpaid) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 2 emi, 1 unpaid in notice sent :: {pp_2emi_miss_in_ca_lid_f_1_unpaid}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 2 emi, 1 unpaid in notice sent ***")

    def test_noticeSent_3emi_1paid_2unpaid(self, url):
        global paidBeforeLetter, paidAfterLetter, total_emi_amt_1p_2u, emi3_amount, paidBeforeLetter_1p_2u, paidAfterLetter_1p_2u, total_emi_amt_3, fillingInProgress_lid, pp_gt_70_3emi_lid_f_1p_2u

        pp_gt_70_3emi_lid_f_1p_2u = []

        for e in legalNotice_data:

            if e["Emi 1 status"] == "PAID" and e["Emi 2 status"] == "UNPAID" and e["Emi 3 amount"] == "UNPAID" and e[
                "Emi 4 amount"] == "-":

                emi2_amount_1p_2u = int(e["Emi 2 amount"].replace(",", ""))
                emi3_amount_1p_2u = int(e["Emi 3 amount"].replace(",", ""))

                total_emi_amt_1p_2u = emi2_amount_1p_2u + emi3_amount_1p_2u


                if e["Amount paid (before letter)"]:
                    paidBeforeLetter_1p_2u = int(e["Amount paid (before letter)"].replace(",", ""))

                if e["Amount paid (after letter)"]:
                    paidAfterLetter_1p_2u = int(e["Amount paid (after letter)"].replace(",", ""))

                total_paid_1p_2u = paidBeforeLetter + paidAfterLetter
                # print("totalPaid::",totalPaid)

                pp_emi_3_1p_2u = round((total_paid_1p_2u / total_emi_amt_1p_2u) * 100, 0)
                # print("pp_emi_2::",pp_emi_2)

                if pp_emi_3_1p_2u > 70.0:
                    pp_gt_70_3emi_lid_f_1p_2u.append(e['Loan ID'])
                    # print("pp_emi_2::",pp_emi_2)

        pp_3emi_miss_in_ca_lid_f_1p_2u = []
        for f in pp_gt_70_3emi_lid_f_1p_2u:
            if f not in case_lid:
                pp_3emi_miss_in_ca_lid_f_1p_2u.append(f)

        if len(pp_3emi_miss_in_ca_lid_f_1p_2u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 1 paid, 2 unpaid in notice sent ::{pp_3emi_miss_in_ca_lid_f_1p_2u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 1 paid, 2 unpaid in notice sent ***")

    def test_notice_3emi_2paid_1unpaid(self, url):
        global paidBeforeLetter_2p_1u, paidAfterLetter_2p_1u

        pp_gt_70_3emi_lid_f_2p_1u = []

        for g in legalNotice_data:

            if g["Emi 1 status"] == "PAID" and g["Emi 2 status"] == "PAID" and g["Emi 3 amount"] == "UNPAID" and g["Emi 4 amount"] == "-":

                emi3_amount_2p_1u = int(g["Emi 3 amount"].replace(",", ""))


                if g["Amount paid (before letter)"]:
                    paidBeforeLetter_2p_1u = int(g["Amount paid (before letter)"].replace(",", ""))

                if g["Amount paid (after letter)"]:
                    paidAfterLetter_2p_1u = int(g["Amount paid (after letter)"].replace(",", ""))

                total_paid_2p_1u = paidBeforeLetter_2p_1u + paidAfterLetter_2p_1u


                pp_emi_3_2p_1u = round((total_paid_2p_1u / emi3_amount_2p_1u) * 100, 0)


                if pp_emi_3_2p_1u > 70.0:
                    pp_gt_70_3emi_lid_f_2p_1u.append(g['Loan ID'])


        pp_3emi_miss_in_ca_lid_f_2p_1u = []
        for h in pp_gt_70_3emi_lid_f_2p_1u:
            if h not in case_lid:
                pp_3emi_miss_in_ca_lid_f_2p_1u.append(h)

        if len(pp_3emi_miss_in_ca_lid_f_2p_1u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 2 paid, 1 unpaid in notice sent ::{pp_3emi_miss_in_ca_lid_f_2p_1u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 2 paid, 1 unpaid in notice sent ***")


    def test_notice_3emi_3unpaid(self, url):
        global paidBeforeLetter_3emi_3u, paidAfterLetter_3emi_3u

        pp_gt_70_3emi_lid_f_3u = []


        for i in legalNotice_data:

            if i["Emi 1 status"] == "UNPAID" and i["Emi 2 status"] == "UNPAID" and i["Emi 3 amount"] == "UNPAID" and i[
                "Emi 4 amount"] == "-":

                emi1_amount_3emi_3u = int(i["Emi 1 amount"].replace(",", ""))
                emi2_amount_3emi_3u = int(i["Emi 2 amount"].replace(",", ""))
                emi3_amount_3emi_3u = int(i["Emi 3 amount"].replace(",", ""))

                total_emi_amt_3u = emi1_amount_3emi_3u + emi2_amount_3emi_3u + emi3_amount_3emi_3u


                if i["Amount paid (before letter)"]:
                    paidBeforeLetter_3emi_3u = int(i["Amount paid (before letter)"].replace(",", ""))

                if i["Amount paid (after letter)"]:
                    paidAfterLetter_3emi_3u = int(i["Amount paid (after letter)"].replace(",", ""))

                total_paid_3emi_3u = paidBeforeLetter_3emi_3u + paidAfterLetter_3emi_3u
                # print("totalPaid::",totalPaid)

                pp_emi_3_3u = round((total_paid_3emi_3u / total_emi_amt_3u) * 100, 0)


                if pp_emi_3_3u > 70.0:
                    pp_gt_70_3emi_lid_f_3u.append(i['Loan ID'])


        pp_3emi_miss_in_ca_lid_f_3u = []
        for j in pp_gt_70_3emi_lid_f_3u:
            if j not in case_lid:
                pp_3emi_miss_in_ca_lid_f_3u.append(j)

        if len(pp_3emi_miss_in_ca_lid_f_3u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 3 emi, 3 unpaid in notice sent ::{pp_3emi_miss_in_ca_lid_f_3u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 3 emi, 3 unpaid in notice sent ***")


    def test_notice_4emi_1paid_3unpaid(self, url):
        global paidBeforeLetter_4emi_1p_3u, paidAfterLetter_4emi_1p_3u


        pp_gt_70_4emi_lid_f_1p_3u = []

        for k in legalNotice_data:

            if k["Emi 1 status"] == "PAID" and k["Emi 2 status"] == "UNPAID" and k["Emi 3 amount"] == "UNPAID" and k[
                "Emi 4 amount"] == "UNPAID":

                emi2_amount_1p_3u = int(k["Emi 2 amount"].replace(",", ""))
                emi3_amount_1p_3u = int(k["Emi 3 amount"].replace(",", ""))
                emi4_amount_1p_3u = int(k["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_1p_3u = emi2_amount_1p_3u + emi3_amount_1p_3u + emi4_amount_1p_3u


                if k["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_1p_3u = int(k["Amount paid (before letter)"].replace(",", ""))

                if k["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_1p_3u = int(k["Amount paid (after letter)"].replace(",", ""))


                total_paid_4emi_1p_3u = paidBeforeLetter_4emi_1p_3u + paidAfterLetter_4emi_1p_3u


                pp_emi_4_1p_3u = round((total_paid_4emi_1p_3u / total_emi_amt_4emi_1p_3u) * 100, 0)


                if pp_emi_4_1p_3u > 70.0:
                    pp_gt_70_4emi_lid_f_1p_3u.append(k['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_1p_3u = []
        for l in pp_gt_70_4emi_lid_f_1p_3u:
            if l not in case_lid:
                pp_4emi_miss_in_ca_lid_f_1p_3u.append(l)

        if len(pp_4emi_miss_in_ca_lid_f_1p_3u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 1 paid, 3 unpaid in notice sent ::{pp_4emi_miss_in_ca_lid_f_1p_3u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 1 paid, 3 unpaid in notice sent ***")


    def test_notice_4emi_2paid_2unpaid(self, url):
        global paidBeforeLetter_4emi_2p_2u, paidAfterLetter_4emi_2p_2u

        pp_gt_70_4emi_lid_f_2p_2u = []

        for m in legalNotice_data:

            if m["Emi 1 status"] == "PAID" and m["Emi 2 status"] == "PAID" and m["Emi 3 amount"] == "UNPAID" and m[
                "Emi 4 amount"] == "UNPAID":


                emi3_amount_4emi_2p_2u = int(m["Emi 3 amount"].replace(",", ""))
                emi4_amount_4emi_2p_2u = int(m["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_2p_2u = emi3_amount_4emi_2p_2u + emi4_amount_4emi_2p_2u


                if m["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_2p_2u = int(m["Amount paid (before letter)"].replace(",", ""))

                if m["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_2p_2u = int(m["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_2p_2u = paidBeforeLetter_4emi_2p_2u + paidAfterLetter_4emi_2p_2u


                pp_emi_4_2p_2u = round((total_paid_4emi_2p_2u / total_emi_amt_4emi_2p_2u) * 100, 0)


                if pp_emi_4_2p_2u > 70.0:
                    pp_gt_70_4emi_lid_f_2p_2u.append(m['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_2p_2u = []
        for n in pp_gt_70_4emi_lid_f_2p_2u:
            if n not in case_lid:
                pp_4emi_miss_in_ca_lid_f_2p_2u.append(n)

        if len(pp_4emi_miss_in_ca_lid_f_2p_2u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 2 paid, 2 unpaid in notice sent::{pp_4emi_miss_in_ca_lid_f_2p_2u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 2 paid, 2 unpaid in notice sent ***")

    def test_notice_4emi_3paid_1unpaid(self, url):
        global paidBeforeLetter_4emi_3p_1u, paidAfterLetter_4emi_3p_1u

        pp_gt_70_4emi_lid_f_3p_1u = []

        for o in legalNotice_data:

            if o["Emi 1 status"] == "PAID" and o["Emi 2 status"] == "PAID" and o["Emi 3 amount"] == "PAID" and o[
                "Emi 4 amount"] == "UNPAID":


                emi4_amount_4emi_3p_1u = int(o["Emi 4 amount"].replace(",", ""))


                if o["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_3p_1u = int(o["Amount paid (before letter)"].replace(",", ""))

                if o["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_3p_1u = int(o["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_3p_1u = paidBeforeLetter_4emi_3p_1u + paidAfterLetter_4emi_3p_1u


                pp_emi_4_3p_1u = round((total_paid_4emi_3p_1u / emi4_amount_4emi_3p_1u) * 100, 0)


                if pp_emi_4_3p_1u > 70.0:
                    pp_gt_70_4emi_lid_f_3p_1u.append(o['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_3p_1u = []
        for p in pp_gt_70_4emi_lid_f_3p_1u:
            if p not in case_lid:
                pp_4emi_miss_in_ca_lid_f_3p_1u.append(p)

        if len(pp_4emi_miss_in_ca_lid_f_3p_1u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 3 paid, 1 unpaid in notice sent ::{pp_4emi_miss_in_ca_lid_f_3p_1u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 3 paid, 1 unpaid in notice sent ***")

    def test_notice_4emi_4unpaid(self, url):
        global paidBeforeLetter_4emi_4u, paidAfterLetter_4emi_4u

        pp_gt_70_4emi_lid_f_4u = []

        for k in legalNotice_data:

            if k["Emi 1 status"] == "UNPAID" and k["Emi 2 status"] == "UNPAID" and k["Emi 3 amount"] == "UNPAID" and k[
                "Emi 4 amount"] == "UNPAID":

                emi1_amount_4emi_4u = int(k["Emi 1 amount"].replace(",", ""))
                emi2_amount_4emi_4u = int(k["Emi 2 amount"].replace(",", ""))
                emi3_amount_4emi_4u = int(k["Emi 3 amount"].replace(",", ""))
                emi4_amount_4emi_4u = int(k["Emi 4 amount"].replace(",", ""))

                total_emi_amt_4emi_4u = emi1_amount_4emi_4u + emi2_amount_4emi_4u + emi3_amount_4emi_4u + emi4_amount_4emi_4u


                if k["Amount paid (before letter)"]:
                    paidBeforeLetter_4emi_4u = int(k["Amount paid (before letter)"].replace(",", ""))

                if k["Amount paid (after letter)"]:
                    paidAfterLetter_4emi_4u = int(k["Amount paid (after letter)"].replace(",", ""))

                total_paid_4emi_4u = paidBeforeLetter_4emi_4u + paidAfterLetter_4emi_4u


                pp_emi4_4u = round((total_paid_4emi_4u / total_emi_amt_4emi_4u) * 100, 0)


                if pp_emi4_4u > 70.0:
                    pp_gt_70_4emi_lid_f_4u.append(k['Loan ID'])


        pp_4emi_miss_in_ca_lid_f_4u = []
        for l in pp_gt_70_4emi_lid_f_4u:
            if l not in case_lid:
                pp_4emi_miss_in_ca_lid_f_4u.append(l)

        if len(pp_4emi_miss_in_ca_lid_f_4u) > 0:
            print(
                f"Error:: paid percentage more than 70 found for 4 emi, 4 unpaid in notice sent ::{pp_4emi_miss_in_ca_lid_f_4u}")
            assert False
        else:
            print("*** remaining paid percentage less than 70 for 4 emi, 4 unpaid in notice sent ***")

