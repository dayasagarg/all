import pytest
import requests
from datetime import datetime,timedelta

class TestBounce:
    @pytest.fixture
    def bcURL(self):
        global resp_all_rep_lo, disb_date_n

        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        curr_str_emi = datetime.strftime(curr, "%d/%m/%Y")

        prev_1 = curr - timedelta(days=1)
        prev_2 = curr - timedelta(days=2)


        pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
        pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")



        pre_str_emi = datetime.strftime(prev_1, "%d/%m/%Y")
        pre_str_emi_2 = datetime.strftime(prev_2, "%d/%m/%Y")


        disb_date = "07-04-2024"
        disb_date_n = datetime.strptime(disb_date, "%d-%m-%Y")

        resp_all_rep_lo = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{pre_str_2}T10:00:00.000Z", "end_date": f"{curr_str}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date



    def test_bounce_charg_m(self, bcURL):
        global autoDebitData

        repay_Data = resp_all_rep_lo.json()["data"]["rows"]
        # print(autoDebitData)
        bounceChMissed_LId_590 = []
        repay_failed_loan_ids = []

        for r in repay_Data:

            if (datetime.strptime(r["Disbursement date"], "%d-%m-%Y")) > disb_date_n:

                if r["Loan id"]:
                    repay_failed_loan_ids.append(r["Loan id"])


        print("repay_failed_loan_ids_count::",len(repay_failed_loan_ids))
        # print("repay_failed_loan_ids::", repay_failed_loan_ids)

        for e in repay_failed_loan_ids:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)

            emiAPI_data = emiAPI.json()["data"]["EMIData"]

            for ed in emiAPI_data:

                if ed["totalBounceCharge"] > 590:
                    bounceChMissed_LId_590.append(e)



        if len(bounceChMissed_LId_590) > 0:
            print(f"Error::bounce charge != 590::{bounceChMissed_LId_590}")
            assert False, "bounce charge not correct"
        else:
            print("*** No bounce charge == 590 ***")
