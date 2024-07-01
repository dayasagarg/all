import math

class TestLoanInterestMadhur:
    def test_disb_interest_m(self, url):
        print("*** Test execution started ***")

        # print(disAPIData)
        diff_int_more = []
        diff_int_less = []
        remain = []

        diff_int_more_lid = []
        diff_int_less_lid = []
        remain_lid = []

        for r in url:
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

        m_3 = [i for i in diff_int_more if i > 3]
        print("m_3::", m_3)

        if len(diff_int_less) > 0:
            print("Error::Interest rate is wrong in case of negative difference::", diff_int_less)
            assert False
        else:
            print("*** Interest rate is correct in case of negative difference ***")

        if len(m_3) > 0:
            print("Error::Interest rate positive difference is more than Rs.3::", m_3)
            assert False
        else:
            print("*** Interest rate positive difference is below Rs.3 ***")

        print("*** Test execution completed ***")

