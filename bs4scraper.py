import requests
from bs4 import BeautifulSoup
import csv
import time

######################## University Notice Crawl #########################

def title_crawling(soup):
    titles = soup.find_all("span",class_="title-wrapper")
    title_list=[]
    for title in titles:
        titletext = title.text.replace('\t','')
        titletext = titletext.replace('공지','[중요] ')
        titletext = titletext.replace('[[중요] ]','[중요]')
        titletext = titletext.replace('\n','')
        title_list.append(titletext)
    return title_list

def date_crawling(soup):
    dates = soup.find_all("td",class_="date")
    date_list=[]
    for date in dates:
        datetext = date.text.replace('\t','')
        datetext = datetext.replace('\n','')
        date_list.append(datetext)
    return date_list

def writer_crawling(soup):
    writers = soup.find_all("td",class_="writer")
    writer_list=[]
    for writer in writers:
        writertext = writer.text.replace('\t','')
        writertext = writertext.replace('\n','')
        writer_list.append(writertext)
    return writer_list

def planner_crawling(soup):
    dates = soup.find_all("span", class_="period")
    titles = soup.find_all("strong", class_="substance")
    plan_list=[]
    for date in dates:
        datetext = date.text.replace('\t','')
        datetext = datetext.replace('\n','')
        plan_list.append(datetext)
        
    for title in titles:
        titletext = title.text.replace('\t','')
        titletext = titletext.replace('\n','')
        plan_list.append(titletext)
    
    return plan_list

def href_crawling(soup):
    hrefs = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    hrefs_list=[]
    for i in range(len(hrefs)):
        if (hrefs[i].startswith('?mode=view&')):
            hrefs_list.append(hrefs[i])

    return hrefs_list

###########################################################################
####################### Weather Informatioon Crawl ########################

def weather_crawling(soup):
    nowTemps = soup.find_all("span",class_="todaytemp")    # 현재 기온
    nowBodyTemps = soup.find_all("span",class_="sensible") # 현재 체감 기온
    YDayCompares = soup.find_all("p",class_="cast_txt")    # 어제보다 기온 비교
    TempMins = soup.find_all("span",class_="min")
    TempMaxs = soup.find_all("span",class_="max")
    nowTempList=[]
    nowBodyTempList=[]
    YDayCompareList=[]
    TempMinList=[]
    TempMaxList=[]
    result=[]
    for nowTemp in nowTemps:
        nowTemptext = nowTemp.text.replace('\t','')
        nowTemptext = nowTemptext.replace('\n','')
        nowTempList.append(nowTemptext)

    for nowBodyTemp in nowBodyTemps:
        nowBodyTemptext = nowBodyTemp.text.replace('\t','')
        nowBodyTemptext = nowBodyTemptext.replace('\n','')
        nowBodyTempList.append(nowBodyTemptext)

    for YDayCompare in YDayCompares:
        YDayComparetext = YDayCompare.text.replace('\t','')
        YDayComparetext = YDayComparetext.replace('\n','')
        YDayCompareList.append(YDayComparetext)
    
    for TempMin in TempMins:
        TempMintext = TempMin.text.replace('\t','')
        TempMintext = TempMintext.replace('\n','')
        TempMinList.append(TempMintext)
    
    for TempMax in TempMaxs:
        TempMaxtext = TempMax.text.replace('\t','')
        TempMaxtext = TempMaxtext.replace('\n','')
        TempMaxList.append(TempMaxtext)
    
    result.append(nowTempList)
    result.append(nowBodyTempList)
    result.append(YDayCompareList)
    result.append(TempMinList)
    result.append(TempMaxList)

    return result
###########################################################################
########################### Air Conditions Crawl ##########################

