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
        driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-50']").click() #checkbox
        time.sleep(7)
        driver.find_element(By.XPATH, "/html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics[4]").click() # Accept
        time.sleep(7)
        driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-48']/textarea").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-48']/textarea").send_keys("0123456789")  # mobile
        time.sleep(5)
        # driver.find_element(By.ID, "flt-semantic-node-48").click()  # Continue
        time.sleep(2)

        #create java script executor instance

        # js_executor = driver.execute_script("arguments[0].value='abc@gmail.com';","//*[@id='flt-semantic-node-48']/textarea")

        #send keys with help of javascript executor

        # js_executor.executeScript("arguments[0].value='abc@gmail.com'")