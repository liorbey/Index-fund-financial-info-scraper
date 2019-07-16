from bs4 import BeautifulSoup
import requests
import csv
import re

fund = input("Please type in a CIK number or a ticker: ")

response = requests.get('https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=13f&dateb=&owner=exclude&count=10'.format(fund))

soup = BeautifulSoup(response.text, "xml")

latest = soup.find('a', {'id':'documentsbutton'})

doclink = latest.get('href')

response2 = requests.get('https://www.sec.gov{}'.format(doclink))

soup2 = BeautifulSoup(response2.text, "xml")

xmldoc = soup2.find('a',string=re.compile(r'^primary_doc.xml'))

finaldoc = xmldoc.get('href')

response3 = requests.get('https://www.sec.gov{}'.format(finaldoc))

soup3 = BeautifulSoup(response3.text, "xml")

pairs = {}
for node in soup3.findAll('edgarSubmission'):
    nodes = node.findAll(text=True)

for keyvalue in nodes:
    if keyvalue != '\n':
        parents = soup3.find(string=re.compile(str(keyvalue)))
        pairs[parents]=parents.parent.name

with open('Lior_Beyderman.tsv', 'w') as tsv_file:
    for key in pairs.keys():
        tsv_file.write("%s\t%s\n"%(pairs[key],key))   


