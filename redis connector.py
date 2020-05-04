import redis

def redisc():
    r = redis.Redis(
    host= "127.0.0.1",
    port= "6379")
    return r

r=redisc()
r.set("foo","bar")
r.get("foo")
