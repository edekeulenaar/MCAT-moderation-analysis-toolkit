from selenium import webdriver
import time, csv, codecs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from random import randint


class xSearch:
    driver = None
    max_tweets=20
    min_delay=2
    max_delay=10
    def __init__(self, username, password, max_tweets=20, min_delay=2, max_delay=10):
        options = webdriver.ChromeOptions()
        
        #start zoomed out, to get more tweets per page
        options.add_argument("force-device-scale-factor=0.95");
        options.add_argument("high-dpi-support=0.95");
        self.driver = webdriver.Chrome(options)
        
        self.login(username, password)
        self.max_tweets = max_tweets
        self.min_delay = min_delay
        self.max_delay = max_delay
    
    def login(self, username, password):
        self.driver.get('https://twitter.com/i/flow/login')
        
        wait = WebDriverWait(self.driver, 30)

        username_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
        )
        username_element.send_keys(username)

        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
        )
        login_button.click()

        password_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
        )
        password_element.send_keys(password)

        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
        )
        login_button.click()

        direct_message_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]'))
        )

    def search(self, term, lang="en"):
        url = "https://x.com/search?lang=%s&q=%s&src=typed_query" % (lang, term)
        self.driver.get(url)
        time.sleep(3)
        
        
        
        for i in range(0,4*self.max_tweets):
            #zoom out
            self.driver.execute_script("document.body.style.zoom='zoom 20'")
            
            #Get middle element
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            section = soup.find('section')
            superdiv = section.find('div').find('div')
            #Start recording only when we have skipped the "people" results at the top
            start = False
            tweets=[['ranking','text']]
            for ranking, div in enumerate(superdiv.findAll('div', recursive=False)):
                if div.text.strip() == "View all":
                    start = True
                if not [ranking, div.text.strip()] in tweets:
                    tweets.append([ranking, div.text.strip()])
            
                if len(tweets) > self.max_tweets:
                    break
            print(i, " iterations,", len(tweets),'tweets')
        
            if len(tweets) > self.max_tweets:
                break
            
            #Scroll down the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(randint(self.min_delay,self.max_delay))
        with codecs.open("tweets_%s_%s_%s.csv" % (term, lang, self.max_tweets), "w", encoding='utf-8') as f:
            w=csv.writer(f, delimiter=';')
            w.writerows(tweets)
            
        
        

if __name__ == '__main__':
    #note: X may ask you for your username if it detects many quick sequential logins.
    #The script is fragile in that if you load data too quickly, it will just throw an error and stop loading tweets. So you'll need to keep an eye on it
    searcher = xSearch(username = "YOUR_EMAIL", password="YOUR_PASSWORD", max_tweets=20, min_delay=2, max_delay=14)
    
    language = "en"
    for keyword in ["trump","melania"]:
    
        searcher.search(keyword,"en")