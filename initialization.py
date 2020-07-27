# Imporitngs


from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd


# Initialization Function

def symbol_scraper():
    scraping_time = str(datetime.datetime.now())


    date = []
    symbol_list = []
    name = []
    count = []
    volume = []
    value = []
    yesterday = []
    first = []
    last = []
    change_last = []
    percentage_last = []
    final = []
    change_final = []
    percentage_final = []
    sym_min = []
    sym_max = []
    eps = []
    pe = []
    buy = []
    sell = []

    link = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131F'
    driver = webdriver.Firefox()
    driver.get(link)
    time.sleep(5)
    scraping_time = str(datetime.datetime.now())
    information = driver.find_element_by_id('main')
    soup = BeautifulSoup(information.get_attribute('innerHTML'), 'html.parser')
    driver.close()
    symbols = soup.findAll("div", {"class": '{c}'})
    print('Number of Symbols Found: ', len(symbols))
    for symbol in symbols:
        list_inner_divs = list(symbol.findAll("div"))

        date.append(scraping_time)
        symbol_list.append(list_inner_divs[0].text)
        name.append(list_inner_divs[1].text)
        count.append(list_inner_divs[2].text)
        volume.append(list_inner_divs[3].text)
        value.append(list_inner_divs[4].text)
        yesterday.append(list_inner_divs[6].text)
        first.append(list_inner_divs[7].text)
        last.append(list_inner_divs[8].text)
        change_last.append(list_inner_divs[9].text)
        percentage_last.append(list_inner_divs[10].text)
        final.append(list_inner_divs[11].text)
        change_final.append(list_inner_divs[12].text)
        percentage_final.append(list_inner_divs[13].text)
        sym_min.append(list_inner_divs[14].text)
        sym_max.append(list_inner_divs[15].text)
        eps.append(list_inner_divs[16].text)
        pe.append(list_inner_divs[17].text)
        buy.append(list_inner_divs[21].text)
        sell.append(list_inner_divs[22].text)

    final_df = pd.DataFrame(list(zip(date, symbol_list, name, count, volume, value, yesterday, first, last, change_last, percentage_last, final, change_final, percentage_final, sym_min, sym_max, eps, pe, buy, sell)), columns = ['date',
                'symbol',
                'name',
                'count',
                'volume',
                'value',
                'yesterday',
                'first',
                'last',
                'change_last',
                'percentage_last',
                'final',
                'change_final',
                'percentage_final',
                'min',
                'max',
                'eps',
                'pe',
                'buy',
                'sell'])

    final_df.to_csv('data.csv')

    return final_df

# Calling the symbol_scraper function would result in the creation of the data.csv file which is essential for proper execution of time basis scarper function, defined in the timely_scraper.py file.

symbols_i_want = symbol_scraper()
