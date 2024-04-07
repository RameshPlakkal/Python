from selenium import webdriver
from selenium.webdriver.common.by import By


class Cookie:
    def __init__(self, URL):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get(URL)

    def click_cookie(self):
        self.driver.find_element(By.ID, "cookie").click()

    def buy_addons(self):

        bot_cookie_money = int(self.driver.find_element(By.ID, "money").text.replace(",", ""))

        if bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyPortal b").
                                          text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyPortal b").click()
        elif bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyShipment b").
                                            text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyShipment b").click()
        elif bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyMine b").
                                            text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyMine b").click()
        elif bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyFactory b").
                                            text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyFactory b").click()
        elif bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").
                                            text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").click()
        elif bot_cookie_money > int(self.driver.find_element(By.CSS_SELECTOR, "#buyCursor b").
                                            text.split("-")[1].strip().replace(",", "")):
            self.driver.find_element(By.CSS_SELECTOR, "#buyCursor b").click()
