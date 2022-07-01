def clog(file):
	nf = open("test.txt", "w")
	for x in file:
		nf.write(x[:x.find('"')]+"\n")
		print(x[:x.find('"')]+"\n")

def ip(file):
	nf = open("count.txt","w")
	for x in file:
		nf.write(x[:x.find('-')-1]+"\n")
		print(x[:x.find('-')])


def filter(arr):
	narr = list(set(arr))
	# print(narr)
	return narr


def pre(f):
	nf = open("test2.txt","w")
	keep = 1
	s = ''
	arr = []
	ak = []
	test = []
	for x in f:
		arr.append(x)

	test = filter(arr)

	i = 0
	while i < len(test):
		j = 0
		while j < len(arr):
			newc = arr[j][:arr[j].find('-')-1]
			if test[i] == newc:
				keep+=1
			j+=1
			print(newc)
		merge = "So lan request: "+str(keep)+" - IP:"+test[i]
		ak.append(merge)
		i+=1
		keep = 0

	for x in ak:
		nf.write(x+"\n")
	# print(keep)
	# print(ak)


def count():
	f = open("count.txt","r")
	pre(f)


f = open("mobilog.txt", "r")
# clog(f)
# ip(f)
pre(f)
# count()