class TestLoanDisbCibil:
    import pytest
    @pytest.fixture
    def url_dis_cibil(self):
        global disAPI, disbData, math
        import requests
        from datetime import datetime, timedelta
        import math

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=7)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disb_url = "https://madhurfinance.com"
        endpoint = "/admin-prod/admin/dashboard/allDisbursedLoans"
        params = {
            "start_date": f"{pre_str}T10:00:00.000Z",
            "end_date": f"{curr_str}T10:00:00.000Z",
            "download": "true"
        }

        disAPI = requests.get(f"{disb_url}{endpoint}", params=params)
        disbData = disAPI.json()["data"]['rows']

    def test_disb_cibil_new_user(self, url_dis_cibil):
        # print("*** Test execution started ***")
        global cibil_pl_less_than_680_lid_count, cibil_pl_less_than_680_lid, cibil_pl_680_700_out_lid_count, cibil_pl_680_700_out_lid, cibil_pl_700_749_out_lid, cibil_pl_700_749_out_lid_count
        global cibil_pl_750_799_out_lid_count, cibil_pl_750_799_out_lid, cibil_pl_750_799_1_lac_out_lid_count, cibil_pl_750_799_1_lac_out_lid
        global cibil_pl_800_830_lid_count, cibil_pl_800_830_lid, cibil_pl_more_than_830_lid_count, cibil_pl_more_than_830_lid
        global cibil_pl_830_plus_and_prem_less_77_count, cibil_pl_830_plus_and_prem_more_77_count, prem_less_77, prem_more_77
        global cs_pl_800_830_interest_less_p1, cs_pl_800_830_interest_more_p1, cs_pl_750_799_interest_less_p2, cs_pl_750_799_interest_more_p2
        global cs_pl_700_749_interest_less_p3, cs_pl_700_749_interest_more_p3
        global cs_pl_680_700_interest_less_p3, cs_pl_680_700_interest_more_p3


        cibil_pl_less_than_680_lid = []
        cibil_pl_680_700_out_lid = []
        cibil_pl_700_749_out_lid = []
        cibil_pl_750_799_out_lid = []
        cibil_pl_750_799_1_lac_out_lid = []
        cibil_pl_800_830_lid = []
        cibil_pl_more_than_830_lid = []


        prem_less_77 = []
        prem_more_77 = []
        cs_pl_800_830_interest_less_p1 = []
        cs_pl_800_830_interest_more_p1 = []
        
        cs_pl_750_799_interest_less_p2 = []
        cs_pl_750_799_interest_more_p2 = []

        cs_pl_700_749_interest_less_p3 = []
        cs_pl_700_749_interest_more_p3 = []

        cs_pl_680_700_interest_less_p3 = []
        cs_pl_680_700_interest_more_p3 = []

        # print(disAPIData)

        # As per new logic (50 % - 75 %), (75 % - 100 %)

        for r in disbData:

            if r["Completed loans"] < 3:

                if (r["Cibil score"] < 680) & (r["Pl score"] < 680):

                    cibil_pl_less_than_680_lid.append(r["Loan ID"])

                elif (680 <= r["Cibil score"] < 700) & (680 <= r["Pl score"] < 700):
                    if r["Approved salary"] < 40000:
                        cibil_pl_680_700_out_lid.append(r["Loan ID"])

                    if round(float(r["Interest rate"].replace("%", "")),1) < 0.3:
                        cs_pl_680_700_interest_less_p3.append(r["Loan ID"])

                    if round(float(r["Interest rate"].replace("%", "")),1) > 0.3:
                        cs_pl_680_700_interest_more_p3.append(r["Loan ID"])


                elif (700 <= r["Cibil score"] <= 749) & (700 <= r["Pl score"] <= 749):

                    # print(r)
                    apprAmt = r["Approved amount"]
                    apprSalary_loan_amt_cal = r["Approved salary"] * 0.50
                    apprSalary_loan_amt_cal_500_round = apprSalary_loan_amt_cal + 500

                    if apprAmt > apprSalary_loan_amt_cal_500_round:
                        cibil_pl_700_749_out_lid.append(r["Loan ID"])

                    if round(float(r["Interest rate"].replace("%", "")),1) < 0.3:
                        cs_pl_700_749_interest_less_p3.append(r["Loan ID"])

                    if round(float(r["Interest rate"].replace("%", "")),1) > 0.3:
                        cs_pl_700_749_interest_more_p3.append(r["Loan ID"])


                elif (750 <= r["Cibil score"] <= 799) & (750 <= r["Pl score"] <= 799):

                    # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                    apprAmt_3 = r["Approved amount"]
                    apprSalary_loan_amt_cal_3 = r["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_3 = apprSalary_loan_amt_cal_3 + 500

                    if apprAmt_3 > apprSalary_loan_amt_cal_500_round_3:
                        cibil_pl_750_799_1_lac_out_lid.append(r["Loan ID"])

                    # print("2::",round(float(r["Interest rate"].replace("%", "")),1))
                        
                    if round(float(r["Interest rate"].replace("%", "")),1) < 0.2:
                        cs_pl_750_799_interest_less_p2.append(r["Loan ID"])

                    if round(float(r["Interest rate"].replace("%", "")),1) > 0.2:
                        cs_pl_750_799_interest_more_p2.append(r["Loan ID"])


                elif (800 <= r["Cibil score"] < 830) & (800 <= r["Pl score"] < 830):

                    apprAmt_4 = r["Approved amount"]
                    apprSalary_loan_amt_cal_4 = r["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_4 = apprSalary_loan_amt_cal_4 + 500

                    if apprAmt_4 > apprSalary_loan_amt_cal_500_round_4:
                        cibil_pl_800_830_lid.append(r["Loan ID"])

                    if float(r["Interest rate"].replace("%", "")) < 0.1:
                        cs_pl_800_830_interest_less_p1.append(r["Loan ID"])

                    if float(r["Interest rate"].replace("%", "")) > 0.1:
                        cs_pl_800_830_interest_more_p1.append(r["Loan ID"])


                elif r["Cibil score"] > 830 & r["Pl score"] > 830:
                    apprAmt_5 = r["Approved amount"]
                    apprSalary_loan_amt_cal_5= r["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_5 = apprSalary_loan_amt_cal_5 + 500

                    if apprAmt_5 > apprSalary_loan_amt_cal_500_round_5:
                        cibil_pl_more_than_830_lid.append(r["Loan ID"])


                    if float(r["Interest rate"].replace("%", "")) < 0.077:
                        prem_less_77.append(r["Loan ID"])

                    if float(r["Interest rate"].replace("%", "")) > 0.077:
                        prem_more_77.append(r["Loan ID"])

                # elif r["Cibil score"] > 830 & r["Pl score"] > 830:



        cibil_pl_less_than_680_lid_count = len(cibil_pl_less_than_680_lid)
        cibil_pl_680_700_out_lid_count = len(cibil_pl_680_700_out_lid)
        cibil_pl_700_749_out_lid_count = len(cibil_pl_700_749_out_lid)
        cibil_pl_750_799_out_lid_count = len(cibil_pl_750_799_out_lid)
        cibil_pl_750_799_1_lac_out_lid_count = len(cibil_pl_750_799_1_lac_out_lid)
        cibil_pl_800_830_lid_count = len(cibil_pl_800_830_lid)
        cibil_pl_more_than_830_lid_count = len(cibil_pl_more_than_830_lid)

        cibil_pl_830_plus_and_prem_less_77_count = len(prem_less_77)
        cibil_pl_830_plus_and_prem_more_77_count = len(prem_more_77)

        # print("cibil_pl_less_than_680_lid::",cibil_pl_less_than_680_lid)
        # print("cibil_pl_700_749_out_lid::",cibil_pl_700_749_out_lid)
        # print("cibil_pl_750_799_out_lid::",cibil_pl_750_799_out_lid)
        # print("cibil_pl_750_799_1_lac_out_lid::",cibil_pl_750_799_1_lac_out_lid)
        # print("cibil_pl_800_800_lid::",cibil_pl_800_800_lid)
        # print("prem_less_77::",prem_less_77)
        # print("prem_more_77::",prem_more_77)

        # print("cibil_pl_less_than_680_lid_count ::",cibil_pl_less_than_680_lid_count)
        # print("cibil_pl_700_749_out_lid_count::",cibil_pl_700_749_out_lid_count)
        # print("cibil_pl_750_799_out_lid_count::",cibil_pl_750_799_out_lid_count)
        # print("cibil_pl_750_799_1_lac_out_lid_count::",cibil_pl_750_799_1_lac_out_lid_count)
        # print("cibil_pl_800_800_lid_count::",cibil_pl_800_800_lid_count)
        # print("cibil_pl_830_plus_and_prem_less_77_count_r::",cibil_pl_830_plus_and_prem_less_77_count_r)

    def test_cs_pl_less_than_680(self):
        if cibil_pl_less_than_680_lid_count > 0:
            print(f" Error :: loans are not rejected if cibil_and_pl_less_than_680 ::New User:: {cibil_pl_less_than_680_lid}")
            assert False
        else:
            print("*** loans are rejected if cibil_and_pl_less_than_680 ::New User::***")

    def test_cs_pl_680_700_out(self):
        if cibil_pl_680_700_out_lid_count > 0:
            print(
                f" Error :: loans are not rejected if cibil_pl_680_700_out_lid and salary < 40 k ::New User:: {cibil_pl_680_700_out_lid}")
            assert False
        else:
            print("*** loans are rejected if cibil_pl_680_700_out_lid and salary < 40 k ::New User:: ***")

    def test_cs_pl_700_749_out(self):
        if cibil_pl_700_749_out_lid_count > 0:
            print(
                f" Error :: loan not rejected for cibil_pl_700_749 range and 50 % out salary ::New User:: {cibil_pl_700_749_out_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_700_749 ::New User:: ***")

    #

    def test_cs_pl_750_799_1_lac_out(self):
        if cibil_pl_750_799_1_lac_out_lid_count > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 ::New User:: {cibil_pl_750_799_1_lac_out_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_750_799  ::New User::***")

    #
    def test_cs_pl_800_830(self):
        if cibil_pl_800_830_lid_count > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_800_830 ::New User:: {cibil_pl_800_830_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_800_830 ::New User:: ***")

    def test_cs_pl_mt_830(self):
        if cibil_pl_more_than_830_lid_count > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_more_than_830_lid  ::New User:: {cibil_pl_more_than_830_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_more_than_830_lid ::New User:: ***")

    def test_cs_pl_830_l(self):
        if cibil_pl_830_plus_and_prem_less_77_count > 0:
            print("Error:: premium user issue with less than 0.077/day interest rate for new user :",prem_less_77)
            assert False
        else:
            print(f" No premium user issue with less than 0.077/day interest rate for new user ")

    def test_cs_pl_830_m(self):
        if cibil_pl_830_plus_and_prem_more_77_count > 0:
            print(f"Error:: premium user issue with more than 0.077/day interest rate for new user ::{prem_more_77}")
            assert False
        else:
            print(f"*** No premium user issue with more than 0.077/day interest rate for new user ***")


    def test_cs_pl_800_830_interest_less_p1(self):
        if len(cs_pl_800_830_interest_less_p1) > 0:
            print("Error::cs_pl_800_830_interest_less_p1 user issue with less than 0.1/day interest rate for new user ::",cs_pl_800_830_interest_less_p1)
            assert False
        else:
            print("*** No cs_pl_800_830_interest_less_p1 user issue with less than 0.1/day interest rate for new user ***")


    def test_cs_pl_800_830_interest_more_p1(self):
        if len(cs_pl_800_830_interest_more_p1) > 0:
            print("Error::cs_pl_800_830_interest_more_p1 user issue with more than 0.1/day interest rate for new user ::",cs_pl_800_830_interest_more_p1)
            assert False
        else:
            print("*** No cs_pl_800_830_interest_more_p1 user issue with more than 0.1/day interest rate for new user ***")
            
            
    
    def test_cs_pl_750_799_interest_less_p2(self):
        if len(cs_pl_750_799_interest_less_p2) > 0:
            print("Error::cs_pl_750_799_interest_less_p2 user issue with less than 0.2/day interest rate for new user ::",cs_pl_750_799_interest_less_p2)
            assert False
        else:
            print("*** No cs_pl_750_799_interest_less_p2 user issue with less than 0.2/day interest rate for new user ***")


    def test_cs_pl_750_799_interest_more_p2(self):
        if len(cs_pl_750_799_interest_more_p2) > 0:
            print("Error::cs_pl_750_799_interest_more_p2 user issue with more than 0.2/day interest rate for new user ::",cs_pl_750_799_interest_more_p2)
            assert False
        else:
            print("*** No cs_pl_750_799_interest_more_p2 user issue with more than 0.2/day interest rate for new user ***")

    def test_cs_pl_700_749_interest_less_p3(self):
        if len(cs_pl_700_749_interest_less_p3) > 0:
            print(
                "Error::cs_pl_700_749_interest_less_p3 user issue with less than 0.3/day interest rate for new user ::",
                cs_pl_700_749_interest_less_p3)
            assert False
        else:
            print(
                "*** No cs_pl_700_749_interest_less_p3 user issue with less than 0.3/day interest rate for new user ***")

    def test_cs_pl_700_749_interest_more_p3(self):
        if len(cs_pl_700_749_interest_more_p3) > 0:
            print(
                "Error::cs_pl_700_749_interest_more_p3 user issue with more than 0.3/day interest rate for new user ::",
                cs_pl_700_749_interest_more_p3)
            assert False
        else:
            print(
                "*** No cs_pl_700_749_interest_more_p3 user issue with more than 0.3/day interest rate for new user ***")



    def test_cs_pl_680_700_interest_less_p3(self):
        if len(cs_pl_680_700_interest_less_p3) > 0:
            print(
                "Error::cs_pl_680_700_interest_less_p3 user issue with less than 0.3/day interest rate for new user ::",
                cs_pl_680_700_interest_less_p3)
            assert False
        else:
            print(
                "*** No cs_pl_680_700_interest_less_p3 user issue with less than 0.3/day interest rate for new user ***")

    def test_cs_pl_680_700_interest_more_p3(self):
        if len(cs_pl_680_700_interest_more_p3) > 0:
            print(
                "Error::cs_pl_680_700_interest_more_p3 user issue with more than 0.3/day interest rate for new user ::",
                cs_pl_680_700_interest_more_p3)
            assert False
        else:
            print(
                "*** No cs_pl_680_700_interest_more_p3 user issue with more than 0.3/day interest rate for new user ***")



    def test_disb_cibil_repeat_user(self, url_dis_cibil):
        print("*** Test execution started ***")
        global cibil_less_than_680_lid_count_r, cibil_less_than_680_lid_r, cibil_pl_680_700_out_lid_count_r, cibil_pl_680_700_out_lid_r, cibil_700_749_out_lid_r, cibil_700_749_out_lid_count_r
        global cibil_750_799_out_lid_count_r, cibil_750_799_out_lid_r, cibil_750_799_1_lac_out_lid_count_r, cibil_750_799_1_lac_out_lid_r
        global cibil_800_830_lid_count_r, cibil_800_830_lid_r, cibil_more_than_830_lid_count_r, cibil_more_than_830_lid_r
        global cibil_830_plus_and_prem_less_77_count_r, prem_less_77_r, prem_more_77_r, cibil_830_plus_and_prem_more_77_count_r
        global cs_800_830_interest_less_p1_r, cs_800_830_interest_more_p1_r, cs_750_799_interest_less_p2_r, cs_750_799_interest_more_p2_r
        global cs_pl_700_749_interest_less_p3_r, cs_pl_700_749_interest_more_p3_r
        global cs_pl_680_700_interest_less_p3_r, cs_pl_680_700_interest_more_p3_r

        disAPIData = disAPI.json()["data"]["rows"]

        cibil_less_than_680_lid_r = []
        cibil_pl_680_700_out_lid_r = []
        cibil_700_749_out_lid_r = []
        cibil_750_799_out_lid_r = []
        cibil_750_799_1_lac_out_lid_r = []
        cibil_800_830_lid_r = []
        cibil_more_than_830_lid_r = []


        prem_less_77_r = []
        prem_more_77_r = []
        cs_800_830_interest_less_p1_r = []
        cs_800_830_interest_more_p1_r = []

        cs_750_799_interest_less_p2_r = []
        cs_750_799_interest_more_p2_r = []

        cs_pl_700_749_interest_less_p3_r = []
        cs_pl_700_749_interest_more_p3_r = []

        cs_pl_680_700_interest_less_p3_r = []
        cs_pl_680_700_interest_more_p3_r = []

        # print(disAPIData)

        for s in disAPIData:
            # print(s)
            # if s["Completed loans"] > 3 and isinstance(s["Cibil score"],str):
            #     # print(s["Cibil score"],type(s["Cibil score"]))
            #
            #     if s["Cibil score"] :
            #         print(s["Cibil score"])
            # cibil_pl_less_than_700_lid_r.append(s["Loan ID"])

            if s["Completed loans"] > 3 and isinstance(s["Cibil score"], int):
                # print(s["Cibil score"],type(s["Cibil score"]))
                if s["Cibil score"] < 680:
                    cibil_less_than_680_lid_r.append(s["Loan ID"])


                elif (680 <= s["Cibil score"] < 700):
                    if s["Approved salary"] < 40000:
                        cibil_pl_680_700_out_lid.append(s["Loan ID"])

                    if round(float(s["Interest rate"].replace("%", "")),1) < 0.3:
                        cs_pl_680_700_interest_less_p3_r.append(s["Loan ID"])

                    if round(float(s["Interest rate"].replace("%", "")),1) > 0.3:
                        cs_pl_680_700_interest_more_p3_r.append(s["Loan ID"])


                elif 700 <= s["Cibil score"] <= 749:
                    apprAmt_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_r = s["Approved salary"] * 0.50
                    apprSalary_loan_amt_cal_500_round_r = apprSalary_loan_amt_cal_r + 500

                    if apprAmt_r > apprSalary_loan_amt_cal_500_round_r:
                        cibil_700_749_out_lid_r.append(s["Loan ID"])

                    if round(float(s["Interest rate"].replace("%", "")),1) < 0.3:
                        cs_pl_700_749_interest_less_p3_r.append(s["Loan ID"])

                    if round(float(s["Interest rate"].replace("%", "")),1) > 0.3:
                        cs_pl_700_749_interest_more_p3_r.append(s["Loan ID"])

                elif (750 <= s["Cibil score"] <= 799):

                    # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                    apprAmt_3_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_3_r = s["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_3_r = apprSalary_loan_amt_cal_3_r + 500

                    if apprAmt_3_r > apprSalary_loan_amt_cal_500_round_3_r:
                        cibil_750_799_1_lac_out_lid_r.append(s["Loan ID"])
                        
                    if float(s["Interest rate"].replace("%", "")) < 0.2:
                        cs_750_799_interest_less_p2_r.append(s["Loan ID"])

                    if float(s["Interest rate"].replace("%", "")) > 0.2:
                        cs_750_799_interest_more_p2_r.append(s["Loan ID"])
                        

                elif 800 <= s["Cibil score"] <= 830:
                    apprAmt_4_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_4_r = s["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_4_r = apprSalary_loan_amt_cal_4_r + 500

                    if apprAmt_4_r > apprSalary_loan_amt_cal_500_round_4_r:
                        cibil_800_830_lid_r.append(s["Loan ID"])

                    if float(s["Interest rate"].replace("%", "")) < 0.1:
                        cs_800_830_interest_less_p1_r.append(s["Loan ID"])

                    if float(s["Interest rate"].replace("%", "")) > 0.1:
                        cs_800_830_interest_more_p1_r.append(s["Loan ID"])

                    # print("lid::", s["Loan ID"])
                    # print("apprSalary_loan_amt_cal::", apprSalary_loan_amt_cal_r)
                    # print("apprSalary_loan_amt_cal_500_round::", apprSalary_loan_amt_cal_500_round_r)
                    # print("apprAmt::", apprAmt_r)

                elif s["Cibil score"] > 830:

                    apprAmt_5_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_5_r = s["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_5_r = apprSalary_loan_amt_cal_5_r + 500

                    if apprAmt_5_r > apprSalary_loan_amt_cal_500_round_5_r:
                        cibil_more_than_830_lid_r.append(s["Loan ID"])


                    if float(s["Interest rate"].replace("%", "")) < 0.077:
                        prem_less_77_r.append(s["Loan ID"])

                    if float(s["Interest rate"].replace("%", "")) > 0.077:
                        prem_more_77_r.append(s["Loan ID"])


        cibil_less_than_680_lid_count_r = len(cibil_less_than_680_lid_r)
        cibil_pl_680_700_out_lid_count_r = len(cibil_pl_680_700_out_lid_r)
        cibil_700_749_out_lid_count_r = len(cibil_700_749_out_lid_r)
        cibil_750_799_out_lid_count_r = len(cibil_750_799_out_lid_r)
        cibil_750_799_1_lac_out_lid_count_r = len(cibil_750_799_1_lac_out_lid_r)
        cibil_800_830_lid_count_r = len(cibil_800_830_lid_r)
        cibil_more_than_830_lid_count_r = len(cibil_more_than_830_lid_r)

        cibil_830_plus_and_prem_less_77_count_r = len(prem_less_77_r)
        cibil_830_plus_and_prem_more_77_count_r = len(prem_more_77_r)

        # print("cibil_pl_less_than_700_lid_count ::",cibil_pl_less_than_680_lid_r)
        # print("cibil_pl_700_749_out_lid_r::",cibil_pl_700_749_out_lid_count_r)
        # print("cibil_pl_750_799_out_lid_count_r::",cibil_pl_750_799_out_lid_count_r)
        # print("cibil_pl_750_799_1_lac_out_lid_count_r::",cibil_pl_750_799_1_lac_out_lid_count_r)
        # print("cibil_pl_800_800_lid_count_r::",cibil_pl_800_800_lid_count_r)

        # print("prem_less_77_r::",prem_less_77_r)
        # print("prem_more_77_r::",prem_more_77_r)

    def test_cs_less_than_680_r(self):
        if cibil_less_than_680_lid_count_r > 0:
            print(
                f" Error :: loans are not rejected if cibil_and_pl_less_than_680 ::Repeat User:: {cibil_less_than_680_lid_r}")
            assert False
        else:
            print("*** loans are rejected if cibil_and_pl_less_than_680 ::Repeat User:: ***")

    def test_cs_680_700_out_r(self):
        if cibil_pl_680_700_out_lid_count_r > 0:
            print(
                f" Error :: loans are not rejected if cibil_680_700_out_lid and salary < 40 k ::Repeat User:: {cibil_pl_680_700_out_lid_r}")
            assert False
        else:
            print("*** loans are rejected if cibil_680_700_out_lid and salary < 40 k ::Repeat User:: ***")

    def test_cs_700_749_out_r(self):
        if cibil_700_749_out_lid_count_r > 0:
            print(
                f" Error :: loan not rejected for cibil_pl_700_749 range and 50 % out salary ::Repeat User:: {cibil_700_749_out_lid_r}")
            assert False
        else:
            print(
                "*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_700_749 ::Repeat User:: ***")

    def test_cs_750_799_1_lac_out_r(self):
        if cibil_750_799_1_lac_out_lid_count_r > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 ::Repeat User:: {cibil_750_799_1_lac_out_lid_r}")
            assert False
        else:
            print(
                "*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 and ::Repeat User:: ***")

    def test_cs_800_830_r(self):
        if cibil_800_830_lid_count_r > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_800_830 ::Repeat User:: {cibil_800_830_lid_r}")
            assert False
        else:
            print(
                "*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_800_830 ::Repeat User:: ***")

    def test_cs_pl_mt_830_r(self):
        if cibil_more_than_830_lid_count_r > 0:
            print(
                f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_more_than_830_lid :: {cibil_more_than_830_lid_count_r}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_more_than_830_lid:: Repeat User ***")

    def test_cs_830_l_r(self):
        if cibil_830_plus_and_prem_less_77_count_r > 0:
            print(
                f"Error:: premium user issue with less than 0.077/day interest rate for repeat user ::{prem_less_77_r}")
            assert False
        else:
            print(f"*** No premium user issue with less than 0.077/day interest rate for repeat user ***")

    def test_cs_830_m_r(self):
        if cibil_830_plus_and_prem_more_77_count_r > 0:
            print(
                f"Error:: premium user issue with more than 0.077/day interest rate for repeat user ::{prem_more_77_r}")
            assert False
        else:
            print(f"*** No premium user issue with more than 0.077/day interest rate for repeat user ***")

    def test_cs_800_830_interest_less_p1_r(self):
        if len(cs_800_830_interest_less_p1_r) > 0:
            print("Error::cs_800_830_interest_less_p1_r user issue with less than 0.1/day interest rate for repeat user ::",cs_800_830_interest_less_p1_r)
            assert False
        else:
            print("*** No cs_800_830_interest_less_p1_r user issue with less than 0.1/day interest rate for repaeat user ***")

    def test_cs_800_830_interest_more_p1_r(self):
        if len(cs_800_830_interest_more_p1_r) > 0:
            print("Error::cs_800_830_interest_less_p1_r user issue with more than 0.1/day interest rate for repeat user ::",cs_800_830_interest_more_p1_r)
            assert False
        else:
            print("*** No cs_800_830_interest_less_p1_r user issue with more than 0.1/day interest rate for repaeat user ***")

    def test_cs_750_799_interest_less_p2_r(self):
        if len(cs_750_799_interest_less_p2_r) > 0:
            print(
                "Error::cs_750_799_interest_less_p2_r user issue with less than 0.2/day interest rate for repeat user ::",
                cs_750_799_interest_less_p2_r)
            assert False
        else:
            print(
                "*** No cs_750_799_interest_less_p2_r user issue with more than 0.2/day interest rate for repeat user ***")


    def test_cs_750_799_interest_more_p2_r(self):
        if len(cs_750_799_interest_more_p2_r) > 0:
            print(
                "Error::cs_750_799_interest_more_p2_r user issue with more than 0.2/day interest rate for repeat user ::",
                cs_750_799_interest_more_p2_r)
            assert False
        else:
            print(
                "*** No cs_750_799_interest_more_p2_r user issue with more than 0.2/day interest rate for repeat user ***")


    def test_cs_700_749_interest_less_p3_r(self):
        if len(cs_pl_700_749_interest_less_p3_r) > 0:
            print(
                "Error::cs_pl_700_749_interest_less_p3_r user issue with less than 0.3/day interest rate for repeat user ::",
                cs_pl_700_749_interest_less_p3_r)
            assert False
        else:
            print(
                "*** No cs_pl_700_749_interest_less_p3_r user issue with less than 0.3/day interest rate for repeat user ***")

    def test_cs_pl_700_749_interest_more_p3_r(self):
        if len(cs_pl_700_749_interest_more_p3_r) > 0:
            print(
                "Error::cs_pl_700_749_interest_more_p3_r user issue with more than 0.3/day interest rate for repeat user ::",
                cs_pl_700_749_interest_more_p3)
            assert False
        else:
            print(
                "*** No cs_pl_700_749_interest_more_p3_r user issue with more than 0.3/day interest rate for repeat user ***")

    def test_cs_pl_680_700_interest_less_p3_r(self):
        if len(cs_pl_680_700_interest_less_p3_r) > 0:
            print(
                "Error::cs_pl_680_700_interest_less_p3_r user issue with less than 0.3/day interest rate for repeat user ::",
                cs_pl_680_700_interest_less_p3_r)
            assert False
        else:
            print(
                "*** No cs_pl_680_700_interest_less_p3_r user issue with less than 0.3/day interest rate for repeat user ***")

    def test_cs_pl_680_700_interest_more_p3_r(self):
        if len(cs_pl_680_700_interest_more_p3_r) > 0:
            print(
                "Error::cs_pl_680_700_interest_more_p3_r user issue with more than 0.3/day interest rate for repeat user ::",
                cs_pl_680_700_interest_more_p3_r)
            assert False
        else:
            print(
                "*** No cs_pl_680_700_interest_more_p3_r user issue with more than 0.3/day interest rate for repeat user ***")


    print("Test Execution Completed")
