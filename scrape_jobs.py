from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
browser = webdriver.Chrome()

# URL of the Indeed job search results
url = f"https://www.indeed.com/jobs?q=software+developer&l=Lynnwood%2C+WA&sc=0kf%3Aattr%28FCGTU%7CHFDVW%7CQJZM9%7CUTPWG%252COR%29%3B&radius=10&vjk=77a57a3b8d3120c5"

# Navigate to the website
browser.get(url)

# Wait for a few seconds to allow the page to load
time.sleep(2)

# Scroll down to trigger the loading of more job listings
browser.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)  # Wait again for the new listings to load

# Find and extract job titles
job_titles = browser.find_elements(
    By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul'
)

# Loop through the found elements and print their text
for title in job_titles:
    print(title.text)

# Close the browser when you're done
browser.quit()
