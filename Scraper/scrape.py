from selenium import webdriver
import requests, time
import os

DRIVER_PATH = "./chromedriver"

def scrape(q:str, limit:int=15):
    driver = webdriver.Chrome(DRIVER_PATH)
    search_url = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q="+q
    driver.get(search_url)
    elements = driver.find_elements_by_class_name('rg_i')
    os.mkdir("../Images/"+q)
    i=0
    for e in elements:
        try:
            e.click()
            time.sleep(5)
        except:
            driver.execute_script("window.scrollTo(0,window.scrollY+200)")
            continue
        element = driver.find_elements_by_class_name('v4dQwb')
        if i==0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
            big_img = element[1].find_element_by_class_name('n3VNCb')
        url = big_img.get_attribute("src")
        print(url)
        i+=1
        filename = "../Images/"+q+"/"+q+"-"+str(i)+".jpeg"
        download_image(url,filename)
        if(i==limit):
            break


def download_image(url:str,filename:str):
    try:
        response = requests.get(url)
        if response.status_code==200:
            with open(filename,"wb") as file:
                file.write(response.content)
    except:
        return

scrape("Dogs", limit=5)