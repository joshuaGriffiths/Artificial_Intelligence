#JOSHUA GRIFFITHS
#Problem Set 4 Question 2
#Fall 2017
#ARTIFICIAL INTELEGENCE

import random
from random import randrange
import numpy as np

def isUpset(cityState,citizen):

	if type == 0:
		return False

	else:#there is someone living there

		if countNeighbors(cityState,citizen) < 2:
			return True

		else: return False


def countNeighbors(cityState,citizen):

	type = cityState[citizen]  # should be a 0,1,2
	neighborNumber = 0

	if type == 0:
		return -1

	elif citizen == 0:
		
		if type == cityState[59]:
			neighborNumber += 1
		if type == cityState[58]:
			neighborNumber += 1
		if type == cityState[citizen + 1]:
			neighborNumber += 1
		if type == cityState[citizen + 2]:
			neighborNumber += 1

	elif citizen == 1:

		if type == cityState[59]:
			neighborNumber += 1
		if type == cityState[citizen - 1]:
			neighborNumber += 1
		if type == cityState[citizen + 1]:
			neighborNumber += 1
		if type == cityState[citizen + 2]:
			neighborNumber += 1

	elif citizen == 59:

		if type == cityState[citizen - 2]:
			neighborNumber += 1
		if type == cityState[citizen - 1]:
			neighborNumber += 1
		if type == cityState[0]:
			neighborNumber += 1
		if type == cityState[1]:
			neighborNumber += 1

	elif citizen == 58:

		if type == cityState[citizen - 2]:
			neighborNumber += 1
		if type == cityState[citizen - 1]:
			neighborNumber += 1
		if type == cityState[citizen + 1]:
			neighborNumber += 1
		if type == cityState[0]:
			neighborNumber += 1

	else:
		if type == cityState[citizen-2]:
			neighborNumber += 1
		if type == cityState[citizen - 1]:
			neighborNumber += 1
		if type == cityState[citizen + 1]:
			neighborNumber += 1
		if type == cityState[citizen + 2]:
			neighborNumber += 1

	return neighborNumber

def main():

	city = []
	for i in range (27):
		city.append(1)
		city.append(2)
	for i in range(6):
		city.append(0)

	random.shuffle(city)

	print (city)
	print (len(city))
	print ""


	i = 0
	while i != 400:
		#Find a new home
		randCit = randrange(0, len(city))

		if isUpset(city,randCit) == True:

			choose = 4
			while choose !=0:

				pickZero = randrange(0, len(city))
				choose = city[pickZero]

			city[pickZero] = city[randCit]
			city[randCit] = 0

		if (i % 20 == 0):
			print (city)

		i += 1


if __name__ == '__main__':
	main()
