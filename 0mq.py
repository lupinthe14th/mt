import zmq, sys, json
sock = zmq.Context().socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5556")
sock.send_string(json.dumps([{"src": " ".join(sys.argv[1:])}]),encoding='utf-8')
print(sock.recv_string(encoding='utf-8'))
