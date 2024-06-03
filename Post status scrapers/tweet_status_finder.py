from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv, codecs


class tweetStatusFinder:
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome()


    def checkTweet(self, tweetId):
        self.driver.get('https://x.com/DonaldJTrumpJr/status/%s' % tweetId)
        time.sleep(3)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        results = []
        for a in soup.findAll('article'):
            results.append(a.text)
        
        #seems to always be second element, this needs thorough testing though
        return results[1]
    def close(self):
        self.driver.close()

if __name__ == "__main__":
    tweetids = ['1324425447548047361', '1792963675097313565']
    
    outfile="test.csv"
    
    statusFinder=tweetStatusFinder()
    
    out=[['tweetId','result']]
    
    for i, tweetId in enumerate(tweetids):
        if i % 10 == True:
            print("%s/%s" % (i, len(tweetids)))
        res = statusFinder.checkTweet(tweetId)
        out.append([tweetId, res.strip()])
        
    statusFinder.close()
    with codecs.open(outfile, 'w', encoding='utf-8') as f:
        w=csv.writer(f, delimiter=';')
        w.writerows(out)