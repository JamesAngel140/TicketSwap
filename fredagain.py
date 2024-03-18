from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz

chrome_options = Options()
chrome_options.add_argument(
    r"user-data-dir=c:\Users\james\AppData\Local\Google\Chrome\User Data\Profile 1")
driver = webdriver.Chrome(chrome_options=chrome_options)

index = 12800836

1280788

while True: 
    print(index)
    driver.get("https://www.ticketweb.uk/event/four-tet-fred-again-electric-brixton-tickets/" + str(index) + "?pl=electricbrixton")
    try:
        ticketsNotAvaible = driver.find_element( by=By.XPATH, value='/html/body/div[1]/div/div[2]/div[30]/div[2]/div[1]/div/h1/span[2]'); 
        while True: 
            winsound.Beep(freq, duration)
            time.sleep(0.1)
    except:
        index = index + 1



