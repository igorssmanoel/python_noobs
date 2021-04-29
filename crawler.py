from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


email = "igorsergioigorcisco@gmail.com"
senha = "igor80250090"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://twitter.com/login")
browser.maximize_window()
loginInput = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')

loginInput.send_keys(email)

passwordInput = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

passwordInput.send_keys(senha)

submitButton = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')

submitButton.click()

browser.get('https://twitter.com/Astralisgg')

while True:
    sleep(0.1)
    browser.execute_script('window.scrollBy(0, 2)')
