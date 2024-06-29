from datetime import datetime, timedelta

import requests


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
            f"{prod_url}/admin/transaction/allRepaidLoans",
            params={"start_date": f"{previousDateStr}T10:00:00.000Z", "end_date": f"{currentDateStr}T10:00:00.000Z",
                    "page": 1, "pagesize": 10, "getTotal": "true", "download": "true",
                    "verify": "False"})  # current date

        arl_d = url_arl.json()["data"]["rows"]

        disb_date = "07-04-2024"
        disb_date_n = datetime.strptime(disb_date, "%d-%m-%Y")

    def test_deferred_amt(self, url):
        lid_arl = []

        for d in arl_d:
            if (datetime.strptime(d["Disbursement date"], "%d-%m-%Y")) > disb_date_n:
                if d["Loan id"]:
                    lid_arl.append(d["Loan id"])

        def_int_issue_with_partpay = []
        part_lid = []

        for n, r in enumerate(lid_arl):
            # if n == 70:
            #     break

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": r},
                verify=False)  # current date

            response_tran = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails?", params={"loanId": r},
                verify=False)  # current date
            response_tran_d = response_tran.json()["data"]

            repay_date_em1 = []
            repay_date_em2 = []
            repay_date_em3 = []
            repay_date_em4 = []
            diff_days = []

            for n, t in enumerate(response_tran_d):
                if n == 70:
                    break

                if t["Pay type"] == "PARTPAY" and t["Status"] == "COMPLETED":
                    # print("t::",t)

                    # repay_date = datetime.strptime(t["Repaid date"], "%d/%m/%Y")

                    if "1" in t["EMI"]:
                        repay_date_em1.append(datetime.strptime(t["Repaid date"], "%d/%m/%Y"))
                    if "2" in t["EMI"]:
                        repay_date_em2.append(datetime.strptime(t["Repaid date"], "%d/%m/%Y"))
                    if "3" in t["EMI"]:
                        repay_date_em3.append(datetime.strptime(t["Repaid date"], "%d/%m/%Y"))
                    if "4" in t["EMI"]:
                        repay_date_em4.append(datetime.strptime(t["Repaid date"], "%d/%m/%Y"))


            # # Print the dates in the format "date/month/year"
            # # repay_date_em11= [date.strftime("%d/%m/%Y") for date in repay_date_em1]
            # # repay_date_em22=[date.strftime("%d/%m/%Y") for date in repay_date_em2]
            # # repay_date_em33= [date.strftime("%d/%m/%Y") for date in repay_date_em3]
            # # repay_date_em44= [date.strftime("%d/%m/%Y") for date in repay_date_em4]
            #
            print("lid::", r)
            print("repay_date_em1::", repay_date_em1)
            print("repay_date_em2::", repay_date_em2)
            print("repay_date_em3::", repay_date_em3)
            print("repay_date_em4::", repay_date_em4)






            # repay_date_em1 = []
            # repay_date_em2 = []
            # repay_date_em3 = []
            # repay_date_em4 = []
            # diff_days = []
            # for n, t in enumerate(response_tran_d):
            #     if n == 70:
            #         break
            #
            #     if t["Pay type"] == "PARTPAY" and t["Status"] == "COMPLETED":
            #         if "1" in t["EMI"]:
            #             repay_date_em1.append(t["Repaid date"])
            #         if "2" in t["EMI"]:
            #             repay_date_em2.append(t["Repaid date"])
            #         if "3" in t["EMI"]:
            #             repay_date_em3.append(t["Repaid date"])
            #         if "4" in t["EMI"]:
            #             repay_date_em4.append(t["Repaid date"])

            # print("lid::", r)
            # print("repay_date_em1::", repay_date_em1)
            # print("repay_date_em2::", repay_date_em2)
            # print("repay_date_em3::", repay_date_em3)
            # print("repay_date_em4::", repay_date_em4)

            # Convert
            # string
            # dates
            # to
            # datetime
            # objects

            # dates = [datetime.strptime(date, "%d/%m/%Y") for date in repay_date_em1]
            # print(dates)

            # for date in repay_date_em1:
            #     d = datetime.strptime(date,"%d/%m/%Y")
            #     print("date::",d)

            # Calculate the difference between consecutive dates
            differences = [(repay_date_em1[i] - repay_date_em1[i - 1]).days for i in range(1, len(repay_date_em1))]
            diff_days.append(differences)
            print("diff_days::",diff_days)

            #     if t["Repaid date"]:
            #         repay_date.append(t["Repaid date"])
            #
            # print("repay_date::",repay_date)

            # [part_lid.append(r) for t in response_tran_d if t["Pay type"] == "PARTPAY"]

        #     emi_resp = response.json()["data"]["EMIData"]
        #
        #     emi_int = response.json()["data"]["interestRate"]
        #     eil = []
        #
        #     # print("emi_int::",eil)
        #
        #     for w in emi_int:
        #         emi_int = response.json()["data"]["interestRate"]
        #         # eil.append(emi_int)
        #         # print("emi_int::",emi_int)
        #
        #     # print("eil::",eil)
        #
        #     for e in emi_resp:
        #
        #         def_int = e["deferredInterest"]
        #         prin = e["principal"]
        #         delay_days = e["penaltyDays"]
        #         # int_rate = w["interestRate"]
        #
        #         print("lid::",r)
        #         print("def_int::",def_int)
        #
        #         # print("prin::",prin)
        #         # print("delay_days::",delay_days)
        #         # print("int_rate::",emi_int)
        #
        #         # print("prin::",type(prin))
        #         # print("delay_days::",type(delay_days))
        #         # print("int_rate::",type(emi_int))
        #
        #         def_int_cal = math.ceil(prin * round(float(emi_int),3)/100 * delay_days)
        #         print("def_int_cal::",def_int_cal)
        #
        #         if def_int != def_int_cal:
        #             def_int_issue_with_partpay.append(r)
        #
        #
        #         if def_int != def_int_cal:
        #             print(f"Error:: deferred interest not as expected :: {r}")
        #         else:
        #             print("*** deferred interest is as expected ***")
        #
        #
        # # print("def_int_issue::",def_int_issue)
        # print("part_lid::",part_lid)
        # print("def_int_issue_with_partpay::",def_int_issue_with_partpay)
        #
        # def_int_issue_without_part_pay = set(def_int_issue_with_partpay) - set(part_lid)
        # print("def_int_issue_without_part_pay::",def_int_issue_without_part_pay)

        #
        #
        # if len(def_int_issue_without_part_pay) > 0:
        #     print(f"Error:: deferred interest not as expected :: {def_int_issue_without_part_pay}")
        #     assert False
        # else:
        #     print("*** deferred interest is expected except partpay users ***")
