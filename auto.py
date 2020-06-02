# USING PYTHON FOR AUTOMATION

# How to read files

# # Here we open "inputFile.txt" and configure it for reading. f is an object of type open()
# f = open('inputFile.txt','r')
# # here we print file content
# print(f.read())
# #closing the file
# f.close()

#------------------------------------------------------------------------------------------------
#another way for do the same task is printing row by row in a for loop.

# Here we open "inputFile.txt" and configure it for reading. f is an object of type open()
# f = open('inputFile.txt','r')

# count = 0

# here we print file content by rows in a for loop
# for row in f:
# 	print(str(count) + row)
# 	count = count + 1

# #closing the file
# f.close()

#------------------------------------------------------------------------------------------------

# # first, we open inputFile.txt for reading in f
# f = open('inputFile.txt','r')

# # here we go through f with a for loop and print only those lines that contains a "P" that indicates that studens pass the exams
# for row in f:
# 	row_split = row.split()		# split() method returns a list of strings after breaking the given string by the specified separator

# 	if row_split[2] == 'P':
# 		print(row)

# #closing the file
# f.close()

#---------------------------------------------------------------------------------------------
# writing files in Python

# first, we open inputFile.txt
# f = open('inputFile.txt','r')

# # then, we create passFile.txt for writing those students that have passed the exams
# passFile = open('passFile.txt','w')
# # Here we create failFile.txt for store those students that have failed the exams
# failFile = open('failFile.txt','w')

# # here we go through f with a for loop and print only those lines that contains a "P" that indicates that studens pass the exams
# for row in f:
# 	row_split = row.split()		# split() method returns a list of strings after breaking the given string by the specified separator

# 	if row_split[2] == 'P':
# 		passFile.write(row)		# here we write on passFile.txt those lines that contains a "P"

# 	if row_split[2] == 'F':
# 		failFile.write(row)

# #closing the inputFile
# f.close()
# # after operation, we close passFile.txt
# passFile.close()
# after store information on it, we close failFile.txt
# failFile.close()

#----------------------------------------------------------------------------------------------

# import os
# import shutil # this module allow us to move, copy, rename or delete files or folders from our file system

# # the following instruction store in "directorio_actual" the current work directory
# directorio_actual = os.getcwd()

# # creates a folder named "python_codes"
# # os.makedirs('python_codes')
# # this instruction will return True or False, depending whether the directory exists or not in the location where we are
# print(os.path.isdir('python_codes'))
# # Returns the size of the file between single quotes
# print(os.path.getsize('inputFile.txt'))
# # returns list with all files and directories from the location where we are
# print(os.listdir())
# # returns list with all files and directories from the path 
# print(os.listdir('C:\\wamp'))
# the following sentence copies a file from the directory where we are to another place indicated by a path
# shutil.copy('passFile.txt','C:\\Users\Bangho 5\Desktop\Zorro\Programación')
# moves a file from the directory where we are to another indicated location: shutil.move('file','location')
# shutil.move('passFile.txt','python_codes')

# the following instruction removes a file from the indicated location
# os.unlike('python_codes\\file')
# To delete a folder, we use the following instruction. We can't delete folders that aren't empty
# os.rmdir('borrar')
# To delete a tree (folders that contains files and/or another folders) we use the following instruction
# shutil.rmtree('')

# -------------------------------------------------------------------------------------------------------

# as though ---------------->  como si

# web scraping
# creating a request and parsing

# import requests
# from bs4 import BeautifulSoup 		# BeautifulSoup is a data structure representing a parsed HTML or XML document.

# # url of the page to be scraped
# url = 'http://quotes.toscrape.com/'
# # The requests made is stored in response
# response = requests.get(url)
# # parsed document is stored in soup
# soup = BeautifulSoup(response.text, 'lxml')

# print(soup)

# -----------------------------------------------------------------------------------------
# XML ----------------------->  eXtensible Markup Language
# HTML ---------------------->  
# The difference between XML and HTML is:
#   - XML was designed to carry data - with focus on what data is
#   - HTML was designed to display data - with focus on how data looks


