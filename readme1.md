
#For LOGO Drag

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://imcc.mespune.in/")
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

header = wait.until(
    EC.presence_of_element_located((By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]"))
)
logos = wait.until(
    EC.presence_of_all_elements_located((By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img"))
)
print("Total logos found: ", len(logos))

if len(logos)>=3:
    third_logo = wait.until(EC.visibility_of(logos[2])) #index 2 => 3rd logo
    time.sleep(2)
    actions.click_and_hold(third_logo).move_by_offset(-100,0).release().perform()
    #alternatively:actions.drag_and_drop_by_offset(thrid_logo,-100,0).perform()

    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found")
driver.quit()

----------------------------------------------------------------------------------
//Count logos and drag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://imcc.mespune.in/")
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

# Locate "Prominent Recruiters" header
header = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h2[contains(normalize-space(.),'Prominent Recruiters')]")
    )
)

# Count logos
logos = driver.find_elements(
    By.XPATH, "//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img"
)
print("Total logos found:", len(logos))

if len(logos) >= 3:
    # Always re-fetch the 3rd logo fresh (avoids stale element reference)
    third_logo = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img)[3]")
        )
    )

    time.sleep(2)

    # Drag the 3rd logo 100px to the left
    actions.click_and_hold(third_logo).move_by_offset(-100, 0).release().perform()
    # OR:
    # actions.drag_and_drop_by_offset(third_logo, -100, 0).perform()

    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found")

driver.quit()
------------------------------------------------------------------------------------
--JS Alert--
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

confirm_button = driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
confirm_button.click()
time.sleep(3)

alert = driver.switch_to.alert

print("Alert text: ", alert.text)
alert.accept()

result = driver.find_element(By.ID,"result")
print("Page result after accepting alert: ", result.text)
time.sleep(3)


driver.quit()

-------------------------------------------------------------------------
//alert
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click button to trigger alert
driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()
time.sleep(3)

# Switch to alert
alert = driver.switch_to.alert
print("Alert text:", alert.text)

# Accept the alert
alert.accept()

time.sleep(3)
driver.quit()

-------------------------------------------------
//Checkboxces
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[2]")

time.sleep(5)
if not checkbox1.is_selected():
    checkbox1.click()
time.sleep(5)
if checkbox1.is_selected():
    checkbox1.click()
# time.sleep(5)
# checkbox2.click()
# time.sleep(5)
# checkbox2.click()
# time.sleep(5)

-------------------------------------------------------------
//dropdown types
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

# locate dropdown
mydropdown = driver.find_element(By.ID, "dropdown")
dropdown = Select(mydropdown)

# select by visible text
dropdown.select_by_visible_text("Option 1")
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")

# select by value
dropdown.select_by_value("2")
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")

# select by index (2 → Option 2)
dropdown.select_by_index(2)
time.sleep(2)
print(f"Selected option: {dropdown.first_selected_option.text}")

-----------------------------------------------------------
dropdoen  
#MULTI-SELECT DROPDOWN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://demoqa.com/select-menu")
multi_select_element = driver.find_element(By.ID,"cars")
multi_select = Select(multi_select_element)

multi_select.select_by_visible_text("Volvo")
multi_select.deselect_by_visible_text("Volvo")

multi_select.select_by_index(1)
multi_select.select_by_value("audi")

all_selected_opt_list = multi_select.all_selected_options
for opt in all_selected_opt_list:
    print(opt.text)

multi_select.deselect_by_index(0)
multi_select.deselect_by_value("audi")
multi_select.deselect_all()

-----------------------Frame Switch---------------------
from PIL.ImagePalette import wedge
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from switch_window import option

option=webdriver.ChromeOptions()
option.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=option)
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top") #Switch to top frame (main frame)
print("Switch to top frame")

driver.switch_to.frame("frame-left") #Switch to left frame within top frame
print("Switch to left frame")

left_frame = driver.find_element(By.TAG_NAME, "body")
print("Left Frame Text: ", left_frame.text) #get text from the left frame

driver.switch_to.parent_frame()#Switch back to the top frame
print("Switched back to top frame")

driver.switch_to.frame("frame-middle") #Switch to middle frame within top frame
print("Switch to middle frame")

middle_frame = driver.find_element(By.TAG_NAME, "body")
print("Middle Frame Text: ", middle_frame.text) #get text from the middle frame

driver.switch_to.parent_frame()#Switch back to the top frame
print("Switched back to top frame")

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom") #Now switch to bottom frame
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("Bottom Frame Text: ", bottom_frame.text) # Get text from bottom frame

driver.quit()

----------------------------------------------
//frames
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# ---- TOP → LEFT ----
driver.switch_to.frame("frame-top")   # switch to top frame
print("Switched to top frame")

driver.switch_to.frame("frame-left")  # inside left frame
print("Switched to left frame")
left_frame = driver.find_element(By.TAG_NAME, "body")
print("Left Frame Text:", left_frame.text)

driver.switch_to.parent_frame()       # back to top
print("Back to top frame")

# ---- TOP → MIDDLE ----
driver.switch_to.frame("frame-middle")
print("Switched to middle frame")
middle_frame = driver.find_element(By.ID, "content")
print("Middle Frame Text:", middle_frame.text)

driver.switch_to.parent_frame()       # back to top
print("Back to top frame")

# ---- TOP → RIGHT ----
driver.switch_to.frame("frame-right")
print("Switched to right frame")
right_frame = driver.find_element(By.TAG_NAME, "body")
print("Right Frame Text:", right_frame.text)

# Back to root (default content)
driver.switch_to.default_content()
print("Back to main document")

# ---- BOTTOM ----
driver.switch_to.frame("frame-bottom")
print("Switched to bottom frame")
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("Bottom Frame Text:", bottom_frame.text)

time.sleep(5)
driver.quit()
---------------------------------------
//Facebook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.fb.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# Step 1: Click "Create new account"
create_new_account = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="open-registration-form-button"]'))
)
create_new_account.click()

# Step 2: Fill form fields
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
first_name.send_keys("Arnav")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Chandure")

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("arnav123@example.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("StrongPassword123")

# Step 3: Select date of birth
Select(driver.find_element(By.NAME, "birthday_day")).select_by_visible_text("16")
Select(driver.find_element(By.NAME, "birthday_month")).select_by_visible_text("Sep")
Select(driver.find_element(By.NAME, "birthday_year")).select_by_visible_text("2002")  

# Step 4: Select gender (Male)
gender = driver.find_element(By.XPATH, '//input[@name="sex" and @value="2"]')
gender.click()

# Step 5: Click Sign Up
signup_btn = driver.find_element(By.NAME, "websubmit")
signup_btn.click()

time.sleep(10)
driver.quit()








