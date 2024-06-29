import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # Set Chrome options
# Create ChromeOptions object
chrome_options = Options()

# Disable notifications
prefs = {
    "profile.default_content_setting_values.notifications": 1,  # 1: Allow, 2: Block
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.media_stream": 1,
}
chrome_options.add_experimental_option("prefs", prefs)

# # Create WebDriver
# driver = webdriver.Chrome(options=chrome_options)



class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser, options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(25)
        driver.get("https://devuatapi.com/web-test/") # url
        # driver.get("http://152.67.15.215/lenditt/#/dashboard")  # url

        time.sleep(3)
        yield
        time.sleep(4)
        driver.close()
        driver.quit()
        print("test execution completed")

    # def get_element_by_label(self, setup_teardown, label_str):
    #     elements = driver.find_elements(By.TAG_NAME, "flt-semantics")
    #     for element in elements:
    #         try:
    #             aria_label = element.get_attribute("aria-label")
    #             if aria_label == label_str:
    #                 return element
    #         except Exception as error:
    #             pass
    #     return None


    def test_keyFactStatement(self, setup_teardown):
        # time.sleep(5)
        # driver.find_element(By.XPATH, "//flt-semantics[@id='flt-semantic-node-13']").click() #login
        login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@id='flt-semantic-node-13']")))
        # login.click()

        if login.get_attribute("aria-label") == "Login":
            login.click()


        # driver.execute_script("return document.getElementById('flt-semantic-node-13');").click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//flt-semantics[@style='position: absolute; width: 20px; height: 20px; pointer-events: all; z-index: 1;']").click() #checkbox
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@role='checkbox']")))
        checkbox.click()
        time.sleep(1)
        # # accept
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Accept']").click() # Accept
        accept = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@aria-label='Accept']")))
        accept.click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//textarea[@data-semantics-role='text-field']").click()
        cont = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@aria-label='Continue']")))
        cont.click()
        # time.sleep(4)
        # alert = driver.switch_to.alert
        # alert.accept()  # To accept the alert
        time.sleep(1)
        #
        # driver.find_element(By.XPATH, "//textarea[@data-semantics-role='text-field']").send_keys("0123456782")  # mobile
        mob = WebDriverWait(driver, 15).until(
            # EC.presence_of_element_located((By.CSS_SELECTOR, "flt-semantics:nth-child(3)")))
            EC.presence_of_element_located((By.XPATH, "//textarea[@data-semantics-role='text-field']")))
        mob.send_keys("0123453000")
        time.sleep(1)
        # alert = driver.switch_to.alert
        # alert.accept()  # To accept the alert
        # driver.find_element(By.XPATH, "//textarea[@aria-label='Enter your 10-digit mobile number']").send_keys("0123456789")  # mobile

        # time.sleep(4)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Yes']").click() # Accept
        yes = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@aria-label='Yes']")))
        yes.click()

        time.sleep(1)

        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='NEFT']").click() # Accept
        neft = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics[@aria-label='NEFT']")))
        neft.click()

        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics//textarea[@aria-label='Enter monthly in-hand salary']").send_keys("78268736")
        sal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//flt-semantics//textarea[@aria-label='Enter monthly in-hand salary']")))
        sal.send_keys("78268736")

        time.sleep(1)

        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Continue']").click()
        cont_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Continue']")))
        # time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();", cont_2)
        time.sleep(2)
        cont_2.click()

        time.sleep(1)
        # driver.find_element(By.XPATH, "//input[@id='one-time-code']").send_keys("1111") # otp
        otp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics//input[@id='one-time-code']")))
        otp.send_keys("1111")
        time.sleep(1)
        # driver.find_element(By.XPATH, "//textarea[@aria-label='Enter Email ID']").send_keys("abxscxs@gmail.com")  # email
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@aria-label='Enter Email ID']")))
        email.send_keys("abcxs@gmail.com")
        # driver.execute_script("return document.getElementsByTagName('textarea')[0]").send_keys("abxscxs@gmail.com")
        time.sleep(1)
        # driver.find_element(By.XPATH, "//textarea[@aria-label='Enter PAN number']").send_keys("sadpl1111q")  # pan
        pan = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@aria-label='Enter PAN number']")))
        pan.send_keys("sadpl1111q")

        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Loan purpose']").click()
        l_purp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Loan purpose']")))
        l_purp.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Education']").click()
        l_purp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Education']")))
        l_purp.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Communication Language']").click()
        comm_lan = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Communication Language']")))
        comm_lan.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='English']").click()
        eng = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='English']")))
        eng.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Are you politically exposed?']").click()
        poli = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Are you politically exposed?']")))
        poli.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='No']").click()
        no = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='No']")))
        no.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Employment status']").click()
        emp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Employment status']")))
        emp.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Salaried']").click()
        sal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Salaried']")))
        sal.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Marital status']").click()
        mart_st = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Marital status']")))
        mart_st.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Single']").click()
        sing = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Single']")))
        sing.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//textarea[@aria-label='Enter mother name']").send_keys("gvhkd")
        moth = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@aria-label='Enter mother name']")))
        moth.send_keys("gvhkd")
        time.sleep(1)

        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Do you own a vehicle?']").click()
        veh = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Do you own a vehicle?']")))
        veh.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='2 Wheeler']").click()
        w_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='2 Wheeler']")))
        w_2.click()
        # driver.find_element(By.XPATH, "//flt-semantics[@style='position: absolute; width: 658px; height: 32.0156px; transform-origin: 0px 0px 0px; transform: matrix(1, 0, 0, 1, 10, 10); pointer-events: all; z-index: 1;']").click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//textarea[@aria-label='Enter mother name']").click()
        mo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@aria-label='Enter mother name']")))
        mo.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Highest level of education").click()
        # driver.find_element(By.CSS_SELECTOR, "flt-semantics:nth-child(9)").click() #Highest level of education
        edu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "flt-semantics:nth-child(9)")))
        edu.click()
        time.sleep(1)
        # driver.find_element(By.CSS_SELECTOR, "flt-semantics:nth-child(6)").click() #Masters Degree
        mast = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "flt-semantics:nth-child(6)")))
        mast.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Your residential status']").click()
        resi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Your residential status']")))
        resi.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Owned']").click()
        own = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Owned']")))
        own.click()
        time.sleep(1)
        # driver.find_element(By.CSS_SELECTOR, "flt-semantics:nth-child(11)").click()  # sal_bank
        sal_bnk = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "flt-semantics:nth-child(11)")))
        sal_bnk.click()
        time.sleep(1)
        # driver.find_element(By.CSS_SELECTOR, "flt-semantics:nth-child(2)").click()  # bank
        bnk = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "flt-semantics:nth-child(2)")))
        bnk.click()
        time.sleep(1)
        # driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Continue']").click()
        cont = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//flt-semantics[@aria-label='Continue']")))
        cont.click()
        time.sleep(1)


