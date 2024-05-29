# MCAT

MCAT (Moderation Capture and Analysis Toolkit) is a collection of Python functions that collect and analyse platform moderation policies and practices. 

For now, current scripts use Selenium to collect moderation statuses from Facebook, Instagram and YouTube posts listed in a local CSV. Moderation statuses include "This post is not available" or "This post has been removed for [x] policy infringement." As they are scrapers, these scripts are subjet to very frequent changing -- so please do expect errors.

Just specify the path to your CSV and whether you'd like the script to process all CSVs from a folder, or just one file. Please modify the script accordingly where indicated by comments (a comment looks like this: "# [comment]"). 

If possible, future functions should include: 
- Collecting and analysing platform policies from the Platform Governance Archive (v. 1 and 2) and other datasets from peer-reviewed research;
- Verifying if a search term is labelled or banned by TikTok;
- Getting tweet and other post rankings for a given search;
- and other.

Requirements and instructions are listed in the README file. 
