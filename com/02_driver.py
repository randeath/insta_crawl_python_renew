from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../webdriver/chromedriver"
)

url = "https://www.instagram.com/explore/tags/%EB%B0%9C%EB%A0%88/"
driver.get(url)
# driver.close()
