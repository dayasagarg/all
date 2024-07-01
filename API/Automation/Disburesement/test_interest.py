import math

class TestLoanInterest:
    import pytest
    @pytest.fixture
    def url_dis_int(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=7)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{curr_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})


    def test_disb_interest(self, url_dis_int):
        print("*** Test execution started ***")
        global cibil_pl_less_than_680_lid_count, cibil_pl_less_than_680_lid, cibil_pl_700_749_out_lid, cibil_pl_700_749_out_lid_count
        global cibil_pl_750_799_out_lid_count, cibil_pl_750_799_out_lid, cibil_pl_750_799_1_lac_out_lid_count, cibil_pl_750_799_1_lac_out_lid
        global cibil_pl_800_800_lid_count, cibil_pl_800_800_lid
        global cibil_pl_830_plus_and_prem_less_77_count, cibil_pl_830_plus_and_prem_more_77_count, prem_less_77, prem_more_77

        disAPIData = disAPI.json()["data"]["rows"]


        cibil_pl_less_than_680_lid = []
        cibil_pl_700_749_out_lid = []
        cibil_pl_750_799_out_lid = []
        cibil_pl_750_799_1_lac_out_lid = []
        cibil_pl_800_800_lid = []

        prem_less_77 = []
        prem_more_77 = []



        # print(disAPIData)
        diff_int_more = []
        diff_int_less = []
        remain = []

        diff_int_more_lid = []
        diff_int_less_lid = []
        remain_lid = []

        for r in disAPIData:
            total_int_amt = r["Total interest amount"]
            days = r["Loan tenure (days)"]
            int_rate = float((r["Interest rate"]).replace("%",""))
            appr_amt = r["Approved amount"]

            total_int_amt_f = int(((appr_amt * int_rate)/100) * days)

            # print(type(int_rate))

            print("lid::",r["Loan ID"])
            print("total_int_amt::",total_int_amt)
            print("total_int_amt_f::",total_int_amt_f)
            diff = total_int_amt - total_int_amt_f
            # diff_int.append(diff)

            if diff < 0:
                diff_int_less_lid.append(r["Loan ID"])
                diff_int_less.append(diff)
            elif diff > 0:
                diff_int_more_lid.append(r["Loan ID"])
                diff_int_more.append(diff)
            else:
                remain_lid.append(r["Loan ID"])
                remain.append(diff)

        print("diff_int_more::",diff_int_more)
        print("diff_int_less::",diff_int_less)
        print("remain::",remain)

        print("diff_int_more_lid::", diff_int_more_lid)
        print("diff_int_less_lid::", diff_int_less_lid)
        print("remain_lid::", remain_lid)
