from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import winsound
from selenium.webdriver.common.proxy import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor










from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Get free proxies for rotating
def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)
    
    IPandPort = []
    for proxy in proxies:
        fullIp = proxy['IP Address'] + ':' + proxy['Port']
        IPandPort.append(fullIp)
    
    return IPandPort


free_proxies = get_free_proxies(driver)

print(free_proxies)

    


def run_session(proxy):
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy,
    "proxyType": "MANUAL",
    }

    webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

    opts = Options()
    user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'


    capabilities = webdriver.DesiredCapabilities.CHROME
    opts.add_argument("user-agent="+user_agent)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.ticketswap.uk/event/ss22-solomun/early-entrance-tickets/2e5713bb-0b51-4a2b-8dfc-1fd94db522d5/2013550")
    time.sleep(10)
    try:
        while True:
            time.sleep(10)
            available = driver.find_element(
            by=By.XPATH, value='//*[@id="__next"]/header/div[3]/div/div[1]/span').text
            if(available == '0'):
                driver.refresh()
            else:
                list = driver.find_element(
                    by=By.XPATH, value='/html/body/div[1]/div[2]/div[4]/ul/li[1]')
                list.click()
                time.sleep(0.7)
                button = driver.find_element(
                    by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/div[3]/button')
                button.click()
                time.sleep(0.1)
    except:
        winsound.Beep(freq, 500)
        time.sleep(0.01)
        winsound.Beep(freq, 500)
        time.sleep(0.1)
        winsound.Beep(freq, 500)
        time.sleep(0.1)

with ThreadPoolExecutor(max_workers=20) as executor:
	executor.map(run_session, free_proxies)

