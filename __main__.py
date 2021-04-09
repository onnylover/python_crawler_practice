from datetime import datetime, time
import time
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

from collection import crawler
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def crawling_pelicana():
    results = []

    for index in count(start=1,step=1):
        url = f"https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si="
        html = crawler.crawling(url)
        bs = BeautifulSoup(html,"html.parser")
        tag_table = bs.find("table",attrs={"class":["table","mt20"]})
        tag_tbody = tag_table.find("tbody")
        tags_tr = tag_tbody.find_all("tr")

        #end 검출
        if (len(tags_tr)) == 0:
            print("No results : finish at index no. " + str(index))
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[3]
            citi = address.split()[:2]
            t = (name, address) + tuple(citi)
            results.append(t)
            # print(name, address, citi)

        # print(len(tags_tr))
    # store (thru pandas)
    table = pd.DataFrame(results, columns=["name", "address", "sido", "gugun"])
    table.to_csv("results/pelicana.csv",encoding="utf-8",mode="w",index=True)

    # print(results)

def crawling_nene():
    pass

def crawling_kyochon():
    pass

def crawling_goobne():

    url = "http://www.goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome("/Volumes/Geozedo60/Python/chromedriver")
    wd.get(url)
    time.sleep(3)

    results = []

    for index in count(start=1,step=1):
        # Java 기능으로 내용을 콜 함
        script = f"store.getList({index})"
        wd.execute_script(script)
        print(f"{datetime.now()}: success for request [{script}]")
        time.sleep(3)

        # JavaScript의 HTML 실행결과 (랜더링 결과)
        html = wd.page_source

        # 파싱하기 (bs4)
        bs = BeautifulSoup(html,"html.parser")
        tag_tbody = bs.find("tbody", attrs={"id":"store_list"})
        tags_tr = tag_tbody.find_all("tr")

        # End 검출
        if tags_tr[0].get("class") is None:
            print("No results : finish at index no. " + str(index))
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[6]
            citi = address.split()[:2]
            t = (name, address) + tuple(citi)
            results.append(t)
    # print(results)
    # 브라우저 닫기
    wd.close()

    # store (thru pandas)
    table = pd.DataFrame(results, columns=["name", "address", "sido", "gugun"])
    table.to_csv("results/goobne.csv", encoding="utf-8", mode="w", index=True)

if __name__ == "__main__":
    # crawling_pelicana()
    crawling_goobne()
    # crawling_kyochon()
    # crawling_nene()