#prob1
def prob1():
	print("Problem 1:")

	a = [1, 4, 16, 25, 36, 49, 64, 81, 100]
	b = []
	
	for x in a:
		if x%2==0:
			b.append(x)
	
	return b
	
#prob2
def fibo(x):
	if x == 0:
		return [0]
	elif x==1:
		return [0,1]
	else: 
		fiblist = fibo(x-1)
		fiblist.append(fiblist[-1]+fiblist[-2])
		return fiblist

def prob2():
	print("\nProblem 2:")
	x = input("How many Fibonacci numbers would you like to generate: ")
	return fibo(int(x))
	
#prob3

def palindrome(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]


	if x == word:
		return(word +' is a palindrome ')
	else:
		return(word + ' is not a Palindrome')

def prob3():
	print("\nProblem 3:")
	word = input('enter a string: ')
	return palindrome(word)
	
#prob4
def nodupes(x):
	return list(set(x))
	
def prob4():
	print("\nProblem 4:")
	list = [1,1,2,3,4,7,7,8,3,9,15,26]
	print ("list")
	print(list)
	print ("no dupes list")
	return (nodupes(list))
	
#prob5

def prob5():
	print("\nProblem 5:")
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

	result = [i for i in a if i in b]
	return nodupes(result)

#prob6
birthdays = {
	"Bob": "04/20/1969",
	"Joe": "05/15/1969",
	"Jeff": "04/20/1985",
	"Dwight": "02/20/1963"
}

def prob6():
	print("\nProblem 6:")
	name = input("Who's Birthday would you like to look up?: ")
	return (name+"'s birthday is "+ birthdays[name])

	

print(prob1())
print(prob2())
print(prob3())
print(prob4())
print(prob5())
print(prob6())