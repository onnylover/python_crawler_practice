from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 8888

#기능이 담긴 클래스 상속
class MyHttpRequestHandeler(BaseHTTPRequestHandler):
    def do_GET(self):

        #favicon = 웹사이트 대표 아이
        #pathing기능
        result = urlparse(self.path)
        print(result)

        if result.path == "/":
            # 정상응답처리, header 처리 (요기 구간을 바꿔주면 서버가 가지고 있는 역할이 나누어짐)
            self.send_response(200)
            self.send_header("Contents-Type", "text/html; charset=utf-8")
            self.end_headers()
            # 서버에 대한 응
            self.wfile.write("<h1>Hello World --- Main</h1>".encode("utf-8"))
        elif result.path == "/board":
            # 파라메타 활용
            params = parse_qs(result.query)
            print(params)
            # 정상응답처리, header 처리 (요기 구간을 바꿔주면 서버가 가지고 있는 역할이 나누어짐)
            self.send_response(200)
            self.send_header("Contents-Type", "text/html; charset=utf-8")
            self.end_headers()
            # 서버에 대한 응
            self.wfile.write("""
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                </head>
                <body>
                    <h1>Hello World --- board by handtype </h1>
                </body>
            </html>
            """.encode("utf-8"))

#서버 생성 및 실행
http = HTTPServer(("0.0.0.0", port),MyHttpRequestHandeler)
print(f"Server Running On : Port{port}")
http.serve_forever()
