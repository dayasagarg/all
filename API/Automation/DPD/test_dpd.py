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



    def test_dpd_2(self, url):
        global lid_arl
        # print("arl_d::",arl_d)
        a13 = list(range(1, 4))
        a_4_15 = list(range(4, 15))
        a_15_31 = list(range(15, 31))
        a_31_61 = list(range(31, 61))

        a13_p_m = []
        a_4_15_p_m = []
        a_15_31_p_m = []
        a31_61_p_m = []
        a61pls_p_m = []

        lid_arl = []
        part_lid = []

        for d in arl_d:
            if (datetime.strptime(d["Disbursement date"], "%d-%m-%Y")) > disb_date_n:
                if d["Loan id"]:
                    lid_arl.append(d["Loan id"])


        for n, r in enumerate(lid_arl):

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": r},
                verify=False)  # current date

            emi_r = response.json()["data"]["EMIData"]
            for d in emi_r:

                if d["penaltyDays"] in a13:
                    pen_amt_1 = d["totalPenalty"]
                    pen_amt_cal_1 = math.ceil(round(d["principal"] * 0.05 + (d["principal"] * 0.05 * 0.18), 3))

                    print("lid::",r)
                    print("pen_amt_1::",pen_amt_1)
                    print("pen_amt_cal_1::",pen_amt_cal_1)

                    if pen_amt_1 != pen_amt_cal_1:
                        a13_p_m.append(r)

                elif d["penaltyDays"] in a_4_15:
                    pen_amt_2 = d["totalPenalty"]
                    pen_amt_cal_2 = math.ceil(round(d["principal"] * 0.1 + (d["principal"] * 0.1 * 0.18), 3))

                    print("lid::", r)
                    print("pen_amt_2::", pen_amt_2)
                    print("pen_amt_cal_2::", pen_amt_cal_2)


                    if pen_amt_2 != pen_amt_cal_2:
                        a_4_15_p_m.append(r)

                elif d["penaltyDays"] in a_15_31:
                    pen_amt_3 = d["totalPenalty"]
                    pen_amt_cal_3 = math.ceil(round(d["principal"] * 0.15 + (d["principal"] * 0.15 * 0.18), 3))

                    print("lid::", r)
                    print("pen_amt_3::",pen_amt_3)
                    print("pen_amt_cal_3::",pen_amt_cal_3)

                    if pen_amt_3 != pen_amt_cal_3:
                        a_15_31_p_m.append(r)

                elif d["penaltyDays"] in a_31_61:
                    pen_amt_4 = d["totalPenalty"]
                    pen_amt_cal_4 = math.ceil(round(d["principal"] * 0.20 + (d["principal"] * 0.20 * 0.18), 3))

                    print("lid::", r)
                    print("pen_amt_4::",pen_amt_4)
                    print("pen_amt_cal_4::",pen_amt_cal_4)

                    if pen_amt_4 != pen_amt_cal_4:
                        a31_61_p_m.append(r)

                elif d["penaltyDays"] > 61:
                    pen_amt_5 = d["totalPenalty"]
                    pen_amt_cal_5 = math.ceil(round(d["principal"] * 0.25 + (d["principal"] * 0.25 * 0.18), 3))

                    print("lid::", r)
                    print("pen_amt_5::",pen_amt_5)
                    print("pen_amt_cal_5::",pen_amt_cal_5)

                    if pen_amt_5 != pen_amt_cal_5:
                        a61pls_p_m.append(r)

        print("a13_p_m::", a13_p_m)
        print("a_4_15_p_m::", a_4_15_p_m)
        print("a_15_31_p_m::", a_15_31_p_m)
        print("a31_61_p_m::", a31_61_p_m)
        print("a61pls_p_m::", a61pls_p_m)

        all_day_issue = a13_p_m + a_4_15_p_m + a_15_31_p_m + a31_61_p_m + a61pls_p_m

        print("all_day_dpd_issue_with_partpay_count::", len(all_day_issue))
        print("all_day_dpd_issue_with_partpay::", all_day_issue)


        for n, r in enumerate(all_day_issue):

            response_tran_dpd = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails", params={"loanId": r},
                verify=False)  # current date
            response_tran_d = response_tran_dpd.json()["data"]

            [part_lid.append(r) for t in response_tran_d if t["Pay type"] == "PARTPAY"]

        # print("part_lid::",part_lid)

        all_day_issue_except_partpay = set(all_day_issue) - set(part_lid)


        if len(all_day_issue_except_partpay) > 0:
            print(f"Error:: DPD/penal charges are not as Expected except partpay user::{all_day_issue_except_partpay}")
            assert False
        else:
            print("*** DPD/penal charges are as expected except partpay user ***")
