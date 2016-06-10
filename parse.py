#!/usr/bin/env python3
import re
import requests

"""
This script parses the html from the echanted learning website and prints it to stdout.
We get about 20,000 words.
"""

ENCHANTED_LEARNING_BASE = "http://www.enchantedlearning.com/wordlist/"
FILETYPE = '.shtml'
WORD=r"^(\w+)<BR>$"
WORDLIST_LINK = r'^<a href="/wordlist/(\w+)\.shtml.*$'


def find_occurences(text, regex):
    return re.findall(regex, text, re.MULTILINE)

def getPages():
    """ get all possible pages from teh enchangtedlearning site """
    text = getPage("farm")
    return find_occurences(text, WORDLIST_LINK)

def getPage(wordPackName):
    """ fetch a page from the website """
    url = ENCHANTED_LEARNING_BASE + wordPackName + FILETYPE
    response = requests.get(url)
    # check for errors
    response.raise_for_status()
    return response.text

def getWords(wordPackName):
    """ parse a page to get the words """
    page = getPage(wordPackName)
    return find_occurences(page, WORD)

def showResults(header, data):
    print header
    print
    for line in data:
        print line

def scrapeAllWeCan():
    if not os.path.exists(RESULTS_DIR):
        os.mkdir(RESULTS_DIR)
    for page in getPages():
        words = getWords(page)
        header = '\n' + '*' * 20 + '\n' + page
        showResults(header, words)

RESULTS_DIR = "./word-data/"
def printInNiceFiles():
    import os
    import sys
    if not os.path.exists(RESULTS_DIR):
        os.mkdir(RESULTS_DIR)

    for page in getPages():
        words = getWords(page)
        outputFile = RESULTS_DIR + page + ".txt"
        # this prints an extra newline, which I subsequently removed with the perl script
        # perl -pi -e 'chomp if eof' filename
        with open(outputFile, 'w') as sys.stdout:
            for line in words:
                print line

printInNiceFiles()
