def print_all_elements(p):
	i = 0
	while i <= len(p) - 1:
		print p[i]
		i = i + 1


def print_all_elements(p):
	for e in p:
		print e

mylist = [1,2,[3,4]]
print_all_elements(mylist)


def sum_list(list):
	b = 0
	for a in list:
		b = a + b
	return b

print sum_list([1,7,4])

def measure_udacity(U):
	count = 0
	for e in U:
		if e[0] == 'U':
			count = count + 1
	return count

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

# using while loop
def find_element(p,t):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i
		i = i + 1
	return -1

# using for loop
def find_element(p,t):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1

p = [0,1,2]
print p.index(2)

p = [0,1,2]
print 2 in p

def find_element(p,t):
	if t in p:
		return p.index(t)
	else:
		return -1

def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)
