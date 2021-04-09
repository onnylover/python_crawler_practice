from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collection import crawler
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


# 코드
def ex01():
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode("cp949")
    # print(html)

    bs = BeautifulSoup(html, "html.parser")
    divs = bs.find_all("div", attrs={"class": "tit3"})
    # 갯수
    print(len(divs))

    # div의 클래스는 리스트는 아니지만 같은 역할을 함
    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a["href"], sep=":")


# 함수
def ex02():
    html = crawler.crawling(url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn",
                            encoding="cp949"
                            )

    bs = BeautifulSoup(html, "html.parser")
    divs = bs.find_all("div", attrs={"class": "tit3"})

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a["href"], sep=":")

if __name__ == "__main__":
    # ex01()
    ex02()
