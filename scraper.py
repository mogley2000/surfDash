import requests
from bs4 import BeautifulSoup
import logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s-  %(message)s')

# northern beaches swellnet

res = requests.get('https://www.swellnet.com/reports/australia/new-south-wales/northern-beaches/forecast') 
res.raise_for_status
soup = BeautifulSoup(res.content, 'html.parser')
html = soup.find_all("div", {"class": "forecast_tip"}) # scrapes the swell train block of code for the whole div tag that includes class forecast_tip. will ouput 9 items (3 days x 6am, 12pm, 6pm)

dateCond = []
for date in html:
    for text in date.find_all("div", {"class": "tip_date_time"}):
        dateCond.append(text.getText())

waveCond = []
for wave in html:
    for text in wave.find_all("span", {"class": "tip_wave"}):
        waveCond.append(text.getText())

windCond = []
for wind in html:
    for text in wind.find_all("span", {"class": "tip_wind"}):
        windCond.append(text.getText())


logging.debug(dateCond)
logging.debug(waveCond)
logging.debug(windCond)

#dayOne6am = html[0]
#for tag in dayOne6am:
#   conditions = tag.find("tip_date_time")
#logging.debug(conditions)

#dayOne12pm = html[1] # skip 6pm forecast as it is not necessary i.e. html[2] 
#dayTwo6am = html[3]
#dayTwo12pm = html[4]
#dayThree6am = html[6]
#dayThree12pm = html[7]



# TODO: Is there a way to check if certain data point is missing it fills in as a missing value, doesn't just replace index 1 with 0




    
    
 









