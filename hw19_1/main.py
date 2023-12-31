from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open("index.html", "r", encoding="utf-8") as template:
            return template.read()


    def do_GET(self):
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "UTF-8"))


if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
