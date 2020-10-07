from selenium import webdriver
import time
import sys
sys.path.append("..")
from utils.scrapper import get_items
import os

class Driver:
    def __init__(self, params=['--ignore-certificate-errors','--incognito','--headless'],
                 path='chromedriver_win32\\chromedriver.exe'):
        print(os.getcwd())
        options = webdriver.ChromeOptions()
        for param in params:
            options.add_argument(param)

        self.browser = webdriver.Chrome(path, chrome_options=options)

    def scroll_down(self):
        """A method for scrolling the page."""
        # Get scroll height.
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to the bottom.
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load the page.
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height.
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_all_listings(self, url):
        self.browser.get(url)
        self.browser.maximize_window()
        self.scroll_down()
        start = time.time()
        # actually get the links
        page_source = self.browser.page_source
        tag = "article"
        items = get_items(page_source,url,tag)
        print("Number of apartments:", len(items))
        print("Total time:", time.time() - start)
        return items

    def close(self):
        self.browser.close()