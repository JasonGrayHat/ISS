n = 8
answer = 1

for i in range(n,0,-1):
	answer*=i

print(answer)

def fact(n):
	if n == 1:
		return n
	else:
		return n*fact(n-1)

print(fact(8))

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
#a,b,a,b,a
#0,1,1,2,3


def fib(n):
	a = 0
	b = 1
	for i in range(1,n):
		if i%2==0:
			a += b
		else:
			b += a
	if(n%2 == 0):
		return b
	else:
		return a

print(fib(100000))