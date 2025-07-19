import time
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Appium options
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "RFCT70XTZQM",
    "appium:udid": "RFCT70XTZQM",
    "appium:appPackage": "com.target.ui",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.target.login.GateActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Connect to Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Delay and app interaction steps to arrive at the "nearest location" screen
time.sleep(3)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Continue As Guest\")").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ID, value="com.target.ui:id/search_by_zip_address").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ID, value="com.target.ui:id/search_field").click()



time.sleep(3)


# Simulated keyboard input (via touch)
def tap(x, y, delay=0):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    if delay > 0:
        time.sleep(delay)

tap(847, 1623)
tap(572, 1635)
tap(850, 1638)
tap(50, 1623)
tap(145, 1635)
tap(826, 2124)

# Capture GUI before unfolding event
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Simulate fold/unfold delay
time.sleep(10)

# Capture GUI after unfolding event
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# End session
driver.quit()

