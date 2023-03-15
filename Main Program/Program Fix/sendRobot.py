import imp
import redis
import socket
import sys
import argparse
import time
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', type=str,)
args = parser.parse_args()
print(args.integers)
IP = args.integers
host = IP
data_payload = 2048
port = 2000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = (host,port)
redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
print("Memulai Komunikasi...")
while True:
    data = r.get("RefBox")
    sent = sock.sendto(data.encode('utf-8'),server_address)
    print("data terkirim = "+data)
    time.sleep(0.5)
sock.close()

