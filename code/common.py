from seleniumbase import Driver
import requests
from bs4 import BeautifulSoup
import time


def get_soup(url):
    """Takes a URL and returns a BeautifulSoup() instance representing the HTML of the page."""

    driver = Driver(uc=True)

    try:
        driver.get(url)
        time.sleep(8)

        html = driver.page_source
        return BeautifulSoup(html, "html.parser")
    finally:
        driver.quit()
