import tornado.ioloop

from config.app import make_app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado server running on 8888")

    tornado.ioloop.IOLoop.current().start()
