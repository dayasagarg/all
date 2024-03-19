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
                              params={"start_date": f"{pre_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})

        # loanAgrAPI = requests.get("https://chinmayfinserve.com/admin-prod/ admin / esign / getLoanAgreement", params={"loanId":726301})

    def test_agr_disb(self, url_agr_dis):
        global loanAmount,app_amt,loanAgrAPI,intRate,int_rate_la,emi_la,totalEMI,loanAgrAPIDataTenure,loanTenure,loan_tenure_la,name_la,name,nbfc,nbfc_la,procFees,procFees_la, sr,loanAgrAPIDataLoanId,dis_lid,riskFees,riskFees_la,docFees,docFees_la,gstAmt,gst_la,a
        disAPIData = disAPI.json()["data"]["rows"]

        dis_lid = []
        app_amt = []
        loanAmtStr = []
        intRate = []
        totalEMI = []
        loanTenure = []
        name = []
        procFees = []
        docFees = []
        riskFees = []
        gstAmt = []


        for dis in disAPIData:
            if dis["Loan ID"]:
                dis_lid.append(dis["Loan ID"])

            if dis["Approved amount"]:
                app_amt.append(dis["Approved amount"])

            if dis["Interest Rate"]:
                intRate.append(dis["Interest Rate"])

            if dis["Total Emi"]:
                totalEMI.append(dis["Total Emi"])

            if dis["Loan Tenure (Days)"]:
                loanTenure.append(dis["Loan Tenure (Days)"])

            if dis["Name"]:
                name.append(dis["Name"])

            if dis["Processing fees"]:
                procFees.append(dis["Processing fees"])

            if dis["Document Charges"]:
                docFees.append(dis["Document Charges"])

            if dis["Risk assessment fees"]:
                riskFees.append(dis["Risk assessment fees"])

            if dis["GST Amount"]:
                gstAmt.append(dis["GST Amount"])





        # print(riskFees)


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

            loanAgrAPIDataLoanId = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanId"]
            loanAgrAPIDataIntRate = loanAgrAPI.json()["data"]["eSign_agree_data"]["interestRatePerDay"]
            loanAgrAPIDataEMI = loanAgrAPI.json()["data"]["eSign_agree_data"]["numberOfEmis"]
            loanAgrAPIDataTenure = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanTenure"]
            loanAgrAPIDataName = loanAgrAPI.json()["data"]["eSign_agree_data"]["borrowerName"]
            loanAgrAPIDataProcAmt = loanAgrAPI.json()["data"]["eSign_agree_data"]["processingAmount"]
            loanAgrAPIDataDoc = loanAgrAPI.json()["data"]["eSign_agree_data"]["documentAmount"]
            loanAgrAPIDataRisk = loanAgrAPI.json()["data"]["eSign_agree_data"]["riskAssessmentCharge"]
            loanAgrAPIDataSGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["sgstCharges"]
            loanAgrAPIDataCGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["cgstCharges"]


            # print(loanAgrAPIDataRisk)


            if loanAgrAPIData:
                loanAmtStr.append(loanAgrAPIData)

            if loanAgrAPIDataIntRate:
                int_rate_la.append(round(float(loanAgrAPIDataIntRate),2))

            if loanAgrAPIDataEMI:
                emi_la.append(loanAgrAPIDataEMI)

            if loanAgrAPIDataTenure:
                loan_tenure_la.append(int(loanAgrAPIDataTenure))

            if loanAgrAPIDataName:
                name_la.append(loanAgrAPIDataName)

            if loanAgrAPIDataProcAmt:
                proc_fees_str_la.append(loanAgrAPIDataProcAmt)

            if loanAgrAPIDataDoc:
                doc_fees_str_la.append(loanAgrAPIDataDoc)

            if loanAgrAPIDataRisk:
                risk_fees_str_la.append(loanAgrAPIDataRisk)

            if loanAgrAPIDataSGST:
                sgst_str_la.append(math.ceil(float(loanAgrAPIDataSGST.replace("₹",""))))

            if loanAgrAPIDataCGST:
                cgst_str_la.append(math.ceil(float(loanAgrAPIDataCGST.replace("₹",""))))


        gst_la = [sum(i) for i in zip(sgst_str_la,cgst_str_la)]

        # print("cgst_str_la::", cgst_str_la)
        # print("sgst_str_la::", sgst_str_la)
        # print("gst_la", gst_la)
        print("dis_lid::",dis_lid)
        # print("gstAmt::",gstAmt)


        loanAmount = []
        for a in loanAmtStr:
            if "₹" in a:
                ss = a.strip("₹")
                aa = ss.replace(",", "")
                loanAmount.append(int(aa))


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
    #
    #
        # print(riskFees_la)
    #
    #

    def test_loan_amt(self):
        if loanAmount == app_amt:
            print(f"loan amount and approved amount are equal")
        else:
            print(f"loan amount and approved amount are not equal::{lid}")
            assert False



    def test_int_rate(self):
        if intRate == int_rate_la:
            print("intRate and int_rate_la are equal")
        else:
            print("intRate and int_rate_la are not equal")
            assert False

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
    #
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


    def test_risk(self):
        # print(riskFees)
        # print(riskFees_la)
        if riskFees == riskFees_la:
            print("riskFees is equal in both loan agreement and disbursement")
        else:
            print("Error::riskFees mismatched")
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

            print("gst amount in disbursement and loan agreement not matched")
            assert False

