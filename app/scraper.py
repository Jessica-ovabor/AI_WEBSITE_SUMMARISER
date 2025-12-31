from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def web_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)

    search = driver.find_element(By.ID, "InlineSearch")
    search.send_keys("Australia", Keys.RETURN)

    results = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "SearchResultItem"))
    )

    scraped_data = []

    for result in results[:8]:
        scraped_data.append(result.text)

    driver.quit()
    return scraped_data
