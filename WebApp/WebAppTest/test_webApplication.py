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
        driver.implicitly_wait(2)
        driver.get("http://192.168.1.23:8080/web/") # url
        # driver.get("http://152.67.15.215/lenditt/#/dashboard")  # url
        # time.sleep(3)

        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        driver.find_element(By.ID, "flt-semantic-node-13").click() #login
        time.sleep(2)
        driver.find_element(By.ID, "flt-semantic-node-46").click() #checkbox
        time.sleep(3)
        driver.find_element(By.ID, "flt-semantic-node-54").click() # Accept
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='flt-semantic-node-47']/textarea").send_keys(12345)  # mobile
        time.sleep(3)

