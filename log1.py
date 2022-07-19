def clog(file):
	nf = open("count.txt", "w")#test.txt
	for x in file:
		# nf.write(x[:x.find('"')]+"\n")
		nf.write(x[:x.find('-')-1]+' '+x[x.find(':')+1:x.find(':')+9]+"\n")
		# print(x[:x.find('"')]+"\n")
		print(x[:x.find('-')-1]+' '+x[x.find(':')+1:x.find(':')+9]+"\n")

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
	nf = open("test3.txt","w")
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
			if test[i] == arr[j]:
				keep+=1
			j+=1
		
		# check hanh vi theo so luong req la k on
		# if keep < 10:	
		# 	merge = f'So lan request: {str(keep)} - IP: {test[i]}'
		# if keep >= 10:
		# 	merge = f'So lan request: {str(keep)} - "WARNING 1" - IP: {test[i]}'		
		# if keep >= 20:
		# 	merge = f'So lan request: {str(keep)} - "WARNING 2" - IP: {test[i]}'
		# if keep >= 30:
		# 	merge = f'So lan request: {str(keep)} - "BLOCK" - IP: {test[i]}'	
		
		merge = f'{test[i]}'
		ak.append(merge)
		i+=1
		keep = 0

	for x in ak:
		nf.write(x+"")
	# print(keep)
	# print(ak)


def count():
	f = open("count.txt","r")
	pre(f)


f = open("mobilog.txt", "r")
# clog(f)
# ip(f)
# pre(f)
count()