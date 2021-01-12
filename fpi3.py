#!/usr/bin/env python
# coding: utf-8

# In[6]:


conda install selenium


# In[1]:


from pandas.io.html import read_html
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


url = "https://www.fpi.nsdl.co.in/web/Reports/Film_List_All.aspx"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
temp =  soup.prettify()


# In[55]:


def downloadtable():

    result=''
    table = soup.find_all("table")
    for mytable in table:
        table_body = mytable.find('tbody')
        try:
            rows = table_body.find_all('tr')
            row_list=[]
            for tr in rows:
                cols = tr.find_all('td')
                td_list = []
                for td in cols:
                     td_list.append(td.text)
                row_list.append(td_list)
    
        except:
            print ("no tbody")


# In[82]:

    while 1:
            
        try:
               
            driver = set_proxy_details()
            # Opening the website
            driver.get(_URL)     
            # getting the button by class name
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="myTable_next"]'))).click()
            time.sleep(10)
            driver.quit()    
        except Exception as e:
            print ("Error %s"%e)
            driver.quit()



# In[83]:


import pandas as pd
df = pd.DataFrame(row_list)
df = df.replace(',','')
df.to_csv(r'C:\Users\Nityo\Desktop\file6.csv', index=False) 


# In[ ]:





# In[ ]:




