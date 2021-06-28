from selenium import webdriver
from selenium.webdriver.chrome.options import Options   # COMMENT OUT IF USING FIREFOX
#from selenium.webdriver.firefox.options import Options   # UNCOMMENT IF USING FIREFOX
import time
import os

# set path to settings
curr_dir = os.getcwd()
path_set = f'{curr_dir}\\settings.txt'
path_cd = f'{curr_dir}\\chromedriver.exe'   # COMMENT OUT IF USING FIREFOX
#path_gd = f'{curr_dir}\\geckodriver.exe'   # UNCOMMENT IF USING FIREFOX

# set selenium options
sel_options = Options()
sel_options.headless = True

# set path to driver
driver = webdriver.Chrome(executable_path=path_cd, options=sel_options)   # COMMENT OUT IF USING FIREFOX
#driver = webdriver.Firefox(executable_path=path_gd, options=sel_options)   # UNCOMMENT IF USING FIREFOX

# selenium: get webpage
driver.get('https://gasnow.org')

# wait for javascript to load
time.sleep(5)

# click more
button = driver.find_element_by_class_name("more___3MjP6")
button.click()

# add elements to list
elements = []
for element in driver.find_elements_by_xpath('//span'):
    elements.append(element.text)

# load user settings
with open(path_set, "r") as settings:
    settings_list = settings.readlines()
    service = settings_list[0]
    txspeed = settings_list[1]
    txprice = settings_list[2]
    alerturl = settings_list[3]

# search for index of user defined service
search_term = service[:-1]
for item in elements:
    if search_term in item:
        position = elements.index(item)
        break
    else:
        continue

# decide if gas is low enough
index_of_price = []
if txspeed[:-1] == 'rapid':
    index_of_price.append(int(position) + 4)
elif txspeed[:-1] == 'fast':
    index_of_price.append(int(position) + 5)

price = elements[index_of_price[0]]
price_no_dollar = price[1:]

if float(price_no_dollar) <= float(txprice[:-1]):
    print(f"It's {service[:-1]} time!")
    if alerturl[:-1] != r'N/A':
        driver.get(alerturl[:-1])
    else:
        pass
else:
    print(f"It's not {service[:-1]} time!")

# quit driver
driver.close()
driver.quit()
