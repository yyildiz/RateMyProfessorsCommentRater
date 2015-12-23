from selenium import webdriver
from multiprocessing import Process

def webd():
    while True:
        url = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1997063";
        class_name = "nothelpful"
        browser = webdriver.PhantomJS()
        browser.get(url)
        linkElem = browser.find_element_by_class_name(class_name)
        linkElem.click()
        browser.refresh()
        
for i in range(4):
    Process(target=webd).start()
