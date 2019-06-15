myTurnBoolean = 0

for i in range(20):
	if (myTurnBoolean):
		print('It is my turn')
	else:
		print('It is not my turn')
	myTurnBoolean = not myTurnBoolean