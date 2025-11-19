from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# ======================================================
# MASTER SELENIUM DEMO – ALL IMPORTANT COMMANDS
# ======================================================

# Create Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# ======================================================
# PART 1: BASIC NAVIGATION + GOOGLE SEARCH + ATTRIBUTES
# ======================================================
print("\n=== PART 1: Google Search + Element Attributes ===")
driver.get("https://www.google.com")
time.sleep(2)

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Get some attributes (from get_attribute.py)
print("maxlength:", search_box.get_attribute("maxlength"))
print("id:", search_box.get_attribute("id"))
print("value (before typing):", search_box.get_attribute("value"))

# Type IMCC and submit
search_box.send_keys("IMCC Pune")
print("value (after typing):", search_box.get_attribute("value"))
search_box.submit()
time.sleep(3)

print("Page Title:", driver.title)

# Find Google logo (normal img)
try:
    logo_img = driver.find_element(By.XPATH, "//img[@alt='Google']")
    print("Normal logo src:", logo_img.get_attribute("src"))
except:
    print("Normal IMG logo not found, maybe SVG logo is used.")

# ======================================================
# PART 2: SCREENSHOTS, COOKIES, WINDOW RECT (Screenshots&Cookie.py)
# ======================================================
print("\n=== PART 2: Screenshots, Cookies, Window Rect ===")
driver.get("https://www.google.com")
time.sleep(2)

# Locate the search text box and print its rect
search_textbox = driver.find_element(By.NAME, "q")
print("Search box rect details:", search_textbox.rect)

# Locate Google SVG logo (if present) and capture a screenshot of it
try:
    g_logo = driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Google'])[1]")
    g_logo.screenshot("img_searchtextbox_logo.png")
    print("Logo screenshot saved as img_searchtextbox_logo.png")
except:
    print("SVG logo not found, skipping SVG screenshot.")

# Full page screenshot
driver.save_screenshot("img_fullscreen.png")
print("Full page screenshot saved as img_fullscreen.png")

# Print all cookies
print("\nAll Cookies:")
print(driver.get_cookies())

# Get specific cookies (may not exist in all systems)
try:
    print("\nCookie NID:", driver.get_cookie('NID'))
except:
    print("Cookie NID not present.")

try:
    print("Cookie AEC:", driver.get_cookie('AEC'))
except:
    print("Cookie AEC not present.")

# Get window position
print("\nCurrent window position:", driver.get_window_position())

# Resize and reposition
driver.set_window_rect(100, 200, 900, 700)
print("Window repositioned and resized.")
time.sleep(2)

# ======================================================
# PART 3: MULTIPLE WINDOWS / TABS (multipleBrowser.py)
# ======================================================
print("\n=== PART 3: Multiple Windows and Tabs ===")
driver.get("https://www.google.com")
time.sleep(2)

# Open new window
driver.switch_to.new_window("window")
driver.get("https://www.facebook.com")
print("Opened new WINDOW: Facebook")
time.sleep(2)

# Open new tab
driver.switch_to.new_window("tab")
driver.get("https://www.youtube.com")
print("Opened new TAB: YouTube")

time.sleep(5)

# Close current tab (YouTube)
driver.close()
# Switch back to previous window
driver.switch_to.window(driver.window_handles[0])

# ======================================================
# PART 4: DROPDOWN + MULTI-SELECT (Select Class)
# (Combining master + multi-select_Dropdown.py)
# ======================================================
print("\n=== PART 4: Single & Multi-select Dropdowns ===")
driver.get("https://demoqa.com/select-menu")
time.sleep(3)

# Single select dropdown (oldSelectMenu)
dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
dropdown.select_by_index(2)
dropdown.select_by_value("5")
dropdown.select_by_visible_text("Black")
time.sleep(2)

# Multi-select dropdown (cars)
multi_select_element = driver.find_element(By.ID, "cars")
multi = Select(multi_select_element)

# Select and deselect as in your file
multi.select_by_visible_text("Volvo")
time.sleep(1)
multi.deselect_by_visible_text("Volvo")
time.sleep(1)
multi.select_by_index(1)       # Saab
time.sleep(1)
multi.select_by_value("audi")  # Audi
time.sleep(1)

print("Currently selected options in multi-select:")
all_selected_opt_list = multi.all_selected_options
for opt in all_selected_opt_list:
    print(" -", opt.text)

