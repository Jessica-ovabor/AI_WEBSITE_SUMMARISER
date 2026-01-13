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

    results = WebDriverWait(driver, 90).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "SearchResultItem"))
    )

    for result in results[:3]:
        scraped_data = result

    driver.quit()
    return scraped_data


def dynamic_web_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # results = WebDriverWait(driver, 30).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, ""))
    # )

    scraped_data = driver.page_source[:500]

    # for result in results[:3]:
    #     scraped_data.append(result.text)

    driver.quit()
    return scraped_data
