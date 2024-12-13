from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Initialize the Selenium WebDriver (Make sure to download the appropriate driver for your browser)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Replace this URL with the URL of the target website
url = "https://listex.info/uk/product/tvorog-lavka-tradiciy-moloko-bar-18-ua-0250010978411"
driver.get(url)

try:
    # Wait for the button with text "Характеристики" to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Характеристики']")))

    # Click the button
    button.click()

    # Wait for the element to be visible
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"collapseOne\"]/div/div/div[1]/div[6]/table/tbody/tr[1]/td")))

    # Extract the text from the element
    data = element.text

    # Save the data to a CSV file
    csv_file = "scraped_data.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Data"])
        writer.writerow([data])

    print(f"Data successfully scraped and saved to {csv_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
