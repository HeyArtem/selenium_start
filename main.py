from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import user_name, password, url
import time

def login(user_name, password, url):
    try:
        # driver = webdriver.Chrome()
        # # driver.get("http://www.python.org")
        # driver.get("https://www.google.com/")
        # # assert "Python" in driver.title
        # time.sleep(2)
        # elem = driver.find_element(By.NAME, "q")
        # elem.clear()
        # elem.send_keys("pycon")
        # time.sleep(2)
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # time.sleep(4)

        driver = webdriver.Chrome()
        driver.get(url=url)
        time.sleep(2)

        elem = driver.find_element(By.NAME, "email")
        elem.clear()
        elem.send_keys(user_name)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        elem = driver.find_element(By.NAME, "pwd")
        elem.clear()
        elem.send_keys(password)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(7)






        # user_name_input = driver.find_element()
    except Exception as ex:
        print(ex)
    finally:
        # закроет одну вкладку
        driver.close()
        # закроет браузер
        driver.quit()

def main():
    login(user_name=user_name, password=password, url=url)

if __name__ == '__main__':
    main()

