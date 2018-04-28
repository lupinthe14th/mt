import zmq
from argparse import ArgumentParser, SUPPRESS
import json

from logging import basicConfig, getLogger, DEBUG

from japronto import Application

logger = getLogger(__name__)


def unhandled(request):
    1 / 0


def transate(srcList):
    try:
        logger.debug("srcList :{}".format(srcList))
        sock.send_string('[{"src": "日本語"}]', encoding='utf-8')
        recv = sock.recv_string(encoding='utf-8')
        logger.debug("recv :{}".format(recv))
        logger.debug("type(recv) :{}".format(type(recv)))
        code = 200
        message = recv
    except Exception as e:
        logger.error("{0}: {1}".format(type(e), e))
        code = 500
        message = {'message': format(e)}
    finally:
        return code, message

def transate_handler(request):
    text = """Body related properties:
      Mime type: {0.mime_type}
      Encoding: {0.encoding}
      Body: {0.body}
      Text: {0.text}
      Form parameters: {0.form}
      Files: {0.files}
    """.format(request)

    try:
        transateList = request.text
    except Exception as e:
        logger.error("{0}: {1}".format(type(e), e))
    else:
        text += "\nJSON:\n"
        text += str(transateList)

    logger.debug("request :{}".format(text))

    return request.Response(transate(transateList))


def hello(request):
    return request.Response(text='Hello world!')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--debug', default=False)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--port', dest='port', type=int, default=8080)
    parser.add_argument('--worker-num', dest='worker_num', type=int, default=1)
    args = parser.parse_args()

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)  # pylint: disable=E1101
    sock.connect("tcp://127.0.0.1:5556")

    # init logLevel
    if args.debug:
        basicConfig(level=DEBUG)

    app = Application()
    app.router.add_route('/', hello)
    app.router.add_route('/unhandled', unhandled)
    app.router.add_route('/v1/transate', transate_handler, methods=['POST'])
    app.run(debug=args.debug, host=args.host,
            port=args.port, worker_num=args.worker_num)