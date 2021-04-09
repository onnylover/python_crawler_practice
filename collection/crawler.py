import sys
from datetime import datetime
from urllib.request import Request, urlopen


# def error(e):
    # file 에 스탄다드입출력 (키보드, 화면) stdout
    # file open 하면 핸들러 타고 주소로 파일 저장할 수 있음
    # stderr 하면 에러내역을 명시해서 노출
    # print(f"{e}: {datetime.now()}", file=sys.stderr)


def crawling(url="",
             encoding="utf-8",
             err=lambda e:print(f"{e}: {datetime.now()}", file=sys.stderr)):
    try:
        request = Request(url)
        response = urlopen(request)
        print(f"{datetime.now()}: success for request [{url}]")

        receive = response.read()
        # 인코딩할때 에러나면 자동으로 대체 기능 추가
        html = receive.decode(encoding, errors="replace")
        return html

    except Exception as e:
        if err is not None:
            err(e)






