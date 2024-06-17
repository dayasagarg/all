import pytest
# import capabilities
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


from appium_flutter_finder import FlutterElement, FlutterFinder


class TestApp:
    @pytest.fixture
    def setup_teardown(self):
        global driver
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": "14",
            "deviceName": "Redmi 10 Prime 2020",
            "app": r"C:\Users\lendi\OneDrive\Desktop\APK files\Bhavesh\app-release.apk",
            "appPackage": "com.fintech.lenditt",
            "appActivity": "com.fintech.lenditt.MainActivity",
            "udid": "7aa117d30603",
            "autoGrantPermissions" : True

        }
        # "udid": "ZY2239JLP2"

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.implicitly_wait(7)
        yield
        time.sleep(7)
        driver.quit()

    def test_prod_APK(self, setup_teardown):
        # time.sleep(3)
        # driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        # time.sleep(1)
        # skipUpdate = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"UpdateSkip")
        # # skipUpdate = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
        # skipUpdate = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Update_skip']")
        # skipUpdate.click()
        time.sleep(2)

        # login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")

        time.sleep(2)
        login = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login")
        # login = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='login appbar Login']")
        login.click()
        #
        time.sleep(2)
        #
        windSize = driver.get_window_size()

        print("windSize::", windSize)
        print("context:", driver.context)
        deviceSize = driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        time.sleep(2)

        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 9 / 9
        endy = screenHeight / 9
        #
        # time.sleep(11)

        actions = TouchAction(driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        # time.sleep(5)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(2)

        #
        # scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                              'new UiScrollable(new UiSelector()).scrollIntoView(text("CIBIL"))')
        time.sleep(2)
        # cibil = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CIBIL")
        # cibil.click()
        # time.sleep(2)
        # terms = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "T&C ")
        # terms.click()
        # time.sleep(2)
        # terms_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        # terms_cls.click()
        # time.sleep(2)
        # actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        # actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        # time.sleep(2)
        # privacy = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "privacy policy.")
        # privacy.click()
        # time.sleep(3)
        # # priv_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        # priv_cls = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "nav_back_icon")
        # priv_cls.click()
        # time.sleep(2)
        # actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        # actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        # time.sleep(2)

        allow_access = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permissioncheckbox")
        allow_access.click()
        time.sleep(2)
        continueButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue")
        continueButton.click()
        time.sleep(2)

        # MobileTextB = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # mobileTextB = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Enter_your_phone_number']/android.widget.EditText/android.widget.EditText")
        # mobileTextB = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText")

        # mobileTextB.click()

        time.sleep(2)
        driver.press_keycode(15)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(13)
        driver.press_keycode(12)
        #
        # MobileTextB.send_keys("1117779455")exit
        time.sleep(7)
        # logContinueB = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(2)")
        logContinueB = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login_Signup_continue")
        logContinueB.click()

        time.sleep(2)
        # edit = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "number_edit")
        # time.sleep(2)
        # edit.click()
        # time.sleep(2)
        # edit_continue = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login_Signup_continue")
        # edit_continue.click()
        # time.sleep(2)

        # actions.tap(None, 141, 1662, 4).perform()
        # otp = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Otp_Verify_PinCodeTextField']/android.widget.EditText")
        # otp.click()
        # time.sleep(1)
        # otp.send_keys("1111")
        time.sleep(2)
        driver.press_keycode(8)
        time.sleep(2)
        driver.press_keycode(8)
        time.sleep(2)
        driver.press_keycode(8)
        time.sleep(2)
        driver.press_keycode(8)
        #
        # time.sleep(2)
        #
        # referal_code = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
        # referal_code.send_keys("a")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")
        # referal_code.send_keys("b")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(5)")
        # referal_code.send_keys("c")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(6)")
        # referal_code.send_keys("d")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(7)")
        # referal_code.send_keys("e")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(8)")
        # referal_code.send_keys("f")
        # referal_code = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
        # referal_code.send_keys("g")
        # time.sleep(2)
        #
        # apply = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Apply")
        # apply.click()
        # time.sleep(2)
        skip = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Skip")
        # skip = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(9)")
        skip.click()

        time.sleep(1)
        # whilUseApp = driver.find_element(AppiumBy.ID,
        #                                  "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        # whilUseApp = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # whilUseApp.click()
        # time.sleep(3)
        # loanInfoContinue = driver.find_element(AppiumBy.ID, "handy-docs-continue-btn")
        loanInfoContinue = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(13)")
        loanInfoContinue.click()
        time.sleep(3)
        profilePhoto = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "profile-img-empty")
        profilePhoto.click()
        # time.sleep(5)
        # whilUseApp = driver.find_element(AppiumBy.ID,
        #                                  "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        # # whilUseApp = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # whilUseApp.click()
        time.sleep(3)
        takePicture = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "take_picture")
        takePicture.click()
        time.sleep(2)
        retakeSelfi = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"retake_selfi")
        retakeSelfi.click()
        time.sleep(3)
        takePicture = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "take_picture")
        takePicture.click()
        time.sleep(3)
        SelfiContinue = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "selfi_continue")
        # SelfiContinue = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(6)")
        SelfiContinue.click()
        time.sleep(3)

        basicDetail = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Basic_details']/android.view.View[1]")
        basicDetail.click()
        time.sleep(2)

        email = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Basic_details']/android.view.View[2]/android.widget.EditText/android.view.View")
        email.click()
        time.sleep(3)
        email_select = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
        email_select.click()
        time.sleep(4)
        ok = driver.find_element(AppiumBy.ID,"android:id/button2")
        ok.click()
        time.sleep(2)
        # email = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='enter_email_id']/android.view.View")
        # email.click()
        # time.sleep(2)
        # email.clear()
        # time.sleep(2)
        # email.send_keys("a.b@lenditt.com")
        # time.sleep(2)

        pan = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Basic_details']/android.widget.ImageView[1]/android.widget.EditText/android.widget.EditText")
        pan.click()
        time.sleep(1)
        pan.send_keys("ZAATE3487R")
        time.sleep(1)
        name = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Basic_details']/android.view.View[4]/android.widget.EditText/android.widget.EditText")
        name.click()
        time.sleep(1)
        name.send_keys("name sxgsfhg gchg")
        time.sleep(2)
        basicDetail = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Basic_details']/android.view.View[1]")
        basicDetail.click()
        time.sleep(3)


        gen_drop = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"gender-dropdown")
        time.sleep(2)
        gen_drop.click()
        time.sleep(2)
        gen_drop_male = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Male']")
        gen_drop_male.click()
        time.sleep(2)


        # current = driver.current_context
        # print("This is the current driver " + current)
        #
        # # print("This is the dir of the webElement " + str(dir(model)))
        # print("this is the model" + str(gen_drop))
        # action = TouchAction(driver)
        # action.long_press(gen_drop).perform()


        loan_drop = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='loan_purpose_dropdown']")
        loan_drop.click()
        time.sleep(2)
        loan_drop_pup = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Fulfill_your_business_needs']")
        loan_drop_pup.click()
        time.sleep(2)
        personal_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Personal_details_")  # personal details
        personal_details.click()
        time.sleep(2)
        driver.press_keycode(8)
        driver.press_keycode(8)
        driver.press_keycode(8)
        driver.press_keycode(8)
        # personal_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Personal_details_")
        # personal_details.click()
        time.sleep(2)

        # otp_personal = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(3)")
        # otp_personal = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
        # otp_personal.send_keys("1111")
        time.sleep(2)
        marital_status = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Marital_status_dropdown")
        marital_status.click()
        time.sleep(2)
        marital_status_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Single")
        marital_status_dropdown.click()
        time.sleep(2)
        mother_name = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Personal_details_']/android.view.View[2]/android.widget.EditText/android.widget.EditText")
        mother_name.click()
        mother_name.send_keys("SNSKDJC")
        time.sleep(2)
        # personal_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Personal_details_")  # personal details
        # personal_details.click()
        # time.sleep(2)
        vehical = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Do_you_own_a_vehicle_dropdown")
        # vehical = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Do_you_own_a_vehicle_dropdown']")
        # vehical = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(2)")
        vehical.click()
        time.sleep(2)
        vehical_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2_Wheeler")
        vehical_dropdown.click()
        time.sleep(2)
        veh_con_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"vehicle_info_continue")
        veh_con_btn.click()
        time.sleep(3)
        education = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Highest_Level_of_Education_dropdown")
        education.click()
        time.sleep(2)
        education_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Less_than_High_School")
        education_dropdown.click()
        time.sleep(2)
        residential = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Your_residential_status_dropdown")
        residential.click()
        time.sleep(2)
        residential_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Owned")
        residential_dropdown.click()

        time.sleep(2)
        professional_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Professional_details")  # professional details
        professional_details.click()
        time.sleep(3)
        employment_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Employment_status_dropdown")
        employment_details.click()

        time.sleep(2)
        employment_details_options = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Salaried")
        employment_details_options.click()
        time.sleep(3)
        salary = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Professional_details']/android.view.View[2]/android.widget.EditText/android.widget.EditText")
        salary.click()
        salary.send_keys("82345")
        time.sleep(2)
        # professional_details = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Professional_details")  # professional details
        # professional_details.click()
        # actions.tap(None, 160, 1963, 1).perform()
        time.sleep(2)
        continue_register = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"registration-details-btn")
        continue_register.click()
        time.sleep(2)
        actions.tap(None,198,1464,4).perform()
        # set_passcode = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]")
        # set_passcode.click()
        time.sleep(2)
        # set_passcode.send_keys("1111")
        # time.sleep(2)

        # set_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # set_passcode.click()
        time.sleep(2)
        # set_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # set_passcode.click()
        # set_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # set_passcode.click()
        # set_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # set_passcode.click()
        time.sleep(2)
        actions.tap(None, 198, 1464, 4).perform()

        # confirm_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # confirm_passcode.click()
        # confirm_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # confirm_passcode.click()
        # confirm_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # confirm_passcode.click()
        # confirm_passcode = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(0)")
        # confirm_passcode.click()
        time.sleep(4)


        # driver.press_keycode(8)
        # driver.press_keycode(8)
        # driver.press_keycode(8)
        # driver.press_keycode(8)
        # time.sleep(2)

        # confirm_passcode = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "")
        # confirm_passcode.click()
        # confirm_passcode.send_keys("1111")

        # driver.press_keycode(8)
        # driver.press_keycode(8)
        # driver.press_keycode(8)
        # driver.press_keycode(8)

        # time.sleep(2)
        # adhar = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='add_aadhar']/android.widget.EditText")
        adhar = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.widget.EditText/android.widget.EditText")

        adhar.click()
        adhar.send_keys("866232428687")
        # time.sleep(5)
        # adhar_verify_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Verify")
        # adhar_verify_btn = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Verify']")
        # adhar_verify_btn.click()
        time.sleep(2)
        actions.tap(None, 528, 2245, 1).perform()
        time.sleep(3)
        # adhar_verification = driver.find_element(AppiumBy.)
        driver.press_keycode(8)
        time.sleep(1)
        driver.press_keycode(8)
        time.sleep(1)
        driver.press_keycode(8)
        time.sleep(1)
        driver.press_keycode(8)
        time.sleep(1)
        driver.press_keycode(8)
        time.sleep(1)
        driver.press_keycode(8)
        time.sleep(3)
        ### Employment Details ###
        # time.sleep(2)
        companyName = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Enter_cmp_name']/android.widget.EditText/android.view.View")
        companyName.click()
        time.sleep(2)
        companyNameSelect = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                          "Capgemini_technology_services_india_limited")
        companyNameSelect.click()
        time.sleep(2)
        emplSector = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Enter_emp_sector']/android.widget.EditText/android.view.View")
        emplSector.click()
        time.sleep(2)
        emplSectorSelect = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Information_technology")
        emplSectorSelect.click()
        time.sleep(2)
        designation = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Select_designations']/android.widget.EditText/android.view.View")
        designation.click()
        time.sleep(2)
        designationSelect = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Professional")
        designationSelect.click()
        time.sleep(2)
        emp_start_date = driver.find_element(AppiumBy.XPATH,"//android.view.View[@content-desc='Emp_start_date']/android.widget.EditText/android.view.View")
        emp_start_date.click()
        time.sleep(2)
        date = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"18")
        date.click()
        time.sleep(2)
        month = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "December")
        month.click()
        time.sleep(2)
        year = driver.find_element(AppiumBy.XPATH, "//android.widget.SeekBar[@content-desc='2023']")
        year.send_keys("2023")
        time.sleep(2)

        start_date_continue = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "continute_date")
        start_date_continue.click()
        time.sleep(2)

        manager_name = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='enter_director_fullname']/android.widget.EditText/android.widget.EditText")
        manager_name.click()
        time.sleep(3)
        manager_name.send_keys("asdhgfhg")
        time.sleep(2)
        comp_phone_no = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='user_cmp_num']/android.widget.EditText/android.widget.EditText")
        comp_phone_no.click()
        # actions.tap(None, 524, 1312, 1).perform()
        # time.sleep(3)
        comp_phone_no.send_keys("7112345678")
        time.sleep(2)
        lastSalaryDate = driver.find_element(AppiumBy.XPATH, "//android.widget.SeekBar[0]")
        lastSalaryDate.click()
        time.sleep(2)














































        #
        # wait = WebDriverWait(driver, 25, poll_frequency=1,
        #                      ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        # # ele = wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "gender-dropdown")))
        # # ele = wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@content-desc='gender-dropdown']")))
        # ele = wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")))
        #
        # ele.click()
        # # import the Select class
        #
        # # Create the object for Select class
        # dd_options = Select(ele)
        #
        # # List the values in Drop Down
        # # dd_v = dd_options.options
        # for dd_values in dd_options:
        #     print(dd_values.text)

        # Click by Index
        # dd_options.select_by_index(2)
        # time.sleep(2)

        # Click by Value
        # dd_options.select_by_value("Male")
        # time.sleep(2)

        # Click by Text
        # dd_options.select_by_visible_text("Option5")

        # time.sleep(5)
        # driver.quit()
        # gender = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"")
        # time.sleep(2)
        # loanPurp = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"")
        # time.sleep(2)




