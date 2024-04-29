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
        global cibil_pl_less_than_700_lid_count, cibil_pl_less_than_700_lid, cibil_pl_700_749_out_lid, cibil_pl_700_749_out_lid_count
        global cibil_pl_750_799_out_lid_count, cibil_pl_750_799_out_lid, cibil_pl_750_799_1_lac_out_lid_count, cibil_pl_750_799_1_lac_out_lid
        global cibil_pl_800_800_lid_count, cibil_pl_800_800_lid

        disAPIData = disAPI.json()["data"]["rows"]


        cibil_pl_less_than_700_lid = []
        cibil_pl_700_749_out_lid = []
        cibil_pl_750_799_out_lid = []
        cibil_pl_750_799_1_lac_out_lid = []
        cibil_pl_800_800_lid = []



        # print(disAPIData)

        for r in disAPIData:
            if r["Completed loans"] <= 3:

                if (r["Cibil Score"] < 700) & (r["Pl Score"] < 700):
                    if r["Approved Salary"] >= 20000:
                        # print("lid::",r["Loan ID"])
                        cibil_pl_less_than_700_lid.append(r["Loan ID"])

                elif (700 <= r["Cibil Score"] <= 749) & (700 <= r["Pl Score"] <= 749):
                    if r["Approved Salary"] >= 20000:
                        # print(r)
                        apprAmt = r["Approved amount"]
                        apprSalary_loan_amt_cal = r["Approved Salary"] * 0.50
                        apprSalary_loan_amt_cal_500_round = apprSalary_loan_amt_cal + 500

                        if apprAmt > apprSalary_loan_amt_cal_500_round:
                            cibil_pl_700_749_out_lid.append(r["Loan ID"])
