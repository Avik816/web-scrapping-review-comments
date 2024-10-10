from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open IMDb reviews page (replace with the actual reviews page URL you want to scrape)
driver.get('https://www.imdb.com/title/tt2975590/reviews/')  # Update with the correct IMDb URL

# Set up a wait object
wait = WebDriverWait(driver, 10)  # Timeout after 10 seconds if element not found

# Function to click "Load More" button until it disappears
def click_load_more():
    while True:
        try:
            # Wait until the 'Load More' button is clickable
            load_more_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ipl-load-more ipl-load-more--loaded']/button[@id='load-more-trigger']"))
            )

            # Click the "Load More" button until all reviews are loaded
            load_more_button.click()
            print("Clicked 'Load More' button")

            # Wait for new content to load (adjust as needed)
            time.sleep(2)  # Wait time can vary based on network speed and page structure

        except Exception as e:
            # Break loop if no more 'Load More' button is found or other exceptions occur
            print("No more 'Load More' button found .")
            break

click_load_more()

# After loading all comments, scrape the reviews
reviews = driver.find_elements(By.CLASS_NAME, 'ipc-html-content-inner-div')

# Extract and print the text of each review
for i, review in enumerate(reviews):
    print(f"Review {i + 1}: {review.text}\n")

# Close the browser
driver.quit()
