print 'Welcome to the game! Do you want to go left or right?'
response = raw_input()

if response == 'left':
	print 'You fell into a trap and died.'
	exit()
if response == 'right': 
	print 'You move forward and found stairs. Do you want to go down or up?'
	response2 = raw_input()


if response2 == 'down':
	print 'You slowly walk down but unfortunately fell, hit your head and died.'
	exit()
if response2 == 'up':	
	print 'You enter a hallway with a table in the middle and two cups. There is a white and a blue cup. Which will you take?'
	response3 = raw_input()

if response3 == 'blue':
	print 'You magically enter an entirely new world. You see a path ahead and behind you. Which will you take?'
	response4 = raw_input()

	if response4 == 'behind':
		print 'You unexpectedly fell off a cliff and died.'
	
	if response4 == 'ahead':
		print 'You walk til you see a house. Do you enter?'
		response5 = raw_input()
	if response5 == 'yes':
		print 'A witch was waiting inside and she killed you.'
	if response5 == 'no':
		print 'A rock fell out of the sky and killed you.'
		exit()

if response3 == 'white':
	print 'Nothing happened and you continued moving forward. You come across a man. Do you kill him?'
	response6 = raw_input()
if response6 == 'yes':
	print 'You both kill each other.'
	exit()
if response6 == 'no':
	print 'He kills you.'
	exit()
	