#
                elif ((750 <= r["Cibil Score"] <= 799) &  (750 <= r["Pl Score"] <= 799)):

                    if r["Approved Salary"] < 50000:

                        # print("lid::", r["Loan ID"])
                        # if (750 >= r["Cibil Score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_2 = r["Approved amount"]
                        apprSalary_loan_amt_cal_2 = r["Approved Salary"] * 0.50
                        apprSalary_loan_amt_cal_500_round_2 = apprSalary_loan_amt_cal_2 + 500

                        if apprAmt_2 > apprSalary_loan_amt_cal_500_round_2:
                            cibil_pl_750_799_out_lid.append(r["Loan ID"])

                elif (750 <= r["Cibil Score"] <= 799) & (750 <= r["Pl Score"] <= 799):
                    if r["Approved Salary"] >= 100000:
                        # if (750 >= r["Cibil Score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_3 = r["Approved amount"]
                        apprSalary_loan_amt_cal_3 = r["Approved Salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round_3 = apprSalary_loan_amt_cal_3 + 500

                        if apprAmt_3 > apprSalary_loan_amt_cal_500_round_3:
                            cibil_pl_750_799_1_lac_out_lid.append(r["Loan ID"])


                elif r["Cibil Score"] >= 800 & r["Pl Score"] >= 800:
                    if r["Approved Salary"] >= 20000:
                        apprAmt_4 = r["Approved amount"]
                        apprSalary_loan_amt_cal_4 = r["Approved Salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round_4 = apprSalary_loan_amt_cal_4 + 500

                        if apprAmt_4 > apprSalary_loan_amt_cal_500_round_4:
                            cibil_pl_800_800_lid.append(r["Loan ID"])


                        # print(r)
                        # print("lid::",r["Loan ID"])
                        # print("apprSalary_loan_amt_cal::",apprSalary_loan_amt_cal_4)
                        # print("apprSalary_loan_amt_cal_500_round::",apprSalary_loan_amt_cal_500_round_4)
                        # print("apprAmt::", apprAmt_4)





        cibil_pl_less_than_700_lid_count = len(cibil_pl_less_than_700_lid)
        cibil_pl_700_749_out_lid_count = len(cibil_pl_700_749_out_lid)
        cibil_pl_750_799_out_lid_count = len(cibil_pl_750_799_out_lid)
        cibil_pl_750_799_1_lac_out_lid_count = len(cibil_pl_750_799_1_lac_out_lid)
        cibil_pl_800_800_lid_count = len(cibil_pl_800_800_lid)

        # print("cibil_pl_less_than_700_lid::",cibil_pl_less_than_700_lid)
        # print("cibil_pl_700_749_out_lid::",cibil_pl_700_749_out_lid)
        # print("cibil_pl_750_799_out_lid::",cibil_pl_750_799_out_lid)
        # print("cibil_pl_750_799_1_lac_out_lid::",cibil_pl_750_799_1_lac_out_lid)
        # print("cibil_pl_800_800_lid::",cibil_pl_800_800_lid)



        print("cibil_pl_less_than_700_lid_count ::",cibil_pl_less_than_700_lid_count)
        print("cibil_pl_700_749_out_lid_count::",cibil_pl_700_749_out_lid_count)
        print("cibil_pl_750_799_out_lid_count::",cibil_pl_750_799_out_lid_count)
        print("cibil_pl_750_799_1_lac_out_lid_count::",cibil_pl_750_799_1_lac_out_lid_count)
        print("cibil_pl_800_800_lid_count::",cibil_pl_800_800_lid_count)



    def test_cs_pl_less_than_700(self):
        if cibil_pl_less_than_700_lid_count > 0:
            print(f" Error :: loans are not correct if cibil_and_pl_less_than_700:: {cibil_pl_less_than_700_lid}")
            assert False
        else:
            print("*** loans are correct if cibil_and_pl_less_than_700 ***")


    def test_cs_pl_700_749_out(self):
        if cibil_pl_700_749_out_lid_count > 0:
            print(f" Error :: loans are not correct, for cibil_pl_700_749 range and 50 % out salary:: {cibil_pl_700_749_out_lid}")
            assert False
        else:
            print("*** loans are correct, 50 % of salary for cibil_pl_700_749 ***")


    def test_cs_pl_750_799_less_50000_out(self):
        if cibil_pl_750_799_out_lid_count > 0:
            print(f" Error :: loans are not correct, 50 % of salary for cibil_pl_750_799 and salary <= 50 k :: {cibil_pl_750_799_out_lid}")
            assert False
        else:
            print("*** loans are correct, 50 % of salary for cibil_pl_750_799 and salary <= 50 k ***")


    def test_cs_pl_750_799_1_lac_out(self):
        if cibil_pl_750_799_1_lac_out_lid_count > 0:
            print(f" Error :: loans are not correct, 75 % of salary for cibil_pl_750_799 and salary 1 lac+:: {cibil_pl_750_799_1_lac_out_lid}")
            assert False
        else:
            print("*** loans are correct, 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ***")


    def test_cs_pl_800_800(self):
        if cibil_pl_800_800_lid_count > 0:
            print(f" Error :: loans are not correct, 75 % of salary for cibil_pl_800_800 :: {cibil_pl_800_800_lid}")
        else:
            print("*** loans are correct, 75 % of salary for cibil_pl_800_800 ***")



    def test_disb_cibil_repeat_user(self, url_dis_cibil):
        print("*** Test execution started ***")
        global cibil_pl_less_than_700_lid_count_r, cibil_pl_less_than_700_lid_r, cibil_pl_700_749_out_lid_r, cibil_pl_700_749_out_lid_count_r
        global cibil_pl_750_799_out_lid_count_r, cibil_pl_750_799_out_lid_r, cibil_pl_750_799_1_lac_out_lid_count_r, cibil_pl_750_799_1_lac_out_lid_r
        global cibil_pl_800_800_lid_count_r, cibil_pl_800_800_lid_r

        disAPIData = disAPI.json()["data"]["rows"]


        cibil_pl_less_than_700_lid_r = []
        cibil_pl_700_749_out_lid_r = []
        cibil_pl_750_799_out_lid_r = []
        cibil_pl_750_799_1_lac_out_lid_r = []
        cibil_pl_800_800_lid_r = []



        # print(disAPIData)

        for s in disAPIData:
            if s["Completed loans"] > 3:

                if s["Cibil Score"] < 700:
                    cibil_pl_less_than_700_lid_r.append(s["Loan ID"])

                elif 700 <= s["Cibil Score"] <= 749:
                    apprAmt_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_r = s["Approved Salary"] * 0.50
                    apprSalary_loan_amt_cal_500_round_r = apprSalary_loan_amt_cal_r + 500

                    if apprAmt_r > apprSalary_loan_amt_cal_500_round_r:
                        cibil_pl_700_749_out_lid_r.append(s["Loan ID"])

                elif (750 <= s["Cibil Score"] <= 799):
                    if s["Approved Salary"] <= 50000:
                        # if (750 >= r["Cibil Score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_2_r = s["Approved amount"]
                        apprSalary_loan_amt_cal_2_r = s["Approved Salary"] * 0.50
                        apprSalary_loan_amt_cal_500_round_2_r = apprSalary_loan_amt_cal_2_r + 500

                        if apprAmt_2_r > apprSalary_loan_amt_cal_500_round_2_r:
                            cibil_pl_750_799_out_lid_r.append(s["Loan ID"])

                elif (750 <= s["Cibil Score"] <= 799):
                    if s["Approved Salary"] >= 100000:
                        # if (750 >= r["Cibil Score"] <= 799) or (750 >= r["Pl Score"] <= 799):

                        apprAmt_3_r = s["Approved amount"]
                        apprSalary_loan_amt_cal_3_r = s["Approved Salary"] * 0.75
                        apprSalary_loan_amt_cal_500_round_3_r = apprSalary_loan_amt_cal_3_r + 500

                        if apprAmt_3_r > apprSalary_loan_amt_cal_500_round_3_r:
                            cibil_pl_750_799_1_lac_out_lid_r.append(s["Loan ID"])

                elif s["Cibil Score"] >= 800:
                    apprAmt_4_r = s["Approved amount"]
                    apprSalary_loan_amt_cal_4_r = s["Approved Salary"] * 0.75
                    apprSalary_loan_amt_cal_500_round_4_r = apprSalary_loan_amt_cal_4_r + 500

                    if apprAmt_4_r > apprSalary_loan_amt_cal_500_round_4_r:
                        cibil_pl_800_800_lid_r.append(s["Loan ID"])


                    #
                    # print("lid::",s["Loan ID"])
                    # print("apprSalary_loan_amt_cal::",apprSalary_loan_amt_cal_r)
                    # print("apprSalary_loan_amt_cal_500_round::",apprSalary_loan_amt_cal_500_round_r)
                    # print("apprAmt::", apprAmt_r)



        cibil_pl_less_than_700_lid_count_r = len(cibil_pl_less_than_700_lid_r)
        cibil_pl_700_749_out_lid_count_r = len(cibil_pl_700_749_out_lid_r)
        cibil_pl_750_799_out_lid_count_r = len(cibil_pl_750_799_out_lid_r)
        cibil_pl_750_799_1_lac_out_lid_count_r = len(cibil_pl_750_799_1_lac_out_lid_r)
        cibil_pl_800_800_lid_count_r = len(cibil_pl_800_800_lid_r)



        # print("cibil_pl_less_than_700_lid_count ::",cibil_pl_less_than_700_lid_count)
        print("cibil_pl_700_749_out_lid_r::",cibil_pl_700_749_out_lid_count_r)
        print("cibil_pl_750_799_out_lid_count_r::",cibil_pl_750_799_out_lid_count_r)
        print("cibil_pl_750_799_1_lac_out_lid_count_r::",cibil_pl_750_799_1_lac_out_lid_count_r)
        print("cibil_pl_800_800_lid_count_r::",cibil_pl_800_800_lid_count_r)



    def test_cs_pl_less_than_700_r(self):
        if cibil_pl_less_than_700_lid_count_r > 0:
            print(f" Error :: loans are not correct if cibil_and_pl_less_than_700 ::Repeat User:: {cibil_pl_less_than_700_lid_r}")
            assert False
        else:
            print("*** loans are correct if cibil_and_pl_less_than_700 ::Repeat User:: ***")


    def test_cs_pl_700_749_out_r(self):
        if cibil_pl_700_749_out_lid_count_r > 0:
            print(f" Error :: loans are not correct for cibil_pl_700_749 range and 50 % out salary ::Repeat User:: {cibil_pl_700_749_out_lid_r}")
            assert False
        else:
            print("*** loans are correct, 50 % of salary for cibil_pl_700_749 ::Repeat User:: ***")


    def test_cs_pl_750_799_less_50000_out_r(self):
        if cibil_pl_750_799_out_lid_count_r > 0:
            print(f" Error :: loans are not correct, 50 % of salary for cibil_pl_750_799 and salary <= 50 k ::Repeat User:: {cibil_pl_750_799_out_lid_r}")
            assert False
        else:
            print("*** loans are correct, 50 % of salary for cibil_pl_750_799 and salary <= 50 k ::Repeat User:: ***")


    def test_cs_pl_750_799_1_lac_out_r(self):
        if cibil_pl_750_799_1_lac_out_lid_count_r > 0:
            print(f" Error :: loans are not correct, 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ::Repeat User:: {cibil_pl_750_799_1_lac_out_lid_r}")
            assert False
        else:
            print("*** loans are correct, 75 % of salary for cibil_pl_750_799 and salary 1 lac+ ::Repeat User:: ***")


    def test_cs_pl_800_800_r(self):
        if cibil_pl_800_800_lid_count_r > 0:
            print(f" Error :: loans are not correct, 75 % of salary for cibil_pl_800_800 ::Repeat User:: {cibil_pl_800_800_lid_r}")
        else:
            print("*** loans are correct, 75 % of salary for cibil_pl_800_800 ::Repeat User:: ***")


print("Test Execution Completed")



