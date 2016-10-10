def fib(number):
	fibList = [0,1]
	for index in range(2,number):
		new_fib = fibList[index-1]+fibList[index-2]
		if new_fib <= number:
			fibList.append(new_fib)
		else:
			break
	return fibList


print fib(10)