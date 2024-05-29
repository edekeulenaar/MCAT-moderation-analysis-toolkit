# MCAT

MCAT (Moderation Capture and Analysis Toolkit) is a collection of Python functions that collect and analyse platform moderation policies and practices. Modules and methods have been co-developed by Ivan Kisjes, Frank Anemaet, myself, and a little help from gpt-4o.

Current scripts use Selenium to collect moderation statuses from Facebook, Instagram and YouTube posts listed in a local CSV. Moderation statuses include "This post is not available" or "This post has been removed for [x] policy infringement." As they are scrapers, these scripts are subjet to very frequent changing -- so please do expect errors.

Just specify the path to your CSV and whether you'd like the script to process all CSVs from a folder or just one file. Please modify the script where indicated by comments (a comment looks like this: "# [comment]"). 

Future functions should possibly include: 
- Collecting and analysing platform policies from the Platform Governance Archive (v. 1 and 2) and other datasets from peer-reviewed research;
- Verifying if a search term is labelled or banned by TikTok;
- Getting tweet and other post rankings for a given search;
- and other.

# Installation and requirements

## Requirements for both MacOS and Windows:

1.	**Python**: Ensure that Python is installed on the system. You can download it from python.org.
2.	**Pandas**: Install the Pandas library for data manipulation.
pip install pandas
5.	**Selenium**: Install the Selenium library for web automation. pip install selenium
6.	**BeautifulSoup4**: Although not used in your script, it’s good to have for any future HTML parsing. pip install beautifulsoup4
7.	**Chrome WebDriver**: Download the Chrome WebDriver that matches the version of Chrome installed on your system. You can download it from ChromeDriver - WebDriver for Chrome. Ensure that the chromedriver executable is in your system’s PATH or specify its location in the script.

## Additional Steps for MacOS:
1.	**Install Homebrew** (if not already installed): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2.	**Install Chrome** (if not already installed): brew install --cask google-chrome
3.	**Install ChromeDriver**: brew install chromedriver
   
## Additional Steps for Windows:
1.	**Download and Install Chrome** (if not already installed) from Google Chrome.
2.	**Download ChromeDriver**:
–	Download the ChromeDriver from ChromeDriver - WebDriver for Chrome.
–	Unzip the downloaded file and place the chromedriver.exe in a known directory.
–	Add the directory containing chromedriver.exe to your system’s PATH environment variable.
