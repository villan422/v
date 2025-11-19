"""
Selenium All Program Types - Master Script
This single file contains ALL types of Selenium programs you learned:
1. Navigation
2. Find element(s)
3. Search box (send_keys)
4. Window & Tab handling
5. Screenshots
6. Window size & position
7. Dropdown & Multi-select
8. JavaScript Alerts
9. Mouse Hover & Drag (ActionChains)
10. Checkboxes
11. Autocomplete dropdown
12. Frames
13. Waits (Explicit Wait)
14. Simple Social Login Demo
15. Drag and drop

Note:
- Some sites may block automation.
- Run section-by-section if needed.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

# -------------------------------------------------------------------
# 1. BASIC NAVIGATION PROGRAM
# -------------------------------------------------------------------
print("\n=== 1. BASIC NAVIGATION ===")
driver.get("https://www.google.com")
time.sleep(2)
print("Title:", driver.title)
driver.refresh()
time.sleep(1)
driver.back()
driver.forward()

# -------------------------------------------------------------------
# 2. FIND ELEMENT vs FIND ELEMENTS
# -------------------------------------------------------------------
print("\n=== 2. FIND ELEMENT vs FIND ELEMENTS ===")
driver.get("https://www.google.com")
single = driver.find_element(By.XPATH, "//textarea")
multi = driver.find_elements(By.XPATH, "//textarea")
print("Single:", single)
print("Multiple elements count:", len(multi))

# -------------------------------------------------------------------
# 3. SEND_KEYS SEARCH BOX
# -------------------------------------------------------------------
print("\n=== 3. SEARCH USING send_keys ===")
driver.get("https://www.google.com")
box = driver.find_element(By.NAME, "q")
box.send_keys("Selenium WebDriver Python")
box.send_keys(Keys.ENTER)
time.sleep(3)

# -------------------------------------------------------------------
# 4. WINDOWS / TABS HANDLING
# -------------------------------------------------------------------
print("\n=== 4. WINDOWS / TABS HANDLING ===")
driver.get("https://www.google.com")
driver.switch_to.new_window("tab")
driver.get("https://facebook.com")
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

# -------------------------------------------------------------------
# 5. SCREENSHOTS
# -------------------------------------------------------------------
print("\n=== 5. SCREENSHOTS ===")
driver.get("https://www.google.com")
driver.save_screenshot("full_screenshot.png")
print("Screenshot saved.")

# -------------------------------------------------------------------
# 6. WINDOW SIZE & POSITION
# -------------------------------------------------------------------
print("\n=== 6. WINDOW SIZE & POSITION ===")
print("Position:", driver.get_window_position())
driver.set_window_position(50, 50)
driver.set_window_size(900, 600)

# -------------------------------------------------------------------
# 7. DROPDOWN HANDLING
# -------------------------------------------------------------------
print("\n=== 7. DROPDOWN ===")
driver.get("https://demoqa.com/select-menu")
time.sleep(2)
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
dropdown.select_by_index(2)
dropdown.select_by_value("5")
dropdown.select_by_visible_text("Black")

# -------------------------------------------------------------------
# 8. ALERT HANDLING
# -------------------------------------------------------------------
print("\n=== 8. ALERTS ===")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

# -------------------------------------------------------------------
# 9. ACTIONCHAINS – HOVER, DRAG
# -------------------------------------------------------------------
print("\n=== 9. ACTIONCHAINS (HOVER) ===")
driver.get("https://imcc.mespune.in/")
time.sleep(4)
program = driver.find_element(By.XPATH, "//li[@id='menu-item-4383']")
ActionChains(driver).move_to_element(program).perform()

# -------------------------------------------------------------------
# 10. CHECKBOX HANDLING
# -------------------------------------------------------------------
print("\n=== 10. CHECKBOX ===")
driver.get("https://the-internet.herokuapp.com/checkboxes")
cb = driver.find_element(By.XPATH, "//form/input[1]")
if not cb.is_selected():
    cb.click()

# -------------------------------------------------------------------
# 11. AUTOCOMPLETE DROPDOWN
# -------------------------------------------------------------------
print("\n=== 11. AUTOCOMPLETE DROPDOWN ===")
driver.get("https://www.google.com")
search = driver.find_element(By.NAME,"q")
search.send_keys("imcc")
time.sleep(2)
options = driver.find_elements(By.XPATH, "//span[contains(text(),'imcc')]")
print("Suggestions found:", len(options))

# -------------------------------------------------------------------
# 12. FRAMES HANDLING
# -------------------------------------------------------------------
print("\n=== 12. FRAMES ===")
driver.get("https://demoqa.com/frames")
time.sleep(2)
driver.switch_to.frame("frame1")
frame_text = driver.find_element(By.ID, "sampleHeading").text
print("Frame text:", frame_text)
driver.switch_to.default_content()

# -------------------------------------------------------------------
# 13. EXPLICIT WAIT
# -------------------------------------------------------------------
print("\n=== 13. EXPLICIT WAIT ===")
driver.get("https://www.google.com")
wait = WebDriverWait(driver,10)
box = wait.until(EC.presence_of_element_located((By.NAME,"q")))
box.send_keys("Explicit Wait in Selenium")
box.send_keys(Keys.ENTER)

# -------------------------------------------------------------------
# 14. SOCIAL LOGIN DEMO (Snapchat)
# -------------------------------------------------------------------
print("\n=== 14. SOCIAL LOGIN (SNAPCHAT) ===")
driver.get("https://accounts.snapchat.com/accounts/login")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("your_username")
driver.find_element(By.NAME,"password").send_keys("your_password")
print("Credentials filled (login may fail due to security).")

# -------------------------------------------------------------------
# END
# -------------------------------------------------------------------
print("\n=== ALL PROGRAM TYPES EXECUTED ===")
time.sleep(3)
driver.quit()

# ---------------------------------------------------------------
# DRAG AND DROP – STANDARD SELENIUM
# ---------------------------------------------------------------
print("\n=== DRAG AND DROP (Standard) ===")
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)

source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

print("Drag & Drop Completed")
time.sleep(2)



"""
Important Selenium Commands - Full List
1. WebDriver Important Commands
- driver.get(url) - Opens a website
- driver.maximize_window() - Maximizes the browser window
- driver.back() - Go to previous page
- driver.forward() - Go to next page
- driver.refresh() - Refreshes the current page
- driver.quit() - Closes entire browser
- driver.close() - Closes current tab
2. Find Element Commands
- find_element() - Finds one element
- find_elements() - Finds multiple elements
- By.ID - Find using ID
- By.NAME - Find using name
- By.XPATH - Find using XPath
- By.CSS_SELECTOR - Find using CSS selector
- By.CLASS_NAME - Find using class name
- By.TAG_NAME - Find using tag name
- By.LINK_TEXT - Find using full link text
- By.PARTIAL_LINK_TEXT - Find using partial link text
3. WebElement Important Methods
- send_keys() - Types text
- click() - Clicks element
- submit() - Submits form
- clear() - Clears input
- text - Gets visible text
- get_attribute() - Reads HTML attribute
- is_displayed() - Element visible?
- is_enabled() - Element enabled?
- is_selected() - Checkbox/radio selected?
4. Dropdown (Select Class)
- select_by_visible_text() - Select by text
- select_by_value() - Select by value
- select_by_index() - Select by index
- deselect_by_visible_text() - Deselect by text
- deselect_all() - Deselect everything
5. ActionChains Commands
- move_to_element() - Hover action
- click() - Single click
- double_click() - Double click
- context_click() - Right click
- drag_and_drop() - Drag and drop
- click_and_hold() - Hold mouse button
- release() - Release mouse button
6. Alert Handling
- switch_to.alert - Switch to alert
- alert.accept() - Click OK
- alert.dismiss() - Click Cancel
- alert.send_keys() - Type text in alert prompt
7. Window & Frames
- switch_to.window() - Switch to new tab
- window_handles - List of tabs
- switch_to.frame() - Switch to iframe
- switch_to.default_content() - Back to main content
8. Waits
- time.sleep() - Hard wait
- WebDriverWait() - Explicit wait
- presence_of_element_located() - Wait until element exists
- element_to_be_clickable() - Wait until clickable
9. Cookies
- get_cookies() - Get all cookies
- add_cookie() - Add a cookie
- delete_cookie() - Delete specific cookie
- delete_all_cookies() - Clear all cookies
10. Screenshots
- save_screenshot() - Take screenshot
- get_screenshot_as_file() - Alternative screenshot method

"""
