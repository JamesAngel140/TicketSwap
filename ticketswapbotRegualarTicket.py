from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz

chrome_options = Options()
# chrome_options.add_argument(
#     r"user-data-dir=c:\Users\james\AppData\Local\Google\Chrome\User Data\Profile 2")
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://www.ticketswap.uk/event/ss22-solomun/regular-tickets/2e5713bb-0b51-4a2b-8dfc-1fd94db522d5/2013551")
# driver.get('https://www.ticketswap.uk/event/enzo-siragusa-presents-e-dimension/early-entrance-tickets/7f14d504-ebd6-4edc-b512-53b5ba155295/2013547')
original_window = driver.current_window_handle
time.sleep(0.2)

try:
    while True:
        time.sleep(0.2)


        available = driver.find_element(
        by=By.XPATH, value='//*[@id="__next"]/header/div[3]/div/div[1]/span').text
        if(available == '0'):
            time.sleep(3.1)
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


            # button = driver.find_element(
            #     by=By.XPATH, value='/html/body/ticketswap-portal[6]/div/div/div/div/div/div/div/button[1]')
            # button.click()

            # for window_handle in driver.window_handles:
            #     if window_handle != original_window:
            #         driver.switch_to.window(window_handle)
            #         break
            # time.sleep(0.5)

            # input = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
            # input.send_keys("jamesangel1420@gmail.com")
            # input.send_keys(Keys.RETURN)
            # time.sleep(0.5)
            
            # input = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            # input.send_keys("FunkyKong189!")
            # input.send_keys(Keys.RETURN)

            winsound.Beep(freq, duration)
            time.sleep(0.1)
            winsound.Beep(freq, duration)
            time.sleep(0.1)
            winsound.Beep(freq, duration)
            time.sleep(0.1)

 
except:
    winsound.Beep(freq, 500)
    time.sleep(0.01)
    winsound.Beep(freq, 500)
    time.sleep(0.1)
    winsound.Beep(freq, 500)
    time.sleep(0.1)


  

