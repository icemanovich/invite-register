import sys
from app import app

# Used to Unicorn + Nginx
# from werkzeug.contrib.fixers import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':

    host = app.config['APP_HOST']
    port = app.config['APP_PORT']

    ''' Support additional parameters '''
    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = sys.argv[2]

    # logging.basicConfig(filename='logs/error.log', level=logging.WARNING,
    #                     format='[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d]# %(message)s')


    app.run(host=host, port=port, debug=app.config['DEBUG'], threaded=app.config['THREADED'])
