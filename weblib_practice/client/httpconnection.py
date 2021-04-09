from http.client import HTTPConnection

# 접속 객체 생성, HTTPConnection 으로 URL 접속
conn = HTTPConnection("www.example.com")

# 문서 요청
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.reason)

# 헤드 확인에 대한 바디 호출
# GET / HTTP/1.1 과 동일한 호출방법
# 200 OK 조건
if resp.status == 200:
    body = resp.read()
    # byte type이라고 해도 구체적으로 ascii 인지 utf-8인지 인코딩 내역 확인 필요함
    print(type(body), body)

# 실패
# GET /hello.html HTTP/1.1
# 404 Not Found
conn.request("GET", "/hello.html")
resp = conn.getresponse()
print(resp.status, resp.reason)