# Deselect all
multi.deselect_by_index(0)
multi.deselect_by_value("audi")
multi.deselect_all()
time.sleep(2)

# ======================================================
# PART 5: ALERT HANDLING (alert.py + extra prompt)
# ======================================================
print("\n=== PART 5: JavaScript Alerts ===")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

# Simple Alert
print("Triggering simple JS Alert...")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
time.sleep(1)

# Confirm Alert
print("Triggering JS Confirm...")
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()
alert = driver.switch_to.alert
print("Confirm alert text:", alert.text)
alert.accept()   # or alert.dismiss()
time.sleep(1)

result = driver.find_element(By.ID, "result")
print("Page result after accepting confirm:", result.text)

# Prompt Alert
print("Triggering JS Prompt...")
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt = driver.switch_to.alert
prompt.send_keys("Hello Selenium")
prompt.accept()
time.sleep(2)

# ======================================================
# PART 6: CHECKBOX HANDLING (Checkbox.py style)
# ======================================================
print("\n=== PART 6: Checkbox Handling (basic + conditional) ===")
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)

checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

# Click sequence (check.py style)
checkbox1.click()
time.sleep(1)
checkbox1.click()
time.sleep(1)
checkbox2.click()
time.sleep(1)
checkbox2.click()
time.sleep(1)

# Conditional select / unselect (check1.py style)
time.sleep(1)
if not checkbox1.is_selected():
    print("Checkbox1 not selected – selecting now.")
    checkbox1.click()
time.sleep(1)
if checkbox1.is_selected():
    print("Checkbox1 is selected – unselecting now.")
    checkbox1.click()
    time.sleep(1)

# ======================================================
# PART 7: MOUSE HOVER (MouseSimulation.py)
# ======================================================
print("\n=== PART 7: Mouse Hover (ActionChains) ===")
driver.get("https://imcc.mespune.in/")
time.sleep(3)

program_menu = driver.find_element(By.XPATH, "//li[@id='menu-item-4383']")
actions = ActionChains(driver)
actions.move_to_element(program_menu).perform()
print("Hovered over 'Program' menu.")
time.sleep(3)

# ======================================================
# PART 8: AUTOCOMPLETE DROPDOWN (AutocompleteDropdown.py)
# ======================================================
print("\n=== PART 8: Google Autocomplete Dropdown ===")
driver.get("https://www.google.com/")
time.sleep(2)

search_txtbox = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_txtbox.send_keys('imcc')
time.sleep(2)

imcc_dropdown = driver.find_elements(By.XPATH, "//span[contains(normalize-space(), 'imcc')]")
print("Number of dropdown suggestions found:", len(imcc_dropdown))
for i, item in enumerate(imcc_dropdown):
    print(f"{i+1}. {item.text}")

# ======================================================
# PART 9: FIND ELEMENTS (find_elements.py)
# ======================================================
print("\n=== PART 9: find_elements() Demo ===")
driver.get("https://www.google.com/")
time.sleep(2)

multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea")
print("Number of <textarea> elements found:", len(multi_search_txtbox))

if len(multi_search_txtbox) > 0:
    multi_search_txtbox[0].send_keys('imcc')
    multi_search_txtbox[0].send_keys(Keys.ENTER)
    print("Typed 'imcc' in first textarea and pressed Enter.")

time.sleep(5)

# ======================================================
# PART 10: COOKIES + SCREENSHOT + TABS + FRAMES (demoqa)
# ======================================================
print("\n=== PART 10: Cookies, Screenshot, Tabs, Frames (demoqa) ===")
driver.get("https://www.google.com")
time.sleep(2)

# Add & view cookie
driver.add_cookie({"name": "test_cookie", "value": "12345"})
print("Updated Cookies:", driver.get_cookies())
driver.delete_all_cookies()
print("All cookies deleted in this part.")

# Screenshot
driver.save_screenshot("screenshot_master.png")
print("Screenshot saved as screenshot_master.png")

# New tab example.com
driver.execute_script("window.open('https://example.com');")
time.sleep(2)

tabs = driver.window_handles
if len(tabs) >= 2:
    driver.switch_to.window(tabs[1])
    print("Switched to Tab 2:", driver.title)
    driver.switch_to.window(tabs[0])
    print("Back to Tab 1:", driver.title)

