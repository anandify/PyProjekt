import time
import pandas as pd
from bs4 import BeautifulSoup

print("----------------------------------------------------------------------------------------------------------------------")
print("WELCOME TO PyNews V.1.3")
print("----------------------------------------------------------------------------------------------------------------------")

print("To know What others(local + global)are searching, please enter 1 ")
print("To know breaking news headlines, please enter 2")
print("----------------------------------------------------------------------------------------------------------------------")
print("")
ani=int(input("enter no."))
location=input("enter geographic code :")
if location == "IN":
    locationa = "India"
if location == "US":
    locationa = "USA"
if location == "GB":
    locationa = "United Kingdom"
    """
    Parses the Google Trends RSS feed using BeautifulSoup.
    and Returns:
    a CSV for Whatever is asked.
    """
    def trends_retriever(country_code): #Is a Simple module
      xml_document = fetch_xml(country_code)
      soup = BeautifulSoup(xml_document, "lxml")
      titles = soup.find_all("title")
      approximate_traffic = soup.find_all("ht:approx_traffic")
      return {title.text: re.sub("[+,]", "", traffic.text)
            for title, traffic in zip(titles[1:], approximate_traffic)}

if ani == 1:
    if __name__ == '__main__':
        trends = trends_retriever(location)
        dfa = pd.DataFrame(list(trends.items()), columns=['  Words Famous Today in '+locationa, '  Times Searched on Google'])
        print(dfa)
    
from urllib import request
url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
html = request.urlopen(url).read().decode('utf8')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
ti = soup.find_all('title')
to = ti.copy()
le = len(to)
if ani == 2:
    print("")
    print("%d news incoming "%(le-1))
    print("")
    se = pd.Series(to)
    for a in to:
        print(a.text)
        print("")


    print("")
    print(ti) # Prints the tag
    print("")
    print("------------------------------------------------------------------")
    print(se)
    
if ani == 3:
    if __name__ == '__main__':
        trends = trends_retriever("IN")
    print(trends)
    print("")
    print("%d news incoming : "%(le-1))
    print("")
    se = pd.Series(to)
    for a in to:
        print(a.text)
        print("")
    print("")
    print("")
    print("-----------------------------------------------------------------------------------------------------------")
    print(se) # Prints the Series
    print("")
    print("")
    print("-----------------------------------------------------------------------------------------------------------")
    print(ti)# prints the tags
