from argparse import ArgumentParser
from logging import getLogger

import zmq
from sanic import Sanic
from sanic import response as resp
from sanic_cors import CORS

import sentencepiece as spm

logger = getLogger('root')

app = Sanic()
CORS(app)


@app.route('/transate', methods=['POST'])
async def transate_handler(request):
    logger.debug("request.json :{}".format(request.json))
    sock.send_json(tokenize(request.json))
    recv = sock.recv_json()
    logger.debug("recv :{}".format(recv))
    logger.debug("type(recv) :{}".format(type(recv)))
    return resp.json(deTokenize(recv))


def tokenize(jsonData):
    logger.debug("jsonData: {}".format(jsonData))
    for j in jsonData:
        logger.debug("src: {}".format(j['src']))
        j['src'] = " ".join(sp.EncodeAsPieces(j['src']))
        logger.debug("src: {}".format(j['src']))

    logger.debug("jsonData: {}".format(jsonData))
    return jsonData


def deTokenize(lists):
    logger.debug("Lists: {}".format(lists))
    for dictList in lists:
        logger.debug("dictList: {}".format(dictList))
        for dic in dictList:
            logger.debug("dic: {}".format(dic))
            logger.debug("tgt: {}".format(dic['tgt']))
            logger.debug("tgt.split(): {}".format(dic['tgt'].split()))
            dic['tgt'] = sp.DecodePieces(dic['tgt'].split())
            dic['src'] = sp.DecodePieces(dic['src'].split())
            logger.debug("tgt: {}".format(dic['tgt']))
        logger.debug("dictList: {}".format(dictList))

    logger.debug("lists: {}".format(lists))
    return lists


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--debug', default=False)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--port', dest='port', type=int, default=8080)
    parser.add_argument('--workers', dest='workers', type=int, default=1)
    args = parser.parse_args()

    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock = context.socket(zmq.REQ)  # pylint: disable=E1101
    sock.connect("tcp://zmqrep:5556")

    # Sentencepiece init
    sp = spm.SentencePieceProcessor()
    sp.Load(app.config['SP_MODEL'])

    app.run(debug=args.debug, host=args.host,
            port=args.port, workers=args.workers)
