from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def driver_client():
    driver = webdriver.Chrome()
    return driver


def web_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)

    search = driver.find_element(By.ID, "InlineSearch")
    search.send_keys("Australia", Keys.RETURN)

    results = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "SearchResultItem"))
    )

    scraped_data = []

    for result in results[:3]:
        scraped_data.append(result.text)

    driver.quit()
    return scraped_data


def dynamic_web_scraper(url):
    web_driver = driver_client()
    webdriver.get(url)
    search = web_driver.find_element(By.CSS_SELECTOR, "InlineSearch")

    results = WebDriverWait(web_driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "SearchResultItem"))
    )

    scraped_data = []

    for result in results[:3]:
        scraped_data.append(result.text)

    web_driver.quit()
    return scraped_data
