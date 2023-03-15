redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, 
password=redis_password, decode_responses=True)
while(1):
    dataRefree = s.recv(4096)
    r.set("RefBox",dataRefree)
    print(dataRefree)
s.close
