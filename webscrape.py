import requests
from bs4 import BeautifulSoup
def strip_string(string1):
    for i in string1:
        if i=='<':
            var1 = string1[string1.index(i):string1.index(">")+1]
            string1 = string1.replace(var1, "")
    return string1
def scrape_meaning(a):
    URL = f"https://www.dictionary.com/browse/{a}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    meaning = str(soup.find('span', attrs={'class': 'one-click-content css-nnyc96 e1q3nk1v1'}))
    if meaning.endswith("</span> </span>") or meaning.endswith("</span></span>"):
        meaning = meaning[:-7]  
    meaning1 = str(strip_string(meaning))
    if ":" in meaning1:
        meaning1 = meaning1[:meaning1.index(":")]

    if len(meaning1) > 90:
        meaning1 = meaning1[:90] + "\n" + "-" + meaning1[90:]
    
    return meaning1
def scrape_usage(a):
    URL = f"https://www.dictionary.com/browse/{a}"
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    usage = str(soup.find('span', attrs={'class': 'luna-example italic'}))
    usage1 = str(strip_string(usage))
    if len(usage1) > 90:
        usage1 = usage1[:90] + "\n" + "-" + usage1[90:]
    return usage1