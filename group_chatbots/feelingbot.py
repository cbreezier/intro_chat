# message format:
# User: hi, i am a person

user, message = raw_input().split(":")
message = message.lower()
if "@feelingbot" in message:
	if "good" in message or "great" in message or "happy" in message:
		if "not" in message:
			print "@" + user + " is not feeling so good"
		else:
			print "@" + user + " is feeling great!"
	elif "bad" in message or "terrible" in message or "sad" in message:
		print "@" + user + " is not feeling so good"
	else:
		print user, ",I only do feelings!"