import selenium
from selenium import webdriver

url = input("Enter the URL: ")
print("The URL is: " + url)
chrome_driver = webdriver.Chrome()
chrome_driver.get(url)
chrome_driver.quit()

if __name__ == '__main__':
    print(selenium.__version__)