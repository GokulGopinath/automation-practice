from selenium import webdriver
from selenium.webdriver.support.select import Select   #for the select clause

import time


username='John Doe'
pswd='ThisIsNotAPassword'

driver =webdriver.Chrome('F:/chromedriver/chromedriver.exe')
driver.get('https://katalon-demo-cura.herokuapp.com/')



time.sleep(5)
driver.find_element_by_id('btn-make-appointment').click()

time.sleep(5)
# yes=input("Enter:  ")
#Entering uname and pswd
driver.find_element_by_id('txt-username').send_keys(username)
time.sleep(5)

driver.find_element_by_id('txt-password').send_keys(pswd)
# submit
driver.find_element_by_id('btn-login').click() 

# time.sleep(5)

# form

print('Facility:')
opt=int(input(('Enter from following: 1-Tokyo CURA Healthcare Center 2-Hongkong CURA Healthcare Center 3-Seoul CURA Healthcare Center : ')))

dct={1:"Tokyo CURA Healthcare Center", 2:"Hongkong CURA Healthcare Center", 3:"Seoul CURA Healthcare Center"}
sel=Select(driver.find_element_by_id('combo_facility'))
sel.select_by_visible_text(dct[opt])

opt=int(input('Apply for hospital readmission: 1- yes  0- N0: '))
if opt:
	driver.find_element_by_id('chk_hospotal_readmission').click()

print('Healthcare Program: ')
dct1={1:"medicare",2:"medicaid",3:"none"}
opt=int(input('1:medicare,2:medicaid,3:none - '))
driver.find_element_by_id('radio_program_'+dct1[opt]).click()

date_string=input('Enter the visit date: ')
datefield = driver.find_element_by_id('txt_visit_date')
datefield.click()
datefield.send_keys(date_string)


input_text=input('Enter the Comment : ')

driver.find_element_by_id('txt_comment').send_keys(input_text)


driver.find_element_by_id('btn-book-appointment').click()

# time.sleep(5)