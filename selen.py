from msilib.schema import tables
import time
import json
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


PATH ="C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://patent.public.lu/fo-eregister-view/")


action0=ActionChains(driver)
action0.click(driver.find_element_by_id("SPC"))
action0.perform()

action1=ActionChains(driver)
action1.click(driver.find_element_by_id("accordionDiv"))
action1.perform()

driver.implicitly_wait(2)
action2=driver.find_element_by_id("patentDateName")
action2.click()


driver.implicitly_wait(2)
action3=driver.find_element_by_xpath('//*[@id="patentDateName"]/option[3]')
action3.click()

action4=driver.find_element_by_xpath('//*[@id="patentDates"]/div/span[1]/input[1]')
action4.send_keys('01/01/1990')

action5=driver.find_element_by_xpath('//*[@id="patentDates"]/div/span[2]/input[1]')
action5.send_keys('19/04/2022')

action6=driver.find_element_by_id('submitBtn')
action6.send_keys(Keys.RETURN)


driver.implicitly_wait(2)
action7=driver.find_element_by_xpath('//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[1]/select')
action7.click()


driver.implicitly_wait(2)
action8=driver.find_element_by_xpath('//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[1]/select/option[5]')
action8.click()
# driver.implicitly_wait(5)

# try:
#     next =WebDriverWait(driver,10).until(
#             EC.presence_of_element_located((By.XPATH,'//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[10]/a'))
#         )
#     links=driver.find_elements_by_class_name('patent_link')
#     for link in links:
#         print (link.text)
# except :
#         driver.quit()

runtimes=int(driver.find_element_by_xpath('//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[8]').text.split()[1])
# print (runtimes)
# print(type(runtimes))
data=[]
for i in range(runtimes+1):

    try:
        time.sleep(5)
        # driver.implicitly_wait(10)
        links=driver.find_elements_by_class_name('patent_link')
        for link in links:
            data.append (link.text)
            print (link.text)
        time.sleep(5)
        next =WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[10]/a'))
        )
        # driver.implicitly_wait(5)
        # next=driver.find_element_by_xpath('//*[@id="patentsGrid"]/div/div/div[2]/table/tbody/tr/td[10]/a')
        next.click()
        # for i in range(len(data)):
        #     with open('readme.txt', 'w') as f:
        #         f.write(data[i])
        #         f.write('\n')
    except :
        time.sleep(5)
        

time.sleep(5)

dataJson = json.dumps(data)
jsonFile = open("data.json", "w")
jsonFile.write(dataJson)
jsonFile.close()



time.sleep(20)













# try:
#     data =WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.CLASS_NAME,'datagrid-body'))
#     ) 
#     tables = data.find_element_by_tag_name('table')

#     for table in tables:
#        tds=table.find_element_by_class_name('publicationNumber')
#        links=tds.find_elements_by_class_name('patent_link')
#        print (links.text)

# except:
#     driver.quit()












