import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://client-auth-dev.fanfix.dev/login")

# Wait for the email input and send keys
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys("testqa@mailinator.com")

# Wait for the password input and send keys
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys("123456789")

# Submit the form
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button)[2]"))).click()

# Wait for the "New Post" button and click
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/button[1]"))).click()

# Wait for the post caption input and send keys (update selector as required)
# This is commented out because the original selector was incorrect; adjust as necessary
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'post-caption'))).send_keys("This post is done by automation assignment")

# If there's a need to click a button after entering the post caption, do it here
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-bvx9sv']"))).click()

#Select any .jpg file from your system
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='MuiBox-root css-cnbb3m'])[10]"))).click()

#click on the Add Media button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[text() = 'Add Media']"))).click()

#verify if the custom amount is less than $5, the Post button should be disabled
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='MuiChip-label MuiChip-labelMedium css-9iedg7'])[6]"))).click()
Display_Button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='MuiStack-root css-dvxtzn']"))).is_enabled()

if Display_Button == True:
    print("Test case passed")
else:
    print("Test case failed")


#Enter the amount value of $5 for both Subs and Non-subs in the custom amount input field
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='MuiChip-label MuiChip-labelMedium css-9iedg7'])[2]"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//span[@class='MuiChip-label MuiChip-labelMedium css-9iedg7'])[8]"))).click()

#Click on Post Button
Button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation pill-btn css-iugmff']")))
Button.click()

#Refresh the page
driver.refresh()

#At last click on Post Profile button(when custom amount is $5), also verify the post is successfully created Instructions:
Posts_Button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div/div/button[2]/a/p")))
Posts_Button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//div[@class='MuiBox-root css-8v90jo'])[1]"))).click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/p")))
text = element.text
print(text)

if text == "This post is done by automation assignment":
    print("Test Case Passed")
else:
    print("Test Case Failed")

time.sleep(5)
driver.quit()