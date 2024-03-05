#? <차이점>
# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법
                      #   
# 웹 스크래핑(Scraping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법
                      #  데이터만 받아오는 것  
#================================================================#
# 파이썬 스크래핑 패키지 : `beautifulsoup4`
# 파이썬 크로링 패키지 : `selenium`

# pip install beautifulsoup4
# pip install selenium
# 한번에 받는 방법 : pip install beautifulsoup4 selenium (띄어쓰기 사용)
#================================================================#
#>> beautifulsoup4 
import requests #요청보내는 명령어
from bs4 import BeautifulSoup #사용명령어

URL = 'https://naver.com' #ex_네이버로 요청보내기

response = requests.get(URL)
print(response.status_code)  #터미널에 출력값 : <Response [200]>

#출력값 : 100 - 추가요청 . 기다림
       #  200 - 성공
       #  300 - 리소스의 위치가 바뀌었다
       #  400 - 요청자 클라이언트 오류    ... ex) 404 Not Found
       #  500 - 응답자 서버 오류
#-------------------------------------------#
# "HTTP 상태 코드" 검색하면 자세히 알 수 있다

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    a_list = soup.find_all('a')
    print(a_list)
else:
    print(response.status_code)

#================================================================#

# selenium : 직접적으로 브라우저를 바로 켠다
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #검색 작업
from selenium.webdriver.common.keys import Keys #Enter 작업

import time

driver = webdriver.Chrome()
time.sleep(3)

#!이동
driver.get(URL) #네이버 화면을 바로 켠다
time.sleep(3)
#!요소 찾기
search_input = driver.find_element(By.ID, 'query')
#!타이핑 치는 작업
search_input.send_keys('대한민국')
time.sleep(1)
#!Enter 치는 작업
search_input.send_keys(Keys.ENTER)
time.sleep(3)
#!검색된 창에서 특정한 것을 클릭하는 작업
    # 1)클릭할 것을 선택
news_button = driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a')
time.sleep(1)
    # 2)클릭하기
ActionChains(driver).click(news_button).perform()
time.sleep(3)
#!하위 자료 클릭하기
news_title_elements = driver.find_elements(By.CLASS_NAME, 'news_tit')
time.sleep(1)
    #요소로 접근해 반복돌기
for news_title_element in news_title_elements:
    # title = news_title_element.text
    title = news_title_element.get_attribute('title')
    print(title) #안에 있는 큰 제목들이 나온다
time.sleep(1)
#!이전 작업으로 되돌리기
driver.back()
time.sleep(2)
#!news 갔다가 image 로 이동
image_button = driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a')
ActionChains(driver).click(image_button).perform()
time.sleep(2)
#!이미지 가져오기
image_elements = driver.find_elements(By.CLASS_NAME, '_fe_image_tab_content_thumbnail_image')
time.sleep(1)

image_list = []

for image_element in image_elements:
    image_src = image_element.get_attribute('src')
    image_list.append(image_src) 
time.sleep(1)

#! 파이썬으로 폴더 생성
import os

FOLDER_PATH = r'./images/'

if not os.path.isdir(FOLDER_PATH):
    os.mkdir(FOLDER_PATH)
#! 파이썬으로 폴더 생성//
    
#! 파이썬으로 이미지 url 파일 다운로드    
from urllib.request import urlretrieve

number = 1

for image_src in image_list:
    urlretrieve(image_src, FOLDER_PATH + f'{number}.png')
    number += 1
    time.sleep(0.5)
#! 파이썬으로 이미지 url 파일 다운로드//
