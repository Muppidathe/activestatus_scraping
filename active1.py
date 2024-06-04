from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import csv
from selenium.common.exceptions import WebDriverException



#init:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
#account credentials
username="muppidathi._"
password='XXXXXX'                                                                                      
targeturl='https://www.instagram.com/direct/t/17845628168854651/'
#targetusername
instausername="lone._._.wo.lf"
filename=instausername+".csv"
e=False
active_status_text=" "
ref=0

#login:
while(True):
    try:
        driver.get(targeturl)
        eleusername= driver.find_element(By.XPATH,"//input[@name='username' and @type='text']")
        elepass= driver.find_element(By.XPATH,"//input[@name='password' and @type='password']")
        #elelogin= driver.find_element(By.XPATH,"//button[@type='submit']")
        eleusername.send_keys(username)
        elepass.send_keys(password,Keys.ENTER)
        notnowdiv=driver.find_element(By.XPATH,"//div[text()='Not now']")
        notnowdiv.click()
        notnowbtn=driver.find_element(By.XPATH,"//button[text()='Not Now']")
        notnowbtn.click()
        break
    except:
        pass
    time.sleep(60)

#process
try:
    driver.get(targeturl)
    while(True):
        try:
            if ref==6:
                driver.refresh()
                ref=0
            active_status=driver.find_element(By.XPATH,"//a[@href='/"+instausername+"/']//child::div//child::span//child::div[2]//child::span")
            active_status_text=active_status.text
        except NoSuchElementException:
            pass
        except WebDriverException:
            pass
        except Exception as ee:
            print(ee)
        if (active_status_text=='Active now'):
            today=datetime.now()
            today=str(today.day)+"/"+str(today.month)+"/"+str(today.year)
            strtime=datetime.now()
            strtime1=str(strtime.hour)+":"+str(strtime.minute)+":"+str(strtime.second)
            print(today,"    ",strtime1,end="    ")
            file=open(filename,"a")
            csvwriter = csv.writer(file)
            while(True):
                try:
                    driver.refresh()
                    active_status=driver.find_element(By.XPATH,"//a[@href='/"+instausername+"/']//child::div//child::span//child::div[2]//child::span")
                    active_status_text=active_status.text
                except NoSuchElementException :
                    e=True
                    active_status_text="not active"
                except WebDriverException:
                    pass
                except Exception as ee:
                    print(ee)
                
                if(active_status_text!='Active now' or e==True):
                    fintime=datetime.now()
                    fintime1=str(fintime.hour)+":"+str(fintime.minute)+":"+str(fintime.second)
                    totaldur=(fintime-strtime).total_seconds()
                    print(fintime1,"  -> ",totaldur,"    ",e,"\n")
                    csvwriter.writerow([today,strtime1,fintime1,totaldur,e])
                    file.close()
                    e=False
                    break
                #print("innerwhile")            
                time.sleep(2)
        
        #print("outerwhile")
        ref+=1
        time.sleep(5)
        
except KeyboardInterrupt:
    driver.quit()
    
except:
    pass
