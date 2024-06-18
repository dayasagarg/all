import math

class TestLoanDisbCibil:
    import pytest
    @pytest.fixture
    def url_dis_cibil(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=7)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{pre_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})




    def test_disb_cibil_new_user(self, url_dis_cibil):
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

        # As per new logic (50 % - 75 %), (75 % - 100 %)
        #

        for r in disAPIData:
            if r["Completed loans"] < 3:

                if (r["Cibil score"] < 680) & (r["Pl score"] < 680):
                    if r["Approved salary"] >= 20000:
                        # print("lid::",r["Loan ID"])
                        cibil_pl_less_than_680_lid.append(r["Loan ID"])

                elif (700 <= r["Cibil score"] <= 749) & (700 <= r["Pl score"] <= 749):
                    if r["Approved salary"] >= 20000:
                        # print(r)
                        apprAmt = r["Approved amount"]
                        apprSalary_loan_amt_cal = r["Approved salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round = apprSalary_loan_amt_cal + 500

                        if apprAmt > apprSalary_loan_amt_cal_500_round:
                            cibil_pl_700_749_out_lid.append(r["Loan ID"])
#
                elif ((750 <= r["Cibil score"] <= 799) &  (750 <= r["Pl score"] <= 799)):

                    if r["Approved salary"] < 50000:

                        # print("lid::", r["Loan ID"])
                        # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_2 = r["Approved amount"]
                        apprSalary_loan_amt_cal_2 = r["Approved salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round_2 = apprSalary_loan_amt_cal_2 + 500

                        if apprAmt_2 > apprSalary_loan_amt_cal_500_round_2:
                            cibil_pl_750_799_out_lid.append(r["Loan ID"])

                elif (750 <= r["Cibil score"] <= 799) & (750 <= r["Pl score"] <= 799):
                    if r["Approved salary"] >= 100000:
                        # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_3 = r["Approved amount"]
                        apprSalary_loan_amt_cal_3 = r["Approved salary"] * 1
                        apprSalary_loan_amt_cal_500_round_3 = apprSalary_loan_amt_cal_3 + 500

                        if apprAmt_3 > apprSalary_loan_amt_cal_500_round_3:
                            cibil_pl_750_799_1_lac_out_lid.append(r["Loan ID"])


                elif r["Cibil score"] >= 800 & r["Pl score"] >= 800:
                    if r["Approved salary"] >= 20000:
                        apprAmt_4 = r["Approved amount"]
                        apprSalary_loan_amt_cal_4 = r["Approved salary"] * 1
                        apprSalary_loan_amt_cal_500_round_4 = apprSalary_loan_amt_cal_4 + 500

                        if apprAmt_4 > apprSalary_loan_amt_cal_500_round_4:
                            cibil_pl_800_800_lid.append(r["Loan ID"])

                if r["Cibil score"] > 830 & r["Pl score"] > 830:
                    if r["Approved salary"] >= 20000:
                        if float(r["Interest rate"].replace("%","")) < 0.077:
                            prem_less_77.append(r["Loan ID"])

                        if float(r["Interest rate"].replace("%","")) > 0.077:
                            prem_more_77.append(r["Loan ID"])


                        # print(r)
                        # print("lid::",r["Loan ID"])
                        # print("apprSalary_loan_amt_cal::",apprSalary_loan_amt_cal_4)
                        # print("apprSalary_loan_amt_cal_500_round::",apprSalary_loan_amt_cal_500_round_4)
                        # print("apprAmt::", apprAmt_4)





        cibil_pl_less_than_680_lid_count = len(cibil_pl_less_than_680_lid)
        cibil_pl_700_749_out_lid_count = len(cibil_pl_700_749_out_lid)
        cibil_pl_750_799_out_lid_count = len(cibil_pl_750_799_out_lid)
        cibil_pl_750_799_1_lac_out_lid_count = len(cibil_pl_750_799_1_lac_out_lid)
        cibil_pl_800_800_lid_count = len(cibil_pl_800_800_lid)

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
            print(f" Error :: loans are not rejected if cibil_and_pl_less_than_680:: {cibil_pl_less_than_680_lid}")
            assert False
        else:
            print("*** loans are rejected if cibil_and_pl_less_than_680 ***")


    def test_cs_pl_700_749_out(self):
        if cibil_pl_700_749_out_lid_count > 0:
            print(f" Error :: loan not rejected for cibil_pl_700_749 range and 50 % out salary:: {cibil_pl_700_749_out_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_700_749 ***")

#
    def test_cs_pl_750_799_less_50000_out(self):
        if cibil_pl_750_799_out_lid_count > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 50 % of salary for cibil_pl_750_799 and salary <= 50 k :: {cibil_pl_750_799_out_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_750_799 and salary < 50 k ***")


    def test_cs_pl_750_799_1_lac_out(self):
        if cibil_pl_750_799_1_lac_out_lid_count > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 and salary 1 lac+:: {cibil_pl_750_799_1_lac_out_lid}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ***")

#
    def test_cs_pl_800_800(self):
        if cibil_pl_800_800_lid_count > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_800_800 :: {cibil_pl_800_800_lid}")
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_800_800 ***")

    def test_cs_pl_830_l(self):
        if cibil_pl_830_plus_and_prem_less_77_count > 0:
            print("Error:: premium user issue with less than 0.77 intrest rate for new user :")
        else:
            print(f" No premium user issue with less than 0.77 intrest rate for new user ")

    def test_cs_pl_830_m(self):
        if cibil_pl_830_plus_and_prem_more_77_count > 0:
            print(f"Error:: premium user issue with more than 0.77 intrest rate for new user ::{prem_more_77}")
        else:
            print(f"*** No premium user issue with more than 0.77 intrest rate for new user ***")


#
    def test_disb_cibil_repeat_user(self, url_dis_cibil):
        print("*** Test execution started ***")
        global cibil_less_than_680_lid_count_r, cibil_less_than_680_lid_r, cibil_700_749_out_lid_r, cibil_700_749_out_lid_count_r
        global cibil_750_799_out_lid_count_r, cibil_750_799_out_lid_r, cibil_750_799_1_lac_out_lid_count_r, cibil_750_799_1_lac_out_lid_r
        global cibil_800_800_lid_count_r, cibil_800_800_lid_r
        global cibil_830_plus_and_prem_less_77_count_r, prem_less_77_r, prem_more_77_r, cibil_830_plus_and_prem_more_77_count_r

        disAPIData = disAPI.json()["data"]["rows"]


        cibil_less_than_680_lid_r = []
        cibil_700_749_out_lid_r = []
        cibil_750_799_out_lid_r = []
        cibil_750_799_1_lac_out_lid_r = []
        cibil_800_800_lid_r = []

        prem_less_77_r = []
        prem_more_77_r = []



        # print(disAPIData)

        for s in disAPIData:
            # print(s)
            # if s["Completed loans"] > 3 and isinstance(s["Cibil score"],str):
            #     # print(s["Cibil score"],type(s["Cibil score"]))
            #
            #     if s["Cibil score"] :
            #         print(s["Cibil score"])
                    # cibil_pl_less_than_700_lid_r.append(s["Loan ID"])


            if s["Completed loans"] > 3 and isinstance(s["Cibil score"],int):
                # print(s["Cibil score"],type(s["Cibil score"]))
                if s["Cibil score"] < 680:
                    cibil_less_than_680_lid_r.append(s["Loan ID"])

                elif 700 <= s["Cibil score"] <= 749:
                    apprAmt_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_r = s["Approved salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_r = apprSalary_loan_amt_cal_r + 500

                    if apprAmt_r > apprSalary_loan_amt_cal_500_round_r:
                        cibil_700_749_out_lid_r.append(s["Loan ID"])

                elif (750 <= s["Cibil score"] <= 799):
                    if s["Approved salary"] < 50000:
                        # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_2_r = s["Approved amount"]
                        apprSalary_loan_amt_cal_2_r = s["Approved salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round_2_r = apprSalary_loan_amt_cal_2_r + 500

                        if apprAmt_2_r > apprSalary_loan_amt_cal_500_round_2_r:
                            cibil_750_799_out_lid_r.append(s["Loan ID"])

                elif (750 <= s["Cibil score"] <= 799):
                    if s["Approved salary"] >= 100000:
                        # if (750 >= r["Cibil score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_3_r = s["Approved amount"]
                        apprSalary_loan_amt_cal_3_r = s["Approved salary"] * 1
                        apprSalary_loan_amt_cal_500_round_3_r = apprSalary_loan_amt_cal_3_r + 500

                        if apprAmt_3_r > apprSalary_loan_amt_cal_500_round_3_r:
                            cibil_750_799_1_lac_out_lid_r.append(s["Loan ID"])

                elif s["Cibil score"] >= 800:
                    apprAmt_4_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_4_r = s["Approved salary"] * 1
                    apprSalary_loan_amt_cal_500_round_4_r = apprSalary_loan_amt_cal_4_r + 500

                    if apprAmt_4_r > apprSalary_loan_amt_cal_500_round_4_r:
                        cibil_800_800_lid_r.append(s["Loan ID"])

                    # print("lid::", s["Loan ID"])
                    # print("apprSalary_loan_amt_cal::", apprSalary_loan_amt_cal_r)
                    # print("apprSalary_loan_amt_cal_500_round::", apprSalary_loan_amt_cal_500_round_r)
                    # print("apprAmt::", apprAmt_r)


                # if s["Cibil score"] > 830:
                #     if s["Approved salary"] >= 20000:
                #
                #         if float(s["Interest rate"].replace("%", "")) < 0.077:
                #             prem_less_77_r.append(s["Loan ID"])
                #
                #         if float(s["Interest rate"].replace("%", "")) > 0.077:
                #             prem_more_77_r.append(s["Loan ID"])




        cibil_less_than_680_lid_count_r = len(cibil_less_than_680_lid_r)
        cibil_700_749_out_lid_count_r = len(cibil_700_749_out_lid_r)
        cibil_750_799_out_lid_count_r = len(cibil_750_799_out_lid_r)
        cibil_750_799_1_lac_out_lid_count_r = len(cibil_750_799_1_lac_out_lid_r)
        cibil_800_800_lid_count_r = len(cibil_800_800_lid_r)
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
            print(f" Error :: loans are not rejected if cibil_and_pl_less_than_680 ::Repeat User:: {cibil_less_than_680_lid_r}")
            assert False
        else:
            print("*** loans are rejected if cibil_and_pl_less_than_680 ::Repeat User:: ***")


    def test_cs_700_749_out_r(self):
        if cibil_700_749_out_lid_count_r > 0:
            print(f" Error :: loan not rejected for cibil_pl_700_749 range and 50 % out salary ::Repeat User:: {cibil_700_749_out_lid_r}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_700_749 ::Repeat User:: ***")


    def test_cs_750_799_less_50000_out_r(self):
        if cibil_750_799_out_lid_count_r > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 50 % of salary for cibil_pl_750_799 and salary < 50 k ::Repeat User:: {cibil_750_799_out_lid_r}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 50 % of salary for cibil_pl_750_799 and salary <= 50 k ::Repeat User:: ***")


    def test_cs_750_799_1_lac_out_r(self):
        if cibil_750_799_1_lac_out_lid_count_r > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ::Repeat User:: {cibil_750_799_1_lac_out_lid_r}")
            assert False
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ::Repeat User:: ***")


    def test_cs_800_800_r(self):
        if cibil_800_800_lid_count_r > 0:
            print(f" Error :: loans are not rejected if loan amount is more than 75 % of salary for cibil_pl_800_800 ::Repeat User:: {cibil_800_800_lid_r}")
        else:
            print("*** loans are rejected if loan amount is more than 75 % of salary for cibil_pl_800_800 ::Repeat User:: ***")

    def test_cs_830_l_r(self):
        if cibil_830_plus_and_prem_less_77_count_r > 0:
            print(f"Error:: premium user issue with less than 0.77 intrest rate for repeat user ::{prem_less_77_r}")
        else:
            print(f"*** No premium user issue with less than 0.77 intrest rate for repeat user ***")

    def test_cs_830_m_r(self):
        if cibil_830_plus_and_prem_more_77_count_r > 0:
            print(f"Error:: premium user issue with more than 0.77 intrest rate for repeat user ::{prem_more_77_r}")
        else:
            print(f"*** No premium user issue with more than 0.77 intrest rate for repeat user ***")


print("Test Execution Completed")


