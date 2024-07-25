
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome()
comments = [ "A glacier is a slowly moving mass of ice. It forms from compacted snow that has accumulated over many years and often millions of years",
"Glaciers are vast, inescapable forces of nature that shaped the earth ecosystems for thousands of years.","They have the power to breathe new life into the world or to wipe out entire civilizations and forests obliterating everything in sight.",
"The glaciers are melting and I can not help but think this is just the beginning of the end.","I am glad I was there to witness the beauty of the glaciers before they disappeared forever.",
"We need to do something about global warming before its too late and all the glaciers disappear forever!","I love you like I love the glaciers, which is to say a lot because they are beautiful and delicate but also powerful and strong!",
"I can not believe we are finally here!","This place is breathtaking, literally!","I have never seen anything like this before!","Its like a dream come true!"]

from time import sleep
import random 
driver.get('https://www.instagram.com')
sleep(1)
username = driver.find_element("name","username")
password = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
username.send_keys('xyz')
password.send_keys('xyz')
password.submit()
sleep(5)
clicknotnow = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
clicknotnow.click()
sleep(5)
offnotifications = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
offnotifications.click()
sleep(5)
driver.get("https://www.instagram.com/explore/tags/glaciers/")
sleep(5)
post1 = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
post1.click()
sleep(5)
like = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
like.click()
sleep(5)
savepost = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button/div[2]")
savepost.click()
sleep(5)
comment = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
comment.click()
comment = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
comment.click()
comment.send_keys(random.choice(comments))
sleep(3)
postit = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div[2]/div")
postit.click()
sleep(1)
nextpost = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div")
nextpost.click()
sleep(5)
like = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
like.click()
sleep(5)
savepost2 = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button/div[2]")
savepost2.click()
sleep(5)
nextpost2 = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
nextpost2.click()
sleep(5)
driver.quit()


