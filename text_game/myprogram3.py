# Botty

user, message = raw_input().split(":")

if "@myprogram3" in messsage":
	print "Hey there,", user, "Read your message - <", message, ">"

	print 'WELCOME TO THE GAMES! Doth thou wish to embark on a journey left, right, up or down?'
	response1 = raw_input()
	if response1 == 'left':
    	# something is here
    	print 'You found a mysterious bag'
	if not response1 == 'left':
		print 'You fell down the rabbit hole and died'
		print 'press the UP arrow to restart the game'
	else:
		print 'And within the bag is... :p'

