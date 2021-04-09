from bs4 import BeautifulSoup

html = """
<td class="title">
	<div class="tit3" data-no="10">
		<a href="/movie/bi/mi/basic.nhn?code=189075" title="자산어보">자산어보</a>
	</div>
</td>"""


# 1. tag 조회
def ex01():
    # 대상 다음에 어떤 구문인지 인식하게 해줘야함
    bs = BeautifulSoup(html,"html.parser")

    # 특정 장소로 지정할 수 있음
    tag_td = bs.td
    # print(tag_td)
    # tag_a = bs.a
    # 상세화 시킬수도 있음
    tag_a = tag_td.a
    print(tag_a)

    # None
    tag_h1 = bs.td.h1
    print(tag_h1)

# 2. attribute 조회
def ex02():
    bs = BeautifulSoup(html, "html.parser")
    tag_td = bs.find("td", attrs={"class":["title","black"]})
    print(tag_td)

    tag_div = bs.find("div", attrs={"class":"tit3","data-no":"10"})
    print(tag_div)

if __name__ == '__main__':
    # ex01()
    ex02()
