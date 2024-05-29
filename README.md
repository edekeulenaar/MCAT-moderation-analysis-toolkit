# MCAT

MCAT (Moderation Capture and Analysis Toolkit) is a collection of Python functions that collect and analyse platform moderation policies and practices. 

Current scripts use Selenium to collect moderation statuses from Facebook, Instagram and YouTube posts listed in a local CSV. Moderation statuses include "This post is not available" or "This post has been removed for [x] policy infringement." As they are scrapers, these scripts are subjet to very frequent changes -- so please do expect errors.

Future functions should include: 
- Collecting and analysing platform policies from the Platform Governance Archive (v. 1 and 2) and other datasets from peer-reviewed research;
- Verifying if a search term is labelled or banned by TikTok;
- Getting tweet and other post rankings for a given search;

and more.

# Installation and requirements

1.	**Python**: Ensure that Python is installed on the system. You can download it from [python](www.python.org).
   
2.	**Pandas**: Install the Pandas library for data manipulation. Open your command line (e.g. Terminal) and type:

      ```pip install pandas```

3.	**Selenium**: Install the Selenium library for web automation. Open your command line (e.g. Terminal) and type:

      ```pip install selenium```
  	
4.	**BeautifulSoup4**: Although not used in your script, it’s good to have for any future HTML parsing. Open your command line (e.g. Terminal) and type:

      ```pip install beautifulsoup4```

5.	**Chrome WebDriver**: Download the Chrome WebDriver that matches the version of Chrome installed on your system. You can download it from ChromeDriver - WebDriver for Chrome. Ensure that the ```chromedriver``` executable is in your system’s PATH or specify its location in the script.

6. **Homebrew** (if not already installed). Open your command line (e.g. Terminal) and type:

   ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```      
   
8.	**Chrome** (if not already installed). Download it from your browser or open your command line (e.g. Terminal) and type:

      ```brew install --cask google-chrome```

Once you're set up, specify the path to your CSV and whether you'd like the script to process all CSVs from a folder or just one file. Please modify the script where indicated by comments (a comment looks like this: "# [comment]"). 

# Credits

Modules and methods have been co-developed by Open Intelligence Lab folk (Ivan Kisjes and myself), Frank Anemaet, and a little help from gpt-4o.