# Frames demo (demoqa.com/frames)
print("\nTrying Frames demo (demoqa.com/frames)...")
driver.get("https://demoqa.com/frames")
time.sleep(3)

try:
    driver.switch_to.frame("frame1")
    frame_text = driver.find_element(By.ID, "sampleHeading").text
    print("Inside Frame1 Text:", frame_text)
    driver.switch_to.default_content()
except Exception as e:
    print("Frame1 not found or error:", e)

# ======================================================
# PART 11: SIMPLE ALERT DEMO (alertm.py style)
# ======================================================
print("\n=== PART 11: Simple JS Alert Demo ===")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Simple Alert text:", alert.text)
alert.accept()
time.sleep(2)

# ======================================================
# PART 12: CONFIRM ALERT DEMO (alert.py style)
# ======================================================
print("\n=== PART 12: JS Confirm Demo ===")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()
time.sleep(2)

alert = driver.switch_to.alert
print("Alert text (confirm):", alert.text)
alert.accept()

result = driver.find_element(By.ID, "result")
print("Page result after accepting confirm:", result.text)
time.sleep(2)

# ======================================================
# PART 13: DROPDOWN ON the-internet.herokuapp.com (dropdown.py)
# ======================================================
print("\n=== PART 13: Simple Dropdown (the-internet.herokuapp.com/dropdown) ===")
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

mydropdown = driver.find_element(By.ID, "dropdown")
dropdown_simple = Select(mydropdown)

dropdown_simple.select_by_visible_text("Option 1")
time.sleep(2)
print(f"Selected option: {dropdown_simple.first_selected_option.text}")

dropdown_simple.select_by_value("2")
time.sleep(2)
print(f"Selected option: {dropdown_simple.first_selected_option.text}")

dropdown_simple.select_by_index(2)
time.sleep(2)
print(f"Selected option: {dropdown_simple.first_selected_option.text}")

# ======================================================
# PART 14: MULTI-SELECT DROPDOWN AGAIN (dropdown1.py style)
# ======================================================
print("\n=== PART 14: Multi-Select Dropdown (demoqa again) ===")
driver.get("https://demoqa.com/select-menu")
time.sleep(3)

multi_select_element2 = driver.find_element(By.ID, "cars")
multi_select2 = Select(multi_select_element2)

multi_select2.select_by_visible_text("Volvo")
multi_select2.deselect_by_visible_text("Volvo")

multi_select2.select_by_index(1)
multi_select2.select_by_value("audi")

print("Currently selected options (second multi-select run):")
for opt in multi_select2.all_selected_options:
    print(opt.text)

multi_select2.deselect_by_index(0)
multi_select2.deselect_by_value("audi")
multi_select2.deselect_all()
time.sleep(2)

# ======================================================
# PART 15: IFRAME DEMO ON the-internet.herokuapp.com/iframe (frame.py)
# ======================================================
print("\n=== PART 15: IFrame Demo (the-internet.herokuapp.com/iframe) ===")
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)

driver.switch_to.frame("mce_0_ifr")
print("Switched to iframe")

iframe_body = driver.find_element(By.TAG_NAME, "body")
iframe_body.clear()
iframe_body.send_keys("India")
time.sleep(3)

driver.switch_to.default_content()
main_header = driver.find_element(By.TAG_NAME, "h3")
print("Main Document Header:", main_header.text)
time.sleep(2)

# ======================================================
# PART 16: DRAG 3RD RECRUITER LOGO (action1c.py style)
# ======================================================
print("\n=== PART 16: Drag 3rd Recruiter Logo on IMCC Site ===")
driver.get("https://imcc.mespune.in/")
driver.set_page_load_timeout(20)
driver.maximize_window()
time.sleep(5)

wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

header = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h2[contains(normalize-space(.),'Prominent Recruiters')]")
    )
)

logos = driver.find_elements(
    By.XPATH, "//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img"
)
print("Total logos found:", len(logos))

if len(logos) >= 3:
    third_logo = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img)[3]")
        )
    )

    time.sleep(2)

    actions.click_and_hold(third_logo).move_by_offset(-100, 0).release().perform()
    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found – cannot drag 3rd logo.")

# ======================================================
# END
# ======================================================
print("\n=== END OF MASTER SCRIPT ===")
time.sleep(3)
driver.quit()
