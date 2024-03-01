#!/usr/bin/env python
# coding: utf-8
from pydantic_models.pydantic_classes import URLClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def initialize_driver():
    # setup chrome options
    chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless') # ensure GUI is off
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
    # set path to chromedriver as per your configuration
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def close_privacy_warning(driver):
    close_button = driver.find_element(By.ID, "closePrivacyWarning")
    close_button.click()

def click_next_button(driver):
    try:
        next_button = driver.find_element(By.CLASS_NAME, "coveo-pager-next")
        next_button.click()
        time.sleep(2)
        return driver
    except NoSuchElementException:
        return None

def scrape(driver, refresher_readings_list):
    time.sleep(2)  # Wait for the page to load
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all('h4', class_='coveo-title')
    for title in titles:
        link = title.find('a', class_='CoveoResultLink')['href']
        reading = [title.text.strip(), link]
        refresher_readings_list.append(reading)

def get_reading_detail_data(driver, reading):
    driver.get(reading[1])
    time.sleep(5)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    meta_data = soup.find('div', class_="content-utility")
    span_elements = meta_data.find_all('span', class_=['content-utility-curriculum', 'content-utility-topic'])

    data = {
        "title": "",
        "topic": "",
        "published_year": "",
        "level": "",
        "introduction": "",
        "learning_outcomes": "",
        "summary": "",
        "overview": "",
        "link": ""
    }

    # Extract text content from selected span elements
    if len(span_elements) >= 3:  # Ensure 'curriculum', 'topic', and 'level' span elements are present
        data["published_year"] = span_elements[0].text.strip().split()[0]
        data["level"] = span_elements[1].text.strip()
        data["topic"] = span_elements[2].text.strip()

    # Extract data from other sections
    headings = soup.find_all('h2', class_="article-section")
    for section in headings:
        if section.text in ('Introduction', "Learning Outcomes", "Summary", "Overview"):
            if section.text == "Introduction":
                data["introduction"] = section.findParent().text.strip()
            elif section.text == "Learning Outcomes":
                data["learning_outcomes"] = section.find_next().text.strip()
            elif section.text == "Summary":
                data["summary"] = section.find_next().text.strip()
            elif section.text == "Overview":
                data["overview"] = section.find_next().text.strip()

    return data

        
def scrape_reading_detail(refresher_readings_list):
    data_list = []
    driver = initialize_driver()
    for reading in refresher_readings_list:
        reading_detail = get_reading_detail_data(driver, reading)
        
        reading_detail['title'] = reading[0]
        reading_detail['link'] = reading[1]
        try:
            validated_data = URLClass(**reading_detail)
            # If validation is successful, append the validated data to data_list
            data_list.append(reading_detail)
        except ValidationError as e:
            print(reading[0])
            # If validation fails, print the error message and continue to the next reading
            print(f"Validation error for reading: {str(e)}")
        
    driver.quit()
    df = pd.DataFrame(data_list)
    return df


# def main():
refresher_readings_list = []
driver = initialize_driver()
url = "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=10&sort=%40refreadingcurriculumyear%20descending"
driver.get(url)
close_privacy_warning(driver)
for page_num in range(1):
    scrape(driver, refresher_readings_list)
    driver = click_next_button(driver)
    if driver is None:
        break
df = scrape_reading_detail(refresher_readings_list)
print(df)
df.to_csv('refresher_readings.csv', index=False)
# driver.quit()

# if __name__ == "__main__":
#     main()

