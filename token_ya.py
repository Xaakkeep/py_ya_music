import json
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.command import Command
from selenium.webdriver.chrome.service import Service


def is_active(driver):
    try:
        driver.execute(Command.GET_ALL_COOKIES)
        return True
    except Exception:
        return False


def get_token():
    # make chrome log requests
    capabilities = DesiredCapabilities.CHROME
    capabilities["loggingPrefs"] = {"performance": "ALL"}
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
    s = Service(executable_path='chromedriver')
    driver = webdriver.Chrome(service=s)
    
    driver.get(
        "https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d")

    token = None

    while token == None and is_active(driver):
        sleep(1)
        try:
            logs_raw = driver.get_log("performance")
        except:
            pass

        for lr in logs_raw:
            log = json.loads(lr["message"])["message"]
            url_fragment = log.get('params', {}).get('frame', {}).get('urlFragment')

            if url_fragment:
                token = url_fragment.split('&')[0].split('=')[1]

    try:
        driver.close()
    except:
        pass
    
    return token

# print(get_token())


