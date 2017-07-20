import redis

r=redis.StrictRedis(host='localhost',port=6379,db=0)

def func1( upper ):
	for i in range(upper):
		r.set(i,char(i))

func1(30)