###########################################################################
def main() :
    url1 = "https://www.kumoh.ac.kr/ko/sub06_01_01_01.do"
    url2 = "https://ce.kumoh.ac.kr/ce/sub0501.do"
    url3 = "https://www.kumoh.ac.kr/ko/sub06_03_04_04.do"
    weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B1%B0%EC%9D%98%EB%8F%99+%EB%82%A0%EC%94%A8"
    plan_url = "https://www.kumoh.ac.kr/ko/index.do"
    Univ_href_url = "https://www.kumoh.ac.kr/ko/sub06_01_01_01.do"
    Ce_href_url = "https://ce.kumoh.ac.kr/ce/sub0501.do"
    Job_href_url = "https://www.kumoh.ac.kr/ko/sub06_03_04_04.do"
    req1 = requests.get(url1)
    req2 = requests.get(url2)
    req3 = requests.get(url3)
    req4 = requests.get(plan_url)
    req5 = requests.get(weather_url)
    req6 = requests.get(Univ_href_url)
    req7 = requests.get(Ce_href_url)
    req8 = requests.get(Job_href_url)
    soup1 = BeautifulSoup(req1.text, "html.parser")
    soup2 = BeautifulSoup(req2.text, "html.parser")
    soup3 = BeautifulSoup(req3.text, "html.parser")
    soup4 = BeautifulSoup(req4.text, "html.parser")
    soup5 = BeautifulSoup(req5.text, "html.parser")
    soup6 = BeautifulSoup(req6.text, "html.parser")
    soup7 = BeautifulSoup(req7.text, "html.parser")
    soup8 = BeautifulSoup(req8.text, "html.parser")
    title_list1=title_crawling(soup1)
    date_list1=date_crawling(soup1)
    writer_list1=writer_crawling(soup1)
    title_list2=title_crawling(soup2)
    date_list2=date_crawling(soup2)
    writer_list2=writer_crawling(soup2)
    title_list3=title_crawling(soup3)
    date_list3=date_crawling(soup3)
    writer_list3=writer_crawling(soup3)
    plan_list=planner_crawling(soup4)
    weather_list=weather_crawling(soup5)
    Univ_href_list=href_crawling(soup6)
    Ce_href_list=href_crawling(soup7)
    Job_href_list=href_crawling(soup8)
    
    file1 = open('Scrap_Project/data/Univ_Notice.txt','w',newline='', encoding='UTF-8')
    wr1 = csv.writer(file1, delimiter='\t')
    for i in range(len(date_list1)):
        wr1.writerow([date_list1[i], title_list1[i], writer_list1[i]])
    file1.close()

    file2 = open("Scrap_Project/data/Depart_Notice.txt", 'w', newline='', encoding='UTF-8')
    wr2 = csv.writer(file2, delimiter='\t')
    for i in range(len(date_list2)):
        wr2.writerow([date_list2[i], title_list2[i], writer_list2[i]])
    file2.close()

    file3 = open('Scrap_Project/data/Info_Notice.txt','w',newline='', encoding='UTF-8')
    wr3 = csv.writer(file3, delimiter='\t')
    for i in range(len(date_list3)):
        wr3.writerow([date_list3[i], title_list3[i], writer_list3[i]])
    file3.close()

    for i in range(6):
        print(plan_list[i], "\n")
    file4 = open("Scrap_Project/data/Schedule.txt",'w',newline='',encoding='UTF-8')
    wr4 = csv.writer(file4, delimiter='\t')
    for i in range(3):
        wr4.writerow([plan_list[i], plan_list[i + 3]])
    file4.close()

    file5 = open("Scrap_Project/data/Weather_Info.txt",'w',newline='',encoding='UTF-8')
    wr5 = csv.writer(file5, delimiter='\t')
    for i in range(5):
        wr5.writerow([weather_list[i]])
    file5.close()

    file6 = open("Scrap_Project/data/Univ_Notice.txt",'a',newline='', encoding='UTF-8')
    wr6 = csv.writer(file6, delimiter = '\t')
    for i in range(len(Univ_href_list)):
        wr6.writerow([Univ_href_list[i]])
    file6.close()

    file7 = open("Scrap_Project/data/Depart_Notice.txt",'a',newline='', encoding='UTF-8')
    wr7 = csv.writer(file7, delimiter= '\t')
    for i in range(len(Ce_href_list)):
        wr7.writerow([Ce_href_list[i]])
    file7.close

    file8 = open("Scrap_Project/data/Info_Notice.txt",'a',newline='', encoding='UTF-8')
    wr8 = csv.writer(file8, delimiter= '\t')
    for i in range(len(Job_href_list)):
        wr8.writerow([Job_href_list[i]])
    file8.close

while(True):
    main()
    time.sleep(300)