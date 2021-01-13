from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from twilio.rest import Client
from selenium.webdriver.chrome.options import Options
import requests
import json
from datetime import datetime as dt
import sys

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe" #Path to Brave
options.headless = True
driver = webdriver.Chrome(executable_path = "C:/Users/skaranzx16/Downloads/chromedriver_win32/chromedriver.exe", options = options)
driver.maximize_window()
driver.get('https://event.webinarjam.com/live/80/q75q1t82uvrb5wkfo04') #paste video link here
time.sleep(1)

client = Client() #account_sid, auth_token
linkList = []

def login():
    try:
        driver.find_elements_by_class_name("form-control")[0].send_keys(sys.argv[0]) #enter name here
        driver.find_element_by_name("email").send_keys(sys.argv[1]) #enter e-mail address here

    except:
        driver.find_elements_by_class_name("form-control")[0].send_keys('sreekaran')
        driver.find_element_by_name("email").send_keys('sreekaran.srinath@gmail.com')

    driver.find_element_by_id("register_btn").click() #Submit Button
    print(f'Logged In - {dt.now()}')

def findLink(xpath):
    try:
        message = driver.find_element_by_xpath(xpath).text
        print(message)
        if '.com' in message.text or 'forms' in message.text or 'tinyurl' in message.text:
            if message.text not in linkList:
                print(f"Found attendance link - {dt.now()}")
                message = client.messages.create(from_ = 'whatsapp:+14155238886', body = message, to = f'whatsapp:+91enteryournumberhere')
                requests.post('https://discordapp.com/api/webhooks/enteryourwebhooklinkhere', data=json.dumps({'content': message, 'username': 'Attendance Link'}), headers={"Content-Type": "application/json"})
                linkList.append(message.text)

            else:
                print(f"No new link found - trying again - {dt.now()}")
            
    except Exception as e:
        print(f"No message in xpath {xpath} found. Exception {str(e)} occurred. Trying again in 1 second - {dt.now()}")

    time.sleep(1)

login()
while 1:
    findLink('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/span/a')
    findLink('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li[1]/div[1]/div[2]')
    findLink('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li/div[1]/div[2]')
    #         /html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li/div[1]/div[2]
    #         /html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li/div[1]/div[2]