# import requests
# from bs4 import BeautifulSoup 		# BeautifulSoup is a Python library for pulling data out of HTML and XML files.

# # url of the page to be scraped
# url = 'http://quotes.toscrape.com/'
# # The request made is stored in response
# response = requests.get(url)
# # we store the XML content of the web page into the BS object
# soup = BeautifulSoup(response.text, 'lxml')
# # will show the page title
# # print(soup.title)
# # will print the text content of the page
# # print(soup.get_text())
# # do the same thing that "get_text()" 
# # print(soup.text)

# # we store the soup.find_all('span',class_ = 'text') content in quotes. find_all('tag', class_='class')
# quotes = soup.find_all('span',class_ = 'text')
# # we store the soup.find_all('small',class_='author') content in authors. find_all('tag', class_='class')
# authors = soup.find_all('small',class_='author')
# # we store the soup.find_all('div', class_='tags') content in tags. find_all('tag', class_='class')
# tags = soup.find_all('div', class_='tags')
# # here we create a doc.txt to store the text content of requests made previously
# # phrases = open('doc.txt', 'w')

# for i in range(0,len(quotes)):
#     print(quotes[i].text)
#     # phrases.write(str(quotes[i].text))
#     print(authors[i].text)
#     quoteTags = tags[i].find_all('a',class_='tag')
#     for quoteTag in quoteTags:
#         print(quoteTag.text)

# here we close "phrases"
# phrases.close()

#-----------------------------------------------------------------------------------------------
# PAGINATED SCRAPING

# # import BeautifulSoup from bs4
# from bs4 import BeautifulSoup
# # import requests library
# import requests
# # url from the page to be scraped
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# # here we store in response the request made to the url
# response = requests.get(url)
# # then, we parse the response (text content) 
# soup = BeautifulSoup(response.text, 'lxml')

# # we store in "items" the results of find_all for "div" tag and "col-lg-4 col-md-6 mb-4" class
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# # we set a counter to 1 to make a list of the displayed items
# count = 1

# # in a for loop we display the name and the price of each item.
# for i in items:
#     itemName = i.find('h4',class_='card-title').text.strip('\n')    # it stores in "itemName" the content of "i.find().text" instruction. "strip(\n)" allows to delete the following large blank space
#     itemPrice = i.find('h5').text                                   # it stores in "itemPrice" the content of "i.find().text" instruction
#     print('%s )  Price: %s  Item: %s' % (count, itemPrice, itemName))       # here we print the scraping results in the format given there

#     count = count + 1

#-------------------------------------------------------------------------------------------------------------------
# Multi page scraping

# # import BeautifulSoup from bs4
# from bs4 import BeautifulSoup
# # import requests library
# import requests
# # url from the page to be scraped
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# # here we store in response the request made to the url
# response = requests.get(url)
# # then, we parse the response (text content) 
# soup = BeautifulSoup(response.text, 'lxml')

# pages = soup.find('ul', class_='pagination')

# urls = []

# links = soup.find_all('a', class_='page-link')

# for link in links:
#     pageNum = int(link.text) if link.text.isdigit() else None
#     if pageNum != None:
#         x = link.get('href')
#         urls.append(x)
#         # print(urls)

# # print(urls)

# # we set a counter to 1 to make a list of the displayed items
# count = 1

# for i in urls:
#     newUrl = url + i
    
#     response = requests.get(newUrl)
#     soup = BeautifulSoup(response.text, 'lxml')

#     # we store in "items" the results of find_all for "div" tag and "col-lg-4 col-md-6 mb-4" class
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

#     # in a for loop we display the name and the price of each item.
#     for i in items:
#         itemName = i.find('h4',class_='card-title').text.strip('\n')    # it stores in "itemName" the content of "i.find().text" instruction. "strip(\n)" allows to delete the following large blank space
#         itemPrice = i.find('h5').text                                   # it stores in "itemPrice" the content of "i.find().text" instruction
#         print('%s )  Price: %s  Item: %s' % (count, itemPrice, itemName))       # here we print the scraping results in the format given there

