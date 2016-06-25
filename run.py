import sys
from app import app
import logging


if __name__ == '__main__':
    host = app.config['APP_HOST']
    port = app.config['APP_PORT']

    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = sys.argv[2]

    logging.basicConfig(filename='logs/error.log', level=logging.WARNING,
                        format='[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d]# %(message)s')

    app.run(host=host, port=port, debug=app.config['DEBUG'], threaded=app.config['THREADED'])
