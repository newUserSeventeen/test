import redis

r=redis.StrictRedis(host='localhost',port=6379,db=0)

for i in range(30):
	r.set(i,char(i))


