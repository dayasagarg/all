import math
# for on and before April 2024, After may onward new logic

class TestDisbMonthlyLoanFigure:
    import pytest
    @pytest.fixture
    def url_dis(self):
        global disAPI, requests, monthlyFigureReport_disb_chin_data, monthlyFigureReport_disb_lenditt_data
        import requests
        from datetime import datetime, timedelta

        # curr = datetime.now()
        # curr_str = datetime.strftime(curr, "%Y-%m-%d")
        # prev = curr - timedelta(days=30)
        # pre_str = datetime.strftime(prev, "%Y-%m-%d")

        # disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
        #                       params={"start_date": f"{pre_str}T10:00:00.000Z",
        #                               "end_date": f"{curr_str}T10:00:00.000Z",
        #                               "page": 1, "download": "true"})

        disAPI = requests.get("https://chinmayfinserve.com/admin-prod//admin/dashboard/allDisbursedLoans?start_date=2024-04-01T10%3A00%3A00.000Z&end_date=2024-04-30T10%3A00%3A00.000Z&page=1&download=true")

        payload_chn = {
    "page": 1,
    "pagesize": 10,
    "startDate": "2024-04-01T10:00:00.000Z",
    "endDate": "2024-04-30T10:00:00.000Z",
    "report": "Monthly loan figures",
    "appType": "1"
}

        monthlyFigureReport_disb_chin = requests.post("https://chinmayfinserve.com/admin-prod//admin/report/getMonthLoanFigureReport",json=payload_chn)
        monthlyFigureReport_disb_chin_data = monthlyFigureReport_disb_chin.json()

        payload_lndt = {
            "page": 1,
            "pagesize": 10,
            "startDate": "2024-04-01T10:00:00.000Z",
            "endDate": "2024-04-30T10:00:00.000Z",
            "report": "Monthly loan figures",
            "appType": "0"
        }

        monthlyFigureReport_disb_lenditt = requests.post(
            "https://chinmayfinserve.com/admin-prod//admin/report/getMonthLoanFigureReport", json=payload_lndt)
        monthlyFigureReport_disb_lenditt_data = monthlyFigureReport_disb_lenditt.json()

    def test_disb(self, url_dis):
        print("*** Test execution started ***")

        global disData

        disData = disAPI.json()["data"]["rows"]

        # print(disData)
        global new_users_chn, repeat_users_chn, disb_amt_chn, int_amt_chn, proc_fees_chn, doc_fees_chn, doc_fees_chn, online_con_fees_chn, risk_ass_fees_chn, stamp_duty_fees_chn
        # chinmay
        new_users_chn = []
        repeat_users_chn = []

        disb_amt_chn = []

        int_amt_chn = []

        proc_fees_chn = []
        doc_fees_chn = []
        online_con_fees_chn = []
        risk_ass_fees_chn = []
        stamp_duty_fees_chn = []

        global proc_fees_chn_new_user, doc_fees_chn_new_user, online_con_fees_chn_new_user, risk_ass_fees_chn_new_user, stamp_duty_fees_chn_new_user
        # chinmay new user
        proc_fees_chn_new_user = []
        doc_fees_chn_new_user = []
        online_con_fees_chn_new_user = []
        risk_ass_fees_chn_new_user = []
        stamp_duty_fees_chn_new_user = []


        global new_users_lndt, repeat_users_lndt, disb_amt_lndt, int_amt_lndt, proc_fees_lndt, doc_fees_lndt, online_con_fees_lndt, risk_ass_fees_lndt, stamp_duty_fees_lndt
        # lenditt
        new_users_lndt = []
        repeat_users_lndt = []

        disb_amt_lndt = []

        int_amt_lndt = []

        proc_fees_lndt = []
        doc_fees_lndt = []
        online_con_fees_lndt = []
        risk_ass_fees_lndt = []
        stamp_duty_fees_lndt = []

        global proc_fees_lndt_new_user, doc_fees_lndt_new_user, online_con_fees_lndt_new_user, risk_ass_fees_lndt_new_user, stamp_duty_fees_lndt_new_user
        #lenditt new user

        proc_fees_lndt_new_user = []
        doc_fees_lndt_new_user = []
        online_con_fees_lndt_new_user = []
        risk_ass_fees_lndt_new_user = []
        stamp_duty_fees_lndt_new_user = []


        for d in disData:
            if d["App platform"] == "CHINMAY":
                if d["Completed loans"] == 0:
                    new_users_chn.append(d["Loan ID"])

                if d["Completed loans"] > 0:
                    repeat_users_lndt.append(d["Loan ID"])

                if d["Approved amount"]:
                    disb_amt_chn.append(d["Approved amount"])

                if d["Total Interest Amount"]:
                    int_amt_chn.append(d["Total Interest Amount"])

                if d["Processing fees"]:
                    proc_fees_chn.append(d["Processing fees"])

                if d["Document Charges"]:
                    doc_fees_chn.append(d["Document Charges"])

                if d["Online convenience fees"]:
                    online_con_fees_chn.append(d["Online convenience fees"])

                if d["Risk assessment fees"]:
                    risk_ass_fees_chn.append(d["Risk assessment fees"])

                if d["Stamp Duty Fees"]:
                    stamp_duty_fees_chn.append(d["Stamp Duty Fees"])


                if d["Completed loans"] == 0:
                    if d["Processing fees"]:
                        proc_fees_chn_new_user.append(d["Processing fees"])

                    if d["Document Charges"]:
                        doc_fees_chn_new_user.append(d["Document Charges"])

                    if d["Online convenience fees"]:
                        online_con_fees_chn_new_user.append(d["Online convenience fees"])

                    if d["Risk assessment fees"]:
                        risk_ass_fees_chn_new_user.append(d["Risk assessment fees"])

                    if d["Stamp Duty Fees"]:
                        stamp_duty_fees_chn_new_user.append(d["Stamp Duty Fees"])



            if d["App platform"] == "LENDITT":
                if d["Completed loans"] == 0:
                    new_users_lndt.append(d["Loan ID"])

                if d["Completed loans"] > 0:
                    repeat_users_lndt.append(d["Loan ID"])

                if d["Approved amount"]:
                    disb_amt_lndt.append(d["Approved amount"])

                if d["Total Interest Amount"]:
                    int_amt_lndt.append(d["Total Interest Amount"])

                if d["Processing fees"]:
                    proc_fees_lndt.append(d["Processing fees"])

                if d["Document Charges"]:
                    doc_fees_lndt.append(d["Document Charges"])

                if d["Online convenience fees"]:
                    online_con_fees_lndt.append(d["Online convenience fees"])

                if d["Risk assessment fees"]:
                    risk_ass_fees_lndt.append(d["Risk assessment fees"])

                if d["Stamp Duty Fees"]:
                    stamp_duty_fees_lndt.append(d["Stamp Duty Fees"])


                if d["Completed loans"] == 0:
                    if d["Processing fees"]:
                        proc_fees_lndt_new_user.append(d["Processing fees"])

                    if d["Document Charges"]:
                        doc_fees_lndt_new_user.append(d["Document Charges"])

                    if d["Online convenience fees"]:
                        online_con_fees_lndt_new_user.append(d["Online convenience fees"])

                    if d["Risk assessment fees"]:
                        risk_ass_fees_lndt_new_user.append(d["Risk assessment fees"])

                    if d["Stamp Duty Fees"]:
                        stamp_duty_fees_lndt_new_user.append(d["Stamp Duty Fees"])




        # disburesement
        total_chn_disb_report = int((monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total disbursement']).replace(",",""))
        total_lnd_disb_report = int((monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total disbursement']).replace(",",""))
        combine_chn_lnd_disb_report = total_chn_disb_report + total_lnd_disb_report
        total_disb_amt = sum(disb_amt_chn) + sum(disb_amt_lndt)

        print("total_chn_disb_report::",total_chn_disb_report)
        print("total_lnd_disb_report::",total_lnd_disb_report)
        print("combine_chn_lnd_disb_report::",combine_chn_lnd_disb_report)
        print("total_disb_amt::",total_disb_amt)
        disb_amt_chn = sum(disb_amt_chn)
        disb_amt_lndt = sum(disb_amt_lndt)


        print("disb_amt_chn::",disb_amt_chn)
        print("disb_amt_lndt::",disb_amt_lndt)
        print("E:: diff_total_chn_disb_report_and_disb_amt_chn::",total_chn_disb_report - disb_amt_chn)
        print("E:: diff_total_lnd_disb_report_and_disb_amt_lndt::",total_lnd_disb_report - disb_amt_lndt)
        print("E:: diff_total_disb_amt_and_combine_chn_lnd_disb_report::",total_disb_amt - combine_chn_lnd_disb_report)

        assert total_chn_disb_report == disb_amt_chn, "chinmay disbursement report issue"
        assert total_lnd_disb_report == disb_amt_lndt, "lenditt disbursement report issue"
        assert total_disb_amt == combine_chn_lnd_disb_report, "total_disb_amt and combine_chn_lnd_disb_report are not equal"
        # print("*** disburesement amount in report is as per disbursed amount ***")



        # interest
        total_chn_interest_report = int((monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total Expected Interest']).replace(",",""))
        total_lnd_interest_report = int((monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total Expected Interest']).replace(",",""))
        combine_chn_lnd_interest_report = total_chn_interest_report + total_lnd_interest_report
        total_int_amt = sum(int_amt_chn) + sum(int_amt_lndt)

        print("total_int_amt::",total_int_amt)
        print("combine_chn_lnd_interest_report::",combine_chn_lnd_interest_report)

        print("total_chn_interest_report::",total_chn_interest_report)
        print("total_lnd_interest_report::",total_lnd_interest_report)
        print("combine_chn_lnd_interest_report::",combine_chn_lnd_interest_report)
        print("total_int_amt::",total_int_amt)


        int_amt_chn = sum(int_amt_chn)
        int_amt_lndt = sum(int_amt_lndt)
        print("# E:: diff_total_chn_interest_report_and_int_amt_chn::",total_chn_interest_report - int_amt_chn)
        print("# E:: diff_total_lnd_interest_report_and_int_amt_lndt::",total_lnd_interest_report - int_amt_lndt)
        print("# E:: diff_total_int_amt_and_combine_chn_lnd_interest_report::",total_int_amt - combine_chn_lnd_interest_report)

        # assert total_chn_interest_report == int_amt_chn, "chinmay interest amount report issue"
        # assert total_lnd_interest_report == int_amt_lndt, "lenditt interest amount report issue"
        # assert total_int_amt == combine_chn_lnd_interest_report, "total_int_amt and combine_chn_lnd_interest_report not equal"
        # print("*** interest in disburesement report is as per disbursed interest ***")


        # users

        new_users_count = len(new_users_chn) + len(new_users_lndt)
        repeat_users = len(repeat_users_chn) + len(repeat_users_lndt)
        total_disb_loans_count = new_users_count + repeat_users


        chn_new_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['New Loan'])
        chn_repeat_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Repeat Loan'])

        lnd_new_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['New Loan'])
        lnd_repeat_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Repeat Loan'])

        new_user_r = chn_new_loan_r + lnd_new_loan_r
        print("new_user_r::",new_user_r)
        print("new_users_count::",new_users_count)
        print("# E:: diff_new_user_r_and_new_users_count::",new_user_r - new_users_count)
        assert new_user_r == new_users_count
        # print("*** new user in disburesement report is as per disbursed new user ***")

        repeat_user_r = chn_repeat_loan_r + lnd_repeat_loan_r
        print("repeat_user_r::",repeat_user_r)
        print("repeat_users::",repeat_users)
        print("# E:: diff_repeat_user_r_and_repeat_users::",repeat_user_r - repeat_users)
        assert repeat_user_r == repeat_users
        # print("*** repeat user in disburesement report is as per disbursed repeat user ***")

        print("chn_new_loan_r::", chn_new_loan_r)
        print("chn_repeat_loan_r::", chn_repeat_loan_r)
        print("lnd_new_loan_r::",lnd_new_loan_r)
        print("lnd_repeat_loan_r::",lnd_repeat_loan_r)


        combine_chn_lnd_new_repeat_user_r = chn_new_loan_r + chn_repeat_loan_r + lnd_new_loan_r + lnd_repeat_loan_r
        print("total_disb_loans_count::",total_disb_loans_count)
        print("combine_chn_lnd_new_repeat_user_r::",combine_chn_lnd_new_repeat_user_r)
        print("chn_new_loan_r::",chn_new_loan_r)
        print("chn_repeat_loan_r::",chn_repeat_loan_r)
        print("lnd_new_loan_r::",lnd_new_loan_r)
        print("# E:: diff_total_disb_loans_count_and_combine_chn_lnd_new_repeat_user_r::",total_disb_loans_count - combine_chn_lnd_new_repeat_user_r)
        assert total_disb_loans_count == combine_chn_lnd_new_repeat_user_r, "total_disb_loans_count and combine_chn_lnd_new_repeat_user_r are not equal"
        # print("*** total loans in disburesement report is as per disbursed total loans ***")



        # print("combine_chn_lnd_new_repeat_user_r::",combine_chn_lnd_new_repeat_user_r)

        chn_approved_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Approved Loan Application'])
        lnd_approved_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Approved Loan Application'])
        total_chn_lnd_approved_loan_r = chn_approved_loan_r + lnd_approved_loan_r

        print("total_chn_lnd_approved_loan_r::",total_chn_lnd_approved_loan_r)
        print("total_disb_loans_count::",total_disb_loans_count)
        print("chn_approved_loan_r::",chn_approved_loan_r)
        print("lnd_approved_loan_r::",lnd_approved_loan_r)
        print("# E:: diff_total_disb_loans_count_and_total_chn_lnd_approved_loan_r::",total_disb_loans_count - total_chn_lnd_approved_loan_r)
        assert total_disb_loans_count == total_chn_lnd_approved_loan_r, "total_disb_loans_count not equal to total_chn_lnd_approved_loan_r"
        # print("*** total approved loans in disburesement report is as per disbursed total loans ***")


        # fees
        total_fees_chn = sum(proc_fees_chn) + sum(doc_fees_chn) + sum(online_con_fees_chn) + sum(
            risk_ass_fees_chn) + sum(stamp_duty_fees_chn)
        print("total_fees_chn::", total_fees_chn)

        total_fees_lndt = sum(proc_fees_lndt) + sum(doc_fees_lndt) + sum(online_con_fees_lndt) + sum(
            risk_ass_fees_lndt) + sum(stamp_duty_fees_lndt)
        print("total_fees_lndt::", total_fees_lndt)

        total_fees = total_fees_chn + total_fees_lndt

        total_fees_chn_new = sum(proc_fees_chn_new_user) + sum(doc_fees_chn_new_user) + sum(
            online_con_fees_chn_new_user) + sum(risk_ass_fees_chn_new_user) + sum(stamp_duty_fees_chn_new_user)
        total_fees_lndt_new = sum(proc_fees_lndt_new_user) + sum(doc_fees_lndt_new_user) + sum(
            online_con_fees_lndt_new_user) + sum(risk_ass_fees_lndt_new_user) + sum(stamp_duty_fees_lndt_new_user)
        total_fees_chn_lndt_new = total_fees_chn_new + total_fees_lndt_new


        chn_total_exp_fees_r = int((monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total Expected Fees']).replace(",",""))
        lnd_total_exp_fees_r = int((monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total Expected Fees']).replace(",",""))
        combine_chn_lnd_fees_r = chn_total_exp_fees_r + lnd_total_exp_fees_r


        print("combine_chn_lnd_fees_r::",combine_chn_lnd_fees_r)
        print("total_fees::", total_fees)
        print("chn_total_exp_fees_r::",chn_total_exp_fees_r)
        print("lnd_total_exp_fees_r::",lnd_total_exp_fees_r)
        print("# E:: diff_combine_chn_lnd_fees_r_and_total_fees::",combine_chn_lnd_fees_r - total_fees)
        # assert combine_chn_lnd_fees_r == total_fees, "combine_chn_lnd_fees_r not equal to total_fees"
        # print("*** total fees in disburesement report is as per disbursed total_fees ***")

        # New Loan Expected Fees
        new_loan_expected_fees_chn_r = int((monthlyFigureReport_disb_chin_data["data"]["rows"][0]['New Loan Expected Fees']).replace(",",""))
        new_loan_expected_fees_lndt_r = int((monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['New Loan Expected Fees']).replace(",",""))
        new_loan_expected_fees_chn_lndt_total_r = new_loan_expected_fees_chn_r + new_loan_expected_fees_lndt_r


        print("new_loan_expected_fees_chn_lndt_total_r::",new_loan_expected_fees_chn_lndt_total_r)
        print("total_fees_chn_lndt_new::",total_fees_chn_lndt_new)
        print("# E:: diff_new_loan_expected_fees_chn_lndt_total_r_and_total_fees_chn_lndt_new::",new_loan_expected_fees_chn_lndt_total_r - total_fees_chn_lndt_new)
        assert new_loan_expected_fees_chn_lndt_total_r == total_fees_chn_lndt_new
        # print("*** new_loan_expected_fees for chn_lndt in disburesement report is as per disbursed total_fees ***")

