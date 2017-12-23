# _*_coding:utf-8_*_
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import psutil
import time
class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index01.html')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        pass

    def on_message(self, message):
        while True:
            psutil.cpu_times()
            time.sleep(1)
            self.write_message(u"Your message was: "+str(psutil.cpu_times()))

    def on_close(self):
        pass

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler)
        ]

        settings = { "template_path": "."}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

