from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import os


search = input("검색할 내용을 입력해 주세요")
if search != "" :

    url = "https://www.instagram.com/explore/tags/" + search + "/"
    driver = webdriver.Chrome(
        executable_path="../webdriver/chromedriver"
    )
    driver.get(url)
    ## 인스타그램 열기 ##

    sleep(4) #웹페이지 기다려주는 시간
    elem = driver.find_elements_by_class_name('_2hvTZ.pexuQ.zyHYP')
    elem[0].send_keys('randeath2')
    elem[1].send_keys('Trust927!')
    sleep(1)
    elem[1].send_keys(Keys.ENTER)
    sleep(7)
    driver.get(url)


    pageString = driver.page_source

    print(pageString)

    #인스타 껍데기
    #인스타 내용<div class="Nnq7c aaa">
    # driver.close()
