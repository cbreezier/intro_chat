# message format:
# User: hi i am a person

user, message = raw_input().split(":")

if "@songbot" in message:
	if "baby" in message:
		print "Baby, baby, baby oooh"
		print "Like baby, baby, baby nooo"
		print "Like baby, baby, baby oooh"
		print "I thought you'd always be mine!"
	elif "let it go" in message:
		print "Let it go, let it go"
		print "Can't hold it back anymore"
		print "Let it go, let it go"
		print "Turn away and slam the door!"
	elif "witch doctor" in message:
		print "Oh yah"
		print "Look at it go"
		print "Roll out the barrel"
		print "Feel it in your bones!"
	else:
		print "Unkown. Known songs are: baby, let it go, witch doctor"