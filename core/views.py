from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from time import sleep
from selenium import webdriver
import time
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
from . import loginInfo
# Create your views here.
import requests
import json

def home(request):
	return render(request, 'core/home.html')

def profile(request):

	try:		
		# browser = webdriver.Firefox()
		# browser.implicitly_wait(5)

		# browser.get('https://www.instagram.com/')

		# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
		# login_link.click()

		# sleep(2)

		# username_input = browser.find_element_by_css_selector("input[name='username']")
		# password_input = browser.find_element_by_css_selector("input[name='password']")

		# username_input.send_keys("yabesh__")
		# password_input.send_keys("Yabesh@12")

		# login_button = browser.find_element_by_xpath("//button[@type='submit']")
		# login_button.click()

		# sleep(5)

		# browser.close()


  
		  
		usr="samyabeshv@gmail.com" 
		pwd="Yabesh@12" 
		  
		driver = webdriver.Chrome(ChromeDriverManager().install()) 
		driver.get('https://www.instagram.com/') 
		print ("Opened instagram") 
		sleep(1) 
		  
		username_box = driver.find_element_by_name('username')
		username_box.send_keys(usr) 
		print ("Email Id entered") 
		sleep(1) 
		  
		password_box = driver.find_element_by_name('password')
		password_box.send_keys(pwd) 
		print ("Password entered") 
		login_box = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div") 
		login_box.click() 
		  
		print ("Done") 
		# input('Press anything to quit') 
		# driver.quit() 
		# print("Finished") 
		return HttpResponse("Profile")
	except Exception as e:
		raise e
	else:
		pass
	finally:
		pass