from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import pandas as pd
import time

driver = webdriver.Chrome('C:\\Users\\elga_\\Downloads\\chromedriver_win32\\chromedriver')
driver.get('https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/')
# driver.get('https://www.fhi.no/sv/smittsomme-sykdommer/corona/dags--og-ukerapporter/dags--og-ukerapporter-om-koronavirus/')

python_button = driver.find_elements_by_xpath("//button[@id='viewTable']")
python_button[0].send_keys("\n")
python_button[1].send_keys("\n")
python_button[2].send_keys("\n")

# python_path = driver.find_elements_by_xpath("//div[@class='fhi-border fhi-border--thick fhi-border-light-grey']")
# print(len(python_path))



python_path = driver.find_element_by_css_selector('path.highcharts-point.highcharts-color-0.highcharts-name-rogaland.highcharts-key-no-ro-11')
hover = ActionChains(driver).move_to_element(python_path)
hover.perform()
# print(python_path.is_selected())

content = driver.page_source

soup = BeautifulSoup(content, features="lxml")

driver.quit()

# g.highcharts-label.highcharts-tooltip.highcharts-color-0

# for table in soup.findAll('div', attrs={'class':'highcharts-container'}):
#     for textt in table.findAll('text'):
#         print(textt.text)

# for table in soup.findAll('table', attrs={'class':'standardTable'}):
#     print(table.text)


# for table in soup.findAll('div', attrs={'class':'fhi-row fhi-row--fill'}):
#     # print(table.text)
#     for thead in table.findAll('path'):
#         print(thead.text)
# #         for th in thead.findAll('th', attrs={'class':'text'}):

columns_positive = []
date_positive = []
values_positive = []
for table in soup.findAll('table', attrs={'id':'highcharts-data-table-0'}):
    for thead in table.findAll('thead'):
        for th in thead.findAll('th', attrs={'class':'text'}):
            columns_positive.append(th.text)
    for tbody in table.findAll('tbody'):
        for th1 in tbody.findAll('th', attrs={'class':'text'}):
            date_positive.append(th1.text)
        for tr in tbody.findAll('tr'):
            row1 = []
            for td in tr.findAll('td', attrs={'class':'number'}):
                row1.append(td.text)
            values_positive.append(row1)

df_positive_result = pd.DataFrame(values_positive, columns=columns_positive[1:4])
df_positive_result['Date']=date_positive

print(df_positive_result.head())


columns_cumulative_new = []
date_cumulative_new = []
values_cumulative_new = []
for table in soup.findAll('table', attrs={'id':'highcharts-data-table-1'}):
    for thead in table.findAll('thead'):
        for th in thead.findAll('th', attrs={'class':'text'}):
            columns_cumulative_new.append(th.text)
    for tbody in table.findAll('tbody'):
        for th1 in tbody.findAll('th', attrs={'class':'text'}):
            date_cumulative_new.append(th1.text)
        for tr in tbody.findAll('tr'):
            row1 = []
            for td in tr.findAll('td', attrs={'class':'number'}):
                row1.append(td.text)
            print(row1)
            values_cumulative_new.append(row1)

df_cumulative_new = pd.DataFrame(values_cumulative_new, columns=columns_cumulative_new[1:3])
df_cumulative_new['Date']=date_cumulative_new

print(df_cumulative_new.head())

columns = []
ages = []
values = []
for table in soup.findAll('table', attrs={'id':'highcharts-data-table-2'}):
    for thead in table.findAll('thead'):
        for th in thead.findAll('th', attrs={'class':'text'}):
            columns.append(th.text)
    for tbody in table.findAll('tbody'):
        for th1 in tbody.findAll('th', attrs={'class':'text'}):
            ages.append(th1.text)
        for tr in tbody.findAll('tr'):
            row1 = []
            for td in tr.findAll('td', attrs={'class':'number'}):
                row1.append(td.text)
            values.append(row1)




df_age_gender = pd.DataFrame(values, columns=columns[1:4])
df_age_gender['Age']=ages
df_age_gender['Women'] = pd.to_numeric(df_age_gender['Women'])
df_age_gender['Men'] = pd.to_numeric(df_age_gender['Men'])

print(df_age_gender.head())


store_date = str(date.today())+'_'+ str(datetime.today().hour) +'_'+ str(datetime.today().minute)


df_positive_result.to_pickle('data_covid/df_positive_result_' + store_date + '.pkl')
df_cumulative_new.to_pickle('data_covid/df_cumulative_new_' + store_date + '.pkl')
df_age_gender.to_pickle('data_covid/df_age_gender_' + store_date + '.pkl')
