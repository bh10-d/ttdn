# def ip(file):
# 	nf = open("time.txt","w")
# 	for x in file:
# 		nf.write(x[x.find(':')+1:x.find(':')+9]+"\n")
# 		print(x[x.find(':')+1:x.find(':')+9])

import geocoder

# def clog(file):
# 	nf = open("test.txt", "w")
# 	for x in file:
# 		# nf.write(x[:x.find('"')]+"\n")
# 		print(x[:x.find('"')]+"\n")

def location(file):
	nf = open("location.txt","w")
	for x in file:
		ip = geocoder.ip(x)
		nf.write("IP: "+x+"- Location: "+str(ip.city.encode("utf-8")))
		# print(ip.city)

f = open("count.txt", "r")
location(f)