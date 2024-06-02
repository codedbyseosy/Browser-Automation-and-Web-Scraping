from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/eseoseodion/Downloads/chromedriver-mac-x64/chromedriver')

def get_driver():
    # Set options/protocols to make browsing easier
    options = webdriver.ChromeOptions() # create an instance of the class
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                                ["enable-automation"])
    options.add_argument("disable-blink-features-AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)

    #Connecting the driver to a webpage
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()

    # Extracting an element from the driver
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())

