import requests
from bs4 import BeautifulSoup
import logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s-  %(message)s')

# northern beaches swellnet
def northScrape():
    res = requests.get('https://www.swellnet.com/reports/australia/new-south-wales/northern-beaches/forecast') 
    res.raise_for_status
    soup = BeautifulSoup(res.content, 'html.parser')
    elemDate = soup.select('.tip_date_time')
    for date in elemDate:
        logging.debug(date.getText())


    elemWaveHeight = soup.select('.tip_wave')
    for wave in elemWaveHeight:
        logging.debug(wave.getText())




