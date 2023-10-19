from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
browser = webdriver.Chrome()

# URL of the Indeed job search results
url = f"https://www.indeed.com/jobs?q=software+developer&l=Lynnwood%2C+WA&from=searchOnHP&vjk=46875250593820e9"

# Navigate to the website
browser.get(url)

# Wait for a few seconds to allow the page to load
time.sleep(2)

# Scroll down to trigger the loading of more job listings
browser.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)  # Wait again for the new listings to load

# Find and extract job titles
job_titles = browser.find_elements(By.CLASS_NAME, "jobTitle")
job_locations = browser.find_elements(By.CLASS_NAME, "company_location")
print("\nSOFTWARE DEVELOPER JOBS\n================\n")
i = 0

# Loop through the found elements and print their text
for job_element in job_titles:
    print(i)
    print("JOB TITLE:", job_element.text)
    print("JOB COMPANY AND LOCATION:", job_locations[i].text)
    print()
    print()

    i += 1

# Close the browser when you're done
browser.quit()
