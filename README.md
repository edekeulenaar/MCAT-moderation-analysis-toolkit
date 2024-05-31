
# MCAT: Moderation Capture and Analysis Toolkit

MCAT is a collection of Python functions that collect and analyze platform moderation policies and practices.

Current scripts use Selenium to collect moderation statuses from Facebook, Instagram, and YouTube posts listed in a local CSV. Moderation statuses include "This post is not available" or "This post has been removed for [x] policy infringement." As they are scrapers, these scripts are subject to very frequent changes, so please do expect errors.

Future functions should include:
- Collecting and analyzing platform policies from the Platform Governance Archive (v. 1 and 2) and other datasets from peer-reviewed research;
- Verifying if a search term is labeled or banned by TikTok;
- Getting tweet and other post search rankings to study demotion;

and more.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/mcat.git
cd mcat
pip install -r requirements.txt
```

## Requirements

The `requirements.txt` file includes all necessary packages:

```
pandas
selenium
beautifulsoup4
```

### Additional Requirements

1. **Chrome WebDriver**: Download the Chrome WebDriver that matches the version of Chrome installed on your system. You can download it from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure that the `chromedriver` executable is in your system’s PATH or specify its location in the script.
2. **Homebrew** (if not already installed). Open your command line (e.g. Terminal) and type:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```      
3. **Chrome** (if not already installed). Download it from your browser or open your command line (e.g. Terminal) and type:
   ```bash
   brew install --cask google-chrome
   ```

## Post Status Scrapers

The post status scrapers collect moderation statuses from Facebook, Instagram, and YouTube posts listed in a local CSV. 

### Usage

Specify the path to your CSV and whether you'd like the script to process all CSVs from a folder or just one file. Please modify the script where indicated by comments.

**Run the script:**

Execute the script with Python:

    ```bash
    python textdiff_calculator.py
    ```

or run it with your local script editor. 

## TextDiff Calculator

This script calculates the absolute and relative text differences between rows in a policy CSV file or between policy markdown files. It can handle text differences over specified time intervals (day, week, month, or year).

### Features

- Calculates text differences for a specified column in one or several CSV files stored in the current repository directory.
- Calculates text differences for markdown files in the current repository directory.
- Outputs a CSV with original columns plus additional columns for text differences, time intervals, and changes (text removals and additions per time interval).

### Usage

1. **Edit the script to specify your input type, file path, and parameters.**

    Open `textdiff_calculator.py` and modify the following lines as per your requirements:

    ```python
    if __name__ == "__main__":
        # Directly specify your input CSV or markdown directory and parameters here
        input_type = "markdown"  # choose "markdown" or "csv" depending on what kind of policy files you want to process
        input_path = "path/to/your/file/or/folder/with/files"  # path to your CSV file or Markdown format directory

        if input_type == "csv":
            date_column = "Date"  # Specify what the column with dates is called
            text_column = "Text"  # Specify what the column with text is called
            time_interval = "week"  # Choose day, week, month, or year for text differences
            process_csv(input_path, date_column, text_column, time_interval)
        elif input_type == "markdown":
            time_interval = "week"  # Ensure the time interval is consistent
            process_markdown_files(input_path, time_interval)
    ```

2. **Run the script:**

Execute the script with Python:

    ```bash
    python textdiff_calculator.py
    ```
or run it with your local script editor. 

## Methods

Methods and scripts have been written, brainstormed, or appeared in Lao Tzu-like dreams of members of Open Intelligence Lab and the Digital Methods Initiative, collaborators from various universities (University of Groningen, University of Bremen, PUC Rio, Sciences Po Média Lab), Frank Anemaet, and a little help from GPT-4.

### Origin of Methods

```
de Keulenaar, E. and Rogers, R. (2024) ‘After deplatforming: the return of trace research for the study of platform effects’, in T. Venturini et al. (eds) The SAGE Handbook of Data and Society: An Interdisciplinary Reader in Critical Data Studies. London: SAGE (to be published in June of 2024).
```

**Please cite this piece when using any of these scripts**.

The majority of moderation policies available in the "Content moderation policies" folder have been made available by the Open Terms Archive and the Platform Governance Archive(s), the latter of which is maintained by the University of Bremen. Please cite them when using policies tagged as "PGA" as follows:

```
Katzenbach, C., et al. (2023). The Platform Governance Archive. Centre for Media, Communication and Information Research (ZeMKI), University of Bremen. DOI: 10.17605/OSF.IO/XSBPT. URL: https://platformgovernancearchive.org.
```

## More Platform Policy Datasets

For now, MCAT focuses specifically on Community Guidelines. The Open Terms Archive and the Platform Governance Archive have a lot more to offer. Check out:

 1. The [Open Terms Archive datasets](https://opentermsarchive.org/en/datasets/), including for [Generative AI](https://github.com/openTermsArchive/GenAI-versions/releases/tag/dataset-GenAI-2024-05-27), [P2B Compliance](https://github.com/openTermsArchive/p2b-compliance-versions/releases/tag/dataset-p2b-compliance-2024-05-27), [online dating](https://github.com/openTermsArchive/dating-versions/releases/tag/dataset-dating-2024-05-27), French [elections](https://github.com/openTermsArchive/france-elections-versions/releases/tag/dataset-2022-09-28) and [digital services](https://github.com/openTermsArchive/france-versions/releases/tag/dataset-france-2024-05-27), and [other policies collected by volunteers](https://github.com/openTermsArchive/contrib-versions/releases/tag/dataset-contrib-2024-05-27).
 2. The Platform Governance Archive, namely [PGA v. 1](https://github.com/PlatformGovernanceArchive/pga-corpus/releases) (YouTube TOS, Facebook, Twitter, and Instagram circa 2005-2021) and [PGA v. 2](https://github.com/OpenTermsArchive/pga-versions) (everything from Bluesky to WeChat, 2021-ongoing).

Consider citing the PGA 1 archive as follows:
```
Dataset PGA v1 Katzenbach, C., Kopps, A., Magalhaes, J. C., Redeker.  D., Sühr, T. (2023). Platform Governance Archive (PGA) v1. [data set]. DOI: 10.17605/OSF.IO/XSBPT. URL: https://www.platformgovernancearchive.org/data/dataset-pga-v1-historical-dataset/.
```

and PGA 2:
```
Dataset PGAv2 Katzenbach, C., Dergacheva, D., Fischer, A., Kopps, A., Kolesnikov, S., Redeker. D., Viejo Otero, P. (2023). Platform Governance Archive (PGA) v2. [data set]. DOI: 10.17605/OSF.IO/XSBPT. URL: https://www.platformgovernancearchive.org/data/dataset-pga-v2-ongoing-collection/
```
