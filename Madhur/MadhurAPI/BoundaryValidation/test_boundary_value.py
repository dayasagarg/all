
class TestAppAmt:
    def test_dis_loan_amt_lower(self, url):

        loanID = []
        for d in url:
            # print(d)
            if d["Approved amount"] < 10000:
                loanID.append(d["Loan ID"])
        # print(loanID)

        count_loan = len(loanID)

        if count_loan > 0:
            print(f"Error::Approved amount is below Rs.10 k found :: loanID :: {loanID}")
            assert False
        else:
            print("*** Approved amount is above Rs.10 k ***")

    def test_dis_loan_amt_upper(self,url):

        l_Id_upper = []
        for da in url:
            if da["Approved amount"] > 37500:
                l_Id_upper.append(da["Loan ID"])

        count_l_Id_upper = len(l_Id_upper)

        if count_l_Id_upper > 0:
            print(f"Error:: Approved amount is above Rs.37500 found :: l_Id_upper :: {l_Id_upper}")
            assert False
        else:
            print("*** Approved amount is below Rs.37500 ***")


    def test_emi_limit(self,url):

        lIdEMI = []
        for d in url:
            if (d["Total EMI"] < 2 or d["Total EMI"] > 2):
                lIdEMI.append(d["Loan ID"])


        count_lIdEMI = len(lIdEMI)

        if count_lIdEMI > 0:
            print(f"Error:: EMI not within limit of 2:: lIdEMI :: {lIdEMI}")
            assert False
        else:
            print("*** EMI's are within limit of 2 ***")


    def test_disb_int_rate(self,url):

        l_id_intRate_less_77 = []
        l_id_intRate_above_1 = []

        for inte in url:
            if float(inte["Interest rate"].replace("%","")) < 0.077:
                l_id_intRate_less_77.append(inte["Loan ID"])

            elif float(inte["Interest rate"].replace("%","")) > 0.3:
                l_id_intRate_above_1.append(inte["Loan ID"])

        count_l_id_intRate_77 = len(l_id_intRate_less_77)
        count_l_id_intRate_1 = len(l_id_intRate_above_1)


        if count_l_id_intRate_77 > 0:
            print(f"Error:: Interest rate below 0.077% /day found :: l_id :: {l_id_intRate_less_77}")
            assert False
        else:
            print("*** Interest rate is not below 0.077% /day or 28 % /annum ***")


        if count_l_id_intRate_1 > 0:
            print(f"Error:: Interest rate above 0.3% /day found :: l_id :: {l_id_intRate_above_1}")
            assert False
        else:
            print("*** Interest rate is not above 0.3% /day or 108 % /annum ***")


    def test_loan_tenure(self,url):

        loan_id_tenure = []
        for lt in url:
            if  (lt["Loan tenure (days)"] < 42 or lt["Loan tenure (days)"] > 72):
                loan_id_tenure.append(lt["Loan ID"])

        count_l_data = len(loan_id_tenure)
        # print("count_l_data::",count_l_data)

        if count_l_data > 0:
            print(f"Errors::loan tenure not within 42 to 72 days :: loan_id_tenure :: {loan_id_tenure}")
            assert False
        else:
            print("loan tenure is within 42 to 72 days")


    def test_dis_salary_amt_lower(self, url):

        loanID_sal = []
        for s in url:

            if s["Approved salary"] < 20000:
                loanID_sal.append(s["Loan ID"])
        # print(loanID)

        count_loan_sal = len(loanID_sal)

        if count_loan_sal > 0:
            print(f"Error:: Loan accepted if Approved Salary is below Rs.20000 found :: loanID :: {loanID_sal}")
            assert False
        else:
            print("*** Loan rejected if Approved Salary is below Rs.20000 ***")

    def test_dis_salary_amt_upper(self,url):

        loanID_sal = []
        for s in url:

            if s["Approved salary"] > 50000:
                loanID_sal.append(s["Loan ID"])
        # print(loanID)

        count_loan_sal = len(loanID_sal)

        if count_loan_sal > 0:
            print(f"Error:: Loan accepted if Approved Salary is above Rs.50 k found :: loanID :: {loanID_sal}")
            assert False
        else:
            print("*** Loan rejected/moved to chinmay if Approved Salary is above Rs.50 k ***")
        print("### Test Execution Completed ###")
