import requests
from bs4 import BeautifulSoup
import logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s-  %(message)s')

# northern beaches swellnet

res = requests.get('https://www.swellnet.com/reports/australia/new-south-wales/northern-beaches/forecast') 
res.raise_for_status
soup = BeautifulSoup(res.content, 'html.parser')
html = soup.findAll("div", {"class": "forecast_tip"}) # scrapes the swell train block of code for the whole div tag that includes class forecast_tip. 
                                                      # will ouput 9 items (3 days x 6am, 12pm, 6pm)
conditions = []

dayOne6am = html[0]
for tag in dayOne6am:
    conditions = tag.findAll("div", {})

dayOne12pm = html[1] # skip 6pm forecast as it is not necessary i.e. html[2] 
dayTwo6am = html[3]
dayTwo12pm = html[4]
dayThree6am = html[6]
dayThree12pm = html[7]




    
    
 









