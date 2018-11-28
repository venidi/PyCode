from selenium import webdriver

browser = webdriver.Chrome('E:\chromedriver\chromedriver.exe')

browser.get(r'https://tuchong.com/tags/%E5%B0%91%E5%A5%B3')
print(browser.page_source)
browser.execute_script('alert("To Bottom")')
browser.close()