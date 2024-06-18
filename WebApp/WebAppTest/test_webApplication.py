from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time



class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://devuatapi.com/web-test/") # url
        # driver.get("http://152.67.15.215/lenditt/#/dashboard")  # url
        time.sleep(3)

        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        time.sleep(1)
        driver.find_element(By.ID, "flt-semantic-node-13").click() #login
        time.sleep(5)
        # driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-50']").click() #checkbox
        driver.find_element(By.ID, "flt-semantic-node-51").click()  # checkbox
        time.sleep(7)
        # accept
        driver.find_element(By.XPATH, "/html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics[4]").click() # Accept
        time.sleep(5)
        # driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-48']/textarea").click()
        # time.sleep(5)

        # driver.find_element(By.ID, "flt-semantic-node-67").send_keys("0123456789")  # mobile
        # driver.find_element(By.ID, "/html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]").send_keys("0123456789")  # mobile
        time.sleep(5)
        # driver.find_element(By.ID, "flt-semantic-node-48").click()  # Continue
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#flt-semantic-node-67 > textarea").send_keys("0123456789")  # mobile
        time.sleep(5)
        driver.find_element(By.ID, "one-time-code").send_keys("1111")  # otp
        time.sleep(5)
        # driver.find_element(By.CSS_SELECTOR, "#flt-semantic-node-81 > textarea").send_keys("abxscxs@gmail.com")  # email
        time.sleep(5)
        driver.find_element(By.ID, "flt-semantic-node-100").send_keys("abxscxs@gmail.com")  # email
        time.sleep(5)





        # time.sleep(5)
        # driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-81']").send_keys("abxscxs@gmail.com")  # email
        # time.sleep(5)
        # driver.find_element(By.XPATH, "/html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics").send_keys("abxscxs@gmail.com")  # email
        # time.sleep(5)





        # js_executor = driver.execute_script("arguments[0].value='abc@gmail.com';","//*[@id='flt-semantic-node-48']/textarea")

        #send keys with help of javascript executor

        # js_executor.executeScript("arguments[0].value='abc@gmail.com'")



