from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

from bs4 import BeautifulSoup 
from datetime import date
from datetime import datetime

import pandas as pd 
import numpy as np
import os

import time

def select_option(id_or_name, values_to_click, is_multi=True):
    select_disease = Select(driver.find_element_by_id(id_or_name))
    if is_multi:
        select_disease.deselect_all()
    for option_korona in select_disease.options:
        for option_ in values_to_click:
            if option_korona.get_attribute("text") == option_:
                option_korona.click()

driver = webdriver.Chrome('/home/efs/tools/chromedriver/chromedriver')
driver.get('http://www.msis.no/')

# first menu click 
driver.switch_to_frame("contents")
first_menu = driver.find_element_by_partial_link_text("Lag")
first_menu.click()

driver.switch_to_default_content()
driver.switch_to_frame("main") 

select_option("m_ctrlDiagnose", ["Koronavirus med utbruddspotensial"])
select_option("m_ctrlYears", ["2020"])
select_option("m_ctrlAldersgruppe", ["2020"])


# select_option("m_ctrlRader", ["Fylke"], False)
m_ctrlRader = driver.find_element_by_xpath("//select[@name='m_ctrlRader']")
all_options1 = m_ctrlRader.find_elements_by_tag_name("option")
all_options1[0].click()
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()


# select_option("m_ctrlKolonner", ["Måned"], False)
m_ctrlKolonner = driver.find_element_by_xpath("//select[@name='m_ctrlKolonner']")
all_options2 = m_ctrlKolonner.find_elements_by_tag_name("option")
all_options2[2].click()

driver.find_element_by_id("m_ctrlLagRapport").click()

driver.implicitly_wait(5)

driver.find_element_by_id("m_ucReportGrid_m_ctrlLagreSomExcel").click()


# m_ctrlYears
# m_ctrlMonths
# m_ctrlFylke
# m_ctrlSmitteverdensdel
# m_ctrlKjonn
# m_ctrlAldersgruppe


# content = driver.page_source
# soup = BeautifulSoup(content, features="lxml")

#driver.quit()

print("Finish.")

