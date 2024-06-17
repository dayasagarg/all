import pytest
import requests
import json
import math
from datetime import datetime, timedelta

# from 14 May 2024



currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format

previousDate = currentFullTime - timedelta(days=15)
previousDateStr = datetime.strftime(previousDate, "%Y-%m-%d")

class TestFCC:
    def test_getRepayment_fcc(self):
        global fcc_cal

        responseAllLoanID = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{previousDateStr}T10:00:00.000Z", "end_date": f"{currentDateStr}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date


        '''getting loan ids from Repayment'''
        repay_d = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)

        prep_lid = []
        for d in repay_d:
            if (datetime.strptime(d["Disbursement date"], "%d-%m-%Y")) > datetime.strptime("14-05-2024", "%d-%m-%Y"):


                # fcc = d["Foreclosure Charge"]

                if d["Repaid flag"] == "Pre-Paid":
                    if d["Loan id"]:
                        prep_lid.append(d["Loan id"])

                    #     print("lid::", d["Loan id"])
                    # fcc_cal = math.ceil(0.04 * d["Principal"])
                    #
                    # print("fcc_cal::",fcc_cal)
                    #
                    #
                    # print("fcc::",fcc)

        # print("prep_lid::",prep_lid)



        prep_lid_3 = []
        for n, d in enumerate(repay_d):

            if d.get("Repaid flag") == "Pre-Paid":
                if "FULLPAY" in d["EMI Types"]:
                    disbursement_date = datetime.strptime(d["Disbursement date"], "%d-%m-%Y")
                    repaid_date = datetime.strptime(d["Repaid Date"], "%d-%m-%Y")
                    if repaid_date < (disbursement_date + timedelta(days=3)):
                        # print("Disbursement Date + 3 days:", disbursement_date + timedelta(days=3))
                        # print("Repaid Date:", repaid_date)
                        # print("Loan id if paid within 3 days:", d.get("Loan id"))
                        prep_lid_3.append(d.get("Loan id"))



        print("prep_lid_3::",prep_lid_3)

        fcc_issue = []

        for n, t in enumerate(prep_lid_3):

            trans = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": t},
                verify=False)  # current date

            tran_d = trans.json()["data"]


            for td in tran_d:
                if td["Pay type"] == "FULLPAY":
                    print("lid::",t)

                    fcc = td["For closure charge"]

                    print("fcc::",fcc)

                    # fcc_cal = math.ceil(math.ceil(0.04 * td["Principal"]) + (math.ceil(0.04 * td["Principal"])*0.18))

                    fcc_cal = math.ceil(math.ceil(0.04 * td["Principal"] + (0.04 * td["Principal"]) * 0.18))

                    print("fcc_cal::",fcc_cal)

                    if fcc != fcc_cal:
                        try:
                            fcc != fcc_cal + 1
                        except:
                            fcc_issue.append(t)


        # print("fcc_issue::",fcc_issue)

        fcc_excl_3 = set(fcc_issue) - set(prep_lid_3)
        fcc_incl_3 = set(prep_lid_3) - set(fcc_issue)
        print("fcc_excl_3_c::", len(fcc_excl_3))
        print("fcc_excl_3::",fcc_excl_3)
        print("fcc_incl_3::",fcc_incl_3)


        if len(fcc_excl_3) > 0:
            print(f"Error:: foreclosure charge is not as expected:: {fcc_issue}")
            assert False
        else:
            print("*** foreclosure charge is as expected ***")


