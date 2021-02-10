# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class TestDd():
  def setup_method(self, method):
    self.opts = Options()
    self.opts.headless = True
    self.driver = webdriver.Chrome(options=self.opts)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dd(self):
    self.driver.get("https://rozetka.com.ua/ua/playstation_5/p223588825/")
    self.driver.set_window_size(1920, 970)
    self.driver.find_element(By.XPATH, "/html/body/app-root/div/div[1]/app-rz-product/div/product-tab-main/div[1]/div[1]/div[2]/product-main-info/div/div/app-product-buy-btn/app-buy-button/button")
  
