import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# # Set Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")

class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("https://devuatapi.com/web-test/") # url
        # driver.get("http://152.67.15.215/lenditt/#/dashboard")  # url

        time.sleep(3)
        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        time.sleep(5)
        driver.find_element(By.XPATH, "//flt-semantics[@id='flt-semantic-node-13']").click() #login
        time.sleep(3)
        driver.find_element(By.XPATH, "//flt-semantics[@style='position: absolute; width: 20px; height: 20px; pointer-events: all; z-index: 1;']").click() #checkbox

        time.sleep(3)
        # # accept
        driver.find_element(By.XPATH, "//flt-semantics[@role='button']").click() # Accept
        # time.sleep(3)
        driver.find_element(By.XPATH, "//textarea[@data-semantics-role='text-field']").click()
        # # time.sleep(5)
        #
        driver.find_element(By.XPATH, "//textarea[@data-semantics-role='text-field']").send_keys("0123456789")  # mobile
        time.sleep(4)
        # Set Chrome options
        chrome_options = Options()
        # chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--enable-notifications")  # Enable notifications
        time.sleep(5)
        driver.find_element(By.XPATH, "//flt-semantics//input[@id='one-time-code']").send_keys("1111") # Accept
        time.sleep(3)

        driver.find_element(By.XPATH, "//textarea[@aria-label='Enter Email ID']").send_keys("abxscxs@gmail.com")  # email
        time.sleep(3)
        driver.find_element(By.XPATH, "//textarea[@aria-label='Enter PAN number']").send_keys("sadpl1111q")  # pan
        time.sleep(3)
        driver.find_element(By.XPATH, "//flt-semantics[@aria-label='Loan purpose']").click()
        time.sleep(3)



        #
        #
        #
        #
        # # js_executor = driver.execute_script("arguments[0].value='abc@gmail.com';","//*[@id='flt-semantic-node-48']/textarea")
        #
        # #send keys with help of javascript executor
        #
        # # js_executor.executeScript("arguments[0].value='abc@gmail.com'")






        # login = driver.find_elements(By.TAG_NAME, "flt-semantics") #login
        #
        # for n,i in enumerate(login):
        #     if n == 9:
        #         break
        #     i.click()
        #     # time.sleep(4)
        #
        #     if n == 17:
        #         break
        #     i.click()
        #     time.sleep(4)













