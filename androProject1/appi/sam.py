from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options


desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "10",
    "deviceName": "Pixel_3a",
    "app": "C://APK files//Mahalaxmi Dindarshika 2023_41.0_Apkpure.apk",
    "appPackage": "com.mahalaxmi.marathi.pro",
    "appActivity": "com.mahalaxmi.marathi.pro.MainActivity",
    "udid": "emulator-5554"}

# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# driver = webdriver.Remote("http://localhost:4723/wd/hub",)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


ele_id = driver.find_element(AppiumBy.ID, "com.mahalaxmi.marathi.pro:id/imageViewVarshikAlokan")
ele_id.click()

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "10",
    "deviceName": "Pixel_3a",
    "app": "C://APK files//Mahalaxmi Dindarshika 2023_41.0_Apkpure.apk",
    "appPackage": "com.mahalaxmi.marathi.pro",
    "appActivity": "com.mahalaxmi.marathi.pro.MainActivity",
    "udid": "emulator-5554"}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(AppiumBy.ID, "com.mahalaxmi.marathi.pro:id/imageViewVarshikAlokan")
ele_id.click()

