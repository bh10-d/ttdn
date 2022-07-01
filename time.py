# def ip(file):
# 	nf = open("time.txt","w")
# 	for x in file:
# 		nf.write(x[x.find(':')+1:x.find(':')+9]+"\n")
# 		print(x[x.find(':')+1:x.find(':')+9])


def clog(file):
	nf = open("test.txt", "w")
	for x in file:
		# nf.write(x[:x.find('"')]+"\n")
		print(x[:x.find('"')]+"\n")

f = open("mobilog.txt", "r")
clog(f)