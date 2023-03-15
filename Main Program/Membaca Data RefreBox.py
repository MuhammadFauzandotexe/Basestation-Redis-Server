import argparse
import redis
import time
import socket
import socket
import os
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', type=str,)
args = parser.parse_args()
print(args.integers)
IP = args.integers
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 
s.connect((IP, 28097))

redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
while(1):
    dataRefree = s.recv(4096)
    r.set("RefBox",dataRefree)
    print(dataRefree)
s.close
# 192.168.100.79
