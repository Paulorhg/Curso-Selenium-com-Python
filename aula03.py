from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()

browser.get(url)

sleep(3)

a = browser.find_element(By.TAG_NAME, "a")
a.click()

p = browser.find_element(By.TAG_NAME, "p")
print(f'texto a: {a.text}')
print(f'texto p: {p.text}')
# browser.quit()