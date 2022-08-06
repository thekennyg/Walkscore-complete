
# WalkScore Extraction

WalkScore Extraction by Kenny Li
#### This project was designed (happily) for Dr. Wu's research group.
## Installation
This script requires Python 3 to run. For best performance, download Python 3.10 found here: https://www.python.org/downloads/release/python-3105/.



This project **requires the installation of** prerequisites (aiohttp, numpy, matplotlib) in order to work properly.

To install the prerequisites run this command in terminal:

```
pip install numpy aiohttp matplotlib
```
Note that Python 3.10 should automatically have pip installed with it. If it isn't, read this: https://pip.pypa.io/en/stable/installation/


    
## Basic Usage
This script scrapes data from WalkScore's website. 

By default, the script opens 'input.csv', then gets the address from column 'Match_addr'. You can edit main.py to change the names.

The script grabs the following score types: walk, bike, transit. It then creates a timestamped folder and within that, a timestamped csv file with all the scores added. You can also uncomment some code to genereate graphs.

Note: Some scores may have 0 values in one of the score categories.
# Important
Scraping WalkScore should not have a large ratelimit. However, roughly <1% of the csv file will be skipped. The 'recheck.csv' file has all error generated csv lines (wrong address formatting, timeouts). You can simply copy and paste it back in input.csv to recheck them.

Addresses with no scores will always be put in the recheck.csv.

# Even more Important
If something along the lines of '[WinError 10053] An established connection was aborted by the software in your host machine' occurs, it is due to antivirus/firewall settings on your computer. Running it on my mac, i got through the sample file in a minute, but windows users may have to change some settings.
![App Screenshot](https://i.ibb.co/XZrBkZG/new.jpg)
![App Screenshot](https://i.ibb.co/3zvYpGR/ewven-newer.jpg)
![App Screenshot](https://i.ibb.co/dWSYr38/Screenshot-2022-08-03-at-4-11-07-PM.png)
