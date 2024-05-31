# MCAT: Moderation capture and analysis toolkit

MCAT is a collection of Python functions that collect and analyse platform moderation policies and practices. 

Current scripts use Selenium to collect moderation statuses from Facebook, Instagram and YouTube posts listed in a local CSV. Moderation statuses include "This post is not available" or "This post has been removed for [x] policy infringement." As they are scrapers, these scripts are subjet to very frequent changes -- so please do expect errors.

Future functions should include: 
- Collecting and analysing platform policies from the Platform Governance Archive (v. 1 and 2) and other datasets from peer-reviewed research;
- Verifying if a search term is labelled or banned by TikTok;
- Getting tweet and other post search rankings to study demotion;

and more.

# Installation and requirements

1.	**Python**: Ensure that Python is installed on the system. You can download it from [python](www.python.org).
   
2.	**Pandas**: Install the Pandas library for data manipulation. Open your command line (e.g. Terminal) and type:

      ```
  	pip install pandas
      ```

4.	**Selenium**: Install the Selenium library for web automation. Open your command line (e.g. Terminal) and type:

      ```
  	pip install selenium
      ```
  	
6.	**BeautifulSoup4** for HTML parsing. Open your command line (e.g. Terminal) and type:

      ```
  	pip install beautifulsoup4
      ```

8.	**Chrome WebDriver**: Download the Chrome WebDriver that matches the version of Chrome installed on your system. You can download it from ChromeDriver - WebDriver for Chrome. Ensure that the ```chromedriver``` executable is in your system’s PATH or specify its location in the script.

9. **Homebrew** (if not already installed). Open your command line (e.g. Terminal) and type:

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```      
   
11.	**Chrome** (if not already installed). Download it from your browser or open your command line (e.g. Terminal) and type:

      ```
   	brew install --cask google-chrome
      ```

Once you're set up, specify the path to your CSV and whether you'd like the script to process all CSVs from a folder or just one file. Please modify the script where indicated by comments (a comment looks like this: "# [comment]"). 

# Methods

Modules and methods have been co-developed by Open Intelligence Lab folk (Ivan Kisjes and myself), Frank Anemaet, and a little help from gpt-4o. 

Methods originate from: 

```
de Keulenaar, E. and Rogers, R. (2024) ‘After deplatforming: the return of trace research for the study of platform effects’, in T. Venturini et al. (eds) The SAGE Handbook of Data and Society: An Interdisciplinary Reader in Critical Data Studies. London: SAGE (to be published in June of 2024).
```

**Please cite this piece when using any of these scripts**. 

The majority of moderation policies available in the "Content moderation policies" folder has been made available by the Open Terms Archive and the Platform Governance Archive(s), the latter of which is maintained by the University of Bremen. Please cite them when using policies tagged as "PGA" as follows: 

```
Katzenbach, C., et al. (2023). The Platform Governance Archive. Centre for Media, Communication and Information Research (ZeMKI), University of Bremen. DOI: 10.17605/OSF.IO/XSBPT. URL: https://platformgovernancearchive.org.
```

# More platform policy datasets

For now, MCAT focuses specifically on Community Guidelines. The Open Terms Archive and the Platform Governance Archive have a lot more to offer. Check out: 

 1. The [Open Terms Archive datasets]([url](https://opentermsarchive.org/en/datasets/)), including for [Generative AI]([url](https://github.com/openTermsArchive/GenAI-versions/releases/tag/dataset-GenAI-2024-05-27)), [P2B Compliance]([url](https://github.com/openTermsArchive/p2b-compliance-versions/releases/tag/dataset-p2b-compliance-2024-05-27)), [online dating]([url](https://github.com/openTermsArchive/dating-versions/releases/tag/dataset-dating-2024-05-27)), French [elections]([url](https://github.com/openTermsArchive/france-elections-versions/releases/tag/dataset-2022-09-28)) and [digital services]([url](https://github.com/openTermsArchive/france-versions/releases/tag/dataset-france-2024-05-27)), and [other policies collected by volunteers]([url](https://github.com/openTermsArchive/contrib-versions/releases/tag/dataset-contrib-2024-05-27)).
 2. The Platform Governance Archive, namely [PGA v. 1]([url](https://github.com/PlatformGovernanceArchive/pga-corpus/releases)) (YouTube TOS, Facebook, Twitter and Instagram circa 2005-2021) and [PGA v. 2]([url](https://github.com/OpenTermsArchive/pga-versions)) (everything from Bluesky to WeChat, 2021-ongoing).

Consider citing the PGA 1 archive as follows: 
```
Dataset PGA v1 Katzenbach, C., Kopps, A., Magalhaes, J. C., Redeker.  D., Sühr, T. (2023). Platform Governance Archive (PGA) v1. [data set]. DOI: 10.17605/OSF.IO/XSBPT. URL: https://www.platformgovernancearchive.org/data/dataset-pga-v1-historical-dataset/.
```

and PGA 2: 
```
Dataset PGAv2 Katzenbach, C., Dergacheva, D., Fischer, A., Kopps, A., Kolesnikov, S., Redeker. D., Viejo Otero, P. (2023). Platform Governance Archive (PGA) v2. [data set]. DOI: 10.17605/OSF.IO/XSBPT. URL: https://www.platformgovernancearchive.org/data/dataset-pga-v2-ongoing-collection/
```
