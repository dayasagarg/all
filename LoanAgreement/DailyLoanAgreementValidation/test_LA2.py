from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import pypdf
from datetime import datetime
from datetime import timedelta
import json
import math


# JSON reader
file = open("input.json")
info = json.load(file)
email = info["user2"]["email"]
password = info["user2"]["password"]
otp1 = info["user2"]["otp1"]
otp2 = info["user2"]["otp2"]
otp3 = info["user2"]["otp3"]
otp4 = info["user2"]["otp4"]
loanID = info["user2"]["loanID"]
loanPdf = info["user2"]["loanPdf"]


# PDF reader
reader = pypdf.PdfReader(loanPdf)  # pdf file location
firstPage = reader.pages[0].extract_text()
thirdPage = reader.pages[2].extract_text()
fourthPage = reader.pages[3].extract_text()
fifthPage = reader.pages[4].extract_text()
sixthPage = reader.pages[5].extract_text()
seventhPage = reader.pages[6].extract_text()
eighthPage = reader.pages[7].extract_text()
ninthPage = reader.pages[8].extract_text()
eleventhPage = reader.pages[10].extract_text()
fourteenthPage = reader.pages[13].extract_text()


class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver

        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://chinmayfinserve.com/chinmay/#/dashboard") # url
        # driver.get("http://152.67.15.215/lenditt/#/dashboard")  # url
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys(email) #email
        time.sleep(2)
        driver.find_element(By.ID, "login-btn").click() #button
        time.sleep(2)
        driver.find_element(By.ID, "login-password").send_keys(password) #password
        time.sleep(2)
        driver.find_element(By.ID, "login-btn").click() #button
        # driver.find_element(By.XPATH, "//*[@id="login-btn"]").click()  # button
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='OTP']/div/input[1]").send_keys(otp1)  # otp
        driver.find_element(By.XPATH, "//*[@id='OTP']/div/input[2]").send_keys(otp2)  # otp
        driver.find_element(By.XPATH, "//*[@id='OTP']/div/input[3]").send_keys(otp3)  # otp
        driver.find_element(By.XPATH, "//*[@id='OTP']/div/input[4]").send_keys(otp4)  # otp
        time.sleep(17)
        # element = driver.find_element(By.ID, "login-btn2") #button
        time.sleep(1)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        # driver.find_element(By.ID,"login-btn2").click() #button
        time.sleep(1)
        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        driver.find_element(By.ID, "mainSearch").send_keys(loanID)  # search box
        time.sleep(4)
        driver.find_element(By.ID, "master-search-name-mobile").click()  # click user
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(4)


        '''SCHEDULE-CUM-KEY FACT STATEMENT'''

        # Name of Borrower
        profileName = driver.find_element(By.ID,"user-full-name").text
        time.sleep(2)
        print(f"### 'profileName':'{profileName}' ###")
        time.sleep(1)

        try:
            if profileName in firstPage:
                print(f" *** 'profileName':'{profileName}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

            assert profileName in firstPage, "profileName is matched with KEY FACT STATEMENT in first Page of pdf"

        except:
            try:
                if 'Name of Borrower' in firstPage:
                    index1 = firstPage.index('Name of Borrower')
                    index2 = firstPage.index('NBFC Name Chinmay Finlease')
                    text = firstPage[index1 + 16:index2]
                    print(f"Name by pdf module :: {text}")

            except:
                pass



        # #loanId
        loanId = driver.find_element(By.XPATH,"//div//table[@id='loanDetails']//tbody[1]//tr[1]//td//a").text
        time.sleep(2)
        if loanId in firstPage:
            print(f" *** 'loanId' :'{loanId}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
        else:
            print(f"Error :: 'loanId' :'{loanId}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

        assert loanId in firstPage, "loanId is matched with KEY FACT STATEMENT in first Page of pdf"

        # #customerId
        customerId = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[1]/app-customer-list-header/div/div[1]/div[1]/div[1]/mat-chip-list/div/mat-chip/span/span").text
        time.sleep(5)
        # print("customerId::",customerId)
        if customerId in firstPage:
            print(f" *** 'customerId' :'{customerId}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
        else:
            print(f"Error :: 'customerId' :'{customerId}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

        assert customerId in firstPage, "customerId is matched with KEY FACT STATEMENT in first Page of pdf"


        # Date of Signing
        try:
            loanAppDate = driver.find_element(By.XPATH, "(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[6]").text
            time.sleep(1)
            LoanApplicationDate = loanAppDate.replace('/','-')

            if LoanApplicationDate in firstPage:
                print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
            else:
                print(
                    f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is not matched with KEY FACT STATEMENT in first Page of pdf *** ")


            assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT in first Page of pdf"

        except:
            try:
                loanAppDate = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[5]").text
                time.sleep(1)
                LoanApplicationDate = loanAppDate.replace('/', '-')

                if LoanApplicationDate in firstPage:
                    print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'LoanApplicationDate' :'{LoanApplicationDate}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

                assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT in first Page of pdf"

            except:

                if 'Date of Signing' in firstPage:
                    index1 = firstPage.index('Date of Signing')
                    index2 = firstPage.index('Name of Borrower')
                    text = firstPage[index1 + 28:index2]
                    print(f"Name by pdf :: {text}")


                # print("LoanApplicationDateA",LoanApplicationDate)


        '''LOAN DETAILS'''
        # # Loan Amount
        apprAmount = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[10]").text
        time.sleep(2)
        lSpace = apprAmount.replace(" ","")


        approvedAmount = lSpace + '.00/-'
        approvedAmount2 = lSpace + '/-'

        approvedAmount3 = str(lSpace)[1] + "," + str(lSpace)[2:4] + str(lSpace)[4:]

        try:
            if approvedAmount in firstPage:
                print(
                    f" *** 'approvedAmount' :'{approvedAmount}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(
                    f"Exception :: 'approvedAmount' :'{approvedAmount}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert approvedAmount in firstPage, "approvedAmount is matched with LOAN DETAILS in first Page of pdf"
        except:
            try:
                if approvedAmount2 in firstPage:
                    print(
                        f" *** 'approvedAmount2' :'{approvedAmount2}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'approvedAmount2' :'{approvedAmount2}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert approvedAmount2 in firstPage, "approvedAmount2 is matched with LOAN DETAILS in first Page of pdf"

            except:
                if approvedAmount3 in firstPage:
                    print(
                        f" *** 'approvedAmount3' :'{approvedAmount3}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'approvedAmount3' :'{approvedAmount3}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert approvedAmount3 in firstPage, "approvedAmount3 is matched with LOAN DETAILS in first Page of pdf"

        # Interest Rate (per Day)
        loanIntPerDay = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[8]").text
        time.sleep(1)
        loanInterestPerDay = loanIntPerDay.replace(" %","00%")
        loanInterestPerDay2 = loanIntPerDay.replace(" %", "%")
        loanInterestPerDay3 = loanIntPerDay.replace(" %", "0%")

        try:
            if loanInterestPerDay in firstPage:
                print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanInterestPerDay in firstPage, "loanInterestPerDay is matched with LOAN DETAILS in first Page of pdf"

        except:

            try:
                if loanInterestPerDay2 in firstPage:
                    print(
                        f" *** 'loanInterestPerDay2' :'{loanInterestPerDay2}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'loanInterestPerDay2' :'{loanInterestPerDay2}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert loanInterestPerDay2 in firstPage, "loanInterestPerDay is matched with LOAN DETAILS in first Page of pdf"

            except:

                if loanInterestPerDay3 in firstPage:
                    print(
                        f" *** 'loanInterestPerDay3' :'{loanInterestPerDay3}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'loanInterestPerDay3' :'{loanInterestPerDay3}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert loanInterestPerDay3 in firstPage, "loanInterestPerDay3 is matched with LOAN DETAILS in first Page of pdf"


        # # Interest Rate (per Annum)
        strLIPD = loanIntPerDay.replace(" %","")
        flotLIPD = float(strLIPD)
        loanIntPerAnnum = flotLIPD * 365
        loanIntPerAnnumFl = math.ceil(float(loanIntPerAnnum))
        loanIntPerAnnumStr = str(loanIntPerAnnumFl)
        # print("loanIntPerDay::",loanIntPerAnnumStr)

        loanIntPerAnnumInt = int(loanIntPerAnnum)
        loanIntPerAnnumStr2 = str(loanIntPerAnnumInt)
        # print("loanIntPerAnnumStr2::", loanIntPerAnnumStr2)

        try:
            if loanIntPerAnnumStr in firstPage:
                print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%'  is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanIntPerAnnumStr in firstPage, "loanIntPerAnnumStr is matched with LOAN DETAILS in first Page of pdf"
        except:
            if loanIntPerAnnumStr2 in firstPage:
                print(f" *** 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Error :: 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%'  is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanIntPerAnnumStr2 in firstPage, "loanIntPerAnnumStr2 is matched with LOAN DETAILS in first Page of pdf"




        # # # Loan Tenure
        loanDurInDays = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[17]").text
        # print("loanDurInDays::",loanDurInDays)
        # time.sleep(1)
        loanDurationInDays = loanDurInDays

        if loanDurationInDays in firstPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN DETAILS in first Page of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN DETAILS in first Page of pdf ")

        assert loanDurationInDays in firstPage, "loanDurationInDays is matched with LOAN DETAILS in first Page of pdf"


        # # Loan Start Date
        loanDisbDate = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[6]").text
        time.sleep(1)
        loanDisbursedDate = loanDisbDate.replace("/","-")

        try:
            if loanDisbursedDate in firstPage:
                print(f" *** 'loanDisbursedDate' :'{loanDisbursedDate}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanDisbursedDate' :'{loanDisbursedDate}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanDisbursedDate in firstPage, "loanDisbursedDate is matched with LOAN DETAILS in first Page of pdf"

        except:

            if 'Loan Start Date' in firstPage:
                indexLSD = firstPage.index('Loan Start Date')
                indexIA = firstPage.index('Interest Amount')
                text = firstPage[indexLSD + 16:indexIA]
                print(f"By pdf :: {text}")


        # Loan End Date
        loanStartDate = datetime.strptime(loanDisbursedDate,"%d-%m-%Y")
        # print("loanStartDate::",loanStartDate)
        loanEndDateTimeFromY = loanStartDate + timedelta(days=int(loanDurInDays)-1)
        # print("loanEndDateTimeFromY::",loanEndDateTimeFromY)

        loanEndDateFromD = datetime.strftime(loanEndDateTimeFromY,'%d-%m-%Y')
        loanEndDate = str(loanEndDateFromD).split(" ")[0]

        loanEndDateTimeFromY2 = loanStartDate + timedelta(days=int(loanDurInDays) - 2)
        loanEndDateFromD2 = datetime.strftime(loanEndDateTimeFromY2, '%d-%m-%Y')
        loanEndDate2 = str(loanEndDateFromD2).split(" ")[0]


        try:
            if loanEndDate in firstPage:
                print(f" *** 'loanEndDate' :'{loanEndDate}' is matched with LOAN DETAILS in first Page of pdf *** ")

            # assert loanEndDate in firstPage, "loanEndDate is matched with LOAN DETAILS in first Page of pdf"

        except:
            if loanEndDate2 in firstPage:
                print(f" *** 'loanEndDate2' :'{loanEndDate2}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Error :: 'loanEndDate2' :'{loanEndDate2}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanEndDate2 in firstPage, "loanEndDate2 is matched with LOAN DETAILS in first Page of pdf"


        '''CHARGES (All charges are non-refundable & applicable post disbursement of loan)'''
        rmLoanAmInt = apprAmount.replace("₹ ","")
        rmChLoanAmInt = rmLoanAmInt.replace(",","")
        loanAmountInt = int(rmChLoanAmInt)

        # #Processing Charges @6.5%
        processChargeInt = math.ceil((loanAmountInt/100) * 6.5)
        processChargeInt2 = int((loanAmountInt / 100) * 6.5)

        processChargeString = format(processChargeInt)
        processChargeRs = "₹" + processChargeString
        processCharge = processChargeRs[0] + processChargeRs[1] +","+ processChargeRs[2:]

        processChargeString2 = format(processChargeInt2)
        processChargeRs2 = "₹" + processChargeString2
        processCharge2 = processChargeRs2[0] + processChargeRs2[1] + "," + processChargeRs2[2:]


        #
        try:
            if processCharge in firstPage:
                print(f" *** 'processCharge' :'{processCharge}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'processCharge' :'{processCharge}' is not matched with CHARGES Section in first Page of pdf ")

            assert processCharge in firstPage, "processCharge is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if processChargeRs in firstPage:
                    print(f" *** 'processChargeRs' :'{processChargeRs}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'processChargeRs' :'{processChargeRs}' is not matched with CHARGES Section in first Page of pdf ")

                assert processChargeRs in firstPage, "processChargeRs is matched with CHARGES Section in first Page of pdf"

            except:
                if processChargeRs2 in firstPage:
                    print(
                        f" *** 'processChargeRs2' :'{processChargeRs2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'processChargeRs2' :'{processChargeRs2}' is not matched with CHARGES Section in first Page of pdf ")

                assert processChargeRs2 in firstPage, "processChargeRs2 is matched with CHARGES Section in first Page of pdf"




        #Document Charges @1%
        docChargFloat = (loanAmountInt/100) * 1
        docChargInt = math.ceil((loanAmountInt / 100) * 1)

        documentCharges = "₹" + str(docChargFloat) + "0"
        documentCharges2 = "₹" + str(docChargInt)
        documentCharges3 = "₹" + str(docChargInt)[0] +","+ str(docChargInt)[1:]

        # print("documentCharges3::",documentCharges3)
        # #
        try:
            if documentCharges in firstPage:
                print(f" *** 'documentCharges' :'{documentCharges}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'documentCharges' :'{documentCharges}' is not matched with CHARGES Section in first Page of pdf ")

            assert documentCharges in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if documentCharges2 in firstPage:
                    print(
                        f" *** 'documentCharges2' :'{documentCharges2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'documentCharges2' :'{documentCharges2}' is not matched with CHARGES Section in first Page of pdf ")

                assert documentCharges2 in firstPage, "is matched with CHARGES Section in first Page of pdf"
            except:
                if documentCharges3 in firstPage:
                    print(
                        f" *** 'documentCharges3' :'{documentCharges3}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'documentCharges3' :'{documentCharges3}' is not matched with CHARGES Section in first Page of pdf ")

                assert documentCharges3 in firstPage, "is matched with CHARGES Section in first Page of pdf"



        # 9% SGST is inclusive As specified by Government of India
        onlineConvenienceFees = 200
        riskAssessmentFees = loanAmountInt * 0.01
        riskAssessmentFees2 = loanAmountInt * 0.025
        riskAssessmentFees3 = loanAmountInt * 0.04

        sgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees ) / 100) * 9
        sgstFloat2 = ((processChargeInt + docChargFloat + onlineConvenienceFees ) / 100) * 9
        sgstFloat3 = ((processChargeInt + docChargFloat + onlineConvenienceFees ) / 100) * 9

        sgst = "₹" + str(round(sgstFloat,2))
        sgst2 = "₹" + str(round(sgstFloat,1))
        sgst3 = "₹" + str(round(sgstFloat2, 1))
        sgst4 = "₹" + str(round(sgstFloat3, 1))
        # print("sgst2::",sgst2)


        try:
            if sgst in firstPage:
                print(f" *** 'sgst' :'{sgst}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f" *** 'sgst' :'{sgst}' is not matched with CHARGES Section in first Page of pdf *** ")

            assert sgst in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if sgst2 in firstPage:
                    print(f" *** 'sgst2' :'{sgst2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'sgst2' :'{sgst2}' is not matched with CHARGES Section in first Page of pdf ")

                assert sgst2 in firstPage, "is matched with CHARGES Section in first Page of pdf"

            except:
                if sgst3 in firstPage:
                    print(f" *** 'sgst3' :'{sgst3}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Error :: 'sgst3' :'{sgst3}' is not matched with CHARGES Section in first Page of pdf ")

                assert sgst3 in firstPage, "is matched with CHARGES Section in first Page of pdf"




        # 9% CGST is inclusive As specified by Government of India
        cgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees) / 100) * 9
        cgstFloat2 = ((processChargeInt + docChargFloat + onlineConvenienceFees) / 100) * 9
        cgstFloat3 = ((processChargeInt + docChargFloat + onlineConvenienceFees) / 100) * 9

        cgst = "₹" + str(round(cgstFloat,2))
        cgst2 = "₹" + str(round(cgstFloat, 1))
        cgst3 = "₹" + str(round(cgstFloat2, 1))
        cgst4 = "₹" + str(round(cgstFloat3, 1))

        try:
            if cgst in firstPage:
                print(f" *** 'cgst' :'{cgst}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f" *** 'cgst' :'{cgst}' is not matched with CHARGES Section in first Page of pdf *** ")
            assert cgst in firstPage, "is matched with CHARGES Section in first Page of pdf"


        except:
            try:
                if cgst2 in firstPage:
                    print(f" *** 'cgst2' :'{cgst2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'cgst2' :'{cgst2}' is not matched with CHARGES Section in first Page of pdf ")
                assert cgst2 in firstPage, "is matched with CHARGES Section in first Page of pdf"

            except:
                if cgst3 in firstPage:
                    print(f" *** 'cgst3' :'{cgst3}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Error :: 'cgst3' :'{cgst3}' is not matched with CHARGES Section in first Page of pdf ")
                assert cgst3 in firstPage, "is matched with CHARGES Section in first Page of pdf"

        #

        #Online convenience fees
        onlineConvenienceFeesString = "₹" + str(onlineConvenienceFees)
        if onlineConvenienceFeesString in firstPage:
            print(f" *** 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is not inside CHARGES Section of first Page of pdf ")

        assert onlineConvenienceFeesString in firstPage, "is inside CHARGES Section of first Page of pdf"


        #Cheque / ECS / SI Return charges
        chequeBounceCharge = "₹500"
        if chequeBounceCharge in firstPage:
            print(f" *** 'chequeBounceCharge' :'{chequeBounceCharge}' is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'chequeBounceCharge' :'{chequeBounceCharge}' is not inside CHARGES Section of first Page of pdf ")

        assert chequeBounceCharge in firstPage, "is inside CHARGES Section of first Page of pdf"


        #Default Interest / Late Payment charges (per day)    ****
        latePaymentChargePerDay = flotLIPD
        latePaymentChargePerDayString = str(latePaymentChargePerDay) + "%"




        if latePaymentChargePerDayString in firstPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched and is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched and not inside CHARGES Section of first Page of pdf ")

        # assert latePaymentChargePerDayString in firstPage, "is matched and within CHARGES Section of first Page of pdf"


        # Default Interest / Late Payment charges (per annual)
        latePaymentChargePerAnnual = round(loanIntPerAnnum,4)
        # print("latePaymentChargePerAnnual::",latePaymentChargePerAnnual)
        # print("loanIntPerAnnum::", loanIntPerAnnum)
        latePaymentChargePerAnnualInt = int(round(loanIntPerAnnum,0))

        latePaymentChargePerAnnualString = str(latePaymentChargePerAnnual) + "00%"
        latePaymentChargePerAnnualString2 = str(latePaymentChargePerAnnual) + "%"
        latePaymentChargePerAnnualString3 = str(latePaymentChargePerAnnualInt)


        try:
            if latePaymentChargePerAnnualString in firstPage:
                print(f" *** 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is not matched with CHARGES Section in first Page of pdf ")

            assert latePaymentChargePerAnnualString in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if latePaymentChargePerAnnualString2 in firstPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is not matched with CHARGES Section in first Page of pdf ")

                assert latePaymentChargePerAnnualString2 in firstPage, "is matched with CHARGES Section in first Page of pdf"

            except:
                if latePaymentChargePerAnnualString3 in firstPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is not matched with CHARGES Section in first Page of pdf ")

                # assert latePaymentChargePerAnnualString3 in firstPage, "is matched with CHARGES Section in first Page of pdf"

            # foreclose
            foreclose = "4"
            if foreclose in firstPage:
                print(f" *** 'foreclose' :'{foreclose}%' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'foreclose' :'{foreclose}%'  is not matched with LOAN DETAILS in first Page of pdf ")

            assert foreclose in firstPage, "foreclose is matched with LOAN DETAILS in first Page of pdf"



        '''LETTER OF SANCTION TO THE BORROWER'''

        # Total amount to be paid  //*[@class="border-gray bg-mail font-weight-bold ng-star-inserted"]//td[6]
        # totalCost = driver.find_element(By.XPATH,"//div[contains(@class,'font-weight-bold numbers mobile-text')]").text
        userSelectedAmt = driver.find_element(By.XPATH, "//*[@id='loanDetails']/tbody/tr[1]/td[10]/div").text
        # print("totalCost::",totalCost)


        if userSelectedAmt in fourthPage:
            print(f" *** 'userSelectedAmt' :'{userSelectedAmt}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
        else:
            print(f"Error :: 'userSelectedAmt' :'{userSelectedAmt}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

        assert userSelectedAmt in fourthPage, "is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"


        #TOTAL PERIOD
        time.sleep(1)
        loanDurationInDays = loanDurInDays + " days"
        totalPeriod = loanDurationInDays

        if totalPeriod in fourthPage:
            print(f" *** 'totalPeriod' :'{totalPeriod}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
        else:
            print(f"Error :: 'totalPeriod' :'{totalPeriod}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

        assert totalPeriod in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"


        # ONLINE CONVENIENCE CHARGES
        onlineConvCharge = 200
        onlineConvChargeString = "₹200"

        if onlineConvChargeString in fourthPage:
            print(f" *** 'onlineConvChargeString' :'{onlineConvChargeString}' is inside LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvChargeString' :'{onlineConvChargeString}' is not inside LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

        assert onlineConvChargeString in fourthPage, "is inside LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"




        #DISBURSEMENT
        # print(f"loanAmountInt::{loanAmountInt}",f"processChargeInt::{processChargeInt}",f"docChargFloat::{docChargFloat}",f"riskAssessmentFees::{riskAssessmentFees}",f"riskAssessmentFees::{riskAssessmentFees2}",f"onlineConvCharge::{onlineConvCharge}",f"sgstFloat::{sgstFloat}",f"cgstFloat::{cgstFloat}",f"sgstFloat2::{sgstFloat2}",f"cgstFloat2::{cgstFloat2}")

        try:
            try:
                disburse = loanAmountInt - (processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                disFloat = str(math.ceil(disburse))
                disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                if disbursement in fourthPage:
                    print(f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                else:
                    print(f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

            except:
                try:
                    disburse = loanAmountInt - (processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                    disFloat = str(math.ceil(disburse-2))[:8]

                    disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                    if disbursement in fourthPage:
                        print(
                            f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                    else:
                        print(
                            f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                    assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                except:
                    try:
                        try:
                            disburse = loanAmountInt - (processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                            disFloat = str(math.ceil(disburse-1))
                            disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]
                            if disbursement in fourthPage:
                                print(
                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                            else:
                                print(
                                    f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                            assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                        except:
                            disburse = loanAmountInt - (
                                        processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                            disFloat = str(math.ceil(disburse - 2))
                            disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                            if disbursement in fourthPage:
                                print(
                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                            else:
                                print(
                                    f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                            assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                    except:
                        try:

                            disburse = loanAmountInt - (
                                        processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                            disFloat = str(math.ceil(disburse))
                            disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]
                            if disbursement in fourthPage:
                                print(
                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                            else:
                                print(
                                    f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                            assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                        except:
                            try:

                                disburse = loanAmountInt - (processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                                disFloat = str(math.ceil(disburse))
                                disbursement = "₹" + disFloat[0:1] + "," + disFloat[1:]
                                if disbursement in fourthPage:
                                    print(
                                        f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                                else:
                                    print(
                                        f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                                assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                            except:
                                try:
                                    disburse = loanAmountInt - (
                                                processChargeInt + docChargFloat + onlineConvCharge + sgstFloat + cgstFloat)
                                    disFloat = str(math.ceil(disburse-1))
                                    disbursement = "₹" + disFloat[0:1] + "," + disFloat[1:]

                                    if disbursement in fourthPage:
                                        print(
                                            f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                                    else:
                                        print(
                                            f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                                    assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                                except:
                                    try:
                                        try:

                                            disburse = loanAmountInt - (
                                                    processChargeInt + docChargFloat + onlineConvCharge + sgstFloat2 + cgstFloat2)
                                            disFloat = str(math.ceil(disburse ))
                                            disbursement = "₹" + disFloat[0:1] + "," + disFloat[1:]
                                            if disbursement in fourthPage:
                                                print(
                                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                                            else:
                                                print(
                                                    f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                                            assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

                                        except:
                                            disburse = loanAmountInt - (
                                                    processChargeInt + docChargFloat + onlineConvCharge + sgstFloat2 + cgstFloat2)
                                            disFloat = str(math.ceil(disburse ))
                                            disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]
                                            if disbursement in fourthPage:
                                                print(
                                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                                            else:
                                                print(
                                                    f"Error :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                                            assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"


                                    except:
                                        disburse = loanAmountInt - (
                                                processChargeInt + docChargFloat + onlineConvCharge + sgstFloat3 + cgstFloat3)
                                        disFloat = str(math.ceil(disburse - 1))
                                        disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                                        if disbursement in fourthPage:
                                            print(
                                                f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf *** ")
                                        else:
                                            print(
                                                f"Error :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf ")

                                        assert disbursement in fourthPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in fourth page of pdf"

        except:
            pass


        '''SECURITY DOCUMENTS'''

        #Sanction Days
        sanctionDays = "10 days"
        if sanctionDays in fifthPage:
            print(f" *** 'sanctionDays' :'{sanctionDays}' is matched with SECURITY DOCUMENTS section in fifth page of pdf *** ")
        else:
            print(f"Error :: 'sanctionDays' :'{sanctionDays}' is not matched with SECURITY DOCUMENTS section in fifth page of pdf ")

        assert sanctionDays in fifthPage, "is matched with SECURITY DOCUMENTS section in fifth page of pdf"


        #Penal interest per day
        penalInterestPerDay = latePaymentChargePerDayString
        if penalInterestPerDay in fourthPage:
            print(f" *** 'penalInterestPerDay' :'{penalInterestPerDay}' is matched with SECURITY DOCUMENTS section in fourth Page of pdf *** ")
        else:
            print(f"Error :: 'penalInterestPerDay' :'{penalInterestPerDay}' is not matched with SECURITY DOCUMENTS section in fourth Page of pdf ")

        assert penalInterestPerDay in fourthPage, "penalInterestPerDay is matched with SECURITY DOCUMENTS section in fourth Page of pdf"



        # Name of Borrower in security document
        try:
            if profileName in fifthPage:
                print(f" *** 'profileName':'{profileName}' is matched with security document section in fifth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with security document section in fifth Page of pdf ")

            assert profileName in fifthPage, "profileName is matched with security document section in fifth Page of pdf"

        except:
            if str(profileName).upper() in fifthPage:
                print(
                    f" *** 'profileName':'{str(profileName).upper()}' is matched with security document section in fifth Page of pdf *** ")
            else:
                print(
                    f"Error :: 'profileName':'{profileName}' is not matched with security document section in fifth Page of pdf ")

            assert str(profileName).upper() in fifthPage, "profileName is matched with security document section in fifth Page of pdf"

        '''Proof of identity'''
        # adhar = driver.find_element(By.ID,"aadhaar").text
        adhar = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/mat-card/div/div[3]/div[2]/span").text


        if adhar in eighthPage:
            print(
                f" *** 'adhar':'{adhar}' is matched with Proof of identity section of eighth Page of pdf *** ")
        else:
            print(
                f"Exception :: 'adhar':'{adhar}' is not matched with Proof of identity section of eighth Page of pdf ")

        assert adhar in eighthPage, "adhar is matched with Proof of identity section of eighth Page of pdf"


        try:
            if profileName in eighthPage:
                print(f" *** 'profileName':'{profileName}' is matched with Proof of identity section of eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with Proof of identity section of eighth Page of pdf ")

            assert profileName in eighthPage, "profileName is matched with Proof of identity section of eighth Page of pdf"

        except:
            try:
                if str(profileName).upper() in eighthPage:
                    print(
                        f" *** 'profileName':'{str(profileName).upper()}' is matched with Proof of identity section of eighth Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'profileName':'{str(profileName).upper()}' is not matched with Proof of identity section of eighth Page of pdf ")

                assert str(profileName).upper() in eighthPage, "profileName is matched with Proof of identity section of eighth Page of pdf"

            except:
                pass

        time.sleep(2)
        otherDetails = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[2]/div").click()
        time.sleep(2)
        # gender = driver.find_element(By.ID,"gender").text
        gender = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/div/mat-tab-body[2]/div/mat-card/div/div[1]/div[2]").text


        if gender in eighthPage:
            print(
                f" *** 'gender':'{gender}' is matched with Proof of identity section of eighth Page of pdf *** ")
        else:
            print(
                f"Exception :: 'gender':'{gender}' is not matched with Proof of identity section of eighth Page of pdf ")

        assert gender in eighthPage, "gender is matched with Proof of identity section of eighth Page of pdf"


        # Email
        basicDetails = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/mat-tab-header/div/div/div/div[1]/div").click()
        time.sleep(2)
        emailS = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/mat-card/div/div[2]/div[2]/div").text
        # emailS = driver.find_element(By.ID,"emailId").text
        time.sleep(2)


        try:
            if emailS in eleventhPage:
                print(f" *** 'email' :'{emailS}' is matched with LOAN AGREEMENT section of eleventh Page of pdf *** ")
            else:
                print(f"Exception :: 'email' :'{emailS}' is not matched with LOAN AGREEMENT section of eleventh Page of pdf ")

            assert emailS in eleventhPage, "email is matched with LOAN AGREEMENT section of eleventh Page of pdf"

        except:
            eindex = emailS.index("View")
            email = emailS[:eindex - 1]

            if email in eleventhPage:
                print(f" *** 'email' :'{email}' is matched with LOAN AGREEMENT of eleventh Page of pdf *** ")
            else:
                print(f"Exception :: 'email' :'{email}' is not matched with LOAN AGREEMENT of eleventh Page of pdf ")

            assert email in eleventhPage, "email is matched with LOAN AGREEMENT in eleventh Page of pdf"


        # PAN number
        # pan = driver.find_element(By.XPATH,"//div[contains(@class,'basic-details d-flex flex-row basic-info-card align-items-center justify-content-between mt-2')][2]//div[2]").text
        # pan = driver.find_element(By.ID,"PAN").text
        # time.sleep(1)
        pan = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/mat-drawer-container/mat-drawer-content/app-customer-list/div[2]/div/div[2]/app-customer-basic-details/mat-card/mat-card-content/mat-tab-group/div/mat-tab-body[1]/div/mat-card/div/div[4]/div[2]/span").text
        time.sleep(2)

        if pan in eleventhPage:
            print(f" *** 'pan' :'{pan}' is matched with LOAN AGREEMENT in eleventh Page of pdf *** ")
        else:
            print(f"Error :: 'pan' :'{pan}' is not matched with LOAN AGREEMENT in eleventh Page of pdf ")

        assert pan in eleventhPage, "pan is matched with LOAN AGREEMENT in eleventh Page of pdf"


        # loan amount
        lA = approvedAmount
        loanAmountstr = lA.replace("/-","")

        lA2 = approvedAmount2
        loanAmountstr2 = lA2.replace("/-","")


        try:
            if loanAmountstr in eleventhPage:
                print(f" *** 'loanAmountstr' :'{loanAmountstr}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
            else:
                print(f"Exception :: 'loanAmountstr' :'{loanAmountstr}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

            assert loanAmountstr in eleventhPage, "loanAmountstr is matched with LOAN AGREEMENT in eleventhPage of pdf"
        except:
            if loanAmountstr2 in eleventhPage:
                print(
                    f" *** 'loanAmountstr2' :'{loanAmountstr2}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
            else:
                print(
                    f"Error :: 'loanAmountstr2' :'{loanAmountstr2}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

            # assert loanAmountstr2 in eighthPage, "loanAmountstr2 is matched with LOAN AGREEMENT in eighth Page of pdf"


        # loan period
        if loanDurationInDays in eleventhPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

        # assert loanDurationInDays in eighthPage, "loanDurationInDays is matched with LOAN AGREEMENT in eighth Page of pdf"


        # loan interest
        #per day

        try:
            if loanInterestPerDay in eleventhPage:
                print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
            else:
                print(f"Exception :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

            assert loanInterestPerDay in eleventhPage, "loanInterestPerDay is matched with LOAN AGREEMENT in eleventhPage Page of pdf"

        except:
            try:
                if loanInterestPerDay2 in eleventhPage:
                    print(
                        f" *** 'loanInterestPerDay2' :'{loanInterestPerDay2}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
                else:
                    print(
                        f"Exception :: 'loanInterestPerDay2' :'{loanInterestPerDay2}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

                # assert loanInterestPerDay2 in eleventhPage, "loanInterestPerDay is matched with LOAN AGREEMENT in eleventhPage of pdf"

            except:

                if loanInterestPerDay3 in eleventhPage:
                    print(
                        f" *** 'loanInterestPerDay3' :'{loanInterestPerDay3}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
                else:
                    print(
                        f"Error :: 'loanInterestPerDay3' :'{loanInterestPerDay3}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

                # assert loanInterestPerDay3 in eleventhPage, "loanInterestPerDay3 is matched with LOAN AGREEMENT in eleventhPage of pdf"

        #per annum

        try:
            if loanIntPerAnnumStr in eleventhPage:
                print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%' is matched with LOAN DETAILS in eleventhPage of pdf *** ")
            else:
                print(f"Exception :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%'  is not matched with LOAN DETAILS in eleventhPage of pdf ")

            assert loanIntPerAnnumStr in eleventhPage, "loanIntPerAnnumStr is matched with LOAN DETAILS in eleventhPagee of pdf"
        except:
            if loanIntPerAnnumStr2 in eleventhPage:
                print(f" *** 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%' is matched with LOAN DETAILS in eleventhPage of pdf *** ")
            else:
                print(f"Error :: 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%'  is not matched with LOAN DETAILS in eleventhPage of pdf ")

            assert loanIntPerAnnumStr2 in eleventhPage, "loanIntPerAnnumStr2 is matched with LOAN DETAILS in eleventhPage of pdf"



        # penalty interest per day

        if latePaymentChargePerDayString in eleventhPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched with LOAN AGREEMENT in eleventhPage of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched with LOAN AGREEMENT in eleventhPage of pdf ")

        assert latePaymentChargePerDayString in eleventhPage, "latePaymentChargePerDayString is matched with LOAN AGREEMENT in eleventhPage of pdf"


        '''Borrower Name in twelthPage page'''

        try:
            if profileName in fourteenthPage:
                print(f" *** 'profileName':'{profileName}' is matched with witness in fourteenth of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with witness in fourteenth of pdf ")

            assert profileName in fourteenthPage, "profileName is matched with witness in fourteenth of pdf"

        except:
            if str(profileName).upper() in fourteenthPage:
                print(f" *** 'profileName':'{str(profileName).upper()}' is matched with witness in fourteenth of pdf *** ")
            else:
                print(f"Error :: 'profileName':'{str(profileName).upper()}' is not matched with witness in fourteenth of pdf ")

            assert str(profileName).upper() in fourteenthPage, "profileName is matched with witness in fourteenth of pdf"




