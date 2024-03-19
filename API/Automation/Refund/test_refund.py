import requests

class TestRefund:
    def test_ref_url(self):
        global allRepay, refund_compl, refund_pend, emiRepaymentStatus, getTransactionDetails

        emiRepaymentStatus = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus?fromDate=2024-02-03T10:00:00.000Z&endDate=2024-02-07T10:00:00.000Z&type=TOTAL&page=1&download=true")



        allRepay = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-05T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")
        # print(allRepay.json())


        headers = {"adminid": "37"}
        # refund_compl = requests.get("https://chinmayfinserve.com/admin-prod/admin/transaction/getRefundableData",params={"startDate":"2024-02-01T10:00:00.000Z","endDate":"2024-02-05T10:00:00.000Z","status":1},headers=headers,verify=False)
        refund_compl = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/getRefundableData?startDate=2024-02-04T10:00:00.000Z&endDate=2024-02-05T10:00:00.000Z&status=1",
            headers=headers)
        refund_pend = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/getRefundableData?startDate=2024-02-01T10:00:00.000Z&endDate=2024-02-04T10:00:00.000Z&status=-1",
            headers=headers)


    # def test_refund_emi_trans(self):   # dev logic lack
    #     emiRepaymentStatus_data = emiRepaymentStatus.json()["data"]["rows"]
    #     # print(emiRepaymentStatus_data)
    #
    #     emiRep_lid = []
    #     for er in emiRepaymentStatus_data:
    #         if er["Today's EMI status"] == "FAILED":
    #             emiRep_lid.append(er["Loan ID"])
    #
    #     # print("emiRep_lid::",emiRep_lid)
    #
    #     refund_tran_lid = []
    #     for el in emiRep_lid:
    #         getTransactionDetails = requests.get(
    #             "https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails",params = {"loanId":el})
    #
    #         getTransactionDetails_data = getTransactionDetails.json()["data"]
    #         # print(getTransactionDetails_data)
    #
    #
    #         for t in getTransactionDetails_data:
    #             if t["Pay type"] == "REFUND":
    #                 refund_tran_lid.append(el)
    #
    #     print("refund_tran_lid::",refund_tran_lid)






    def test_refund_amt(self):
        global dupl_repay_lid,match_app_auto

        allRepay_data = allRepay.json()["data"]["rows"]

        un_repay_lid = []
        dupl_repay_lid = []

        app = []
        auto = []

        for r in allRepay_data:

            if (r["Repayment via"] == "APP") and (r["Repayment via"] == "AUTODEBIT"):
                app.append(r["Loan id"])

            # if :
            #     auto.append(r["Loan id"])


            # if r["Loan id"] not in un_repay_lid:
            #     un_repay_lid.append(r["Loan id"])
            # else:
            #     dupl_repay_lid.append(r["Loan id"])

        print(app)

        match_app_auto = []
        for ap in app:
            if ap in auto:
                match_app_auto.append(ap)

        print("match_app_auto::", match_app_auto)


    #
    # def test_ref_completed(self):
    #     refund_compl_data = refund_compl.json()["data"]["rows"]
    #     # print(refund_compl_data)
    #
    #     refund_comp_loan_ids = []
    #     for rc in refund_compl_data:
    #         if rc["loanId"]:
    #             refund_comp_loan_ids.append(rc["loanId"])
    #
    #     ref_miss_compl = []
    #
    #     for dut in match_app_auto:
    #
    #         if dut not in refund_comp_loan_ids:
    #             ref_miss_compl.append(dut)
    #
    #     print("refund_comp_loan_ids::", refund_comp_loan_ids)
    #     print("ref_miss_compl::", ref_miss_compl)
    #
    #     # print("un_repay_lid",un_repay_lid)
    #     # print("dupl_repay_lid:: ", dupl_repay_lid)
