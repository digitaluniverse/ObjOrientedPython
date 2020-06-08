import statistics
import random


def prob1():
	print("Problem 1:")

	phoneDict = {}
	with open("directory.txt") as directoryFile:
			for line in directoryFile:
				text = line.split("    ")
				phoneDict[text[0]] = text[1]
	print(phoneDict.keys())
	name = input("Enter a name to see the phone number associated with it: ")
	print("{}'s Phone Number is {} ".format(name ,phoneDict.get(name)))
	
	
def prob2():
	print("\nProblem 2:")

	String = input("Enter some words or something to form a sentance... Or Don't 2020 is fucked either way: ")
	String = String.casefold()
	chars = len(String)
	print("Number of characters : {} ".format(chars))
	words = len(String.split(" "))
	vowel_count = 0
	vowels = set("aeiou")
	print("Number of words : {} ".format(words))
	for i in String:
		if i in vowels:
			vowel_count = vowel_count+1
	print("Number of Vowels : {}".format(vowel_count))

nameList = []
gradeList = []
letterList = []

def findMean():
	count = 0
	for n in gradeList:
		count = count + n
	mean = count / len(gradeList)
	a = mean
	return a


def findStandard():
	standard = statistics.stdev(gradeList)
	return standard

def readData():
	with open("studentgrades.txt") as openfile:
		for line in openfile:
			fields = line.split("    ")
			nameList.append(fields[0])
			gradeList.append(int(fields[1]))

	meanOne = findMean()
	standard = findStandard()
	for i in gradeList:
		if meanOne + standard <= i:
			letterList.append('A')
		elif meanOne + (standard / 3) <= i < meanOne + standard:
			letterList.append('B')
		elif meanOne - (standard / 3) <= i < (meanOne + standard / 3):
			letterList.append('C')
		elif meanOne - standard <= i < meanOne - (standard / 3):
			letterList.append('D')
		else:
			letterList.append('F')
def prob3():
	print("\nProblem 3:")

	readData()

	print("Class Average: {} \nStandard Deviation: {}".format(findMean(),findStandard()))
	count = len(gradeList)
	for n in range(count):
		print("{}'s Numerical Grade is: {} and their Letter Grade is an: {} ".format(nameList[n], gradeList[n], letterList[n]))
	letter_dict = { }
	increment = 1
	count = 0
	for m in range(len(letterList)):
		if letterList[m] == "A":
			count =+ increment
			letter_dict["A"] = count
		elif letterList[m] == "B":
			count = + increment
			letter_dict["B"] = count
		elif letterList[m] == "C":
			count = + increment
			letter_dict["C"] = count
		elif letterList[m] == "D":
			count = + increment
			letter_dict["D"] = count
		else:
			count = + increment
			letter_dict["F"] = count

	print("Letter grades of students: {} ".format(letter_dict))
	
def prob4():
	print("\nProblem 4:")

	count = 11
	listOne = []
	listTwo = []
	listLarge = [] 
	for i in range(count):
		listOne.append(random.randint(0, 10))
		listTwo.append(random.randint(0, 10))
	print("List One: {} ".format(listOne))
	print("List Two: {} ".format(listTwo))
	for i in range(count):
		if listOne[i] > listTwo[i]:
			listLarge.append(listOne[i])
		elif listTwo[i] > listOne[i]:
			listLarge.append(listTwo[i])
	print("Big List: {} ".format(listLarge))



prob1()
prob2()
prob3()
prob4()