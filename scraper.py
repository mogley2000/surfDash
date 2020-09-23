import requests
from bs4 import BeautifulSoup
import logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s-  %(message)s')
from tabulate import tabulate 

# northern beaches swellnet

url = "https://www.swellnet.com/reports/australia/new-south-wales/northern-beaches/forecast"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.content, 'html.parser')
forecast = soup.find_all("div", {"class": "forecast_tip"}) # scrapes the swell train block of code for the whole div tag that includes class forecast_tip. will ouput 9 items (3 days x 6am, 12pm, 6pm)

def getData(html, attribute, _class, index):
    result = []
    for tag in html:
        for item in tag.find_all(attribute, {"class": _class})[index]:
            if item is not None:
                result.append(item)
            else:
                result.append("N/A")
    return result

date = getData(forecast, "div", "tip_date_time", 0)
train1 = getData(forecast, "div", "tip_train", 0)
train2 = getData(forecast, "div", "tip_train", 1)
wave = getData(forecast, "span", "tip_wave", 0)

logging.debug(date)
logging.debug(train1)
logging.debug(train2)
logging.debug(wave)

forecast_data = list(zip(date, train1, train2, wave))
headers = ["Date", "Primary Swell", "Secondary Swell", "Wave Height"]

print(tabulate([*forecast_data], headers=headers))

#for tag in forecast:
#    secondary = tag.find("div", {"class": "tip_train"})
#    logging.debug(secondary) 
    

#trainCond = []
#for train2 in forecast:
#    for text in train2.find_all("div", {"class": "tip_train"})[1]:
#        trainCond.append(text.getText())
#logging.debug(trainCond)

#waveCond = []
#for wave in forecast:
#    for text in wave.find_all("span", {"class": "tip_wave"}):
#        waveCond.append(text.getText())

#windCond = []
#for wind in forecast:
#    for text in wind.find_all("span", {"class": "tip_wind"}):
#        windCond.append(text.getText())


#logging.debug(dateCond)
#logging.debug(waveCond)
#logging.debug(windCond)

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




    
    
 









