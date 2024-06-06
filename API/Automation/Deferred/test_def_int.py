import requests
import math
from datetime import datetime, timedelta

class TestPenalFees:
    import pytest

    @pytest.fixture
    def url(self):
        global url_arl, arl_d, disb_date_n, disAPI_d


        currentFullTime = datetime.now()  # whole date
        currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
        currentDateF = datetime.strptime(currentDateStr, "%Y-%m-%d")
        print("currentDateStr::", currentDateStr)

        previousDate = currentDateF - timedelta(days=1)
        previousDateStr = datetime.strftime(previousDate, "%Y-%m-%d")
        previousDateStr_n = datetime.strftime(previousDate, "%d-%m-%Y")

        prod_url = "https://chinmayfinserve.com/admin-prod"
        stage_url = "https://chinmayfinserve.com/stagging"

        url_arl = requests.get(
            f"{prod_url}/admin/transaction/allRepaidLoans", params={"start_date":f"{previousDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","page":1,"pagesize":10,"getTotal":"true","download":"true",
            "verify":"False"})  # current date

        arl_d = url_arl.json()["data"]["rows"]

        disb_date = "07-04-2024"
        disb_date_n = datetime.strptime(disb_date, "%d-%m-%Y")


    def test_deferred_amt(self,url):
        lid_arl = []

        for d in arl_d:
            if (datetime.strptime(d["Disbursement date"], "%d-%m-%Y")) > disb_date_n:
                if d["Loan id"]:
                    lid_arl.append(d["Loan id"])


        def_int_issue_with_partpay = []
        part_lid = []

        for n, r in enumerate(lid_arl):


            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": r},
                verify=False)  # current date

            response_tran = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails?", params={"loanId": r},
                verify=False)  # current date
            response_tran_d = response_tran.json()["data"]

            [part_lid.append(r) for t in response_tran_d if t["Pay type"] == "PARTPAY"]


            emi_resp = response.json()["data"]["EMIData"]

            emi_int = response.json()["data"]["interestRate"]
            eil = []

            # print("emi_int::",eil)

            for w in emi_int:
                emi_int = response.json()["data"]["interestRate"]
                # eil.append(emi_int)
                # print("emi_int::",emi_int)

            # print("eil::",eil)

            for e in emi_resp:

                def_int = e["deferredInterest"]
                prin = e["principal"]
                delay_days = e["penaltyDays"]
                # int_rate = w["interestRate"]

                print("lid::",r)
                print("def_int::",def_int)

                # print("prin::",prin)
                # print("delay_days::",delay_days)
                # print("int_rate::",emi_int)

                # print("prin::",type(prin))
                # print("delay_days::",type(delay_days))
                # print("int_rate::",type(emi_int))

                def_int_cal = math.ceil(prin * round(float(emi_int),3)/100 * delay_days)
                print("def_int_cal::",def_int_cal)

                if def_int != def_int_cal:
                    def_int_issue_with_partpay.append(r)


                if def_int != def_int_cal:
                    print(f"Error:: deferred interest not as expected :: {r}")
                else:
                    print("*** deferred interest is as expected ***")


        # print("def_int_issue::",def_int_issue)
        print("part_lid::",part_lid)
        print("def_int_issue_with_partpay::",def_int_issue_with_partpay)

        def_int_issue_without_part_pay = set(def_int_issue_with_partpay) - set(part_lid)


        if len(def_int_issue_without_part_pay) > 0:
            print(f"Error:: deferred interest not as expected :: {def_int_issue_without_part_pay}")
            assert False
        else:
            print("*** deferred interest is expected except partpay users ***")
