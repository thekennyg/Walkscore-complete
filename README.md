
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

By default, the script opens 'sample.csv', then gets the address from column 'Match_addr'. You can edit main.py to change the names.

The script grabs the following score types: walk, bike, transit. It then creates a timestamped folder of when the script was run with graphs for each address.
It will then write the scores in a timestamped copy of the original csv file but with the scores.


# Important
Due to the absence of a WalkScore API and rate limits, the script cannot return all csv lines in one go. I have tested that ~50/60% of the csv file will run, and the remainder will be placed in the recheck.csv file. You can then copy this to put it back in the sample.csv file to recheck. This is due to the fact that the script cannot infinitely loop until the asyncronous timer ends.



![App Screenshot](https://i.ibb.co/XZrBkZG/new.jpg)
![App Screenshot](https://i.ibb.co/3zvYpGR/ewven-newer.jpg)
