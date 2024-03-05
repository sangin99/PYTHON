#? <차이점>
# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법
                      #   
# 웹 스크래핑(Scraping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법
                      #  데이터만 받아오는 것  

# 파이썬 스크래핑 패키지 : `beautifulsoup4`
# 파이썬 크로링 패키지 : `selenium`

# pip install beautifulsoup4
# pip install selenium
# 한번에 받는 방법 : pip install beautifulsoup4 selenium (띄어쓰기 사용)

#>> beautifulsoup4 
import requests #요청보내는 명령어
from bs4 import BeautifulSoup #사용명령어

URL = 'https://naver.com' #ex 네이버로 요청보내기

response = requests.get(URL)
print(response)