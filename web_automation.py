from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Create the Browser Instance and Request the URL -------------------------------------------
browser = webdriver.Chrome('chromedriver.exe')

sleep(1)

browser.maximize_window()
sleep(1)
browser.get('https://www.saucedemo.com/')

sleep(1)

# Login Process -----------------------------------------------------------------------------

usename_input = browser.find_element(By.NAME, "user-name")
sleep(1)
usename_input.send_keys('standard_user')

sleep(1)

password_input = browser.find_element(By.NAME, "password")
sleep(1)
password_input.send_keys('secret_sauce')

sleep(3)
login_btn = browser.find_element(By.NAME, "login-button").click()

sleep(3)

# Add to Cart Process -----------------------------------------------------------------------

item1 = browser.find_element(By.CLASS_NAME , "inventory_item_name").click()
sleep(3)

add_to_cart1 = browser.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
sleep(3)

back = browser.find_element(By.NAME, "back-to-products").click()
sleep(3)

add_to_cart2 = browser.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light").click()
sleep(3)

add_to_cart3 = browser.find_element(By.NAME, "add-to-cart-sauce-labs-fleece-jacket").click()
sleep(3)


# Cart and Checkout -------------------------------------------------------------------------

cart = browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

sleep(3)

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)

checkout = browser.find_element(By.NAME, "checkout").click()
sleep(3)


# Fill Checkout Form ------------------------------------------------------------------------

f_name_input = browser.find_element(By.NAME, "firstName")
sleep(1)
f_name_input.send_keys('Yassir')

sleep(1)

l_name_input = browser.find_element(By.NAME, "lastName")
sleep(1)
l_name_input.send_keys('AZ')

sleep(1)

zip_input = browser.find_element(By.NAME, "postalCode")
sleep(1)
zip_input.send_keys('20000')

sleep(1)
continuee = browser.find_element(By.NAME, "continue").click()
sleep(3)

# Finish THE Checkout ------------------------------------------------------------------------

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)

finish = browser.find_element(By.NAME, "finish").click()
sleep(3)

# Quit the Browser
browser.quit()