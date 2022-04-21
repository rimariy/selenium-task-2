import json
from msilib.schema import tables
import time
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


PATH ="C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://patent.public.lu/fo-eregister-view/")

driver.implicitly_wait(5)

number = driver.find_element_by_id('number')

numberInput= number.find_element_by_id('number')

search = driver.find_element_by_id('submitBtn') 

action0=ActionChains(driver)
action0.click(driver.find_element_by_id("SPC"))
action0.perform()

driver.implicitly_wait(5)


# Opening JSON file
f = open('data.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
pageData=[]
# Iterating through the json
# list



for i in data:
    numberInput= number.find_element_by_id('number')    
    numberInput.send_keys(i)
    time.sleep(3)
    search = driver.find_element_by_id('submitBtn')
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        Product_Name=driver.find_element_by_xpath('//*[@id="Main"]/p/strong[2]').text
    except:
        Product_Name=''
    
    try:
        Basic_Patent_Number=driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[1]/dd[4]/a').text
    except:
        Basic_Patent_Number==''
    
    try:
        Owner_Name=driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[9]/dd').text 
    except:
        Owner_Name=''

    try:
        Legal_Status = driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[1]/dd[5]').text 
    except:
        Legal_Status = ''
    
    try:
        Filing_Date = driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[5]/dd[1]').text 
    except:
        Filing_Date = ''
    
    try:
        SPC_Expiri_Date = driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[6]/dt[7]').text
    except:
        SPC_Expiri_Date = ''
    
    try:
        Marketing_Authorization_Number = driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[3]/dd[1]').text
    except:
        Marketing_Authorization_Number = ''

    try:
        Marketing_Authorization_Date =  driver.find_element_by_xpath('//*[@id="Main"]/div[3]/div[2]/div[2]/div[1]/div/dl[4]/dd[1]').text 
    except:
        Marketing_Authorization_Date = ''

    pageData.append({
        'Publication Number' : i ,
        'Product Name ' : Product_Name ,
        'Basic Patent Number ' :  Basic_Patent_Number,
        'Owner Name ' : Owner_Name,
        'Legal Status ' :  Legal_Status,
        'Filing Date ' : Filing_Date,
        'SPC Expiri Date ' : SPC_Expiri_Date ,
        'Marketing Authorization Number ' : Marketing_Authorization_Number ,
        'Marketing Authorization Date' : Marketing_Authorization_Date   
    })
    dataJson = json.dumps(pageData)
    jsonFile = open("data2.json", "w")
    jsonFile.write(dataJson)
    jsonFile.write(dataJson)
    jsonFile.close()

    print (pageData)
    time.sleep(3)
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    time.sleep(3)
    number = driver.find_element_by_id('number')
    numberInput= number.find_element_by_id('number')    
    numberInput.clear()






# Closing file
f.close()