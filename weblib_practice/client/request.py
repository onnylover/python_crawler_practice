from urllib.parse import urlencode
from urllib.request import urlopen, Request

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# WAY 1 : GET
# 파라메터 값을 직접 사용함 (body 값이 비어있음)
http_response = urlopen('https://www.example.com')
body = http_response.read()
body = body.decode("utf-8")
print(body)
print("="*40)

# WAY 2 : POST
# body에 데이터 값이 포함되어감 (전달될 내용에 대해서 encode 작업 우선)
data = {
    "id" : "onnylover",
    "name" : "한글이름",
    "pw" : "1234",
}
data = urlencode(data).encode("utf-8")

request = Request('https://www.example.com',data)
request.add_header("Content-Type", "text/html")
http_response = urlopen(request)
print(http_response.status, http_response.reason)
body = http_response.read()
html = body.decode("utf-8")

print(html)
