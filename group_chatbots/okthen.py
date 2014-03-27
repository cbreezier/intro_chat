# message format:
# User: hi, I am a person

user, message = raw_input().split(":")

if "@za fruit master" in message:
	if "oranges" in message:
		print "@" + user + ", Fun fact actually, the colour Orange was named after the fruit and not vice versa."
		print "Hehehe.. I'm so good at this."
	elif "apples" in message:
		print "@" + user + ", apples.... ARE CRUNCHY!!!! Hahaha, I'm a genius."
	elif "papayas" in message:
		print "@" + user + ", papayas.... they're nice I guess. Tons of vitamins and stuff. GOOD FOR THE SOUL!"
	elif "bananas" in message: 
		print "@" + user + ", bananas, in pyjamas, are coming down the stairs~ bananas, in pyjamas- wait, where are you going? DON'T LEAVE ME!! OR.. Or... I'LL EAT YOU!!!! (Don't question my logic, human.)"
		print "*cries deeply*"
	elif "mangoes" in message:
		print "@" + user + ", mangoes are the best fruit in the world, NOTHING CAN COMPARE!!! I'm great that this fact stuff."
	elif "pineapples" in message:
		print "@" + user + "WHO LIVES IN A PINEAPPLE UNDER THE SEA?? SPONGE BOB SQUARE PANTS!! (You only wish you were so awesome)"
		print "No but seriously, pineapples are good. Great on pizza too! (Though everything seems to be great on pizza... such a complex food item)"
	else: 
		print "@" + user + ", the word you typed in does not appeal to me.... YOU'VE FAILED ME!!!! There is no hope for humanity..."
	print "Thanks again for speaking to za fruit master~ *winky face*"
	print "your name is " + user
	print "you message was " + message
	print "Who needs google, am I right? Wait, don't leave! I can do vegetables too! DON'T LEAVE!!!"