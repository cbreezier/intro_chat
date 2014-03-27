# message format:
# User: hi, I am a person

user, message = raw_input().split(":")
if "@different ways to say hi (phonetically spelt)" in message:
	print "@" + user
	if "japanese" in message:
		print "konnichiwa"
	elif "chinese" in message:
		print "ni hao"
	elif "french" in message:
		print "Bonjour"
	elif "korean" in message:
		print "annyeonghaseyo"
	elif "spanish" in message:
		print "hola"
	elif "italian" in message 
		print "ciao"
	elif "thai" in message
		print "Sawadi"
	elif "swedish" in message
		print "hallo"
	elif "albanian" in message
		print "pershendatje"
	
	else:
		print "@" + user + "sorry, i dont know that specific language"