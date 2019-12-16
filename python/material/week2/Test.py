def testFunction():
	return 5,4,6

testVar,testVar1,testVar2 = testFunction()
print(testVar,testVar1,testVar2)

testVar,testVar1,testVar2 = (5,4,6)
print(testVar,testVar1,testVar2)