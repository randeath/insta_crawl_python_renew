from libs.crawler import crawl

url = "https://www.instagram.com/"

pageString = crawl(url)
print(pageString)
