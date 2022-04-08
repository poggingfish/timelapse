from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime
class bot():
    def __init__(self, canvas, path):
        self.canvas = canvas
        self.path = path       
        options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
    def setup(self):
        sleep(1)
        self.driver.get("https://pixelplace.io/"+self.canvas+"#x=803&y=786&s=3.38")
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[11]/a[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[5]/ul[2]/li[2]/a").click()
    def download(self):
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[5]/div[4]/div[1]/form/button[2]").click()