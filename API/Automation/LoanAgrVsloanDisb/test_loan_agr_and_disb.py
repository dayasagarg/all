import math

class TestLoanAgrDis:
    import pytest

    @pytest.fixture
    def url_agr_dis(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=1)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")



        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{curr_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})


    def test_agr_disb(self, url_agr_dis):
        global loanAmount,app_amt,loanAgrAPI,intRate_disb,int_rate_la,emi_la,totalEMI,loanAgrAPIDataTenure,loanTenure,loan_tenure_la,name_la,name,nbfc,nbfc_la,procFees,procFees_la, sr,loanAgrAPIDataLoanId,dis_lid,riskFees,riskFees_la,docFees,docFees_la,gstAmt,gst_la,a
        disAPIData = disAPI.json()["data"]["rows"]

        dis_lid = []
        app_amt = []
        loanAmtStr = []
        intRate_disb = []
        totalEMI = []
        loanTenure = []
        name = []
        procFees = []
        docFees = []
        gstAmt = []


        for dis in disAPIData:
            if dis["Loan ID"]:
                dis_lid.append(dis["Loan ID"])

            if dis["Approved amount"]:
                app_amt.append(dis["Approved amount"])

            if dis["Interest rate"]:
                intRate_disb.append(float(dis["Interest rate"].replace("%","")))

            if dis["Total EMI"]:
                totalEMI.append(dis["Total EMI"])

            if dis["Loan tenure (days)"]:
                loanTenure.append(dis["Loan tenure (days)"])

            if dis["Name"]:
                name.append(dis["Name"])

            if dis["Processing fees"]:
                procFees.append(dis["Processing fees"])

            if dis["Document charges"]:
                docFees.append(dis["Document charges"])

            if dis["GST amount"]:
                gstAmt.append(dis["GST amount"])



        # print(riskFees)
        # print("app_amt::",app_amt)


        global lid

        int_rate_la = []
        emi_la = []
        loan_tenure_la = []
        name_la = []
        proc_fees_str_la = []
        doc_fees_str_la = []
        risk_fees_str_la = []
        sgst_str_la = []
        cgst_str_la = []



        for lid in dis_lid:

            loanAgrAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/esign/getLoanAgreement",
                                      params={"loanId": lid})

            loanAgrAPIData = loanAgrAPI.json()["data"]["eSign_agree_data"]["emiTotalPrincipal"]
            loanAmtStr.append(loanAgrAPIData)
            # print("loanAgrAPIData::",loanAgrAPIData)

            loanAgrAPIDataLoanId = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanId"]
            loanAgrAPIDataIntRate = loanAgrAPI.json()["data"]["eSign_agree_data"]["interestRatePerDay"]
            int_rate_la.append(round(float(loanAgrAPIDataIntRate), 3))

            loanAgrAPIDataEMI = loanAgrAPI.json()["data"]["eSign_agree_data"]["numberOfEmis"]
            emi_la.append(loanAgrAPIDataEMI)

            loanAgrAPIDataTenure = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanTenure"]
            loan_tenure_la.append(int(loanAgrAPIDataTenure))

            loanAgrAPIDataName = loanAgrAPI.json()["data"]["eSign_agree_data"]["borrowerName"]
            name_la.append(loanAgrAPIDataName)

            loanAgrAPIDataProcAmt = loanAgrAPI.json()["data"]["eSign_agree_data"]["processingAmount"]
            proc_fees_str_la.append(loanAgrAPIDataProcAmt)

            loanAgrAPIDataDoc = loanAgrAPI.json()["data"]["eSign_agree_data"]["documentAmount"]
            doc_fees_str_la.append(loanAgrAPIDataDoc)

            loanAgrAPIDataRisk = loanAgrAPI.json()["data"]["eSign_agree_data"]["riskAssessmentCharge"]
            risk_fees_str_la.append(loanAgrAPIDataRisk)

            loanAgrAPIDataSGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["sgstCharges"]
            sgst_str_la.append(math.ceil(float(loanAgrAPIDataSGST.replace("₹", ""))))

            loanAgrAPIDataCGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["cgstCharges"]
            cgst_str_la.append(math.ceil(float(loanAgrAPIDataCGST.replace("₹", ""))))


            # print(loanAgrAPIDataRisk)


        gst_la = [sum(i) for i in zip(sgst_str_la,cgst_str_la)]

        # print("cgst_str_la::", cgst_str_la)
        # print("sgst_str_la::", sgst_str_la)
        # print("gst_la", gst_la)
        print("dis_lid::",dis_lid)
        print("dis_lid_count::", len(dis_lid))
        # print("gstAmt::",gstAmt)


        loanAmount = []
        for a in loanAmtStr:
            if "₹" in a:
                ss = a.strip("₹")
                aa = ss.replace(",", "")
                loanAmount.append(int(aa))

        print("loanAmount::",loanAmount)
        print("app_amt::",app_amt)



        procFees_la = []
        for f in proc_fees_str_la:
            if "₹" in f:
                sr = f.strip("₹")
                rc = sr.replace(",", "")
                procFees_la.append(int(rc))
            else:
                pass

        docFees_la = []
        for d in doc_fees_str_la:
            if "₹" in d:
                ds = d.strip("₹")
                rd = ds.replace(",", "")
                docFees_la.append(int(rd))
            else:
                pass
    #
        riskFees_la = []
        for l in risk_fees_str_la:
            if "₹" in l:
                # lr = l.strip("₹")
                rc = l.replace("₹", "")
                riskFees_la.append(int(rc))
            else:
                pass


        print(riskFees_la)



    def test_loan_amt(self):
        if loanAmount == app_amt:
            print(f"loan amount and approved amount are equal")
        else:
            print(f"loan amount and approved amount are not equal::{lid}")
            assert False


    def test_int_rate(self):
        if intRate_disb == int_rate_la:
            print("intRate_disb and int_rate_la are equal")
            print("intRate_disb::",intRate_disb)
            print("int_rate_la::",int_rate_la)
        else:
            print("intRate and int_rate_la are not equal")
            print("intRate_disb::",intRate_disb)
            print("int_rate_la::",int_rate_la)

            # for j in range(len(intRate_disb)):
            #     diff_int_rate = intRate_disb[j] - int_rate_la[j]
            #
            #     print("diff_int_rate::",diff_int_rate)



            # print("intRate_count::", len(intRate))
            # print("int_rate_la_count::", len(int_rate_la))
            #
            # assert False

    def test_total_emi(self):
        if totalEMI == emi_la:
            print("totalEMI and emi_la are equal")
        else:
            print("totalEMI and emi_la are not equal")
            assert False
    #
    #
    def test_tenure(self):
        if loanTenure == loan_tenure_la:
            print("loan tenure in disbursement and loan agreement are equal")
        else:
            print("loan tenure in disbursement and loan agreement are not equal")
            assert False

    def test_name(self):
        if name == name_la:
            print("Name is equal in loan agreement and disburement")
        else:
            print("Name mismatch is found")
            assert False

    def test_proc_fees(self):
        # print(dis_lid)
        # print("procFees::",procFees)
        # print("procFees_la::",procFees_la)
        proc_fees_diff_total = list(map(lambda a,b:a-b, procFees,procFees_la))
        # print("proc_fees_diff_total::",proc_fees_diff_total)

        proc_fees_diff_max = [p for p in proc_fees_diff_total if p > 0 or p < 0]
        print("proc_fees_diff_max",proc_fees_diff_max)

        if procFees == procFees_la:
            print("procFees is equal in both loan agreement and disbursement")
        else:
            print(f"procFees is mismatched::{lid}")
            assert False


    def test_doc_fees(self):

        if docFees == docFees_la:
            print("docFees is equal in both loan agreement and disbursement")
        else:
            print("docFees mismatched")
            assert False



    def test_gst(self):
        # print("gstAmt::",gstAmt)
        # print("gst_la::",gst_la)

        gst_diff_total = list(map(lambda x,y:x-y,gstAmt,gst_la))

        gst_diff_max = [g for g in gst_diff_total if g < 0 or g > 0]
        print("gst_diff_max::",gst_diff_max)

        if gstAmt == gst_la:
            print("gst amount in disbursement and loan agreement matched")
        else:
            gst_msg = [m for m in gst_diff_max if m > 2 or m < -2]
            print(f"Difference more than Rs.2 encountered in gst::{gst_msg}")
            assert len(gst_msg) == 0, "Difference more than Rs.2 encountered in gst"

            print("Error:: gst amount in disbursement and loan agreement not matched")
            assert False

