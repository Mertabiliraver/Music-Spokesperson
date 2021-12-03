# -*- coding:utf-8 -*-
import time
from selenium import webdriver as wd
import speech_recognition as sr

class mainClass():

    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n[ Şarkı sözü yada ismi söyleyiniz ]")
            audio = r.listen(source)
            print("Şarkı sözleri aranıyor!\n")
            metin = str(r.recognize_google(audio,language = "tr"))
            
            
            return metin
            
            
            
    def texts(text):
        optionss = wd.ChromeOptions()
        optionss.add_argument('--headless')
        optionss.add_argument('disable-infobars')
        optionss.add_experimental_option('excludeSwitches', ['enable-logging'])
        optionss.add_argument('disable-popup-blocking')
        driver = wd.Chrome(options=optionss)
        driver.get(f"""https://www.google.com/search?q={text} şarkısı sözleri""")
        index1 = 1
        index2 = 1
        while True:
            try:       
                try:
                    yazı = driver.find_element_by_xpath(f"//*[@id='rso']/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[{index1}]/span[{index2}]").text
                    print("[ "+yazı+" ]")
                    index2 += 1
                except:
                    index2 = 1
                    index1 += 1
                    yazı = driver.find_element_by_xpath(f"//*[@id='rso']/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[{index1}]/span[{index2}]").text
                    print("[ "+yazı+" ]")
                
                time.sleep(0.2)
            except:
                print("\n[ Bitti ]")
                driver.quit()
                input("'Quit' for 'ENTER'")
                break
            
a1 = mainClass.listen()
mainClass.texts(a1)
