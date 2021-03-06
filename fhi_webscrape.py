from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import pandas as pd
import time

caption_check_8 = "init-8"
caption_check_2 = "init-2"
while (caption_check_8 != "Number of reported cases by municipality") | (caption_check_2 != "Number of confirmed COVID-19 cases by age and sex") :
    driver = webdriver.Chrome('/home/efs/tools/chromedriver/chromedriver')
    #driver = webdriver.Firefox('/bin/')
    driver.implicitly_wait(30)
    driver.get('https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/')
    # driver.get('https://www.fhi.no/sv/smittsomme-sykdommer/corona/dags--og-ukerapporter/dags--og-ukerapporter-om-koronavirus/')


    # python_button = driver.find_elements_by_xpath("//button[@id='viewTable']")
    # python_button[0].send_keys("\n")
    # python_button[1].send_keys("\n")
    # python_button[2].send_keys("\n")

    # python_path = driver.find_elements_by_xpath("//div[@class='fhi-border fhi-border--thick fhi-border-light-grey']")
    # print(len(python_path))


    # print(python_path.is_selected())

    try:
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "path.highcharts-point.highcharts-color-0.highcharts-name-rogaland.highcharts-key-no-ro-11")))

        python_path = driver.find_element_by_css_selector('path.highcharts-point.highcharts-color-0.highcharts-name-rogaland.highcharts-key-no-ro-11')
        hover = ActionChains(driver).move_to_element(python_path)
        hover.perform()
    finally:
        content = driver.page_source
        driver.quit()

    soup = BeautifulSoup(content, features="lxml")
    caption_check_8 = soup.find('table', attrs={'id':'highcharts-data-table-8'}).find('caption').text
    caption_check_2 = soup.find('table', attrs={'id':'highcharts-data-table-2'}).find('caption').text
    print(caption_check_8 + " - " + caption_check_2)

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
            values_cumulative_new.append(row1)

df_cumulative_new = pd.DataFrame(values_cumulative_new, columns=columns_cumulative_new[1:3])
df_cumulative_new['Date']=date_cumulative_new

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
df_age_gender[['Women', 'Men']] = df_age_gender[['Women', 'Men']].apply(pd.to_numeric)


columns_dead = []
ages_dead = []
values_dead = []
for table in soup.findAll('table', attrs={'id':'highcharts-data-table-5'}):
    for thead in table.findAll('thead'):
        for th in thead.findAll('th', attrs={'class':'text'}):
            columns_dead.append(th.text)
    for tbody in table.findAll('tbody'):
        for th1 in tbody.findAll('th', attrs={'class':'text'}):
            ages_dead.append(th1.text)
        for tr in tbody.findAll('tr'):
            row1 = []
            for td in tr.findAll('td', attrs={'class':'number'}):
                row1.append(td.text)
            values_dead.append(row1)


df_age_gender_dead = pd.DataFrame(values_dead, columns=columns[1:4])

df_age_gender_dead['Age']=ages_dead
df_age_gender_dead[['Women', 'Men']] = df_age_gender_dead[['Women', 'Men']].apply(pd.to_numeric)

print(df_age_gender_dead.head())

columns_municipal = []
municipal = []
number = []
for table in soup.findAll('table', attrs={'id':'highcharts-data-table-8'}):
    for thead in table.findAll('thead'):
        for th in thead.findAll('th', attrs={'class':'text'}):
            columns_municipal.append(th.text)
    for tbody in table.findAll('tbody'):
        for th1 in tbody.findAll('th', attrs={'class':'text'}):
            municipal.append(th1.text)
        for tr in tbody.findAll('tr'):
            row1 = []
            for td in tr.findAll('td', attrs={'class':'number'}):
                row1.append(td.text)
            number.append(row1)


df_municipal = pd.DataFrame(number, columns=columns_municipal[1:2])

df_municipal['Kommune']=municipal
df_municipal[['Number']] = df_municipal[['Number']].apply(pd.to_numeric)


# store_date = str(date.today())+'_'+ str(datetime.today().hour) +'_'+ str(datetime.today().minute)
store_date = str(date.today())

df_positive_result.to_pickle('/media/efs/Data1/python_workspace/ws1/covid19_related/data_covid/df_positive_result_' + store_date + '.pkl')
df_cumulative_new.to_pickle('/media/efs/Data1/python_workspace/ws1/covid19_related/data_covid/df_cumulative_new_' + store_date + '.pkl')
df_age_gender.to_pickle('/media/efs/Data1/python_workspace/ws1/covid19_related/data_covid/df_age_gender_' + store_date + '.pkl')
df_age_gender_dead.to_pickle('/media/efs/Data1/python_workspace/ws1/covid19_related/data_covid/df_dead_age_gender_' + store_date + '.pkl')
df_municipal.to_pickle('/media/efs/Data1/python_workspace/ws1/covid19_related/data_covid/df_municipal_' + store_date + '.pkl')


