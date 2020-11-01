import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s-  %(message)s')
from tabulate import tabulate 
import json

# northern beaches swellnet

url = "https://www.swellnet.com/reports/australia/new-south-wales/northern-beaches/forecast"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.content, 'html.parser')
forecast = soup.find_all("div", {"class": "forecast_tip"}) # scrapes the swell train block of code for the whole div tag that includes class forecast_tip. will ouput 9 items (3 days x 6am, 12pm, 6pm)

def getData(html, attribute, _class, index):
    result = []
    for tag in html:
        try:
            for item in tag.find_all(attribute, {"class": _class})[index]:
                if item is not None:
                    result.append(item)
                else:
                    result.append("N/A")
        except IndexError:
            result.append("N/A")
    return result

def runScraper():
    date = getData(forecast, "div", "tip_date_time", 0)
    wave = getData(forecast, "span", "tip_wave", 0)
    wind = getData(forecast, "span", "tip_wind", 0)
    train1 = getData(forecast, "div", "tip_train", 0)
    train2 = getData(forecast, "div", "tip_train", 1)

    forecast_data = list(zip(date, wave, wind, train1, train2))
    headers = ["Date", "Wave Height", "Wind", "Primary Swell", "Secondary Swell"]
   
    tabulated = tabulate([*forecast_data], headers=headers, tablefmt = 'html')
    #print(tabulated)

    return(tabulated)

#scrape tide data from willyweather
url_tide = 'https://tides.willyweather.com.au/nsw/sydney/fort-denison.html'
res_tide = requests.get(url_tide)
res_tide.raise_for_status
soup_tide = BeautifulSoup(res_tide.content, 'html.parser')
forecast_tide = soup_tide.find("section", {"class": "forecast"})
day_block = forecast_tide.find_all("time")
#day_1 = day_block[0]
#day_2 = day_block[1]
#day_3 = day_block[2]
#day_4 = day_block[3]
#day_5 = day_block[4]

#tide_data = []
#for tag in day_1.next_sibling:
#    tide = tag.get_text(" / ")
#    tide_data.append(tide)

#print(tide_data)



def getTideData(html, index):
    tide_data=[]
    for tag in html[index].next_sibling:
        tide_data.append(tag.get_text(" / ")) 
    return tide_data

def runTideDataScraper():
    day_1 = getTideData(day_block, 0)
    day_2 = getTideData(day_block, 1)
    day_3 = getTideData(day_block, 2)
    day_4 = getTideData(day_block, 3)
    day_5 = getTideData(day_block, 4)
    forecast_tideData = list(zip(day_1, day_2, day_3, day_4, day_5))
    print(forecast_tideData)
runTideDataScraper()




    #for item in tag.find_all(["time", "li", {"class": ["point-low", "point-high"]}]):
     #  print(item)


# scrape bom json for north head 
#bom_northhead_url = "http://www.bom.gov.au/fwo/IDN60701/IDN60701.95768.json"
#northhead_res = requests.get(bom_northhead_url)
#northhead_res.raise_for_status
#json_data = json.loads(northhead_res.text)
#logging.debug(type(json_data))

#def json_print(order, attribute):
    #print(json_data['observations']['data'][order][attribute])

#json_print(0, 'local_date_time')
#json_print(1, 'local_date_time')


#for item in json_data['observations']['data']:
    #print(item['local_date_time'])

    
        #for subitem in item['local_date_time']:
        #print (subitem) 





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




    
    
 









