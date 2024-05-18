import requests
from datetime import datetime, timedelta

class TestPenalFees:
    import pytest


    @pytest.fixture
    def url(self):
        global url_arl, arl_d, disb_date_n


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


    def test_dpd(self,url):
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

        for d in arl_d:
            if d["Loan id"]:
                lid_arl.append(d["Loan id"])


            if (datetime.strptime(d["Disbursement date"], "%d-%m-%Y")) > disb_date_n:

                if d["Delay days (as on today)"] in a13:
                    pen_amt_1 = d["Penalty Amt."]
                    pen_amt_cal_1 = int(round(d["Principal"] * 0.05 + (d["Principal"] * 0.05 * 0.18),0))

                    # print("pen_amt_1::",pen_amt_1)
                    # print("pen_amt_cal_1::",pen_amt_cal_1)


                    if pen_amt_1 != pen_amt_cal_1:
                        a13_p_m.append(d["Loan id"])


                elif d["Delay days (as on today)"] in a_4_15:
                    pen_amt_2 = d["Penalty Amt."]
                    pen_amt_cal_2 = int(round(d["Principal"] * 0.1 + (d["Principal"] * 0.1 * 0.18),0))

                    if pen_amt_2 != pen_amt_cal_2:
                        a_4_15_p_m.append(d["Loan id"])


                elif d["Delay days (as on today)"] in a_15_31:
                    pen_amt_3 = d["Penalty Amt."]
                    pen_amt_cal_3 = int(round(d["Principal"] * 0.15 + (d["Principal"] * 0.15 * 0.18),0))

                    if pen_amt_3 != pen_amt_cal_3:
                        a_15_31_p_m.append(d["Loan id"])

                elif d["Delay days (as on today)"] in a_31_61:
                    pen_amt_4 = d["Penalty Amt."]
                    pen_amt_cal_4 = int(round(d["Principal"] * 0.20 + (d["Principal"] * 0.20 * 0.18),0))

                    if pen_amt_4 != pen_amt_cal_4:
                        a31_61_p_m.append(d["Loan id"])

                elif d["Delay days (as on today)"] > 61:
                    pen_amt_5 = d["Penalty Amt."]
                    pen_amt_cal_5 = int(round(d["Principal"] * 0.25 + (d["Principal"] * 0.25 * 0.18),0))

                    if pen_amt_5 != pen_amt_cal_5:
                        a61pls_p_m.append(d["Loan id"])



        print("a13_p_m::",a13_p_m)
        print("a_4_15_p_m::",a_4_15_p_m)
        print("a_15_31_p_m::",a_15_31_p_m)
        print("a31_61_p_m::",a31_61_p_m)
        print("a61pls_p_m::",a61pls_p_m)

        all_day_issue = a13_p_m + a_4_15_p_m + a_15_31_p_m + a31_61_p_m + a61pls_p_m

        print("all_day_dpd_issue_total::",len(all_day_issue))

        if len(all_day_issue) > 0:
            print(f"Error:: DPD/penal charges are not as Expected ::{all_day_issue}")
            assert False
        else:
            print("*** DPD/penal charges are as expected ***")



    # def test_deferred_amt(self,url):
    #     global lid_arl
    #
    #
    #
    #     arl_lid = [i["Loan id"] for i in arl_d]
    #     # arl_lid = []
    #     #
    #     # for i in arl_d:
    #     #     if i["Loan id"]:
    #     #         arl_lid.append(i["Loan id"])
    #
    #     # print("arl_lid::",arl_lid)
    #
    #
    #     for n, r in enumerate(arl_lid):
    #         if n == 3:
    #             break
    #
    #
    #         response = requests.get(
    #             "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": r},
    #             verify=False)  # current date
    #
    #         emi_resp = response.json()["data"]["EMIData"]
    #
    #         emi_int = response.json()["data"]["interestRate"]
    #         eil = []
    #
    #
    #         # print("emi_int::",eil)
    #
    #         for w in emi_int:
    #             emi_int = response.json()["data"]["interestRate"]
    #             # eil.append(emi_int)
    #             # print("emi_int::",emi_int)
    #
    #         # print("eil::",eil)
    #
    #
    #
    #             for e in emi_resp:
    #
    #                 prin = e["principal"]
    #                 delay_days = e["penaltyDays"]
    #                 # int_rate = w["interestRate"]
    #
    #                 print("prin::",prin)
    #                 print("delay_days::",delay_days)
    #                 print("int_rate::",emi_int)













