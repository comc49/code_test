#!/usr/bin/env python 3.3
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from lettuce import *

f1=open('./testfile', 'w+')
#@before.all
#def setup_browser():
#    world.browser = webdriver.Firefox()

@step('I am at "(.+)"')
def go_to_url(step, url):
   print "SUP"
   #global world
   #world.browser.get(url)

@step('I enter username as "([\w\d]+)"')
def enter_user_name(step, user_name):
   #print >>f1,"YOOOOOOOOO"
   #global world
   #global f1
   #world.browser.get("http://sendgrid.com/docs/api_workshop.html")
   #select = world.browser.find_element_by_xpath("//div[@id='controls']")
   #print>>f1, select.find_element_by_xpath(".//a[@id='toggle-methods']").text

   driver = webdriver.Firefox()
   driver.get("http://sendgrid.com/docs/api_workshop.html")
   driver.find_element_by_id('header-top').find_element_by_tag_name("a").click()
   driver.find_element_by_id('login_username').send_keys("comc49")
   driver.find_element_by_id('login_password').send_keys("sendgridcodetest")
   #driver.find_element_by_class_name('submit button').find_element_by_tag_name("input").click()
   driver.find_element_by_class_name('button-inner').click()
   driver.implicitly_wait(3)
   driver.get("http://sendgrid.com/docs/api_workshop.html")
   driver.implicitly_wait(1)

   #select2 = select.find_elements_by_tag_name("body")
   #select3 = select2.find_elements_by_tag_name("div")
   #select4 = select3.find_elements_by_tag_name("div")
   #select5 = select4.find_elements_by_tag_name("div")
   #select6 = select5.find_elements_by_tag_name("article")
   #select7 = select6.find_elements_by_tag_name("iframe")
   #clicked = world.browser.find_elements_by_id("logo").click()
   #allOptions = select.find_element_by_id("toggle-methods")
   #for option in select:
   #       print >>f1, "Value is: " + option.get_attribute("id") 
   #       print >>f1, "Value is: " + option.get_attribute("text") 
   #       print >>f1, "Value is: " + option.get_attribute("class") 
   #       option.click()
   #world.browser.find_element_by_id("key")

#@step('I enter password as "sendgridcodetest"')
#def

#@step('I click "Expand Methods" for mail api method')
#def click_expand(step):
#   global world
   #world.browser.find_element_by_id("toggle-methods").click

@step('I fill in parameter "to" as "bkoo004@ucr.edu"')
def fill_in_to(step, field, email):
   print >> f1, field + " " + email

#@step('I fill in parameter "toname" as "Bob"')
#def
#@step('I fill in parameter "x-smtpapi" as '{ "category": "newuser" }'')
#def
#@step('I fill in parameter "fromname" as "Brian"')
#def
#@step('I fill in parameter "subject" as "testing"')
#def
#@step('I fill in parameter "text" as "hi this is a test mail"')
#def
#@step('I fill in parameter "html" as "sup"')
#def
#@step('I fill in parameter "bcc" as "comc39@naver.com"')
#def
#@step('I fill in parameter "date" as "Thu, 17 Apr 2014 20:51:52 -0700"')
#def
#@step('I fill in parameter "headers" as '')
#def
#@step(' I fill in parameter "files" as "files[file1.doc]=example.doc"')
#def
#@step('I click "Try it!" button')
#def
#@step('I should see "success" in the response body')
#def
#browser.get('http://ilearn.ucr.edu')
#browser.close()
