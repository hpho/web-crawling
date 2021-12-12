# science direct

from selenium import webdriver
from time import sleep
import os
import shutil
import pandas as pd

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass
        #print ('Error: Creating directory. ' +  directory)

# extract text file

search_key = ['biodegradable polymer','sustainability']
donwload_dir = r'C:\Users\GT1030\Downloads'
save_dir = r'update_folder'

driver = webdriver.Chrome(r'C:\Users\GT1030\Desktop\chromedriver_win32\chromedriver')

for i in search_key:
    driver.get('https://www.sciencedirect.com/search?qs={}&show=100&offset=0'.format(i.replace(' ','%20')))
    num_page = int(driver.find_element_by_xpath("""//*[@id="srp-pagination"]/li[1]""").text.split(' ')[-1])
    for j in range(num_page):
        driver.get('https://www.sciencedirect.com/search?qs={}&show=100&offset={}'.format( i.replace(' ','%20'),j*100 ))
        driver.find_element_by_xpath("""//*[@id="srp-toolbar"]/div[1]/div[1]/div/label/span[1]""").click()
        driver.find_element_by_xpath("""//*[@id="srp-toolbar"]/div[1]/div[3]/div/div/button/span/span""").click()
        driver.find_element_by_xpath("""/html/body/div[5]/div/div/div/p/div/div/button[4]/span""").click()
        sleep(2)

    # Extracting keywords

    file_list = os.listdir(donwload_dir)
    files_ = [s for s in file_list if "ScienceDirect_citations" in s]
    createFolder(save_dir+'\'+i)
    for j in files_:
        shutil.move(download_dir+'\'+i+'\'+j,save_dir+'\'+i+'\'+j)

    """    
    for j,i in enumerate([s for s in file_list if "ScienceDirect_citations" in s]):
        f = open(r'{}\{}'.format(download_dir,i),'r',encoding='utf-8')
        keywords = [s for s in f.readlines() if "Keywords:" in s]
        df = pd.DataFrame(keywords)
        df_ = df[0].str.split(';',expand=True)
        df_[0] = df_[0].str[10:]
        df_.to_csv(r'{}\{}_keywords_{}.csv'.format( save_dir,i.replace(' ','_'), j+1),header=True,index=False)
        f.close()
        os.remove('{}\{}'.format(download_dir,i))
    """