#         count = count + 1               


#----------------------------------------------------------------------------------------------
# Automating web browwing with Selenium
# Basic browser interactions

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions. This is useful for doing more complex actions like hover over and drag and drop

# here we create the driver for manage the Chrome browser
driver = webdriver.Chrome()
# here we maximize the window
driver.maximize_window()
# then we go to the page where we want to work
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# we sleep the program to give the page time to complete its content
time.sleep(5)
# here we store the result of the search (using xpath) in messageField
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# then, we send the sentence beteen quotes by send_keys()
messageField.send_keys("Hello World")
# here, we store the xpath of a button in "show Message Button" to click on it
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
# here, we store the xpath of a blank field in "additionField1" to send a number
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('100')
# here, we store the xpath of a blank field in "additionField2" to send a number
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('100')

showResult = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
showResult.click()

#-------------------------------------------------------------------------------------------------
# Handling drag and drop with Selenium

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains  # ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions. This is useful for doing more complex actions like hover over and drag and drop

# driver = webdriver.Chrome()

# driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# driver.maximize_window()

# time.sleep(5)

# source = driver.find_element_by_xpath('//*[@id="box3"]')
# dest = driver.find_element_by_xpath('//*[@id="box103"]')

# actions = ActionChains(driver)
# actions.drag_and_drop(source, dest).perform()

#-------------------------------------------------------------------------------------------------------
# Selenium explicit wait functions

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# url = 'https://www.google.com.ar/earth/'

# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()

# wait = WebDriverWait(driver, 10)
# launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
# launchEarthButton.click()

#----------------------------------------------------------------------------------------------------------
#Automating with APIs

# import requests
# import json

# baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'

# parameters = {'upc' : '073366118238'}

# response = requests.get(baseUrl, params=parameters)

# print(response.url)

# content = response.content
# info = json.loads(content)
# item = info['items']
# itemInfo = item[0]
# title = itemInfo['title']
# brand = itemInfo['brand']
# print(title)
# print(brand)
# # print(type(info))
# # print(info)

#----------------------------------------------------------------------------------
# Using API keys

# import requests

# baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
# parameters = {'APPID' : '0c27fe88a716c808168a7e0268ef47e1' , 'q' : 'Seattle, US'}

# response = requests.get(baseUrl, params=parameters)

# print(response.content)

# ---------------------------------------------------------------------------------------
# Go to see https://rapidapi.com/ for 

# Ejercicio 1 - Funcion retorna alumnos aprobados
# Escribir una función que reciba una diccionario con las notas de los alumnos y retorne una serie con las notas de aquellos aprobados ordenadas 
# de mayor a menor.

# import pandas as pd

# def aprobados(notas):
#     aprobados=[]
#     for nota in notas:
#         if notas[nota]>6:
#             aprobados.append(notas[nota])
    
#     ordenados=pd.Series(sorted(aprobados))
#     return(ordenados)


# # Implementación

# notas = {'Deadpool':9, 'Wolverine':6.5, 'Spidy':4, 'Dopinder': 8.5, 'Weasel': 5}

# aprobados(notas)

# print(aprobados(notas))


# Ejercicio 2 - Función que cree y muestre un DataFrame
# Escribir una función que liste los doce meses calendario de 2019 con ventas, gastos y neto obtenido. 
# Usar diccionarios y asignar valores aleatorios (De forma manual o con funciones). Usar la función plot para graficar el 
# contenido de un DataFrame.

# import pandas as pd

# anual = {'Enero':[], 'Febrero':[], 'Marzo':[], 'Abril':[], 'Mayo':[], 'Junio': [],
#         'Julio':[], 'Agosto':[], 'Septiembre':[], 'Octubre':[], 'Noviembre':[], 'Diciembre':[]}

# for meses in anual:
#   band1 = 0
#   while band1 != 1:
#     ventas = float(input("Ingrese el valor de las ventas: "))
#     if ventas < 0:
#       print("Error, ingrese un valor válido")
#     else:
#       band1 = 0

# print ()

