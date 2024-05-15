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

        new_users = []
        repeat_users = []

        disb_amt = []
        int_amt = []

        proc_fees = []
        doc_fees = []
        online_con_fees = []
        risk_ass_fees = []
        stamp_duty_fees = []

        for d in disData:
            if d["App platform"] == "CHINMAY" or d["App platform"] == "LENDITT":
                if d["Completed loans"] == 0:
                    new_users.append(d["Loan ID"])

                if d["Completed loans"] > 0:
                    repeat_users.append(d["Loan ID"])

                if d["Disbursed Amount"]:
                    disb_amt.append(d["Approved amount"])

                if d["Total Interest Amount"]:
                    int_amt.append(d["Total Interest Amount"])

                if d["Total Interest Amount"]:
                    int_amt.append(d["Total Interest Amount"])

                if d["Processing fees"]:
                    proc_fees.append(d["Processing fees"])

                if d["Document Charges"]:
                    doc_fees.append(d["Document Charges"])

                if d["Online convenience fees"]:
                    online_con_fees.append(d["Online convenience fees"])

                if d["Risk assessment fees"]:
                    risk_ass_fees.append(d["Risk assessment fees"])

                if d["Stamp Duty Fees"]:
                    stamp_duty_fees.append(d["Stamp Duty Fees"])


        total_fees = sum(proc_fees) + sum(doc_fees) + sum(online_con_fees) + sum(risk_ass_fees) + sum(stamp_duty_fees)


        print("total_fees::",total_fees)




        new_users_count = len(new_users)
        repeat_users = len(repeat_users)


        total_disb_loans_count = new_users_count + repeat_users

        # print("new_users_count_disb::",new_users_count)
        # print("repeat_users_disb::",repeat_users)
        # print("total/approved_disb_loans_count::",total_disb_loans_count)
        # print("disb_amt::",disb_amt)

        total_disb_amt = sum(disb_amt)
        total_int_amt = sum(int_amt)

        # print("total_disb_amt::",total_disb_amt)
        # print("total_int_amt::",total_int_amt)

        # Report

        # print("monthlyFigureReport_disb_chin_data::", monthlyFigureReport_disb_chin_data)
        # print("monthlyFigureReport_disb_lenditt_data::", monthlyFigureReport_disb_lenditt_data)

        total_chn_disb_report = (monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total disbursement']).replace(",","")
        total_lnd_disb_report = (monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total disbursement']).replace(",","")
        combine_chn_lnd_disb_report = int(total_chn_disb_report) + int(total_lnd_disb_report)

        assert total_disb_amt == combine_chn_lnd_disb_report, "total_disb_amt and combine_chn_lnd_disb_report are not equal"

        print("total_chn_disb_report::",total_chn_disb_report)
        print("total_lnd_disb_report::",total_lnd_disb_report)
        print("combine_chn_lnd_disb_report::",combine_chn_lnd_disb_report)
        print("total_disb_amt::",total_disb_amt)



        total_chn_interest_report = (monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total Expected Interest']).replace(",","")
        total_lnd_interest_report = (monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total Expected Interest']).replace(",","")
        combine_chn_lnd_interest_report = int(total_chn_interest_report) + int(total_lnd_interest_report)

        # assert total_int_amt == combine_chn_lnd_interest_report, "total_int_amt and combine_chn_lnd_interest_report not equal"

        print("total_chn_interest_report::",total_chn_interest_report)
        print("total_lnd_interest_report::",total_lnd_interest_report)
        print("combine_chn_lnd_interest_report::",combine_chn_lnd_interest_report)
        print("total_int_amt::",total_int_amt)


        chn_new_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['New Loan'])
        chn_repeat_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Repeat Loan'])


        lnd_new_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['New Loan'])
        lnd_repeat_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Repeat Loan'])

        new_user_r = chn_new_loan_r + lnd_new_loan_r
        print("new_user_r::",new_user_r)

        assert new_user_r == new_users_count

        repeat_user_r = chn_repeat_loan_r + lnd_repeat_loan_r
        print("repeat_user_r::",repeat_user_r)
        assert repeat_user_r == repeat_users

        print("chn_new_loan_r::", chn_new_loan_r)
        print("chn_repeat_loan_r::", chn_repeat_loan_r)
        print("lnd_new_loan_r::",lnd_new_loan_r)
        print("lnd_repeat_loan_r::",lnd_repeat_loan_r)


        combine_chn_lnd_new_repeat_user_r = chn_new_loan_r + chn_repeat_loan_r + lnd_new_loan_r + lnd_repeat_loan_r
        assert total_disb_loans_count == combine_chn_lnd_new_repeat_user_r, "total_disb_loans_count and combine_chn_lnd_new_repeat_user_r are not equal"
        print("total_disb_loans_count::",total_disb_loans_count)
        print("combine_chn_lnd_new_repeat_user_r::",combine_chn_lnd_new_repeat_user_r)
        print("chn_new_loan_r::",chn_new_loan_r)
        print("chn_repeat_loan_r::",chn_repeat_loan_r)
        print("lnd_new_loan_r::",lnd_new_loan_r)


        # print("combine_chn_lnd_new_repeat_user_r::",combine_chn_lnd_new_repeat_user_r)

        chn_approved_loan_r = int(monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Approved Loan Application'])
        lnd_approved_loan_r = int(monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Approved Loan Application'])
        total_chn_lnd_approved_loan_r = chn_approved_loan_r + lnd_approved_loan_r
        assert total_disb_loans_count == total_chn_lnd_approved_loan_r, "total_disb_loans_count not equal to total_chn_lnd_approved_loan_r"

        print("total_chn_lnd_approved_loan_r::",total_chn_lnd_approved_loan_r)
        print("total_disb_loans_count::",total_disb_loans_count)
        print("chn_approved_loan_r::",chn_approved_loan_r)
        print("lnd_approved_loan_r::",lnd_approved_loan_r)

        chn_total_exp_fees_r = int((monthlyFigureReport_disb_chin_data["data"]["rows"][0]['Total Expected Fees']).replace(",",""))
        lnd_total_exp_fees_r = int((monthlyFigureReport_disb_lenditt_data["data"]["rows"][0]['Total Expected Fees']).replace(",",""))
        combine_chn_lnd_fees_r = chn_total_exp_fees_r + lnd_total_exp_fees_r
        # assert combine_chn_lnd_fees_r == total_fees, "combine_chn_lnd_fees_r not equal to total_fees"

        print("combine_chn_lnd_fees_r::",combine_chn_lnd_fees_r)
        print("total_fees::", total_fees)
        print("chn_total_exp_fees_r::",chn_total_exp_fees_r)
        print("lnd_total_exp_fees_r::",lnd_total_exp_fees_r)


