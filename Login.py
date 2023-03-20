from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

config = {
    'EMAIL': 'cheryl.huang+ent01@mlytics.com',
    'PASSWORD': '12345678'
}

login_url = 'https://portal.mlytics.co/login'


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(login_url)
    elem = driver.find_element(By.ID, 'input-28')
    elem.clear()
    elem.send_keys(config['EMAIL'])
    elem = driver.find_element(By.ID, 'input-32')
    elem.clear()
    elem.send_keys(config['PASSWORD'])
    elem = driver.find_element(By.XPATH,
                               '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/span/form/div[4]/button/span')
    elem.click()
    time.sleep(3)

    #elem = add site?

if __name__ == '__main__':
    main()
