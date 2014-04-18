#!/usr/bin/env python
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from lettuce import *

f1=open('./testfile', 'w+')
@before.all
def setup_browser():
    world.browser = webdriver.Firefox()

@step('I am at "(.+)"')
def go_to_url(step, url):
   global world
   world.browser.get(url)

@step('I enter username as "([\w\d]+)"')
def enter_user_name(step, user_name):
   global world
   world.browser.find_element_by_id('key').send_keys(pw)


@step('I enter password as "([\w]+)"')
def enter_pw(step, pw):
   global world
   world.browser.find_element_by_id('secret').send_keys(pw)

@step('I click "Expand Methods" for mail api method')
def click_expand(step):
   global world
   world.browser.find_element_by_id("toggle-methods").click

@step('I fill in parameter "([\w]+)" as "([\w]+@[\w]+.[\w]+)"')
def fill_in_to(step, field, email):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[1]/x:td[2]/x:input")
   form.send_keys(email)
@step('I fill in parameter "([\w]+)" as "([\w]+)"')
def fill_in_toname(step, field, name):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[2]/x:td[2]/x:input")
   form.send_keys(name)
   
@step('I fill in parameter \'(.+)\'')
def fill_in_smtpapi(step, field, smtpapi):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[3]/x:td[2]/x:input")
   form.send_keys(smtapi)

@step('I fill in parameter "([\w]+)" as "([\w]+@[\w]+.[\w]+)"')
def fill_in_from(step, field, from_email):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[4]/x:td[2]/x:input")
   form.send_keys(from_email)

@step('I fill in parameter "([\w]+)" as "([\w]+)"')
def fill_in_fromname(step, field, fromname):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[5]/x:td[2]/x:input")
   form.send_keys(fromname)

@step('I fill in parameter "([\w]+)" as "([\w]+)"')
def fill_in_subject(step, field, subject):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[6]/x:td[2]/x:input")
   form.send_keys(subject)

@step('I fill in parameter "([\w]+)" as "(.+)"')
def fill_in_text(step, field, text):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[7]/x:td[2]/x:input")
   form.send_keys(text)


@step('I fill in parameter "([\w]+)" as ')
def fill_in_html(step, field, html_text):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[8]/x:td[2]/x:input")
   form.send_keys(html_text)

@step('I fill in parameter "([\w]+)" as "([\w]+@[\w]+.[\w]+)"')
def fill_in_bcc(step, field, bcc_email):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[9]/x:td[2]/x:input")
   form.send_keys(bcc_email)

@step('I fill in parameter "([\w]+)" as "([\w]+, [\d]+ [\w]+ [\w]{4} [\d]{2}:[\d]{2}:[\d]{2} -[\d]{4})"')
def fill_in_date(step, field, date):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[10]/x:td[2]/x:input")
   form.send_keys(date)

@step('I fill in parameter "headers" as \'(.+)\'')
def fill_in_headers(step, field, headers):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[11]/x:td[2]/x:input")
   form.send_keys(headers)

@step(' I fill in parameter "([\w]+)" as "(.+)"')
def fill_in_files(step, field, file_list):
   global world
   form = world.browser.find_element_by_xpath("id('body-container')/x:ul/x:li[6]/x:ul/x:li/x:form/x:table/x:tbody/x:tr[12]/x:td[2]/x:input")
   form.send_keys(file_list)


@step('I click "(.+)" button')
def click_to_send(step,button_name):
   global world
   world.browser.find_element_by_id("Mail")


@step('I should see "(.+)" in the response body')
def sent_sucessfully(step, keyword):
   global world 
   response = world.browser.find_element_by_class_name("response prettyprint error")
   response_body = response.browser.find_elements_by_class_name("pun")
   for span in response_body:
      if span.match("success") == "success":
         print "Mail sent correctly"
      else:
        raise Exception("Mail did not send correctly")



#code for logging into sendgrid
#I thought after logging in I will be able to access the elements but that did not work
   #driver = webdriver.Firefox()
   #driver.get("http://sendgrid.com/docs/api_workshop.html")
   #driver.find_element_by_id('header-top').find_element_by_tag_name("a").click()
   #driver.find_element_by_id('login_username').send_keys("")
   #driver.find_element_by_id('login_password').send_keys("")
   #driver.find_element_by_class_name('button-inner').click()
   #driver.implicitly_wait(3)
   #driver.get("http://sendgrid.com/docs/api_workshop.html")
   #driver.implicitly_wait(1)
