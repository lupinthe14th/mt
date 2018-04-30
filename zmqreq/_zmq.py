import zmq, sys
sock = zmq.Context().socket(zmq.REQ)
sock.connect("tcp://zmqrep:5556")
sock.send_json([{"src": " ".join(sys.argv[1:])}])
print(sock.recv_json())
