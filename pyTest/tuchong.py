from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')

browser.get(r'https://www.zhihu.com/question/20796474')
# print(browser.page_source)
# browser.execute_script('alert("To Bottom")')

links = browser.find_elements_by_xpath(r'//*[@id="QuestionAnswers-answers"]/*/*/*/*/*/*/*/*/*/*/img')

# print(links.get_attribute('s'))
print(links)
for link in links:
    print(link.get_attribute('src'))
# browser.close()


