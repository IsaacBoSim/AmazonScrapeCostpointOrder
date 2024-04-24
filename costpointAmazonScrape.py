import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_amazon(url):
    options = Options()
    options.headless = True
    # Set up the ChromeDriver path using the Service class
    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Wait for the title to be loaded
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "productTitle"))
    )

    # Extract data using Selenium
    title = driver.find_element(By.ID, "productTitle").text.strip()
    price = driver.find_element(By.CSS_SELECTOR, 'span.a-price span.a-offscreen').text.strip()
    description = driver.find_element(By.ID, "featurebullets_feature_div").text.strip()
    # vendor = driver.find_element(By.ID, "bylineInfo").text.strip()

    driver.quit()
    return title, price, description


def fill_costpoint_form(item_data, form_url):
    options = Options()
    # Set any desired options here
    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(form_url)

    # Fill out the form fields using the updated Selenium 4 syntax
    driver.find_element(By.NAME, 'Item').send_keys(item_data[0])
    driver.find_element(By.NAME, 'Price').send_keys(item_data[1])
    driver.find_element(By.NAME, 'Description').send_keys(item_data[2])
    # driver.find_element(By.NAME, 'Vedor Part').send_keys(item_data[3])
    # driver.find_element(By.NAME, 'BUYER').send_keys('BUYER01')

    # Submit the form

    driver.quit()


# Main execution
if __name__ == "__main__":
    item_url = input("Enter the Amazon item URL: ")
    form_url = input("Enter the Costpoint URL: ")
    #quantity = input("Enter Quantity: ")

    item_data = scrape_amazon(item_url)
    fill_costpoint_form(item_data, form_url)
